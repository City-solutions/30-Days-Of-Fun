# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for test_caase in range (n):
    s = input('')
    even =''
    odd =''
    for i in range (len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd+= s[i]
    
    print(f'{even} {odd}')
        
    
