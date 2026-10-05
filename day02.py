# 최근 이벤트 되돌리기 (Ctrl + Z)
# Stack은 가장 최근에 추가한 이벤트를 되돌리므로
# Ctrl + Z 에는 Stack이 알맞다.

# 이때 pop은 O(1), append 는 분할 상환 O(1)인데
# 파이썬의 리스트는 동적배열로 구현되어 있어서 
# 리스트가 커지는 과정에서 여유 공간을 확보하고, 공간이 부족하면 재할당이 필요할 수 있음
# 따라서 일반적인 경우 O(1)이지만, 가끔 더 큰 메모리 공간을 잡고 
# 기존 N개의 원소들을 모두 새 공간으로 복사하므로 O(N)의 시간이 걸린다.

Recent_event = ["주가 급락", "거래량 급증", "신용등급 하락"]


print(Recent_event.pop()) # 되돌리기 : O(1)
print(Recent_event.pop()) # 되돌리기

Recent_event.append("실적 전망 하향") # 추가: 분할상환 O(1)

print(Recent_event.pop())
print(Recent_event.pop())

try:    
    Recent_event.pop() # Error: Pop from empty list
except IndexError: 
    print("Stack is Empty!")


#----
# Queue
# List로 Q를 구현하면 list.pop(0) 연산이 O(N) : 맨 앞 요소를 제거하면 뒤의 요소들을 한칸씩 이동해야 함
# Deque로 구현하면 Double-Ended로 구현이 가능하여 앞뒤로 요소를 빼고 더할 수 있음

# Queue는 기본적으로 FIFO 구조라,
# 들어온 순서대로 처리할 수 있음

from collections import deque

queue = deque()
queue.append("주가 급락")
queue.append("거래량 급증")
queue.append("신용등급 하락")

print(queue)

print(queue.popleft()) # 주가 급락
print(queue.popleft()) # 거래량 급증
queue.append("실적 전망 하향") # 실적 전망 하향 추가

print(queue.popleft()) # 신용 등급 하락
print(queue.popleft()) # 실적 전망 하향

try: 
    queue.popleft() # 빈 큐 처리하기
except IndexError:
    print("Queue is Empty!")

