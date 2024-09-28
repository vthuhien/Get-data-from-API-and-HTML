import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
total = len(std)
check = 0

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
                    check +=1
            
            if(data[1] == "khtn"):
                for i in range(3,6):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1
                        check +=1
            if(data[1] == "khxh"):
                for i in range(6,9):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1
                        check +=1
            
        data = file.readline()

tmp = total - check
print(tmp)

# print(cnt_no_exam[i])


#tính phần trăm
in_percent = [0] * 9
for i in range(0,9):
    in_percent[i] = round((cnt_exam[i]/tmp)*100,2) #97087 = tổng std 


# print(in_percent)




import matplotlib.pyplot as plt

# Create a single subplot
fig, ax = plt.subplots()

subject = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD')
x = np.array(subject)
y = np.array(in_percent)

plt.barh(x, y)
plt.xlabel('percent')
plt.title('Bar Chart - Thống kê điểm trung bình của học sinh')
plt.show()
