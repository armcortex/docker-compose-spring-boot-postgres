# docker-compose-spring-boot-postgres
## Target
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
   模擬五百位使用者同時呼叫, 產出測試報告
   Reference: https://locust.io/

## Step 0. Init
Load parameters into shell environments
- `source .env`

## Step 1. Start Demo App
- `docker-compose up`

Make sure `docker ps`, 3 container is up
![Docker PS](./doc/docker_ps.png)

Demo App Home Page: http://localhost:8080
![Demo App](./doc/demo_app_homepage.png)


## Step 2. Test POST/GET Method
- `docker-compose exec python-env python ./script/tests_post_get_method.py`

Result
![GET/POST Testing](./doc/post_get_tests.png)


## Step 3. Check database table content
- `docker-compose exec  postgresdb psql -U $POSTGRESDB_USER -d $POSTGRESDB_DATABASE -c "SELECT t.* FROM public.items t LIMIT 5;"`

After step 2., it should have 5 data in the table.

Result
![Database Query](./doc/db_query.png)

## Step 4. Check OpenAPI 3.0
swagger-ui
- URL: http://localhost:8080/swagger-ui/index.html

Result
![OpenAPI Spec](./doc/openapi_spec.png)

api-docs
- URL: http://localhost:8080/v3/api-docs

Result
![API Docs](./doc/api-docs.png)

## Step 4. Insert 10K data into Database
- Python lib Method with multi-processing
  - `docker-compose run python-env python ./script/insert_data_python.py`

Result
![Insert 10k data](./doc/insert_10k.png)

## Step 5. Check Table Count
- `docker-compose exec  postgresdb psql -U $POSTGRESDB_USER -d $POSTGRESDB_DATABASE -c "SELECT COUNT(*) FROM public.items;"`

Result
![Check Table Count](./doc/check_table_count.png)

## Step 6. Locust Stress Test
For CLI
- ` docker-compose exec python-env /bin/bash -c "locust -f ./script/locust_items_test.py --headless --users 500 --spawn-rate 100 -H http://app:8080 --run-time 10m"`

For WebUI
- ` docker-compose exec python-env /bin/bash -c "locust -f ./script/locust_items_test.py --users 500 --spawn-rate 100 -H http://app:8080 --run-time 10m"`

Result: RPS 166<br>
500 User Statistics
![Locust Statistics](./doc/locust_chart_500_user.png)

500 User Chart
![Locust Chart](./doc/locust_chart_500_user.png)


## Remove All
- `docker-compose down --rmi all`

## Helper scripts
Some helper scripts to make life easier
- [Load Database Table](./script/import_table.sh): `./script/import_table.sh`
- [Export Database Table](./script/export_table.sh): `./script/export_table.sh`
- [Simple Test POST Script](./script/tests_post_method.sh): `./script/tests_post_method.sh`
- [Simple Test GET Script](./script/test_get_method.sh): `test_get_method.sh`
