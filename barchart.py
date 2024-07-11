import matplotlib.pyplot as plt
import numpy as np

with open("data_clean.csv", "r" , encoding ="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
# xoá th cuối 
std.pop()
total_std = len(std)  

title = title.split(",")  
subject = title[1:]
# print(subject)


for i in range(len(std)):
    std[i] = std[i].split(",")

not_exam = [0] *len(subject)

# print(std[-1]) 


#môn nào k thi +1
for s in std:
    for i in range(1,9):
        if s[i] =="-1":
            not_exam[i-1]+=1 

# print(not_exam)

#tính phần trăm
in_percent = [0] * len(subject)
for i in range(0,9):
    in_percent[i] = round((not_exam[i]/total_std)*100,2)

# print(in_percent)
# print(subject)
# print(not_exam)  


# fig, axis = plt.subplot()
# import matplotlib.pyplot as plt

# Create a single subplot
fig, ax = plt.subplots()

subject = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD')
y_pos = np.arange(len(subject))

# performance = [10,8,6,4,2,1]

plt.bar(y_pos, in_percent, align='center', alpha=0.5)
plt.xticks(y_pos, subject)

ax.set_ylim(0,100)

plt.ylabel('percent')
plt.title('Bar Chart - Thống kê số học sinh không tham gia thi theo từng môn') 

# make value
rects = ax.patches
for rect, label in zip(rects, not_exam):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )

plt.show()
