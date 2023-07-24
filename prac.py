height=1.75
weight=80.5
BMI=weight/(height**2)

if BMI<18.5:
    print('过轻')
elif 18.5<BMI<25:
    print('正常')
elif 25<BMI<28:
    print('过重')
elif 28<BMI<32:
    print('肥胖')
elif BMI>32:
    print('严重肥胖')
