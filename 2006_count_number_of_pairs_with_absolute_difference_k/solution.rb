# LeetCode 2006 - Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_k_difference(nums, k)
  freq = Hash.new(0)
  ans = 0
  nums.each do |x|
    ans += freq[x - k]
    ans += freq[x + k]
    freq[x] += 1
  end
  ans
end
