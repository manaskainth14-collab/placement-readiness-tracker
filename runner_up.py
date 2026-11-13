# Task 3: Runner-up score (second-highest distinct score)
n = int(input())
scores = list(map(int, input().split()))

distinct = sorted(set(scores), reverse=True)   # remove duplicates, sort high -> low
print(distinct[1])                             # second-highest distinct score