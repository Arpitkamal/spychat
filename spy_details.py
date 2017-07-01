from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None


class chatmessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me= sent_by_me


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[91m'
    BLACK = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED='\033[31m'

spy=Spy('bond','Mr',20,4.8)

friend_one=Spy('arpit','MR',20,4.0)
friend_two=Spy('raja','MR',20,4.0)
friend_three=Spy('vivek','MR',21,4.8)

friends=[friend_one,friend_two,friend_three]

