# LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

# @param {Integer[]} arr
# @return {Integer}
def find_length_of_shortest_subarray(arr)
  n = arr.length
  right = n - 1
  right -= 1 while right.positive? && arr[right - 1] <= arr[right]
  return 0 if right.zero?
  answer = right
  left = 0
  while left.zero? || (left < n && arr[left - 1] <= arr[left])
    right += 1 while right < n && arr[right] < arr[left]
    answer = [answer, right - left - 1].min
    left += 1
    break if left >= n
  end
  answer
end
