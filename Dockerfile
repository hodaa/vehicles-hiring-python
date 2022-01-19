# start by pulling the python image
FROM python:3.8-alpine

WORKDIR /www/var
COPY ./requirements.txt /www/var/requirements.txt
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
