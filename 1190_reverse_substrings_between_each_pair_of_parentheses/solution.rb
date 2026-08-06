# LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

# @param {String} s
# @return {String}
def reverse_parentheses(s)
  stack = []
  s.each_char do |ch|
    if ch == ")"
      chunk = []
      chunk << stack.pop while !stack.empty? && stack[-1] != "("
      stack.pop
      stack.concat(chunk)
    else
      stack << ch
    end
  end
  stack.join
end
