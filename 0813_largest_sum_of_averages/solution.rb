# LeetCode 0813 - Largest Sum of Averages
# https://leetcode.com/problems/largest-sum-of-averages/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def largest_sum_of_averages(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0.0)
  nums.each_with_index { |num, i| prefix[i + 1] = prefix[i] + num }

  average = ->(i, j) { (prefix[j] - prefix[i]) / (j - i) }

  dp = (1..n).map { |i| average.call(0, i) }
  (2..k).each do |groups|
    nxt = Array.new(n, 0.0)
    (groups - 1...n).each do |i|
      best = 0.0
      (groups - 2...i).each do |j|
        cand = dp[j] + average.call(j + 1, i + 1)
        best = cand if cand > best
      end
      nxt[i] = best
    end
    dp = nxt
  end
  dp[-1]
end
