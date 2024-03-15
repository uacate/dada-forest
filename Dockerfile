# FROM postgres:16.2-alpine
# RUN apk add git build-base clang llvm13-dev
# WORKDIR /home
# RUN git clone --branch v0.6.1 https://github.com/pgvector/pgvector.git
# WORKDIR /home/pgvector
# RUN make
# RUN make install

# ARG PG_MAJOR=16
# FROM postgres:$PG_MAJOR
# ARG PG_MAJOR

# COPY . /tmp/pgvector

# RUN apt-get update && \
# 		apt-mark hold locales && \
# 		apt-get install -y --no-install-recommends build-essential postgresql-server-dev-$PG_MAJOR && \
# 		cd /tmp/pgvector && \
# 		make clean && \
# 		make OPTFLAGS="" && \
# 		make install && \
# 		mkdir /usr/share/doc/pgvector && \
# 		cp LICENSE README.md /usr/share/doc/pgvector && \
# 		rm -r /tmp/pgvector && \
# 		apt-get remove -y build-essential postgresql-server-dev-$PG_MAJOR && \
# 		apt-get autoremove -y && \
# 		apt-mark unhold locales && \
# 		rm -rf /var/lib/apt/lists/*

ARG PG_MAJOR=16
FROM postgres:$PG_MAJOR
ARG PG_MAJOR

COPY ./pgvector /tmp/pgvector

RUN apt-get update && \
		apt-mark hold locales && \
		apt-get install -y --no-install-recommends build-essential postgresql-server-dev-$PG_MAJOR && \
		cd /tmp/pgvector && \
		make clean && \
		make OPTFLAGS="" && \
		make install && \
		mkdir /usr/share/doc/pgvector && \
		cp LICENSE README.md /usr/share/doc/pgvector && \
		rm -r /tmp/pgvector && \
		apt-get remove -y build-essential postgresql-server-dev-$PG_MAJOR && \
		apt-get autoremove -y && \
		apt-mark unhold locales && \
		rm -rf /var/lib/apt/lists/*