import requests
import datetime
from bs4 import BeautifulSoup

def convert_dates(start_date, end_date):
    cur_date = start_date
    str_date = cur_date.strftime('%Y.%m.%d')
    str_dates = [str_date]
    
    while (cur_date != end_date):
        cur_date += datetime.timedelta(days=1)
        str_date = cur_date.strftime('%Y.%m.%d')
        str_dates.append(str_date)
    return str_dates

def _create_urls(cur_keyword, str_dates):
    urls = list(map(lambda d:
    f"https://search.naver.com/search.naver?where=news&query={cur_keyword}&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={d}&de={d}",
    str_dates))
    return urls

def parse(keywords, str_dates):
    cur_keyword = keywords.pop()
    urls = _create_urls(cur_keyword, str_dates)

    for url in urls:
        try:
            req = requests.get(f"{url}")
            html = req.text
            is_ok = req.ok
            print(is_ok)
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.select_one(".all_my > span")
            print(temp.get_text())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    keywords = input("Please enter a search term." +
    "If you have multiple search terms, separate them with commas (no white space).\n"+
    "ex) python,node,go\n").split(",")
    
    dates = list(map(lambda date:
    datetime.datetime.strptime(str(date), '%Y-%m-%d'),
    input("Please enter start date and end date you want to search." +
    "ex) 2020-09-03,2020-10-10\n").split(",")))

    answer = input(f"what you entered \nkeywords => {keywords}\ndates => {dates}\nGo? Y / else\n")
    if(answer == 'Y'):
        strart_date = dates[0]
        end_date = dates[1]
        str_dates = convert_dates(strart_date, end_date)
        parse(keywords, str_dates)