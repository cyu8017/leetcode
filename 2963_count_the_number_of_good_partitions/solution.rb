# LeetCode 2963 - Count the Number of Good Partitions
# https://leetcode.com/problems/count-the-number-of-good-partitions/

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_partitions(nums)
  mod = 1_000_000_007
  last = {}
  nums.each_with_index { |v, i| last[v] = i }
  ans = 1
  finish = 0
  nums.each_with_index do |v, i|
    finish = last[v] if last[v] > finish
    ans = ans * 2 % mod if i == finish && i != nums.length - 1
  end
  ans
end
