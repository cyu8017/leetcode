# LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def make_similar(nums, target)
  nums = nums.sort
  target = target.sort
  odd_n = []
  even_n = []
  odd_t = []
  even_t = []
  nums.each { |x| (x.even? ? even_n : odd_n) << x }
  target.each { |x| (x.even? ? even_t : odd_t) << x }
  ans = 0
  odd_n.each_index do |i|
    diff = odd_n[i] - odd_t[i]
    ans += diff / 2 if diff > 0
  end
  even_n.each_index do |i|
    diff = even_n[i] - even_t[i]
    ans += diff / 2 if diff > 0
  end
  ans
end
