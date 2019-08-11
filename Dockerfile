
FROM centos:7
MAINTAINER jaimevalero78@yahoo.es

RUN rpm -ivh https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install  iputils mysql-server wget mysql vim cpanm gcc git  && yum clean all
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y yum-utils centos-release-scl
RUN yum-config-manager --enable remi-php56

RUN yum install -y rh-python36  vim php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo ansible sshpass && yum clean all
RUN scl enable rh-python36 "pip install --upgrade pip"

RUN mkdir /app /var/log/inventario/ /var/spool/uploads


ADD app /app
ADD env /app
RUN find /app

RUN scl enable rh-python36 "pip install -r /app/requirements.txt"

ENTRYPOINT /bin/bash /app/entrypoint.sh
