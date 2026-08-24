# LeetCode 2223 - Sum of Scores of Built Strings
# https://leetcode.com/problems/sum-of-scores-of-built-strings/

# @param {String} s
# @return {Integer}
def sum_scores(s)
  n = s.length
  z = Array.new(n, 0)
  l = r = 0
  (1...n).each do |i|
    z[i] = [r - i + 1, z[i - l]].min if i <= r
    z[i] += 1 while i + z[i] < n && s[z[i]] == s[i + z[i]]
    if i + z[i] - 1 > r
      l = i
      r = i + z[i] - 1
    end
  end
  n + z[1..].sum
end
