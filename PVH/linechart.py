import matplotlib.pyplot as plt
import numpy as np
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
title = title.split(',')
sbj = title[1:]

cnt_exam =  [0] * 9
cnt_no_exam =  [0] * 9
with open("data_clean.csv", "r", encoding="utf8") as file:

    data = file.readline()
    
    # print(total_std)
    # print(data)
    while(data != ""):


        if (data[0] == '0'):
            data = data.split(',')
            score = data[2:]
            for i in range(3):
                if (score[i] != '-1'):
                    cnt_exam[i] +=1
                else:
                    cnt_no_exam[i] +=1

            if(data[1] == "khtn"):
                for i in range(3,6):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1
            if(data[1] == "khxh"):
                for i in range(6,9):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1

        data = file.readline()

# điểm trung bình, % của mỗi học sinh
average = [0] * 9


for i in range(len(cnt_no_exam)):
    average[i] = round((cnt_no_exam[i]/len(std)) * 100,2) 

print(cnt_no_exam)    
print(average)

fig, ax = plt.subplots()

subject = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD')
y_pos = np.arange(len(subject))
x_pos = np.arange(len(subject))

# performance = [10,8,6,4,2,1]

plt.bar(y_pos, average, align='center', alpha=0.5)
plt.xticks(y_pos, subject)
plt.plot(x_pos, average, color='red')
plt.grid(True)

plt.xticks(y_pos, subject)
ax.set_ylim(0,20)
plt.ylabel('percent')
plt.title('Line Chart - Thống kê số học sinh không tham gia thi theo từng môn') 

# make value
rects = ax.patches
for rect, label in zip(rects, cnt_no_exam):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom"
    )

plt.show()
