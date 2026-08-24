# LeetCode 0594 - Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
  counts = Hash.new(0)
  nums.each { |value| counts[value] += 1 }
  best = 0
  counts.each do |value, count|
    best = [best, count + counts[value + 1]].max if counts.key?(value + 1)
  end
  best
end
