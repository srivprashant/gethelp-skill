from mycroft import MycroftSkill, intent_file_handler


class Gethelp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gethelp.intent')
    def handle_gethelp(self, message):
        self.speak_dialog('gethelp')


def create_skill():
    return Gethelp()

