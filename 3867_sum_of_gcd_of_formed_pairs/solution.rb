# LeetCode 3867 - Sum of GCD of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

# @param {Integer[]} nums
# @return {Integer}
def gcd_sum(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  prefix_gcd = Array.new(n, 0)
  mx = 0
  n.times do |i|
    mx = [mx, nums[i]].max
    prefix_gcd[i] = gcd.call(nums[i], mx)
  end
  prefix_gcd.sort!
  ans = 0
  (n / 2).times { |i| ans += gcd.call(prefix_gcd[i], prefix_gcd[n - i - 1]) }
  ans
end
