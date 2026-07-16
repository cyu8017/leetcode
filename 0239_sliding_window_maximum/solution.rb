# LeetCode 0239 - Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sliding_window(nums, k)
  window = []
  result = []

  nums.each_with_index do |num, index|
    while !window.empty? && nums[window.last] <= num
      window.pop
    end
    window.push(index)
    window.shift if window.first <= index - k
    result.push(nums[window.first]) if index >= k - 1
  end

  result
end
