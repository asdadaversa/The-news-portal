import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal_service.settings')
django.setup()
import requests
from bs4 import BeautifulSoup
from fresh_news.models import News


def parse_space_com_links(base_url: str):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all('li', class_='day-article')

    with open("space.com.txt", "a+") as file:
        count_links = 0
        for link in links:
            href = link.a['href']
            print(href)
            count_links += 1
            file.write(f"{href}\n")
        print(f"total_links: {count_links}")


# parse_space_com_links("https://www.space.com/news/archive/2024/05")


def parse_space_com_page(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]
        for link in all_unique_links:
            try:
                page = requests.get(link)
                soup = BeautifulSoup(page.text, "html.parser")
                title = soup.find("h1").get_text()
                content = soup.find("div", class_="text-copy bodyCopy auto").find_all("p")
                paragraphs = [p.get_text() for p in content]
                final_content = " ".join([f"{i}\n" for i in paragraphs])
                image_url = (soup.find('source')['srcset'] if soup.find('source') else None).split(",")[4]
                print(f"now parce url: {link}")
                print(f"title: {title}")
                print(f"final_content: {final_content}")
                print(f"image_url: {image_url}")
                print()

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


parse_space_com_page("space.com.txt")
