source ../.env

docker-compose exec postgresdb pg_dump \
  --clean \
  -U ${POSTGRESDB_USER} \
  -t ${POSTGRESDB_TABLE} \
  -d ${POSTGRESDB_DATABASE} \
  -p ${POSTGRESDB_DOCKER_PORT} \
  > ../sample/dumpfile.sql
