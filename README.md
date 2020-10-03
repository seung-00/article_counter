# article_counter

A program that crawls the number of news that matches the search term on Naver News by date.

검색어와 일치하는 네이버 뉴스 개수를 일자별로 크롤링하는 프로그램입니다.

---

here is tutorial

```
➜ python src/parser.py
Please enter a search term.If you have multiple search terms, separate them with commas (no white space).
   ex) python,node,go
➜ 코로나,COVID-19

Please enter start date and end date you want to search.
   ex) 2020-09-03,2020-10-10
➜ 2020-01-19,2020-01-22

What you entered...
   keywords => ['코로나', 'COVID-19']
   dates => [datetime.datetime(2020, 1, 19, 0, 0), datetime.datetime(2020, 1, 22, 0, 0)]
Go? Y / else
➜ Y

...

done!
```

| keywords | 2020.01.19 | 2020.01.20 | 2020.01.21 | 2020.01.22 |
| -------- | ---------- | ---------- | ---------- | ---------- |
| 코로나   | 48         | 958        | 1,367      | 2,121      |
| COVID-19 | 0          | 0          | 0          | 2          |