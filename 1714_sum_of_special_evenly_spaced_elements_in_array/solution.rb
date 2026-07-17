# LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
# https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def solve(nums, queries)
  mod = 10**9 + 7
  n = nums.length
  block = Integer.sqrt(n) + 1
  dp = Array.new(block) { Array.new(n, 0) }
  (1...block).each do |step|
    (n - 1).downto(0) do |i|
      dp[step][i] = (nums[i] + (i + step < n ? dp[step][i + step] : 0)) % mod
    end
  end
  queries.map do |start, step|
    if step < block
      dp[step][start]
    else
      total = 0
      (start...n).step(step) { |i| total += nums[i] }
      total % mod
    end
  end
end
