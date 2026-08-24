# LeetCode 0856 - Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

# @param {String} s
# @return {Integer}
def score_of_parentheses(s)
  stack = [0]
  s.each_char do |ch|
    if ch == "("
      stack << 0
    else
      val = stack.pop
      stack[-1] += [2 * val, 1].max
    end
  end
  stack[0]
end
