import os

current_dir = os.getcwd()
path = os.path.join(current_dir,"comic book")

total = 0
for clas in os.listdir(path):
    print("clas : ",clas)
    no = len(os.listdir(os.path.join(path,clas)))
    total += no
    print(no)

print("total : ",total)