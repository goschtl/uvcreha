from more.chameleon import ChameleonApp
from more.transaction import TransactionApp
from more.basicauth import BasicAuthIdentityPolicy


class BaseApp(TransactionApp):
    pass


class HTMLApp(ChameleonApp, BaseApp):
    pass


class RESTApp(BaseApp):
    pass


@HTMLApp.template_directory()
def get_template_directory():
    return 'templates'


@HTMLApp.setting_section(section='chameleon')
def get_chameleon_settings():
    return {'debug': True}


@BaseApp.mount(path='/html', app = HTMLApp)
def mount_html_app():
    return HTMLApp()


@BaseApp.mount(path='/api', app = RESTApp)
def mount_rest_app():
    return RESTApp()


@BaseApp.identity_policy()
def get_identity_policy():
    return BasicAuthIdentityPolicy()


@BaseApp.verify_identity()
def verify_identity(identity):
    def user_has_password(username, password):
        if username == "cklinger" and password == "passwort":
            return True
    return user_has_password(identity.userid, identity.password)

from webob.exc import HTTPForbidden

@BaseApp.view(model=HTTPForbidden)
def make_unauthorized(self, request):
    @request.after
    def set_status_code(response):
        response.status_code = 401
        response.headers.extend({'WWW-Authenticate': 'Basic'})
    return "Unauthorized"
