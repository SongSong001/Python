#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# server.py


from wsgiref.simple_server import  make_server

from  t2 import  application
httpd=make_server('',8000,application)
httpd.serve_forever()