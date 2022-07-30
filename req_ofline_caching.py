# import requests
# import json
# import os

# file=os.path.exists("requets.json")
# if file==False:

#     url=requests.get('https://api.merakilearn.org/courses')
#     r=json.loads(url.text)
#     # print(r)
#     with open("requets.json","w") as f:
#         json.dump(r,f,indent=4)
#     i=0
#     while i<len(r):
#         print(i+1,r[i]["name"],r[i]["id"])
#         i+=1
#     print(" ")    
#     course_no=int(input("select which course you want display  :"))
#     print(course_no,r[course_no-1]["name"])
#     course_id=r[course_no-1]["id"]
#     a=os.path.exists(str(course_id)+".json")
#     if a==False:
#         url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
#         deta=json.loads(url1.text)
#         file=str(course_id)+".json"
#         with open(file,"w") as f2:
#             json.dump(deta,f2,indent=6)
#         print(r[course_no-1]['name'],"-",r[course_no-1]["id"])
#         i = 0
#         while i < len(deta["course"]["exercises"]):
#             print((i+1),".",deta["course"]["exercises"][i]["name"])
#             print(deta["course"]["exercises"][i]["slug"])
#             i+=1


#         topic=int(input("enter the topic no:- "))
#         topic  = topic-1
#         i = 0
#         while i < len(deta["course"]["exercises"][topic]["content"]):
#             print(deta["course"]["exercises"][topic]["content"][i]["value"])
#             print()
#             i+=1
#         while topic <= len(deta["course"]["exercises"]):
#             next_previuos = input("previous or next(p&n):")
#             if  next_previuos == "p": #and next_previuos!= "n":
#                 topic-=1
#                 if next_previuos == "p" and topic >=1:
#                     print(deta["course"]["exercises"][topic]["name"],"\n")
#                     i = 0 
#                     while i < len(deta["course"]["exercises"][topic]["content"]):
#                         print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                         i+=1
                        
#                 else :
#                     i = 0
#                     while i < len(deta):
#                         print(str(i+1),deta["course"]["exercises"][i]["name"])
#                         i+=1
#             elif  next_previuos == "n":# and next_previuos!="p":
#                 topic+=1
#                 if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
#                         print(deta["course"]["exercises"][topic]["name"],"\n")
#                         i = 0 
#                         while i < len(deta["course"]["exercises"][topic]["content"]):
#                             print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                             i+=1
#                 if topic+1 == len(deta["course"]["exercises"]):
#                     print("topic is completed.")
#                     break

#             elif next_previuos=="stop":
#                 break    
#             else:
#                 print("wrong user_input ")
#                 break
#     else:
#         if a==True:
#             d=open(str(course_id)+".json","r")
#             deta=json.load(d)
#             i = 0
#             while i < len(deta["course"]["exercises"]):
#                 print((i+1),".",deta["course"]["exercises"][i]["name"])
#                 print(deta["course"]["exercises"][i]["slug"])
#                 i+=1


#             topic=int(input("enter the topic no:- "))
#             topic  = topic-1
#             i = 0
#             while i < len(deta["course"]["exercises"][topic]["content"]):
#                 print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                 print()
#                 i+=1
#             while topic <= len(deta["course"]["exercises"]):
#                 next_previuos = input("previous or next(p&n):")
#                 if  next_previuos == "p": #and next_previuos!= "n":
#                     topic-=1
#                     if next_previuos == "p" and topic >=1:
#                         print(deta["course"]["exercises"][topic]["name"],"\n")
#                         i = 0 
#                         while i < len(deta["course"]["exercises"][topic]["content"]):
#                             print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                             i+=1
                            
#                     else :
#                         i = 0
#                         while i < len(deta):
#                             print(str(i+1),deta["course"]["exercises"][i]["name"])
#                             i+=1
#                 elif  next_previuos == "n":# and next_previuos!="p":
#                     topic+=1
#                     if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
#                             print(deta["course"]["exercises"][topic]["name"],"\n")
#                             i = 0 
#                             while i < len(deta["course"]["exercises"][topic]["content"]):
#                                 print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                                 i+=1
#                     if topic+1 == len(deta["course"]["exercises"]):
#                         print("topic is completed.")
#                         break

