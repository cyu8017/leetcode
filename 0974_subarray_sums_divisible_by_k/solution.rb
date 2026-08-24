# LeetCode 0974 - Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_div_by_k(nums, k)
  count = Hash.new(0)
  count[0] = 1
  prefix = 0
  ans = 0
  nums.each do |x|
    prefix = (prefix + x) % k
    ans += count[prefix]
    count[prefix] += 1
  end
  ans
end
