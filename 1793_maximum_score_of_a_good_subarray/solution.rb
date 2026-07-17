# LeetCode 1793 - Maximum Score of a Good Subarray
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  n = nums.length
  stack = []
  ans = 0
  (0..n).each do |i|
    while !stack.empty? && (i == n || nums[i] < nums[stack.last])
      mid = stack.pop
      left = stack.empty? ? 0 : stack.last + 1
      right = i - 1
      if left <= k && k <= right
        score = nums[mid] * (right - left + 1)
        ans = score if score > ans
      end
    end
    stack.push(i)
  end
  ans
end
