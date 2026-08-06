# LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

# @param {String} seq
# @return {Integer[]}
def max_depth_after_split(seq)
  depth = 0
  ans = Array.new(seq.length, 0)
  seq.each_char.with_index do |ch, i|
    if ch == "("
      ans[i] = depth % 2
      depth += 1
    else
      depth -= 1
      ans[i] = depth % 2
    end
  end
  ans
end
