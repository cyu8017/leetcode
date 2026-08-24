# LeetCode 3743 - Maximize Cyclic Partition Score
# https://leetcode.com/problems/maximize-cyclic-partition-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  n = nums.length
  a = nums + nums
  k = n if k > n
  best = 0
  neg = -(10**18)
  (0...n).each do |start|
    seg = a[start, n]
    dp = Array.new(n + 1) { Array.new(k + 1, neg) }
    dp[0][0] = 0
    (1..n).each do |i|
      (1..[k, i].min).each do |j|
        mx = neg
        i.downto(j) do |t|
          mx = seg[t - 1] if seg[t - 1] > mx
          if dp[t - 1][j - 1] > neg
            cand = dp[t - 1][j - 1] + mx
            dp[i][j] = cand if cand > dp[i][j]
          end
        end
      end
    end
    best = dp[n][k] if dp[n][k] > best
  end
  best
end
