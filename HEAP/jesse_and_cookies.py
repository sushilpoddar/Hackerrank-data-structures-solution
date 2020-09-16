import heapq as hq

if __name__ == "__main__":
    n, k = map(int, input().strip().split(' '))
    cookies = list(map(int, input().strip().split(' ')))
    q = []
    res = 0
    
    for elem in cookies:
        hq.heappush(q, elem)
    
    while any(c < k for c in q) and len(q) > 1:
        last = hq.heappop(q)

        secondlast = hq.heappop(q)
        
        new = last + 2*secondlast
        
        hq.heappush(q, new)
        res += 1
        
    if all(c >= k for c in q):
        print(res)
    else:
        print(-1)
