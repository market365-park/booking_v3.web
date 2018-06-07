from .base import *
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

DATABASES = {
    'ldap': {
        'ENGINE': 'ldapdb.backends.ldap',
        'NAME': 'ldap://192.168.56.101',
        'USER': 'cn=admin,dc=marke,dc=io',
        'PASSWORD': 'duffufkckaRo0',
    },

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = ['ldapdb.router.Router']

AUTH_LDAP_SERVER_URI = "ldap://192.168.56.101"

AUTH_LDAP_BIND_DN = "cn=admin,dc=marke,dc=io"
AUTH_LDAP_BIND_PASSWORD = "duffufkckaRo0"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=marke,dc=io", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "cn",
    "last_name": "sn",
    "email": "mail",
    "phone": "telephoneNumber",
	"username": "uid",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
