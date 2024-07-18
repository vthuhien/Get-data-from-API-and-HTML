cnt_exam =  [0] * 9
cnt_no_exam =  [0] * 9
with open("data_clean", "r", encoding="utf8") as file:
    data = file.readline()
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
        
print(cnt_exam)
print(cnt_no_exam)
