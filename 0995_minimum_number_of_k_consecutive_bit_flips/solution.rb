# LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_k_bit_flips(nums, k)
  n = nums.length
  flip = Array.new(n, 0)
  ans = flipped = 0
  nums.each_with_index do |bit, i|
    flipped ^= flip[i - k] if i >= k
    next unless bit == flipped
    return -1 if i + k > n

    ans += 1
    flipped ^= 1
    flip[i] = 1
  end
  ans
end
