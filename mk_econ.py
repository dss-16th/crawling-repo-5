def MKEcon():
    
    from datetime import datetime
    import requests
    import pandas as pd
    import pymongo
    from bs4 import BeautifulSoup
    
   
    now = datetime.now()
    d = now.day
    url = 'https://www.mk.co.kr/news/bestclick.php?BCC=%B0%E6%C1%A6&NY=2021&NM=03&ND={}'.format(d)
    response = requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    
    # 뉴스 제목 및 링크 수집
    titles = [each.string for each in dom.find_all('dt', 'tit')]
    links = dom.select("#container_left > div.list_area > dl.article_list > dt > a")
    news_link = [link['href'] for link in links]
    
    # 데이터프레임
    titles_pd = pd.DataFrame(titles)
    links_pd = pd.DataFrame(news_link)
    news_econ = pd.concat([titles_pd, links_pd], axis=1)
    news_econ.columns = ['title', 'link']
    
    # 데이터베이스 
    client = pymongo.MongoClient("mongodb://ip")
    collection = client.crawling.mk
    data = {"title": titles,
            "link": news_link}
    
    collection.insert_one(data)
    
    return news_econ
