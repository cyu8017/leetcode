# LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
# https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

# @param {String} sentence
# @param {Integer} k
# @return {Integer}
def minimum_cost(sentence, k)
  words = sentence.strip.split
  n = words.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[n] = 0
  (n - 1).downto(0) do |i|
    length = -1
    (i...n).each do |j|
      length += 1 + words[j].length
      break if length > k

      cost = 0
      if j < n - 1
        extra = k - length
        cost = extra * extra
      end
      dp[i] = [dp[i], cost + dp[j + 1]].min
    end
  end
  dp[0]
end

alias solve minimum_cost
