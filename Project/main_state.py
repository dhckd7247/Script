import random
import os

from pico2d import *

from PyQt5 import QtCore, QtGui, QtWidgets
import game_framework
import start_state

name = "MainState"
image = None
def enter():
    global image
    image = load_image('resource/background.jpg')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DockWidget = QtWidgets.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(755, 724)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget"))




def exit():
    global image
    del(image)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

