for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for col in range(100):
        if arr[0][col] == 1:
            i, j = 0, col   # 기존 col값을 유지하고 j에 새로 할당
            while i < 100:
                if i == 99 and arr[i][j] == 2:     # i = 99 일때 결과값이면 col값을 출력
                    print(f'#{t} {col}')
                if j + 1 < 100 and arr[i][j+1] == 1:    # 오른쪽에 1이 있으면 오른쪽으로 1이 안니올때까지 while문을 돌린다
                    while j + 1 < 100 and arr[i][j + 1] == 1:
                        j += 1
                elif j - 1 >= 0 and arr[i][j-1] == 1:      # 왼쪽에 1이 있으면 왼쪽으로 1이 안나올때까지 while문을 돌린다.
                    while j - 1 >= 0 and arr[i][j - 1] == 1:
                        j -= 1
                i += 1                                      # 두개의 좌우 방향에 안걸리면 i += 1을 해준다.
