import requests

import concurrent
from bs4 import BeautifulSoup

from fresh_news.models import News


def parse_link(link, file_address):
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.find("title").get_text().split("|")[0]
        content = soup.find("div", class_="content-wrapper").get_text()

        print(link)
        print(title)
        print(content)
        with open(file_address, "r+") as file:
            all_unique_links = [row.strip() for row in file]
            if link in all_unique_links:
                all_unique_links.remove(link)
                file.seek(0)
                file.truncate()
                file.write("\n".join(all_unique_links))
        news = News.objects.create(
            title=title,
            text=content,
            from_source=link,
        )
    except Exception as e:
        print(f"Error parsing link {link}: {str(e)}")
        return None


def parse_gizmochina_page(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(parse_link, link, file_address)
                for link in all_unique_links
            ]


parse_gizmochina_page("popsci.com.txt")
