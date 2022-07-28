import json
import requests

r=requests.get('http://api.merakilearn.org/courses')
b=r.json()

with open("courses.json","w")as f:
    s=json.dump(b,f,indent=4)

with open('courses.json')as f:
    t=json.load(f)

c=1 
for i in t:   
    print(c,".",i["name"],": ID-",i['id'])
    c+=1

print()
user=int(input("enter the course number :-"))
print()
print(t[user-1]["name"],": ID-",t[user-1]['id'])
course_id=t[user-1]['id']


    
z=requests.get('http://api.merakilearn.org/courses/'+course_id+'/exercises')
y=z.json()
# print(y)
with open("exercises.json","w")as file:
    k=json.dump(y,file,indent=4)
with open("exercises.json")as file:
    l=json.load(file)


n=1
for i in l["course"]["exercises"]:
    print(n,i["name"],"\n","  ",i["slug"])
    n+=1

print()
slug_user=int(input("enter the slug number:-"))
print()
print("Name :- ",l["course"]["exercises"][slug_user-1]["name"],"\n","Slug :- ",l["course"]["exercises"][slug_user-1]["slug"])

for i in (l["course"]["exercises"][slug_user-1]["content"]):
    print(i["value"])



while slug_user<=len(l["course"]["exercises"]):
    next_privious=input("Enter Next or Privious n/p :")
    if next_privious=="p":
        slug_user=slug_user-1
        if 1<=slug_user:
            print(l["course"]["exercises"][slug_user]["name"])
            i=0
            while i<len(l["course"]["exercises"][slug_user]["content"]):
                print(l["course"]["exercises"][slug_user]["content"][i]["value"])
                i=i+1
        elif slug_user==0:
            print(l["course"]["exercises"][slug_user]["name"])
            i=0
            while i<len(l["course"]["exercises"][slug_user]["content"]):
                print(l["course"]["exercises"][slug_user]["content"][i]["value"])
                i=i+1
        else:
            print("finished")
            break
    elif next_privious=="n":
        slug_user=slug_user+1
        if slug_user<len(l["course"]["exercises"]):
            print(l["course"]["exercises"][slug_user]["name"])
            i=0
            while i<len(l["course"]["exercises"][slug_user]["content"]):
                print(l["course"]["exercises"][slug_user]["content"][i]["value"])
                i=i+1
        if slug_user==len(l["course"]["exercises"]):
            print("Topic is completed")
            break
    else:
        print("user input is wrong:")
        break