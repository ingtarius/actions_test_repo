FROM python:3.10-slim
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD ./src/issues.py /issues.py
CMD ["/issues.py"]
