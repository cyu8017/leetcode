# LeetCode 1553 - Minimum Number of Days to Eat N Oranges
# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

# @param {Integer} n
# @return {Integer}
def min_days(n)
  memo = {}
  dp = lambda do |x|
    return x if x <= 1
    return memo[x] if memo.key?(x)
    memo[x] = 1 + [x % 2 + dp.call(x / 2), x % 3 + dp.call(x / 3)].min
  end
  dp.call(n)
end
