# Deriving from python 3.12
FROM python:3.12.5-bookworm

# Working directory
WORKDIR /usr/app

# Making directory
RUN mkdir ./docker-volume

COPY file_reader.py ./

CMD exec "python3 ./file_reader.py > ./docker-volume/results.txt"

VOLUME [ "./docker-volume" ]