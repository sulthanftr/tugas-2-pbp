from django.test import TestCase
from katalog.models import CatalogItem

class CatalogItemTest(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "iPhone 12 Pro Max",
            item_price = 17999999,
            description = "Original from iBox",
            item_stock = 3,
            rating = 5,
            item_url = "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
        )
        CatalogItem.objects.create(
            item_name = "MG Nu Gundam Ver.Ka",
            item_price = 21999999,
            description = "Bandai Original Ver.Ka Series",
            item_stock = 5,
            rating = 4,
            item_url = "https://www.tokopedia.com/hobbyjapan/mg-nu-gundam-verka"
        )
        CatalogItem.objects.create(
            item_name = "Samsung Galaxy S22",
            item_price = 7999999,
            description = "Specification: Snapdragon 8",
            item_stock = 30,
            rating = 4.5,
            item_url = "https://www.tokopedia.com/mhi-samsung/samsung-galaxy-s22-8-256gb-black"
        )

    def test_catalog_item(self):
        items = CatalogItem.objects.all()
        print()
        for item in items:
            print(f"Name: {item.item_name}")
            print(f"Price: {item.item_price}")
            print(f"Desc: {item.description}")
            print(f"Stock: {item.item_stock}")
            print(f"Rating: {item.rating}")
            print(f"URL: {item.item_url}\n")
