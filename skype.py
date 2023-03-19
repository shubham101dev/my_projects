from skpy import Skype
import os.path
slogin=Skype("nikubrother1001@outlook.com","Shubham@1001")
contact=slogin.contacts["live:.cid.97efd09b80cf4773"]
with open("C:/Users/nikub/OneDrive/Pictures/project.png","rb")as f:
    contact.chat.sendFile(f,"project.png",image=True)
group=slogin.chats.create(["live:.cid.97efd09b80cf4773"])



contact=slogin.contacts["live:.cid.97efd09b80cf4773"]
contact.chat.sendMsg("welcome good morning")

for i in contact:
    print(i)
