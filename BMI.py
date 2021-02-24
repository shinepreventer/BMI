#! /usr/bin/python
# -*- coding: utf-8 -*-
print("请输入身高（米）")
height = input()
print("请输入体重（千克）")
weight = input()
print("请输入腰围（厘米）")
waist = input()
print("请输入性别（男/女）")
gender = input()
BMI = float(weight) / (float(height) * float(height))
print("您的体重指数为: %r," % (BMI))
if BMI <= 18:
    print("体重过低")
elif BMI > 18 and BMI < 24:
    print("体重正常")
elif BMI >= 24 and BMI < 28:
    print("超重")
else:
    print("肥胖")
if gender == "男":
    fatweight = float(waist) * 0.74 - float(weight) * 0.082 - 44.74
    Bodyfatrate = fatweight / float(weight)
    print('您的体脂率为: {:.2f} %'.format(Bodyfatrate * 100))
else:
    fatweight2 = float(waist) * 0.74 - float(weight) * 0.082 - 34.89
    Bodyfatrate2 = fatweight2 / float(weight)
    print('您的体脂率为: {:.2f} %'.format(Bodyfatrate2 * 100))
