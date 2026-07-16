# LeetCode 0032 - Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

# @param {String} s
# @return {Integer}
def longest_valid_parentheses(s)
  stack = [-1]
  best = 0

  s.each_char.with_index do |ch, i|
    if ch == "("
      stack << i
    else
      stack.pop
      if stack.empty?
        stack << i
      else
        best = [best, i - stack[-1]].max
      end
    end
  end

  best
end
