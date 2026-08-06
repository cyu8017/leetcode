# LeetCode 1121 - Divide Array Into Increasing Sequences
# https://leetcode.com/problems/divide-array-into-increasing-sequences/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_divide_into_subsequences(nums, k)
  n = nums.length
  max_freq = 1
  freq = 1
  (1...n).each do |i|
    if nums[i] == nums[i - 1]
      freq += 1
      max_freq = [max_freq, freq].max
    else
      freq = 1
    end
  end
  max_freq * k <= n
end
