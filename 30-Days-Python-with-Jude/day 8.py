from concurrent.futures.process import _python_exit


n = int(input())
dic = {}
for i in range(n):
    phone = list(input().split(" "))
    dic[phone[0]]= phone[1]
while True:
    try:
        j = input()
        if j in dic.keys():
             print(j+'='+dic[j])
        else:
            print("Not found")     
    
    except EOFError:
        break
