import os
from base64 import urlsafe_b64encode as e64

import click
import json


@click.command()
def newsite():
    '''create a new site'''
    pass

@click.command()
def newpost():
    '''create a new post'''
    pass

@click.command()
@click.argument('user')
@click.argument('password',default=None)
def newuser(user,password):
    pw = password if password else e64(os.urandom(9)).decode('ascii')
    print(json.dumps(dict(username=user,password=pw)))
