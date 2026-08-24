# LeetCode 3852 - Smallest Pair With Different Frequencies
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/

# @param {Integer[]} nums
# @return {Integer[]}
def min_distinct_freq_pair(nums)
  cnt = Hash.new(0)
  nums.each { |v| cnt[v] += 1 }
  x = nums.min
  min_y = Float::INFINITY
  cnt.each_key do |y|
    min_y = y if y < min_y && cnt[x] != cnt[y]
  end
  return [-1, -1] if min_y == Float::INFINITY
  [x, min_y.to_i]
end
