from bs4 import BeautifulSoup
import requests

def my_scrapper():
        url = "http://www.liiofindia.org/in/cases"

        payload={}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.request("GET", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')

        urls = open("urls.txt","w")
        urllist = []


        for link in soup.find_all('a'):
            if link['href'].split('/')[1]!='in':
                continue
            print('http://www.liiofindia.org'+link['href'])
            urls.write('http://www.liiofindia.org'+link['href'])
            urls.write('\n')
        print(urllist)


my_scrapper()