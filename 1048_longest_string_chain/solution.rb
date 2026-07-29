# LeetCode 1048 - Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

# @param {String[]} words
# @return {Integer}
def longest_str_chain(words)
  words = words.sort_by(&:length)
  dp = {}
  ans = 1
  words.each do |w|
    dp[w] = 1
    w.length.times do |i|
      prev = w[0...i] + w[(i + 1)..]
      dp[w] = [dp[w], dp[prev] + 1].max if dp.key?(prev)
    end
    ans = [ans, dp[w]].max
  end
  ans
end
