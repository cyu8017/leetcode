# LeetCode 3110 - Score of a String
# https://leetcode.com/problems/score-of-a-string/

# @param {String} s
# @return {Integer}
def score_of_string(s)
  ans = 0
  (1...s.length).each { |i| ans += (s[i - 1].ord - s[i].ord).abs }
  ans
end
