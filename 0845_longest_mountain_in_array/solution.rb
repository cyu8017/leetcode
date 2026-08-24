# LeetCode 0845 - Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/

# @param {Integer[]} arr
# @return {Integer}
def longest_mountain(arr)
  n = arr.length
  ans = 0
  i = 0
  while i < n
    j = i
    if j + 1 < n && arr[j] < arr[j + 1]
      j += 1 while j + 1 < n && arr[j] < arr[j + 1]
      if j + 1 < n && arr[j] > arr[j + 1]
        j += 1 while j + 1 < n && arr[j] > arr[j + 1]
        ans = [ans, j - i + 1].max
        i = j
        next
      end
    end
    i += 1
  end
  ans
end
