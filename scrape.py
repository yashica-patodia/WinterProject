from bs4 import BeautifulSoup
import requests
import os


def collect_urls():
        url = "http://www.liiofindia.org/in/cases"

        payload={}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.request("GET", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')

        urls = open('urls.txt', 'r')
        urllist = urls.readlines()
        print(urllist)

        ### Get urls for various root pages

        # for link in soup.find_all('a'):
        #     if link['href'].split('/')[1]!='in':
        #         continue
        #     print('http://www.liiofindia.org'+link['href'])
        #     urls.write('http://www.liiofindia.org'+link['href'])
        #     urls.write('\n')
        #     urllist.append('http://www.liiofindia.org'+link['href'])
        # print(urllist)

        ### Get urls for pages corresponding to various years

        for baseurl in urllist:
            baseurl = baseurl.split('\n')[0]
            yearpage = requests.request("GET", baseurl, headers=headers, data=payload)
            yearsoup = BeautifulSoup(yearpage.text, 'html.parser')
            print(yearsoup)
            print()

            for year in yearsoup.find_all('blockquote')[1].find_all('a'):
                os.makedirs('./data/'+baseurl.split('/')[-1]+'/'+year['href']+'/')
                index=1
                while(True):
                    pageurl = baseurl+'/'+year['href']+str(index)+'.html'
                    pageresponse = requests.request("GET", pageurl, headers=headers, data=payload)
                    if pageresponse.status_code == 404:
                        break
                    pagesoup = BeautifulSoup(pageresponse.text, 'html.parser')
                    txtfile = open('./data/'+baseurl.split('/')[-1]+'/'+pageurl.split('/')[-2]+'/'+str(index)+'.txt','w',encoding='utf-8')
                    txtfile.write(pagesoup.get_text())
                    txtfile.close()
                    index += 1

collect_urls()