from typing import List
def The_Great_Run(N: int, k: int, arr: List[int]) -> int:
    if N == 0 or k == 0:
        return 0
    if k > N:
        k = N
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k, N):
        current_sum += arr[i] - arr[i-k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

if __name__ == '__main__':
    N,k = map(int,input().split())
    path = list(map(int,input().split()))
    print(The_Great_Run(N,k,path))
