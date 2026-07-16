# LeetCode 0020 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  pairs = { ")" => "(", "]" => "[", "}" => "{" }

  s.each_char do |ch|
    if "([{".include?(ch)
      stack << ch
    elsif stack.empty? || stack.pop != pairs[ch]
      return false
    end
  end

  stack.empty?
end
