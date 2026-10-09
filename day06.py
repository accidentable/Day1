# 6일차 코딩테스트 연습
# 배열에서 두 수를 더해서 타겟이 되는 두 원소의 인덱스를 반환

nums = [2, 7, 11, 15]
target = 9

# target 보다 작은 원소를 더할 배열
#new_arr = []
# target 보다 작은 원소 찾기
#for i in nums:
#   if i < target:
#        new_arr.append(i)
        

#for i in new_arr:
#    for j in new_arr:
#        if (i + j) == target and (i!=j) :
#            print("[" + str(new_arr.index(i)) + "," +  str(new_arr.index(j)) +  "] is answer")
#            new_arr.remove(i)
#            new_arr.remove(j)
            
            
## 수정본 - new arr을 쓰지 않고서 할 수 있을까?

#for i in range(0,len(nums)-1):
#    for j in range(i+1, len(nums)):
#        if nums[i] + nums[j] == target:
#            print("[" + str(i) + "," +  str(j) +  "] is answer")

# 시간복잡도를 O(n) 수준으로 낮출 수 있을까?
# 시간복잡도를 줄이는 과정은 결국 공간복잡도를 희생할 수 밖에 없을까?

seen = {} #dict 선언 target - nums[i]

for i in range(len(nums)):
    curr = nums[i] # 현재값
    ans = target - nums[i] # 필요한 값
    if ans in seen: # 필요한 값이 이미 dict에 있으면
        print(seen[ans] , i) # 출력
    else: # 없으면 현재 값을 dict에 저장
        seen[nums[i]] = i
    