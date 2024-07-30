'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''

T = int(input())

for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # k = 충전 없이 갈 수 있는 거리
    # n = 총 정류장 수
    # m = 충전 가능한 정류장 수
    # arr = 충전 가능한 정류장 배열
    current_pos = 0     # 현재 위치
    charge_count = 0    # 충전 횟수

    # 충전 가능한 정류장 배열 끝에 도착지를 추가 왜? 마지막 충전하고 갈 수 있는지 없는지 확인해야하니까
    arr += [n]

    for i in range(m + 1):
        # 만약 현재 위치에서 다음 충전소까지 거리가 k보다 크면
        if arr[i] - current_pos > k:    # 예를들어 첫 번째 예시에서 i가 2이면 5이므로 5 - 0 은 3보다 크므로 if문에 들어온다
            current_pos = arr[i - 1]    # 그러므로 충전은 그 전 arr[i-1]에서 해야하니 현재 위치를 arr[i-1]로 만든다
            charge_count += 1           # 충전은 했으므로 +1 해준다
            if arr[i] - current_pos > k:    # 만약 현재의 arr[i]에서 arr[i-1]에 해당하는 현재 위치를 뺏을때 k보다 크다면
                charge_count = 0        # 그것은 곧 거리가 더 멀기 때문에 충전을 하지 못하는 상태가 된다.
                break


    print(f'#{tc} {charge_count}')

