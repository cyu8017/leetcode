# LeetCode 3366 - Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/

# @param {Float[][]} ndp
# @param {Float} base
# @param {Integer} na
# @param {Integer} nb
# @param {Integer} v
# @return {void}
def try_cand(ndp, base, na, nb, v)
  ndp[na][nb] = base + v if base + v < ndp[na][nb]
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} op1
# @param {Integer} op2
# @return {Integer}
def min_array_sum(nums, k, op1, op2)
  inf = 1e18
  dp = Array.new(op1 + 1) { Array.new(op2 + 1, inf) }
  dp[0][0] = 0
  nums.each do |x|
    ndp = Array.new(op1 + 1) { Array.new(op2 + 1, inf) }
    (0..op1).each do |a|
      (0..op2).each do |b|
        next if dp[a][b] == inf

        try_cand(ndp, dp[a][b], a, b, x)
        try_cand(ndp, dp[a][b], a + 1, b, (x + 1) / 2) if a < op1
        try_cand(ndp, dp[a][b], a, b + 1, x - k) if b < op2 && x >= k
        if a < op1 && b < op2
          v1 = (x + 1) / 2
          try_cand(ndp, dp[a][b], a + 1, b + 1, v1 - k) if v1 >= k
          try_cand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2) if x >= k
        end
      end
    end
    dp = ndp
  end
  ans = inf
  (0..op1).each do |a|
    (0..op2).each { |b| ans = dp[a][b] if dp[a][b] < ans }
  end
  ans.to_i
end
