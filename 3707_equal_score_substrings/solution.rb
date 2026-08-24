# LeetCode 3707 - Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/

# @param {String} s
# @return {Boolean}
def score_balance(s)
  l = 0
  r = 0
  s.each_char { |c| r += (c.ord - 97) + 1 }
  (0...(s.length - 1)).each do |i|
    x = (s[i].ord - 97) + 1
    l += x
    r -= x
    return true if l == r
  end
  false
end
