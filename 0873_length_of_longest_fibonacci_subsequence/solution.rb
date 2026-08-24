# LeetCode 0873 - Length of Longest Fibonacci Subsequence
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

# @param {Integer[]} arr
# @return {Integer}
def len_longest_fib_subseq(arr)
  index = {}
  arr.each_with_index { |x, i| index[x] = i }
  n = arr.length
  dp = Array.new(n) { Array.new(n, 2) }
  ans = 0
  n.times do |j|
    j.times do |i|
      k = index[arr[j] - arr[i]]
      if !k.nil? && k < i
        dp[i][j] = dp[k][i] + 1
        ans = dp[i][j] if dp[i][j] > ans
      end
    end
  end
  ans >= 3 ? ans : 0
end
