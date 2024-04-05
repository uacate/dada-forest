ARG PG_MAJOR=16
FROM postgres:$PG_MAJOR
ARG PG_MAJOR
# COPY ./pgvector /tmp/pgvector
# COPY ./bin/initdb.sh /docker-entrypoint-initdb.d/initdb.sh

RUN apt-get update && \
		apt-mark hold locales && \
		# apt-get install -y --no-install-recommends build-essential postgresql-server-dev-$PG_MAJOR && \
		# cd /tmp/pgvector && \
		# make clean && \
		# make OPTFLAGS="" && \
		# make install && \
		# mkdir /usr/share/doc/pgvector && \
		# cp LICENSE README.md /usr/share/doc/pgvector && \
		# rm -r /tmp/pgvector && \
		# apt-get remove -y build-essential postgresql-server-dev-$PG_MAJOR && \
		apt-get autoremove -y && \
		# apt-mark unhold locales && \
		rm -rf /var/lib/apt/lists/*


# https://medium.com/@johannes.ocean/setting-up-a-postgres-database-with-the-pgvector-extension-10ab7ff212cc