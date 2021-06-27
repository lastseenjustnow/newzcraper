Guardian news scraper

Demo app drafted to:
1. collect dataset of articles content from a news website
2. apply basic preprocessing & cleansing 
3. store data in MongoDB
4. access dataset via public API

Data could be extracted both using adjacent Flask UI & backend and using command line:
```
curl -X POST 'http://{<hostname>}:5000/search_by_keyword' --data-raw 'keyword={<keyword>}&search=Search%21'
```

Flask UI available at port 5000.
MongoDB express available at port 8081.