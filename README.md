# sample-flask-mod-wsgi-aws
A Sample Flask based Mod-WSGI script for deployment on Redhat or AWS Linux with Apache (httpd)


Yum installs:

1) Install apache:
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-centos-6
2) Install mod-wsgi: 
https://pythonhosted.org/baruwa/community/apache-wsgi.html

3) Add the application at the location /var/www/. So the main folder FlaskApp will be located at /var/www/FlaskApp.
Refer to this resource:
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

4) Setup the virtualenv at FlaskApp/FlaskApp/venv. Refer to the same resource above.

5) Step 4 for the resource above will be different than the current file. Make the configuration file, FlaskApp.conf.
Deploy this at /etc/httpd/conf.d/FlaskApp.conf.
Make sure the config file makes the python site-packages path in WSGI point to virtualenv.

6) Make the WSGI file at the same location as in the git repo. Observe that it has a couple of lines that activate the virtualenv.

7) Run the command: sudo service httpd restart.
This will restart the server.

8) Now hit the public ip address as http://<public_ip_address>

Other resources:
a) http://overskylab.blogspot.com/2014/05/install-flask-with-modwsgi-on-centos-6.html
b) http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/#configuring-apache
c) https://subhoworld.wordpress.com/2014/10/11/setting-up-a-web-server-for-flask-app-deployment-in-mod_wsgi-part-2/
d) https://stackoverflow.com/questions/27450998/run-mod-wsgi-with-virtualenv-or-python-with-version-different-that-system-defaul
e) https://stackoverflow.com/questions/4420218/see-anything-wrong-with-my-attempt-to-get-flask-running-mod-wsgi-virtualenv

