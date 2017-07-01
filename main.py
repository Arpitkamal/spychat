# import  is used take  details from spy_details file
from spy_details import spy,Spy,chatmessage,friends,colors
# for display date,time,year datetime library is imported
from datetime import datetime
# for encryption and decryption of secret message in image
from steganography.steganography import Steganography


#working on spy chat 1
print"hello"
#start working on spy chat
print"let's get started"

# whwn user wants old status by default  we take some old status
STATUS_MESSAGE=["hello python","i am in class ","spy love pthon "]

# function to delete friend from friends if spy is speaking to much
def average_chat(sel_friend,text):
    if len(text.split())>100:
        print "spy is speaking to much "
        del friends[sel_friend]


# function for special secret world send by sender spy it will handle
def check_special_words(a):
    if (a=="NEW"):
        print colors.RED+"spy have new mission "
    elif (a=="SAVE ME"):
        print colors.RED+"spy is in danger"
    elif a=="PROGRESS":
        print colors.RED+"spy's missin is in progress"
    elif a=="WORK":
        print colors.RED+"spy is working  on other mission"
    else:
        print colors.ORANGE+"no special word used by sender"+colors.BLACK



#function to send encrypted message
def send_message():
    friend_choice=select_frined()
    original_image=raw_input("what is the name of the image ?")
    output_image='output.jpg'
    text=raw_input("what do you want to say ?")
    text=text.upper()
    Steganography.encode(original_image,output_image,text)
    # call the chatmessage class by new_chat object
    new_chat=chatmessage(text,True)
    # adding the text to selected friend in chats(in spy class)
    friends[friend_choice].chats.append(new_chat)
    print "your secret message is ready "


#function to read encrypted message by decoding
def read_message():
    sender=select_frined()
    output_path=raw_input("what is name of file ?")
    # store secret text in secret_text
    secret_text=Steganography.decode(output_path)
    secret_text=secret_text.upper()
    # to handle no secret message
    if len(secret_text)==0:
        print "there is no secret message"
    else:
        average_chat(sender,secret_text)
        # to print no of words split the secret_text then find lenght by len() && split() is important otherwise error
        print "he no of words in secret message :"+str(len(secret_text.split()))
        # calling check_special_words for checking special secret message in secre_ttext
        check_special_words(secret_text)
        print "the secret text is :"+secret_text
        #calling chatmessage class by new_chat object
        new_chat=chatmessage(secret_text,False)
        #appending the new_chat in chats for selcted friend
        friends[sender].chats.append(new_chat)
        print "your secret message has been saved "

# function for reading chat history
def read_chat_history():
    read_for=select_frined()
    print "in the read chat"
    for i in friends[read_for].chats:
        #if send_by_me=True then it will show my message
            if (i.sent_by_me==True):
                print colors.BLUE+"Time:[%s]"%(i.time.strftime("%d %B %Y"))+colors.RED+"you said:"+colors.BLACK+"%s"%(i.message)
            else:
                print colors.BLUE+"Time:[%s]"%(i.time.strftime("%d %B %Y")) +colors.RED+"%s:" %(friends[read_for].name)+colors.BLACK+"%s" %(i.message)


#function use to select one friend from many friends
def select_frined():
    item_position = 0
    # showing the all friends from friends dictionary
    for friend in friends:
        print "%d. %s age: %s with ratting %.2f is online" %(item_position,friend.name,friend.age,friend.rating)
        item_position=item_position+1
    friend_choice=int(raw_input("choose your friend"))
    return friend_choice

#function for age validation
def age_val(spy_age):
    age_validation=True
    if spy_age>12 and spy_age<=50:
        age_validation=True
        print "spy is of valid age"
    else:
        age_validation=False
        print"sorry!! you are not of a correct age to be a spy"
    return (age_validation)

# funtion for name validation
def name_vali(spy_name):
        # initialy we set validation as true if name is invalid we will set validation=False
        # when name is valid set validation to true
        validation=True
        if (spy_name.isspace()):
            validation=False
            print "Invalid! you enter space \n A spy need to have valid name "
        elif (spy_name.isdigit()):
            validation=False
            print "Invalid! you enter digit \n A spy need to have valid name "
        elif (spy_name.isalpha()):
            validation=True
        elif len(spy_name)==0:
            validation=False
            print "A spy need to have valid name , please try again "
        # returning  validation
        return (validation)


