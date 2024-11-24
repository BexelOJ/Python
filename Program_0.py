# Print the runner up score
if __name__ == '__main__':
    n = int(input())
    arr_list = []
    arr = map(int, input().split(" "))
    arr_list = list(arr)
    arr_list.sort()
    for i in range(n-1,0,-1):
        if arr_list[i] != arr_list[i-1]:
            break
        else:
            continue
    print(arr_list[i-1])