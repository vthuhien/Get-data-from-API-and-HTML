import os
path = "C:/Users/Admin/Downloads/check"
datas = os.listdir(path);

subject = ['To&#xE1;n', 'V&#x103;n', 'Ngo&#x1EA1;ing&#x1EEF;','L&#xED;','H&#xF3;a','Sinh','S&#x1EED;', '&#x110;&#x1ECB;a',  'GDCD']

title = "Số báo danh,Khối Thi,Toán,Văn,Ngoại Ngữ,Lý,Hoá,Sinh,Sử,Địa lý,GDCD"

with open("data_clean.csv","w",encoding="utf8") as file_title:
    file_title.write(title + "\n")

for i in range(len(datas)):

    list_data =[];
    file_html = path + "/" + datas[i]; 
    # print(file_html)
    sbd =datas[i];
    index = sbd.index(".")
    sbd = str(sbd[:index])
    # print(sbd)
    with open(file_html,"r",encoding="utf8")as file:
        data = file.readline() 
        
        # print(data)
        while(data != ""):
            data =data.replace(" ","") 
            list_data.append(data)
            data = file.readline() 
    list_sbj = [list_data[276],
                list_data[280],
                list_data[292],
                list_data[284],
                list_data[288],
                list_data[296]]
    for i in range(len(list_sbj)):
        list_sbj[i] = list_sbj[i].replace("<td>","")
        list_sbj[i] = list_sbj[i].replace("</td>","")
        tmp = list_sbj[i].index("\n")
        list_sbj[i] = list_sbj[i][:tmp]
    # print(list_obj)

    scores = [list_data[276+1],
                list_data[280+1],
                list_data[284+1],
                list_data[288+1],
                list_data[292+1],
                list_data[296+1]]
    # print(scores)

    for i in range(len(scores)):
        scores[i] = scores[i].replace("<td>","")
        scores[i] = scores[i].replace("</td>","")
        tmp2 = scores[i].index("\n")
        scores[i] = scores[i][:tmp2] 
    # print(scores[i])
    index = ['-1'] * len(subject)
    index_ = []
    for i in range(len(list_sbj)):
        for j in range(len(subject)):
            if(list_sbj[i]==subject[j]):
                index_.append(j)
    
    for i in range(len(index_)):
        index[index_[i]] = scores[i]
    
    s = ""
    for i in index:
        s += i + ","
    s = s[:len(s)-1]

    # check khtn - khxh
    cnt_check = 0
    cnt_check1 = 0

    for i in range(3,9):
        if (index[i] != '-1'):
            cnt_check += 1
        else:
            cnt_check1 += 1
            
    a = ""
    if (cnt_check == 6):
        a += "All"

    if (cnt_check1 == 6):
        a += "NONE"
    
    else:
        x = index[3],index[4],index[5]
        y = index[6],index[7],index[8]
        # print(y)
        # print(x)
        a = ""
        cnt_khtn = 0
        cnt_kkxh = 0
        for i in range(len(x)):
            if(x[i] != '-1'):
                cnt_khtn += 1
        for i in range(len(y)):
            if(y[i] != '-1'):
                cnt_kkxh += 1
        
        if (1 <= cnt_khtn <= 3):
            a += "khtn,"

        if (1 <= cnt_kkxh <= 3):
            a += "khxh,"
    
    tmp = sbd + "," + a + s
    with open("data_clean.csv","a",encoding="utf8") as file_csv:
        file_csv.write(tmp + "\n")
        
    print("SBD : " + str(sbd) + " đã thành công")
