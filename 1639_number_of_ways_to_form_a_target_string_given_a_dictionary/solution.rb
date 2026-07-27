# LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

# @param {String[]} words
# @param {String} target
# @return {Integer}
def num_ways(words, target)
  mod = 1_000_000_007
  m = words[0].length
  dp = Array.new(target.length + 1, 0)
  dp[0] = 1
  (0...m).each do |j|
    count = Array.new(26, 0)
    words.each { |word| count[word[j].ord - 97] += 1 }
    [j + 1, target.length].min.downto(1) do |i|
      dp[i] = (dp[i] + dp[i - 1] * count[target[i - 1].ord - 97]) % mod
    end
  end
  dp[-1]
end
