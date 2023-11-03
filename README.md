# docker-compose-spring-boot-postgres

1. 請實作一個 Java Spring Framework project
   可對 PostgreSQL 做存取
   POST /item
   GET /item?id=**
   Reference :
   https://github.com/bezkoder/docker-compose-spring-boot-postgres

2. https://swagger.io/specification/
   請參考 OpenAPI 3.0 的規範
   實作輸出 API Specification
   https://springdoc.org/

3. 在 Database 內存放上萬筆資料

4. 使用 python locust 對  GET API 做壓力測試
   模擬五百位使用者同時呼叫                                      
   產出測試報告
   Reference :
   https://locust.io/

## Start Demo App
- `docker-compose up`

## Remove All
- `docker compose down --rmi all`

## Python Test POST/GET Method
- `docker-compose exec python-env python ./script/post_get_test.py`
![GET/POST Testing](./doc/post_get_tests.png)