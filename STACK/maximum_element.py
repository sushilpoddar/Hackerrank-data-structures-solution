if __name__ == '__main__':
    N = int(input())
    maxi = 0
    stack = []
    for i in range(N):
        val = list(map(int, input().strip().split()))
        if val[0] == 1:
            maxi = max(maxi, val[1])
            stack.append(val[1])
        elif val[0] == 2:
            if stack.pop() == maxi:
                if len(stack) > 0:
                    maxi = max(stack)
                else:
                    maxi = 0
        elif val[0] == 3:
            print(maxi)
