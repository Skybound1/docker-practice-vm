FROM python:3.6-alpine

ADD requirements.txt /
RUN pip install -r requirements.txt
ADD code.py /

EXPOSE 80
CMD ["python", "/code.py"]
