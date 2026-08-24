# LeetCode 0565 - Array Nesting
# https://leetcode.com/problems/array-nesting/

# @param {Integer[]} nums
# @return {Integer}
def array_nesting(nums)
  best = 0
  nums.length.times do |i|
    next if nums[i] < 0

    length = 0
    j = i
    while nums[j] >= 0
      nxt = nums[j]
      nums[j] = -1
      j = nxt
      length += 1
    end
    best = [best, length].max
  end
  best
end
