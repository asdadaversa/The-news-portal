from celery import shared_task
from .scarpers.gizmochina_com import parse_gizmochina_links
from .scarpers.popsci_com import parse_popsci_com_links


@shared_task
def periodic_parsing_gizmochina_links():
    return parse_gizmochina_links("https://www.gizmochina.com/2024/06/", "2024")


@shared_task
def periodic_parsing_popsci_com_links():
    return parse_popsci_com_links("https://www.popsci.com/category/science/", "page/2/")

