import matplotlib.pyplot as plt
import numpy as np
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
title = title.split(',')
sbj = title[1:]
std.pop()
for i in range(len(std)):
    std[i]=std[i].split(',')
num_sbj = [0] * len(sbj)
average = [0] * len(sbj)
for s in std:
    cnt = 0;
    for i in range(8):
        if( s[i] != '-1'):
            cnt+=1;
    num_sbj[cnt]+=1;

for i in range(len(num_sbj)):
    average[i] = round((num_sbj[i]/len(std))*100,2);

print(num_sbj)
print(average)

fig, ax = plt.subplots()

subject = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD')
y_pos = np.arange(len(subject))
x_pos = np.arange(len(subject))

# performance = [10,8,6,4,2,1]

plt.bar(y_pos, average, align='center', alpha=0.5)
plt.xticks(y_pos, subject)
plt.plot(x_pos, average, color='red', marker='o')

ax.set_ylim(0,70)
plt.ylabel('percent')
plt.title('Line Chart - Thống kê điểm trung bình mỗi môn') 

# make value
rects = ax.patches
for rect, label in zip(rects, num_sbj):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )

plt.show()
