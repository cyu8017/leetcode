# LeetCode 1246 - Palindrome Removal
# https://leetcode.com/problems/palindrome-removal/

# @param {Integer[]} arr
# @return {Integer}
def minimum_moves(arr)
  n = arr.length
  dp = Array.new(n) { Array.new(n, 0) }
  n.times { |i| dp[i][i] = 1 }
  (2..n).each do |length|
    (0..n - length).each do |i|
      j = i + length - 1
      dp[i][j] = 1 + dp[i + 1][j]
      dp[i][j] = [dp[i][j], 1 + (i + 2 <= j ? dp[i + 2][j] : 0)].min if arr[i] == arr[i + 1]
      ((i + 2)..j).each do |k|
        if arr[i] == arr[k]
          dp[i][j] = [dp[i][j], dp[i + 1][k - 1] + (k < j ? dp[k + 1][j] : 0)].min
        end
      end
    end
  end
  dp[0][n - 1]
end
