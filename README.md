다양한 주제의 글들을 챗봇 서비스로 제공
====================================================

## 1. 주제와 목표
브런치와 다양한 뉴스 플랫폼에서 매일 올라오는 글을 크롤링하여 제목, 링크, 요약글을 챗봇으로 제공하는 것이 목표입니다.

## 2. 크롤링 한 웹사이트
 
 * 네이버블로그 : 테크플러스(네이버 메인페이지의 테크 카테고리 관리하는 공식 블로그)
한 주제의 글들을 챗봇 서비스로 제공
 * 매일경제 : 경제 최신뉴스 * 매일경제 : 경제 최신뉴스
 * 브런치


## 3. 물리적 시나리오



## 4. 과정

  * 웹사이트 마다 카테고리 별 크롤링 
    * 테크플러스 : IT > [트렌드/사람/제품]
    * 매일경제 : 경제
  * crontab 설정하여 하루에 한 번 해당 웹사이트 크롤링
  * 크롤링 한 데이터는 mongoDB 에 저장
  * 챗봇 

## 5. 코드 설명




## 6. 문제점

 * 하루에 한 번 '당일 업데이트' 된 데이터만 수집
 * 지난 데이터들 활용 방법 (당일 업데이트 된 데이터를 카테고리 별로 챗봇 구현 하기 때문)


## 7. 진행상황 (임시)
 * 테크플러스 블로그 크롤링 중
 * 매일경제 경제 카테고리 


## 6. Contributor

 * 류승환
 * 정다은 : 테크플러스, 매일경제 크롤링

