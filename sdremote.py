#
# Impress Remote Control protocol impl
#

import socket

class SDRemoteClient():
    def __init__(self):
        self.sock       = None
        self.addr       = ('localhost', 1599)
        self.authorised = False

    def start (self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.addr)
        self.sock.setblocking(False)
        self.send("LO_SERVER_CLIENT_PAIR\nLibreSign2\n12345\n\n")

    def send (self, data):
        sent = self.sock.send(data.encode('utf-8'))
        print("sent", sent)

    def receive (self):
        # TODO handle disconnect
        try:
            data = self.sock.recv(4096)
            self.handle_message(data.decode('utf-8').split('\n'))
        except:
            pass

    def handle_message (self, data):
        print(data)
        msg = data[0]

        # we need to input our pin manually in libreoffice
        if 'LO_SERVER_VALIDATING_PIN' == msg:
            pass

        # authorised
        elif 'LO_SERVER_SERVER_PAIRED' == msg:
            # TODO compare server version?
            # NOTE/TODO this also contains slideshow_finished, slideshow_info
            self.authorised = True

        elif 'slideshow_started' == msg:
            pass

        elif 'slideshow_finished' == msg:
            pass

        elif 'slide_updated' == msg:
            pass

        elif 'slideshow_info' == msg:
            pass

        # base64 preview image, ignore
        elif 'slide_preview' == msg:
            pass
        # slide notes, ignore
        elif 'slide_notes' == msg:
            pass

    def transition_next(self):
        self.sock.send('transition_next\n\n')

    def transition_previous(self):
        self.sock.send('transition_previous\n\n')

    def goto_slide(self, index):
        self.sock.send(f'goto_slide\n{index}\n')

    def presentation_start(self):
        self.sock.send('presentation_start\n\n')

    def presentation_stop(self):
        self.sock.send('presentation_stop\n\n')

    def presentation_resume(self):
        self.sock.send('presentation_resume\n\n')

    def presentation_blank_screen(self):
        self.sock.send('presentation_blank_screen\n\n')

