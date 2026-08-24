# LeetCode 0941 - Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/

# @param {Integer[]} arr
# @return {Boolean}
def valid_mountain_array(arr)
  n = arr.length
  return false if n < 3

  i = 0
  i += 1 while i + 1 < n && arr[i] < arr[i + 1]
  return false if i == 0 || i == n - 1

  i += 1 while i + 1 < n && arr[i] > arr[i + 1]
  i == n - 1
end
