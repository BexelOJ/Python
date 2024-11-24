# Second lowest marks
if __name__ == '__main__':
    student = []
    runner_up = []
    N = int(input())
    for _ in range(N):
        name = input()
        score = float(input())
        student.append([name,score])

    student.sort(key = lambda x : x[1],reverse=True)
    for i in range(N-1,-1,-1):
        if student[i][1] != student[i-1][1]:
            for j in range(i-1,-1,-1):
                runner_up.append(student[j])
                if student[j][1] != student[j-1][1]:
                    break
            break


runner_up.sort(key = lambda x : x[0])

for first_element in runner_up:
    print(first_element[0])



