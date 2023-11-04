source ../.env

docker-compose exec postgresdb psql \
  -U ${POSTGRESDB_USER} \
  -d ${POSTGRESDB_DATABASE} \
  -p ${POSTGRESDB_DOCKER_PORT} \
  -f /app/sample/dumpfile.sql
