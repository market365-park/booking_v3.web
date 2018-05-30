from django.contrib.auth.models import AbstractUser
from django.db import models
from ldapdb.models.fields import CharField, IntegerField, ListField
import ldapdb.models

class User(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True)

# class LdapGroup(ldapdb.models.Model):
#     """
#     Class for representing an LDAP group entry.
#     """
#     # LDAP meta-data
#     base_dn = "ou=users,dc=marke,dc=io"
#     object_classes = ['User Account']
#
#     # posixGroup attributes
#     gid = IntegerField(db_column='gidNumber', unique=True)
#     name = CharField(db_column='cn', max_length=200, primary_key=True)
#     members = ListField(db_column='memberUid')
#
#     def __str__(self):
#         return self.name
#


class LdapUser(ldapdb.models.Model, models.Model):
    """
    Class for representing an LDAP user entry.
    """
    # LDAP meta-data
    base_dn = "ou=users,dc=marke,dc=io"
    object_classes = ['inetOrgPerson']
    USERNAME_FIELD = 'username'

    # inetOrgPerson
    first_name = CharField(db_column='givenName', verbose_name="Prime name")
    last_name = CharField("Final name", db_column='sn')
    email = CharField(db_column='mail')
    phone = CharField(db_column='telephoneNumber', blank=True)

    username = CharField(db_column='uid', primary_key=True)
    password = CharField(db_column='userPassword')

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def set_password(self):
        return self.password
