# LeetCode 1021 - Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/

# @param {String} s
# @return {String}
def remove_outer_parentheses(s)
  ans = []
  depth = 0
  s.each_char do |ch|
    if ch == "("
      ans << ch if depth.positive?
      depth += 1
    else
      depth -= 1
      ans << ch if depth.positive?
    end
  end
  ans.join
end
