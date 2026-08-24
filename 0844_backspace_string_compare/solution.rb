# LeetCode 0844 - Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
  build = lambda do |text|
    stack = []
    text.each_char do |ch|
      if ch == "#"
        stack.pop unless stack.empty?
      else
        stack << ch
      end
    end
    stack
  end

  build.call(s) == build.call(t)
end
