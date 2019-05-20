
class Editor1:
    def execute(self):
        print("compile")
        print("run")

class Editor2:
    def execute(self):
        print("spell check")
        print("debug")
        print("compile")
        print("run")
class Laptop:
    def show(self,editor):
        editor.execute()

ed1=Editor1()
ed2=Editor2()

l1=Laptop()
l1.show(ed2)
