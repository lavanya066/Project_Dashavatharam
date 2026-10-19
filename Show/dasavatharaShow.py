class DashavataraShow:

    def __init__(self, controller):
        self.controller = controller
        self.avatars = []

    def add_avatar(self, avatar):
        self.avatars.append(avatar)

    def play(self):

        print()
        print("================================")
        print("       DASHAVATARA SHOW")
        print("================================")

        for avatar in self.avatars:
            avatar.play(self.controller)

        print()
        print("================================")
        print("         SHOW COMPLETE")
        print("================================")