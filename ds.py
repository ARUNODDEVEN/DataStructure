def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = linear_search(arr, x)
if result != -1:
  print(f"Element {x} is present at index {result}")
else:
  print("Element is not present in the array")
