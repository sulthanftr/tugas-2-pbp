from django.test import Client, TestCase

c = Client()

class ResponseTest(TestCase):
    def testResponseHTML(self):
        response_html = c.get('/mywatchlist/html')
        self.assertEquals(response_html.status_code, 200)

    def testResponseXML(self):
        response_xml = c.get('/mywatchlist/xml')
        self.assertEquals(response_xml.status_code, 200)

    def testResponseJSON(self):
        response_json = c.get('/mywatchlist/json')
        self.assertEquals(response_json.status_code, 200)