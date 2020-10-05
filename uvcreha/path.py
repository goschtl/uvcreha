from .app import BaseApp
from . import model


@BaseApp.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@BaseApp.path(model=model.Greeting, path='/greeting/{person}')
def get_greeting(person):
    return model.Greeting(person)
