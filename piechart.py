import matplotlib.pyplot as plt
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

title = data[0]
std = data[1:]
total_std = len(std)

title = title.split(',')
sbj = title[1:]

for i in range(len(std)):
    std[i] = std[i].split(',')

std.pop()

# đếm tổng số môn hs đã đi thi
num_sbj = [0] * len(sbj)

# điểm trung bình, % của mỗi học sinh
average = [0] * len(sbj)

for s in std:
    count = 0;  #count = 1 là những hs thi 1 môn , count =2 là những hs thi 2 môn
    for i in range(0,8):
        if (s[i] != "-1"): # vì s[0] là sbd thì +1 là điểm toán
            count+=1;

    num_sbj[count] += 1;

for i in range(len(num_sbj)):
    average[i] = round((num_sbj[i]/len(std)) * 100,2) # tổng điểm những môn thi chia cho số môn bạn thi thì ra điểm trung bình

    

# print(average)  
# print(num_sbj)
# print(sum(num_sbj))
# print(len(std))


labels = ('Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh')
sizes = [587, 87, 1417, 12250, 3798, 78948]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightgray']

# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)
# plt.show()

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        pctdistance=1.25, labeldistance=.6,textprops={'size': 'smaller'}, radius=0.5)

plt.axis('equal')  # Đảm bảo biểu đồ hình tròn
plt.title('Pie Chart - Thống kê điểm trung bình mỗi môn')
plt.show()
