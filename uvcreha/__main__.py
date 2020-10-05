import morepath
from .app import BaseApp


def run():
    morepath.autoscan()
    morepath.run(BaseApp())


if __name__ == '__main__':
    run()
