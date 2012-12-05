''' Defines all my datastore entities
'''

from google.appengine.ext import db
from google.appengine.ext import blobstore
import re
from crypto import *

class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    @staticmethod
    def valid_username(username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username and USER_RE.match(username)
    
    @staticmethod
    def valid_password(password):
        PASS_RE = re.compile(r"^.{3,20}$")
        return password and PASS_RE.match(password)

    @staticmethod
    def valid_email(email):
        EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return not email or EMAIL_RE.match(email)

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)

    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email = None):
        pw_hash = make_pw_hash(name, pw)
        return User(name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u

class FileSubmission(db.Model):
    user_name = db.StringProperty(required = True)
    blob_key = blobstore.BlobReferenceProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    filename = db.StringProperty(required = True)

class Assignment(db.Model):
    name = db.StringProperty(required = True)
    blob_key = blobstore.BlobReferenceProperty(required = True)

class Grade(db.Model):
    name = db.StringProperty(required = True)
    grade = db.FloatProperty(required = True)
    assignment = db.IntegerProperty(required = True)
