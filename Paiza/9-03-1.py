class Greeting:

    def __init__(self):

        self.msg = "hello"

        self.target = "paiza"


    def say_hello(self):

        print(self.msg + " " + self.target)


class Hello(Greeting):

        def say_hello(self,a):

        print(self.msg+" "+a)


player = Hello()

player.say_hello("python")