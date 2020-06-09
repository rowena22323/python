import pandas as pd

df = pd.read_csv("C:\\Python_proj\\data\\student.csv")
df2 = pd.DataFrame(df, columns=['sex','weight','height'])
df2['bmi_R']=df2['weight']/((df2['height']/100)*(df2['height']/100))

filterM = df2['sex']=='male'
df_M = df2[filterM]
mr = df_M['bmi_R'].mean()

filterFM = df2['sex']=='female'
df_FM = df2[filterFM]
ms = df_FM['bmi_R'].mean()

while True:
    print("{0:#^37}".format("남녀평균BMI지수"))
    a = int(input("알고싶은 평균 BMI지수의 성별을 입력해 주세요. 남자(1) 여자(2) 종료(3): "))
    if(a == 1):
        print("")
        print(mr)
        print("")
        print("{0:#^43}".format("#"))
    elif(a == 2):
        print("")
        print(ms)
        print("")
        print("{0:#^43}".format("#"))
    elif(a == 3):
        print("")
        print("화면종료")
        print("")
        print("{0:#^43}".format("#"))
        break