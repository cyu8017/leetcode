# LeetCode 1544 - Make The String Great
# https://leetcode.com/problems/make-the-string-great/

# @param {String} s
# @return {String}
def make_good(s)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1] != ch && stack[-1].downcase == ch.downcase
      stack.pop
    else
      stack << ch
    end
  end
  stack.join
end
