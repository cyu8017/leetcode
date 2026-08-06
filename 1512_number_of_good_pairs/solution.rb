# LeetCode 1512 - Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

# @param {Integer[]} nums
# @return {Integer}
def num_identical_pairs(nums)
  counts = Hash.new(0)
  nums.each { |n| counts[n] += 1 }
  counts.values.sum { |n| n * (n - 1) / 2 }
end
