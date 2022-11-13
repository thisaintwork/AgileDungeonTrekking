
ssh root@209.97.148.138
root@209.97.148.138's password: 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Nov 13 21:43:15 UTC 2022

  System load:  0.0                Users logged in:       0
  Usage of /:   10.9% of 24.05GB   IPv4 address for eth0: 209.97.148.138
  Memory usage: 39%                IPv4 address for eth0: 10.17.0.5
  Swap usage:   0%                 IPv4 address for eth1: 10.108.0.2
  Processes:    110

0 updates can be applied immediately.


********************************************************************************

Welcome to DigitalOcean's 1-Click Django Droplet.
To keep this Droplet secure, the UFW firewall is enabled.
All ports are BLOCKED except 22 (SSH), 80 (HTTP), and 443 (HTTPS).

Access the Django admin site
    URL: http://209.97.148.138/admin
    User: django
    Pass: XXXX

Use these SFTP credentials to upload files with FileZilla/WinSCP/rsync:
    Host: 209.97.148.138
    User: django
    Pass: XXXX

Django is configured to use Postgres as its database. Use the following
credentials to manage the database:
    Database: django
    User:     django
    Pass:     XXXX

In a web browser, you can view:
 * The Django 1-Click Quickstart guide: https://do.co/3bY3b67#start
 * The new Django site: http://209.97.148.138

On the server:
  * The Django application is served from /home/django/django_project
  * The Django passwords and keys are saved in /root/.digitalocean_passwords
  * Certbot is preinstalled. Run it to configure HTTPS.

For help and more information, visit https://do.co/3bY3b67

********************************************************************************
To delete this message of the day: rm -rf /etc/update-motd.d/99-one-click
Last login: Sun Nov 13 21:43:16 2022 from 140.221.247.123
root@django-s-1vcpu-1gb-nyc3-01:~# 

