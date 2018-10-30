#!/usr/bin/env bash

which pip
if [ $? != 0 ]
then
    yum -y install python2-pip.noarch
fi
yum -y install net-tools.x86_64

echo "Get public ip geographic location......"
#ip_info=$(curl ipinfo.io)
if [ $(echo $ip_info|grep "country"|grep "CN"|wc -l) == 1 ]
then
    echo "The server's public ip locate in China."
    echo "Pip source is being changed to douban."
    cat > ~/.pip/pip.conf << END
[global]
timeout = 60
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
[install]
use-mirrors = true
mirrors = http://pypi.douban.com
trusted-host = pypi.douban.com
END
fi

package_num=`pip list installed --format=columns|grep shadowsocks|wc -l`
if [ $package_num != 2 ]
then
    echo "Install shadowsocks and shadowsocks-sdk"
    pip install shadowsocks
    pip install shadowsocks-sdk
fi

echo "Startup shadowsocks"
ssserver -d stop > /dev/null 2>&1
ssserver --manager-address 127.0.0.1:62500 -p 65530 -k asdfjl24rojosfgf -d start > /dev/null 2>&1
if [ $? != 0 ]
then
    echo "Shadowsocks start up failed"
fi

echo "Install django if django not installed"
pip install django > /dev/null 2>&1
if [ $? != 0 ]
then
    echo "Django install failed"
fi

#allow_hosts="u'127.0.0.1'"
#ip a|grep inet|grep -v inet6|grep -v "127.0.0.1"| \
#    awk -F' ' '{print $2}'|cut -d '/' -f 1|while read line
#do
#    allow_hosts="${allow_hosts},u'${line}'"
#    sed -i "s/^ALLOWED_HOSTS.*]/ALLOWED_HOSTS = [${allow_hosts}]/g" ssapi/settings.py
#done

./tc.sh
iptables -I INPUT -p tcp --dport 8100 -j ACCEPT
python manage.py runserver 0.0.0.0:8100 > /var/log/django/ssapi.log 2>&1 &
#python manage.py runserver 0.0.0.0:8100

