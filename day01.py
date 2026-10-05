# 1. list
companies = ['APPL', 'NVDA', 'PINT', 'ORCL']

# 회사 3개 추가
companies.append('MU') 
print(companies)
# 두 번째 회사 출력
print(companies[1])
# 마지막 회사 삭제
del companies[-1]
print(companies)

# 2. dict
company_by_code = { "001" : 'Samsung' , "002" : 'SK Hynix', "003" : 'Samsung SDS'}
print(company_by_code)
print(type(company_by_code))

# "001" 회사 조회
print(company_by_code["001"])
# "004"이 존재하는 지 확인
print("004" in company_by_code)

# 3. set
processed_codes = {1,2,2}
print(type(processed_codes))
# add 10
processed_codes.add(10)
print(processed_codes)

# 4. deque
# list로 만들면 pop 연산 시 맨 앞의 값을 제거하고 모든 값을 한 칸씩 당기므로 O(n)
# collections의 deque로 만들면 O(1)
from collections import deque
q = deque()
q.append("A")
q.append("B")
q.append("C")

q.pop() # O(1) -> C pop
print(q)

q.popleft() # A pop
print(q)

# 오늘의 문제

codes = [
    "005930",
    "000660",
    "005930",
    "035420",
    "000660",
    "005930"
]


counts = {} # dict 자료형 선언 

for code in codes :
    if code in counts:
        counts[code] += 1
    else:
        counts[code] = 1
print(counts)
best_codes = None
best_count = 0

for code in codes:
    if counts[code] > best_count:
        best_count = counts[code]
        best_codes = code

print(best_codes)
print(best_count)

# 사용할 자료구조: dict
# 선택한 이유: 각 기업 코드를 key, 등장 횟수를 value로 저장하고 코드별 횟수를 빠르게 조회, 수정하기 위해서 dict를 사용함
# 예상 시간복잡도: O(N) : for문 두개 독립적이고 모두 codes를 1번 순회
# 예상 공간복잡도: O(K), K는 서로 다른 기업의 수 이고 최악의 경우 K = N 이므로 O(N)
