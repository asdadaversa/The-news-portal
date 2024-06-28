import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal_service.settings')
django.setup()

import requests

from bs4 import BeautifulSoup

from fresh_news.models import News


def parse_popsci_com_links(base_url: str, additional_path: str):
    page = requests.get(base_url + additional_path)
    soup = BeautifulSoup(page.text, "html.parser")
    total_pages = soup.find("title").get_text().split(" ")[-4]
    print(total_pages)
    page_urls = [
        base_url + "page/" + str(page_number)
        for page_number in range(1, int(total_pages) + 1)
    ]
    print(page_urls)

    for url in page_urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            with open("popsci.com.txt", "a+") as file:
                file.seek(0)
                existing_urls = [row.strip() for row in file]
                if url in existing_urls:
                    continue
                file.write(f"{url}\n")
                print(f"Now parsed page is: {url}")
                links = soup.find_all("a", class_="card-post-title-link")
                for link in links:
                    href = link.get("href")
                    if href not in existing_urls:
                        file.write(f"{href}\n")
                        print(href)
        except Exception as e:
            print(f"Error saving link: {str(e)}")
            continue


# parse_popsci_com_links("https://www.popsci.com/category/science/", "page/2/")


def parse_popsci_page(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]
        for link in all_unique_links:
            try:
                page = requests.get(link)
                soup = BeautifulSoup(page.text, "html.parser")
                title = soup.find("title").get_text().split("|")[0]
                content = soup.find("div", class_="content-wrapper").get_text()

                print(link)
                print(title)
                print(content)

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
                print(f"Error saving article: {str(e)}")
                continue


# parse_popsci_page("popsci.com.txt")
