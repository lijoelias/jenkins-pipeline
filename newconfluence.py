#!/usr/bin/python

#from __future__ import with_statement
#import sys, string, xmlrpclib, re, os

from __future__ import with_statement
import sys
import os
from xmlrpc.client import ServerProxy, Binary

if len(sys.argv) < 5:
    exit("Usage: " + sys.argv[0] + "test testpage json test.json");



spacekey = sys.argv[1];
pagetitle = sys.argv[2];
contentType = sys.argv[3];
filename = sys.argv[4];

cwd = os.getcwd() # Get the current working directory (cwd)
files = os.listdir(cwd) # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, 'help_en.pdf')

with open(filename, 'rb') as f:
    data = f.read(); # slurp all the data



server = xmlrpclib.ServerProxy('https://lijoelias.atlassian.net/wiki/rest/api/content');
token = server.confluence1.login('lijoelias@gmail.com', 'Pappalil@97510');
page = server.confluence2.getPage(token, spacekey, pagetitle);
if page is None:
    exit("Could not find page " + spacekey + ":" + pagetitle);


attachment = {};
attachment['fileName'] = os.path.basename(filename);
attachment['contentType'] = contentType;

server.confluence1.addAttachment(token, page['id'], attachment, xmlrpclib.Binary(data));