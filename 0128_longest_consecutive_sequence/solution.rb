# LeetCode 0128 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

# @param {Integer[]} nums
# @return {Integer}
def longest_consecutive(nums)
  values = nums.to_h { |number| [number, true] }
  best = 0
  values.each_key do |number|
    next if values.key?(number - 1)

    length = 1
    length += 1 while values.key?(number + length)
    best = [best, length].max
  end
  best
end