# add_friend() function is use to add frinds
def add_friend():
    # new_friend={} dictionary is created to store friends data
    new_friend=Spy('','',0,0.0)

    new_friend.name=raw_input("please ! add your friends name ? ")
    new_friend.salutation=raw_input("Are they MR OR MS")
    new_friend.name=new_friend.salutation+" "+new_friend.name
    new_friend.age=int(raw_input("enter age ?"))
    new_friend.rating=float(raw_input("spy rating ?"))

    if len(new_friend.name)>0:
        print "spy name is not empty"
        if (name_vali(new_friend.name)==True) and age_val(new_friend.age):
            friends.append(new_friend)

    else:
        print "sorry invalid entry . we can't add spy with details you provided"
    # return the no of friends in dictionary
    return len(friends)





# add_status() function is use to add status like in whatsapp
def add_status(current_status_message):
    if current_status_message !=None:
        print "your current status is:"+current_status_message
    else:
        print "you don't have any current messeage"
    question=raw_input("do you want to select status from old status? y/n")
    # if user want to add new status
    # then append new_status to STATUS_MESSAGE
    if question.upper()=="N":
        new_status=raw_input("enter your new status ")
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)
            return(new_status)
        else:
            print "invalid new status need to be enter "
    # if user want to select from STATUS_MESSAGE
    elif question.upper()=="Y":
        # showing all old status
        for i in range(len(STATUS_MESSAGE)):
            print str(i)+"."+STATUS_MESSAGE[i]
        message_selection=int(raw_input("\n choose from above status"))
        # if user enter more than the no of  status in STATUS MESSAGE
        if len(STATUS_MESSAGE)>message_selection:
            update_status_message=STATUS_MESSAGE[message_selection]
        else:
            print "selected message is not in older status "
        return update_status_message

# function for start chat with spy
def start_chat(spy):
    current_status_messesge=None
    print "your current status is "+str(current_status_messesge)
    show_menu=True
    # using while loop so that application does't close untill user whants to exit
    while show_menu:
         menu_choice= "whant you want to do ? \n1 add a status update \n2 add friend \n3 Send a secret message \n4 read a secret message \n5 read chat from user \n6 close application "
         menu_choice=raw_input(menu_choice)


         if len(menu_choice)>0:
             menu_choice=int(menu_choice)

             if menu_choice==1:
                 print "You choose update the status "
                 current_status_messesge=str(add_status(current_status_messesge))
                 print "Your selected status is:"+current_status_messesge
             elif menu_choice==2:
                 number_of_friend=add_friend()
                 print"You have %s friends" %(number_of_friend)
             elif  menu_choice==3:
                 send_message()
             elif menu_choice==4:
                  read_message()
             elif menu_choice==5:
                 read_chat_history()
             else:
                show_menu=False


# taking input from user
# so that user what to continue with existing spy or want new spy
question=raw_input("do you want to continue with "+spy.salutation+" "+ spy.name + " (y/n)")
# question.upper() is use so that if user enter in lower case it will convert to uppercase
if question.upper()=="Y":
    #calling to start_chat function
    # user wants existing spy
    start_chat(spy)
else:
    spy = {
        'name':'',
        'salutation':'',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
    }
    # user wants new spy
    spy_name=raw_input("welcome to spy chat, you must tell me your name first  ?")
    spy_name=spy_name.upper()
    if len(spy_name)>0:
        print "spy name is not empty"
       # calling name_validation function
        if (name_vali(spy_name)==True):
            print "validation is successful ! you enter valid name. "

            #using placeholder
            print "welcome %s glad to have you back with us" %(spy_name)
            #take input from spy mr or miss
            # store it in variable spy_salutation
            spy_salutation=raw_input("what should i call you (MR or MISS) ")
            print spy_salutation+" "+spy_name
            #update the variable spy_name
            spy_name=spy_salutation+" "+spy_name
            print "Alright "+spy_name+" i'd like know little bit more before we proceed..."
            #
            #take input from user
            # raw_input take age as string to convert it into int we use int()
            spy_age=int(raw_input("enter your age "))
            #spy age is between 12 to 50 otherwise reject
            #Nested if
            if (age_val(spy_age)==True):
                spy_rating=float(raw_input("enter your spy ratting"))
                if spy_rating>4.5:
                    print"great ace"
                elif spy_rating<=3.5 and spy_rating>=4.5:
                    print"you are one of good one"
                elif spy_rating<=2.5 and spy_rating>=3.5:
                    print"you can always do better "
                else:
                    print "you can always use somebody in office"

                # initialise spy as online
                spy_online = True
                # Using placeholder
                print colors.GREEN+"authentication is complete .Welcome %s age: %s  ratting: %s proud to have you onboard" % (
                spy_name, spy_age, spy_rating)+colors.BLACK

                start_chat(spy)
            else:
                print "sorry!! please try again"

        else:
            print "sorry !! please try again "
    else:
        print "A spy need to have valid name , please try again!!"
