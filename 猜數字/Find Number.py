import random

print('來猜字吧\n輸入最小值')
min = int(input())
print('最小值為' + str(min) + "\n輸入最大值")
max = int(input())
num = random.randint(min, max)


def main ():
    i = int(0)
    while i < 5:
        print('請輸入猜的數字\n'+'還可以猜的次數'+ str(5-i))
        ans = int(input())
        if min< ans >max:
            print('輸入的數值不在範圍內')
        if min <= ans <= max:
            if ans == num :
                print('答對了')
                break
            if ans > num :
                print('太大了')
                i=i+1
            if ans < num :
                print('太小了')
                i=i+1
            if i == 5 :
                print('再加把勁'+'\n正確答案是\n'+str(num))

main()



