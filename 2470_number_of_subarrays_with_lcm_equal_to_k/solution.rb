# LeetCode 2470 - Number of Subarrays With LCM Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_lcm(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 0
  n = nums.length
  (0...n).each do |i|
    cur = 1
    (i...n).each do |j|
      cur = (cur / gcd.call(cur, nums[j])) * nums[j]
      break if cur > k

      ans += 1 if cur == k
    end
  end
  ans
end
