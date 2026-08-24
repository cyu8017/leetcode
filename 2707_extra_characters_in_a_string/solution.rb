# LeetCode 2707 - Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/

# @param {String} s
# @param {String[]} dictionary
# @return {Integer}
def min_extra_char(s, dictionary)
  dct = {}
  dictionary.each { |w| dct[w] = true }
  n = s.length
  dp = Array.new(n + 1, n)
  dp[0] = 0
  n.times do |i|
    dp[i + 1] = [dp[i + 1], dp[i] + 1].min
    ((i + 1)..n).each do |j|
      dp[j] = [dp[j], dp[i]].min if dct[s[i...j]]
    end
  end
  dp[n]
end
