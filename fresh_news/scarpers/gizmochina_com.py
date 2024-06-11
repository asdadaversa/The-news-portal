from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from fresh_news.models import News


def parse_gizmochina_links(base_url: str, year: str):

    options = Options()
    service = Service()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    total_pages = soup.find("span", class_="pages").get_text().split(" ")[-1]
    print(total_pages)

    page_urls = [
        base_url + "page/" + str(page_number) for page_number in range(1, int(total_pages) + 1)
    ]

    for url in page_urls:
        try:
            with open("gizmochina.com.txt", "a+") as file:
                file.seek(0)
                existing_urls = [row.strip() for row in file]
                if url in existing_urls:
                    continue
                file.write(f"{url}\n")
                driver.get(url)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                links = soup.find_all("div", class_="td-module-thumb")
                print(f"Now parsed page is: {url}")
                for link in links:
                    href = link.a["href"]
                    if href not in existing_urls and year in href:
                        print(href)
                        file.write(f"{href}\n")
        except Exception as e:
            print(f"Error saving link: {str(e)}")
            continue
    driver.quit()


def parse_gizmochina_page(file_address: str):
    with open(file_address, "r+") as file:
        all_unique_links = [row.strip() for row in file]
        for link in all_unique_links:
            try:
                options = Options()
                service = Service()
                options.headless = True
                driver = webdriver.Chrome(service=service, options=options)
                driver.get(link)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                title = soup.find("h1").get_text()
                content = (
                    soup.find("div", class_="td-post-content tagdiv-type")
                    .get_text()
                    .split("RELATED")[0]
                )
                image_url = soup.find("figure").find("img")["src"]
                print(title)
                print(content)
                print(image_url)
                all_unique_links.remove(link)
                file.seek(0)
                file.truncate()
                file.write("\n".join(all_unique_links))
                news = News.objects.create(
                    title=title, text=content, from_source=link, image_url=image_url
                )
            except Exception as e:
                print(f"Error saving article: {str(e)}")
                continue


# parse_gizmochina_links("https://www.gizmochina.com/2024/05/", "2024")
# parse_gizmochina_page("gizmochina.com.txt")
