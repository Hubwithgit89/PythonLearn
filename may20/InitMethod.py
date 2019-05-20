class Computer:
    def __init__(self,cpu,ram):
         self.cpu=cpu
         self.ram=ram

    def config(self):
        print("CONFIG is cpu={}, ram={}".format(self.cpu,self.ram) )

c1= Computer("i5","8GB")
c2= Computer("i7","16GB")


c1.config()
c2.config()
