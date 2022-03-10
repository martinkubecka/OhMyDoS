# How To Install WordPress with LAMP

```
$ sudo apt update
$ sudo apt install apache2 libapache2-mod-php
$ sudo apt install mariadb-client mariadb-server
$ sudo apt install php php-mysql php-xml
$ cd /var/www/html
$ rm *

$ sudo mysql -u root -p
> show databases;
> CREATE DATABASE wordpress;
> CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'password';
> GRANT ALL ON wordpress.* TO 'wpuser'@'localhost';
> FLUSH PRIVILEGES;
> exit

### pick release and download it
### https://wordpress.org/download/releases/
### e.g. wget https://wordpress.org/wordpress-5.3.tar.gz -o wordpress-5.3.tar.gz

$ cd Downloads
$ gunzip wordpress.tar.gz
$ tar xvf wordpress.tar
$ sudo cp -r wordpress /var/www/html
$ cd /var/www/html
$ sudo chown -R www-data:www-data /var/www/html
$ sudo find /var/www/html -type d -exec chmod 755 {} \;
$ sudo find /var/www/html -type f -exec chmod 644 {} \;

$ sudo systemctl restart apache2

### open localhost in your browser and follow the instructions
```