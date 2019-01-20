#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年12月10日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: WebEngineView
@description: 
'''
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class WebEngineView(QWebEngineView):

    DomainCookies = {}  # 存放domain的key-value
    PathCookies = {}  # 存放domain+path的key-value

    def __init__(self, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore(
        ).cookieAdded.connect(self.onCookieAdd)
        self.loadFinished.connect(self.onLoadFinished)

    def onLoadFinished(self):
        print("*****AllDomainCookies:", self.getAllDomainCookies())
        print("*****AllPathCookies:", self.getAllPathCookies())
        print("*****alyl.vip cookie:", self.getDomainCookies(".alyl.vip"))
        print("*****alyl.vip / path cookie:",
              self.getPathCookies(".alyl.vip/"))

    def getAllDomainCookies(self):
        return self.DomainCookies

    def getDomainCookies(self, domain):
        return self.DomainCookies.get(domain, {})

    def getAllPathCookies(self):
        return self.PathCookies

    def getPathCookies(self, dpath):
        return self.PathCookies.get(dpath, {})

    def onCookieAdd(self, cookie):
        '''
        :param cookie: QNetworkCookie
        '''
        domain = cookie.domain()
        path = cookie.path()
        name = cookie.name().data()
        value = cookie.value().data()
        if domain in self.DomainCookies:
            _cookie = self.DomainCookies[domain]
            _cookie[name] = value
        else:
            self.DomainCookies[domain] = {name: value}
        domain_path = domain + path
        if domain_path in self.PathCookies:
            _cookie = self.PathCookies[domain_path]
            _cookie[name] = value
        else:
            self.PathCookies[domain_path] = {name: value}
#         print("add cookie:", cookie.domain(),
#               cookie.path(), cookie.name(), cookie.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebEngineView()
    w.show()
    w.load(QUrl("http://alyl.vip"))
    sys.exit(app.exec_())
