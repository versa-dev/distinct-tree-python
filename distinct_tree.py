import math

def solution(Tree):
  paths = []
  nums = []
  for i in range(len(Tree)):
    if (Tree[i] != "x"):
      path = []
      path.append(Tree[i])
      j = i
      while(j>0):
        j = math.floor((j-1)/2)
        path.append(Tree[j])
      paths.append(path)
      nums.append(len(list(set(path))))

  num = max(nums)
  re_path = []
  for i in range(len(paths)):
    if (num == nums[i]):
      path = paths[i]
      re_path.append(path)
  
  results = []
  for path in re_path:
    result = ""
    for item in path:
      result = item + "-" + result
    results.append(result)
  return results

print("If there is no a leaf, input the 'x' instead of the leaf.")
T = input("Input the tree in type of one-dimensional array: ")
Tree = T.split(",")
print(solution(Tree))