#Description: Linux Academy training fabfile.py
from fabric.api import *
import fabric.api

@fabric.api.task
def run_chef():
    '''Runs chef-client on host'''
    results = run('sudo chef-client')
    if results is not True:
        print(results)

@fabric.api.task
def patch():
    '''Patch host, reboot, and then run chef'''
    results = run('sudo package-cleanup --oldkernels --count=1 -y && sudo yum makecache && sudo yum update -y', pty=False)
    if results is not True:
        print(results)

    print('[{0}] Rebooting system...'.format(fabric.api.env.host))
    fabric.api.reboot(wait=300)

    run_chef()

@fabric.api.task
def uptime():
    '''Uptime on host'''
    run("uptime", pty=True)

@fabric.api.task
def whoami():
    run("whoami", pty=True)

@fabric.api.task
def host_name():
    run("hostname", pty=True)

@fabric.api.task
def hello_world():
    print("Hello world!!!")

@fabric.api.task
def update_server():
    sudo("yum -y upgrade", pty=True)

@fabric.api.task
def nginx_status():
    '''Nginx status'''
    sudo("systemctl status nginx", pty=True)

@fabric.api.task
def nginx_stop():
    '''Stop Nginx'''
    sudo("systemctl stop nginx", pty=True)
    nginx_status()

@fabric.api.task
def nginx_start():
    sudo("systemctl start nginx", pty=True)
    nginx_status()

@fabric.api.task
def install_fabric():
	#This is intended to install fabric on centos7
	#Enabling EPEL repo to install pip on Centos 7
	sudo("yum --enablerepo=extras install epel-release", pty=True)
	#Install pip
	sudo("yum install python-pip", pty=True)
	#Install fabric
	sudo("yum install fabric", pty=True)
