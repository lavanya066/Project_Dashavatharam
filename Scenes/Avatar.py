class Avatar:

    def __init__(self, name, actions):

        self.name = name
        self.actions = actions

    def play(self, controller):

        print()
        print("================================")
        print(f"          {self.name}")
        print("================================")

        for action in self.actions:

            action.execute(controller)