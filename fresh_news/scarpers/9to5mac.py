from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

from fresh_news.models import News


def parse_9to5mac_pages(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]

        for link in all_unique_links:
            try:
                page = requests.get(link)
                soup = BeautifulSoup(page.text, "html.parser")
                title = soup.find("h1").get_text()
                content = soup.find(
                    "div", class_="container med post-content"
                ).get_text().split("Add 9to5Mac to your Google News feed")[0]

                image_url = soup.find(
                    "figure", class_="img-border featured-image"
                ).find("img")["src"]
                print(link)
                print(f"title: {title}")
                print(f"content: {content}")
                print(f"image_url: {image_url}")

                all_unique_links.remove(link)
                file.seek(0)
                file.truncate()
                file.write('\n'.join(all_unique_links))
                news = News.objects.create(
                        title=title,
                        text=content,
                        from_source=link,
                        image_url=image_url
                )
            except Exception as e:
                print(f"Error saving article: {str(e)}")
                continue


def parse_9to5mac_links(base_url: str, month: str):

    start_date = datetime(2024, 5, 1)
    today = datetime.now()
    current_date = start_date
    all_unique_links = []

    while current_date.date() <= today.date():
        try:
            url = base_url + current_date.strftime("%d") + "/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            links = soup.find_all("a")

            unique_links = []

            for link in links:
                href = link.get("href")
                if month in href:
                    clean_href = href.split("?")[0].split("#")[0]
                    if clean_href not in unique_links:
                        unique_links.append(clean_href)

            with open("9tomac.txt", "a+") as file:
                for link in unique_links:
                    print(link)
                    file.write(f"{link}\n")
                print(f"count_links: {len(unique_links)}")

            all_unique_links.extend(unique_links)

            current_date += timedelta(days=1)

        except Exception as e:
            print(f"Error parsing link: {str(e)}")
            continue
