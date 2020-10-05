from .app import BaseApp, HTMLApp, RESTApp
from . import model

class ViewPermission(object):
    pass


@BaseApp.permission_rule(model=model.Root, permission=ViewPermission)
def document_view_permission(identity, model, permission):
    return True


@HTMLApp.html(model=model.Root, template='index.pt', permission=ViewPermission)
def view_root(self, request):
    return {
        'greetings': self.greetings,
        'request': request,
    }



@HTMLApp.html(model=model.Root, name="edit", template='edit.pt', permission=ViewPermission)
class Edit(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self):
        return {
            'greetings': self.context.greetings,
            'request': self.request,
        }

#def edit(self, request):
#    return {
#        'greetings': self.greetings,
#        'request': request,
#    }




@RESTApp.json(model.Root, permission=ViewPermission)
def get_root(self, request):
    return {'class': self.__class__ }

