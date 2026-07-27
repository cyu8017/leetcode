# LeetCode 1614 - Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

# @param {String} s
# @return {Integer}
def max_depth(s)
  depth = ans = 0
  s.each_char do |ch|
    if ch == "("
      depth += 1
      ans = [ans, depth].max
    elsif ch == ")"
      depth -= 1
    end
  end
  ans
end
