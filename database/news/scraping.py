
import feedparser
import requests
from urllib.parse import quote
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed


FONTES = {
    # Brasil
    "InfoMoney - Alumínio":
        "https://www.infomoney.com.br/tudo-sobre/aluminio/feed/",

    "Money Times - Alumínio":
        "https://www.moneytimes.com.br/tag/aluminio/feed/",

    "Google Notícias - Alumínio Brasil":
        "https://news.google.com/rss/search?q=" +
        quote('alumínio commodity OR preço OR mercado Brasil') +
        "&hl=pt-BR&gl=BR&ceid=BR:pt-419",

    "Google Notícias - Alumínio importação e exportação":
        "https://news.google.com/rss/search?q=" +
        quote('alumínio importação exportação Brasil') +
        "&hl=pt-BR&gl=BR&ceid=BR:pt-419",

    # Mercado internacional
    "LME Insight":
        "https://www.lmeinsight.com/zh/rss/",

    "Aluminium Magazine":
        "https://aluminiummagazine.com/mag/news/feed",

    "AG Metal Miner":
        "https://agmetalminer.com/feed/",

    "MINING.COM":
        "https://www.mining.com/feed/",

    "Google Notícias - Aluminium Market":
        "https://news.google.com/rss/search?q=" +
        quote('"aluminium" price OR market OR supply OR demand') +
        "&hl=en-US&gl=US&ceid=US:en",

    "Google Notícias - LME Aluminium":
        "https://news.google.com/rss/search?q=" +
        quote('"LME aluminium" OR "LME aluminum"') +
        "&hl=en-US&gl=US&ceid=US:en",

    "Google Notícias - Alumina e Bauxita":
        "https://news.google.com/rss/search?q=" +
        quote('alumina bauxite production supply market') +
        "&hl=en-US&gl=US&ceid=US:en",

    "Google Notícias - China Aluminium":
        "https://news.google.com/rss/search?q=" +
        quote('China aluminium production exports prices') +
        "&hl=en-US&gl=US&ceid=US:en",

    "Google Notícias - Tariffs and Trade":
        "https://news.google.com/rss/search?q=" +
        quote('aluminium tariffs trade sanctions supply chain') +
        "&hl=en-US&gl=US&ceid=US:en",
}


def coletar_rss(url, fonte):
    noticias = []

    try:
        resposta = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0 (compatible; RSSReader/1.0)"}
        )
        resposta.raise_for_status()

        feed = feedparser.parse(resposta.content)

        for item in feed.entries:
            link = item.get("link")

            if not link:
                continue

            # Tenta obter uma data padronizada para ordenação
            data_publicacao = item.get("published") or item.get("updated")

            data_ordenacao = None
            data_parseada = (
                item.get("published_parsed")
                or item.get("updated_parsed")
            )

            if data_parseada:
                data_ordenacao = datetime(
                    *data_parseada[:6],
                    tzinfo=timezone.utc
                )

            noticias.append({
                "titulo": item.get("title", "").strip(),
                "link": link,
                "data": data_publicacao,
                "fonte": fonte,
                "data_ordenacao": data_ordenacao
            })

        if getattr(feed, "bozo", False):
            print(f"[AVISO] Feed possivelmente malformado: {fonte}")

    except requests.RequestException as erro:
        print(f"[ERRO HTTP] {fonte}: {erro}")

    except Exception as erro:
        print(f"[ERRO] {fonte}: {erro}")

    return noticias


def coletar_todas_as_fontes(fontes=FONTES):
    noticias = []

    # Consulta as fontes em paralelo para reduzir o tempo de espera
    with ThreadPoolExecutor(max_workers=8) as executor:
        tarefas = {
            executor.submit(coletar_rss, url, fonte): fonte
            for fonte, url in fontes.items()
        }

        for tarefa in as_completed(tarefas):
            noticias.extend(tarefa.result())

    # Remove duplicatas pelo link
    unicas = {}

    for noticia in noticias:
        link = noticia["link"].split("#")[0].rstrip("/")

        if link not in unicas:
            unicas[link] = noticia

    noticias = list(unicas.values())

    # Mais recentes primeiro; notícias sem data ficam no final
    noticias.sort(
        key=lambda n: n["data_ordenacao"] or datetime.min.replace(
            tzinfo=timezone.utc
        ),
        reverse=True
    )

    return noticias