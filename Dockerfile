FROM python:3.10-slim
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD ./get_all_issues.py /get_all_issues.py
CMD ["/get_all_issues.py"]
