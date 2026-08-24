# LeetCode 3712 - Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_divisible_by_k(nums, k)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ans = 0
  cnt.each { |key, val| ans += key * val if val % k == 0 }
  ans
end
