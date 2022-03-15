FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r pyyaml pandas

CMD [ "python", "./f1_stream_selector.py" ]