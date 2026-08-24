# LeetCode 0658 - Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/

# @param {Integer[]} arr
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_closest_elements(arr, k, x)
  left = 0
  right = arr.length - k
  while left < right
    mid = (left + right) / 2
    if x - arr[mid] > arr[mid + k] - x
      left = mid + 1
    else
      right = mid
    end
  end
  arr[left, k]
end
