# Deriving from python 3.12
FROM python:3.12.5-bookworm

# Working directory
WORKDIR /usr/app

# Making directory
RUN mkdir ./results

COPY results ./results

COPY file_reader.py ./

CMD [ "python3", "./file_reader.py" ]

VOLUME [ "./results" ]
