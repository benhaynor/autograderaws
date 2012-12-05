import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import os
import sys
import mydatastore

class UserLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'User',
                                   [('name', lambda x: x.decode('utf-8')),
                                    ('email', lambda x: x.decode('utf-8')),
                                    ('pw_hash', lambda x: x.decode('utf-8'))
                                    ])

class GradeLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Grade',
                                   [('name', str),
                                    ('grade', float),
                                    ('assignment', int)
                                    ])

loaders = [UserLoader, GradeLoader]
