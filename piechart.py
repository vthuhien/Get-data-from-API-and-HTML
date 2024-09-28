import matplotlib.pyplot as plt
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
total_std = len(std)

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




labels = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD')
sizes = cnt_exam
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightgray','hotpink']

# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)
# plt.show()

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        pctdistance=1.1, labeldistance=.6,textprops={'size': 'smaller'}, radius=0.5)
plt.legend(title = "Subjects:")
plt.axis('equal')  # Đảm bảo biểu đồ hình tròn
plt.title('Pie Chart - Thống kê tổng số học sinh dự thi các môn')
plt.show()