#                 elif next_previuos=="stop":
#                     break    
#                 else:
#                     print("wrong user_input ")
#                     break
# else:
#     if file==True:
#         a=open("requets.json","r")
#         deta=json.load(a)
#         # print(deta)
#         i=0
#         while i<len(deta):
#             print(i+1,deta[i]["name"],deta[i]["id"])
#             i+=1
#         print(" ")    
#         course_no=int(input("select which course you want display  :"))
#         print(course_no,deta[course_no-1]["name"])
#         course_id=deta[course_no-1]["id"]
#         a=os.path.exists(str(course_id)+".json")
#         if a==False:
#             url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
#             deta=json.loads(url1.text)
#             file=str(course_id)+".json"
#             with open(file,"w") as f2:
#                 json.dump(deta,f2,indent=6)
#             # print(deta[course_no-1]['name'],"-",deta[course_no-1]["id"])
#             i = 0
#             while i < len(deta["course"]["exercises"]):
#                 print((i+1),".",deta["course"]["exercises"][i]["name"])
#                 print(deta["course"]["exercises"][i]["slug"])
#                 i+=1


#             topic=int(input("enter the topic no:- "))
#             topic  = topic-1
#             i = 0
#             while i < len(deta["course"]["exercises"][topic]["content"]):
#                 print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                 print()
#                 i+=1
#             while topic <= len(deta["course"]["exercises"]):
#                 next_previuos = input("previous or next(p&n):")
#                 if  next_previuos == "p": #and next_previuos!= "n":
#                     topic-=1
#                     if next_previuos == "p" and topic >=1:
#                         print(deta["course"]["exercises"][topic]["name"],"\n")
#                         i = 0 
#                         while i < len(deta["course"]["exercises"][topic]["content"]):
#                             print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                             i+=1
                            
#                     else :
#                         i = 0
#                         while i < len(deta):
#                             print(str(i+1),deta["course"]["exercises"][i]["name"])
#                             i+=1
#                 elif  next_previuos == "n":# and next_previuos!="p":
#                     topic+=1
#                     if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
#                             print(deta["course"]["exercises"][topic]["name"],"\n")
#                             i = 0 
#                             while i < len(deta["course"]["exercises"][topic]["content"]):
#                                 print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                                 i+=1
#                     if topic+1 == len(deta["course"]["exercises"]):
#                         print("topic is completed.")
#                         break

#                 elif next_previuos=="stop":
#                     break    
#                 else:
#                     print("wrong user_input ")
#                     break
#         else:
#             if a==True:
#                 d=open(str(course_id)+".json","r")
#                 deta=json.load(d)
#                 i = 0
#                 while i < len(deta["course"]["exercises"]):
#                     print((i+1),".",deta["course"]["exercises"][i]["name"])
#                     print(deta["course"]["exercises"][i]["slug"])
#                     i+=1


#                 topic=int(input("enter the topic no:- "))
#                 topic  = topic-1
#                 i = 0
#                 while i < len(deta["course"]["exercises"][topic]["content"]):
#                     print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                     print()
#                     i+=1
#                 while topic <= len(deta["course"]["exercises"]):
#                     next_previuos = input("previous or next(p&n):")
#                     if  next_previuos == "p": 
#                         topic-=1
#                         if next_previuos == "p" and topic >=1:
#                             print(deta["course"]["exercises"][topic]["name"],"\n")
#                             i = 0 
#                             while i < len(deta["course"]["exercises"][topic]["content"]):
#                                 print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                                 i+=1
                                
#                         else :
#                             i = 0
#                             while i < len(deta):
#                                 print(str(i+1),deta["course"]["exercises"][i]["name"])
#                                 i+=1
#                     elif  next_previuos == "n":# and next_previuos!="p":
#                         topic+=1
#                         if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
#                                 print(deta["course"]["exercises"][topic]["name"],"\n")
#                                 i = 0 
#                                 while i < len(deta["course"]["exercises"][topic]["content"]):
#                                     print(deta["course"]["exercises"][topic]["content"][i]["value"])
#                                     i+=1
#                         if topic+1 == len(deta["course"]["exercises"]):
#                             print("topic is completed.")
#                             break

#                     elif next_previuos=="stop":
#                         break    
#                     else:
#                         print("wrong user_input ")
#                         break


a="today'ss a ggreat day , isn'tt it ?"
b={'o':3,'t':4,'s':5,'g':6}
i=0
l=[]
g=[]
while i<len(a):
    for j in b:
        if a[i]==j:
            l.append(b[j])
        g.append(a[i])
    i+=1
print(l)
print(g)
