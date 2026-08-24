# LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} limit
# @return {Integer}
def max_product(nums, k, limit)
  minv = -5000
  memo = {}
  sum_all = 0
  nums.each { |v| sum_all += v }
  return -1 if k.abs > sum_all

  dp = nil
  dp = lambda do |i, product, state, kk|
    if i == nums.length
      return (kk == 0 && state != 0 && product <= limit) ? product : minv
    end
    key = [i, product, state, kk]
    return memo[key] if memo.key?(key)
    res = dp.call(i + 1, product, state, kk)
    if state == 0
      res = [res, dp.call(i + 1, nums[i], 1, kk - nums[i])].max
    end
    if state == 1
      np = product * nums[i]
      np = limit + 1 if np > limit + 1
      res = [res, dp.call(i + 1, np, 2, kk + nums[i])].max
    end
    if state == 2
      np = product * nums[i]
      np = limit + 1 if np > limit + 1
      res = [res, dp.call(i + 1, np, 1, kk - nums[i])].max
    end
    memo[key] = res
    res
  end
  ans = dp.call(0, 1, 0, k)
  ans == minv ? -1 : ans
end
