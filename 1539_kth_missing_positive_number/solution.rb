# LeetCode 1539 - Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def find_kth_positive(arr, k)
  left = 0
  right = arr.length
  while left < right
    middle = (left + right) / 2
    if arr[middle] - middle - 1 < k
      left = middle + 1
    else
      right = middle
    end
  end
  left + k
end
