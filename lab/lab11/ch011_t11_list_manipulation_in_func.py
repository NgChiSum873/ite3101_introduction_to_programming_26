from typing import List

n = [3, 5, 7]

def list_extender(l: List[int]) -> List[int]:
    new_l = l.copy()
    new_l.append(9)
    return new_l

print(list_extender(n))
print(n) # 原列表不变
