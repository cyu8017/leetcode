# LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  square_free = lambda do |x|
    res = 1
    p = 2
    while p * p <= x
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
      end
      res *= p if cnt.odd?
      p += 1
    end
    res *= x if x > 1
    res
  end

  n = nums.length
  groups = {}
  ans = 0
  (1..n).each do |i|
    sf = square_free.call(i)
    s = groups.fetch(sf, 0) + nums[i - 1]
    groups[sf] = s
    ans = s if s > ans
  end
  ans
end
