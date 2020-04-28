FROM python:3.7.7-alpine3.11 
RUN echo 'Launch DJ python service.' \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U \
    && pip install django==2.2.6
EXPOSE 8000
COPY . /home/site
CMD ["python", "/home/site/manage.py", "runserver","0.0.0.0:8000"]
