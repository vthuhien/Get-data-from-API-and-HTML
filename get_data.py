import os
path = "C:/Users/Admin/Downloads/check"
datas = os.listdir(path);

subject = ['To&#xE1;n', 'V&#x103;n', 'Ngo&#x1EA1;ing&#x1EEF;','L&#xED;','H&#xF3;a','Sinh','S&#x1EED;', '&#x110;&#x1ECB;a',  'GDCD']

print(len(subject))
title = "Số báo danh,Toán,Văn,Ngoại Ngữ,Lý,Hoá,Sinh,Sử,Địa lý,GDCD"

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
    print(s)
    with open("data_clean.csv","a",encoding="utf8") as file_csv:
        file_csv.write(sbd + "," + s + "\n")
    
    print("SBD : " + str(sbd) + " đã thành công")

    