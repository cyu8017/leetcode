# LeetCode 0823 - Binary Trees With Factors
# https://leetcode.com/problems/binary-trees-with-factors/

# @param {Integer[]} arr
# @return {Integer}
def num_factored_binary_trees(arr)
  mod = 10**9 + 7
  arr = arr.sort
  dp = {}
  arr.each_with_index do |x, i|
    ways = 1
    i.times do |j|
      left = arr[j]
      next unless x % left == 0

      right = x / left
      ways = (ways + dp[left] * dp[right]) % mod if dp.key?(right)
    end
    dp[x] = ways
  end
  dp.values.sum % mod
end
