# LeetCode 1003 - Check If Word Is Valid After Substitutions
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  s.each_char do |ch|
    stack << ch
    if stack.length >= 3 && stack[-3..] == %w[a b c]
      3.times { stack.pop }
    end
  end
  stack.empty?
end
