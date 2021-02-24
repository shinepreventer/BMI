print("请输入身高（米）")
height=input()
print("请输入体重（千克）")
weight=input()
BMI=float(weight)/(float(height)*float(height))
print("您的体重指数为: %r," %(BMI))
if BMI<=18:
  print("体重过低")
elif BMI>18 and BMI<24:
    print("体重正常")
elif BMI>=24 and BMI<28:
        print("超重")
else:print("肥胖")

