FROM nginx:1.16-alpine
RUN apk update
RUN apk add py-pip

RUN pip install xlrd
RUN pip install python-dateutil
#RUN pip install reportlab
RUN pip install flask_bootstrap

COPY . /usr/share/nginx/html
#COPY . /usr/src/app/
#WORKDIR /app
