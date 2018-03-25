# -*- coding:utf-8 -*-

i        = 0
residual = 500000.0
interest_tuple = (0.01, 0.02, 0.03, 0.035)
repay = 30000.0
while residual > 0:
    i = i + 1
    print("第",i,"年还是要还钱")
#    print("第",i,"年还是要还钱")
    print("问题在哪？")
    if i <= 4:
        interest = interest_tuple[i - 1]
    else:
        interest = 0.05
    residual = residual*(1 + interest) - repay
print("第",i+1,"年终于还完了")
print("问题在哪？")
raw_input("Press Enter")