#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年3月30日
@author: Irony."[讽刺]
@site: alyl.vip, orzorz.vip, irony.coding.me , irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: TestQSharedMemory
@description: 
'''
from PyQt5.QtWidgets import QWidget


from Application import SharedApplication  # @UnresolvedImport

__version__ = "0.0.1"

class Widget(QWidget):
    
    def __init__(self,*args,**kwargs):
        super(Widget, self).__init__(*args,**kwargs)

if __name__ == "__main__":
    import sys,os
    print(os.getpid())
    app = SharedApplication(sys.argv)
    if app.isRunning():
        print("app have already running")
        sys.exit(0)
    w = Widget()
    w.show()
    sys.exit(app.exec_())