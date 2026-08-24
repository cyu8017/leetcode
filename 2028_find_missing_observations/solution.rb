# LeetCode 2028 - Find Missing Observations
# https://leetcode.com/problems/find-missing-observations/

# @param {Integer[]} rolls
# @param {Integer} mean
# @param {Integer} n
# @return {Integer[]}
def missing_rolls(rolls, mean, n)
  remain = mean * (rolls.length + n) - rolls.sum
  return [] if remain < n || remain > 6 * n

  base_val, extra = remain.divmod(n)
  ans = Array.new(n, base_val)
  extra.times { |i| ans[(i + 1) % n] += 1 }
  ans
end
