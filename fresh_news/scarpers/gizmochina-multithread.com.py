import concurrent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from fresh_news.models import News


def parse_link(link, file_address):
    try:
        options = Options()
        service = Service()
        options.headless = True
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(link)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1").get_text()
        content = soup.find(
            "div", class_="td-post-content tagdiv-type"
        ).get_text().split("RELATED")[0]
        image_url = soup.find("figure").find("img")["src"]
        print(title)
        print(content)
        print(image_url)
        with open(file_address, "r+") as file:
            all_unique_links = [row.strip() for row in file]
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
        print(f"Error parsing link {link}: {str(e)}")
        return None


def parse_gizmochina_page(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(parse_link, link, file_address)
                for link in all_unique_links
            ]


parse_gizmochina_page("gizmochina.com.txt")
