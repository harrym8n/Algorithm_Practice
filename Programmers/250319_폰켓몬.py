def solution(nums):
    if len(set(nums)) > (len(nums)/2):
        answer = (len(nums)/2)
    elif len(set(nums)) <= (len(nums)/2):
        answer = len(set(nums))
    return answer