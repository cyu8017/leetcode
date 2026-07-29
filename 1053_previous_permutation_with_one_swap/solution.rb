# LeetCode 1053 - Previous Permutation With One Swap
# https://leetcode.com/problems/previous-permutation-with-one-swap/

# @param {Integer[]} arr
# @return {Integer[]}
def prev_perm_opt1(arr)
  n = arr.length
  i = n - 2
  i -= 1 while i >= 0 && arr[i] <= arr[i + 1]
  return arr if i < 0

  j = n - 1
  j -= 1 while arr[j] >= arr[i] || arr[j] == arr[j - 1]
  arr[i], arr[j] = arr[j], arr[i]
  arr
end
