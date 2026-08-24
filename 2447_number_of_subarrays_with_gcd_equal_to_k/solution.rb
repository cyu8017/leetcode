# LeetCode 2447 - Number of Subarrays With GCD Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_gcd(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 0
  n = nums.length
  (0...n).each do |i|
    g = 0
    (i...n).each do |j|
      g = gcd.call(g, nums[j])
      break if g < k

      ans += 1 if g == k
    end
  end
  ans
end
