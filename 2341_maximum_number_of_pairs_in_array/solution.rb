# LeetCode 2341 - Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

# @param {Integer[]} nums
# @return {Integer[]}
def number_of_pairs(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  pairs = 0
  left = 0
  cnt.each_value do |c|
    pairs += c / 2
    left += c % 2
  end
  [pairs, left]
end
