FROM centos/python-36-centos7
RUN pip install flask
RUN pip install waitress
#RUN waitress-serve --call 'flaskr:create_app' 
#RUN pip install Crypto
#RUN pip install pycryptodome
RUN pip install pycrypto
#EXPOSE 5000/tcp
ADD Flask_api.py .
CMD ["python","./Flask_api.py"]
#CMD ["uwsgi","app.ini"]
