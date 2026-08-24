# LeetCode 3334 - Find the Maximum Factor Score of Array
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def lcm_int(a, b)
  a / gcd_int(a, b) * b
end

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  n = nums.length
  gcd_all = nums[0]
  lcm_all = nums[0]
  (1...n).each do |i|
    gcd_all = gcd_int(gcd_all, nums[i])
    lcm_all = lcm_int(lcm_all, nums[i])
  end
  ans = gcd_all * lcm_all
  n.times do |skip|
    g = 0
    l = 1
    first = true
    n.times do |i|
      next if i == skip

      if first
        g = l = nums[i]
        first = false
      else
        g = gcd_int(g, nums[i])
        l = lcm_int(l, nums[i])
      end
    end
    next if first

    v = g * l
    ans = v if v > ans
  end
  ans
end
