# LeetCode 2364 - Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

# @param {Integer[]} nums
# @return {Integer}
def count_bad_pairs(nums)
  n = nums.length
  total = n * (n - 1) / 2
  freq = Hash.new(0)
  good = 0
  nums.each_with_index do |x, i|
    key = x - i
    good += freq[key]
    freq[key] += 1
  end
  total - good
end
