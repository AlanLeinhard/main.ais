FROM postgres:14.1
COPY ./docker-entrypoint.sh /
COPY . .


RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /db_create.py

RUN apt-get update && apt-get install -y python3
RUN python3 --version
USER postgres

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]