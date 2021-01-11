# WinterProject -Web Scrapper

## Description

I implemented a multi-level scrapper  which extracts and scrapes data from this [page](http://www.commonlii.org/resources/221.html) .This uses beautiful soup for parsing the data and requests module in python to send  http requests to the web page .This method is capable of extracting .txt and .html files.But for .pdf files I used javascript to run in the console window which automatically downloads the .pdf files .

## How To Use

### Installation

 #### Install beautiful soup

```html
    python -m  pip install bs4
```
 #### Install requests module

```html
   python -m pip install requests
```
 ### Os is python's standard library so no need to download it.
## How To Run 

### For extracting .pdf files run the 2020_pdf file in the console and press Enter.
   * It automatically downloads the pdf files.
### For extracting .txt files perform the following operations-:
  * Run the main.py file . This will first  create a urls.txt file and then start extracting  data from every link in it .
  
