if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    maxim = - 100   
    for i in range(1,5):
        for j in range(1,5):
            sum=  arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if sum>maxim:
                maxim = sum             
    print(maxim)
