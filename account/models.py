from django.contrib.auth.models import AbstractUser
from django.db import models
from ldapdb.models.fields import CharField, IntegerField, ListField
import ldapdb.models

from passlib.hash import ldap_salted_sha1


class User(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True)


class LdapUser(ldapdb.models.Model, models.Model):
    object_classes = ['inetOrgPerson']
    USERNAME_FIELD = 'username'
    # base_dn = "ou=users,dc=connected-car,dc=io"
    base_dn = "ou=users,dc=marke,dc=io"
    first_name = CharField("Name", db_column='cn')
    last_name = CharField("Team", db_column='sn')
    email = CharField("E-mail", db_column='mail')
    phone = CharField("Phone", db_column='telephoneNumber', blank=True)

    username = CharField("Username", db_column='uid', primary_key=True)
    password = CharField(db_column='userPassword')

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def set_password(self, password):
        self.password = ldap_salted_sha1.encrypt(password)

    def get_absolute_url(self):
        return '/'
