from .base import *
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

DATABASES = {
    'ldap': {
        'ENGINE': 'ldapdb.backends.ldap',
        'NAME': 'ldap://10.12.14.78/',
        'USER': 'cn=admin,dc=connected-car,dc=io',
        'PASSWORD': 'devOps!23',
    },

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = ['ldapdb.router.Router']

AUTH_LDAP_SERVER_URI = "ldap://10.12.14.78"

AUTH_LDAP_BIND_DN = "cn=admin,dc=connected-car,dc=io"
AUTH_LDAP_BIND_PASSWORD = "devOps!23"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=connected-car,dc=io", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

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
