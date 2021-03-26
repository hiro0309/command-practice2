import calc_bmi

print("BMI値計算アプリ")

h = int(input("身長(cm):"))
w = int(input("体重(kg):"))
print(f"BMI値:{calc_bmi.bmi(h, w)}")
