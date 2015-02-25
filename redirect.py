#!/usr/bin/python
import webapp
import random
import socket
usuario = socket.gethostname()


class miweb(webapp.webApp):
    def process(self, parsedRequest):
        rand = random.randint(1, 100000000)
        return ("302 Moved Temporarily", "<html><head><meta "
                + "http-equiv='Refresh' content=2; url=http://"
                + usuario + ":1235/" + str(rand)
                + "></head><body>" + str(rand) + "</body></html>\r\n")
if __name__ == "__main__":
    new_web = miweb(usuario, 1235)
