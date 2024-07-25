import os
print("1.write",'\n',"2.read",'\n',"3.append")
option=int(input("Enter your option in run:"))
if(option==1):
    W_file=input("Enter your file name to write:")
    f=open(W_file,'w')
    content=input("Enter your content to write:")
    f.write(content)
    f.close()
elif(option==2):
    data=os.listdir()
    li=[]
    for i in data:
        if i.endswith(".txt"):
            li.append(i)
    print(li)
    r_file=input("Enter your filename to read:")
    for i in data:
        if i==r_file and r_file.endswith(".txt"):
             f=open(r_file,'r')
             print(f.read())
             f.close()
             break
    else:
        print("no such file exists")
        
elif(option==3):
    data=os.listdir()
    li=[]
    for i in data:
        if i.endswith(".txt"):
            li.append(i)
    print(li)
    a_file=input("Enter your filename to append:")
    for i in data:
        if i==a_file and a_file.endswith(".txt"):
             f=open(a_file,'a')
             a_content=input("Enter your content to append:")
             f.write(a_content)
             f.close()
             break
    else:
        print("no such file exists")
   