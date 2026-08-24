# LeetCode 3632 - Subarrays With XOR At Least K
# https://leetcode.com/problems/subarrays-with-xor-at-least-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_with_xor_at_least_k(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    x = 0
    (i...n).each do |j|
      x ^= nums[j]
      ans += 1 if x >= k
    end
  end
  ans
end
