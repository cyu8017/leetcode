# LeetCode 1616 - Split Two Strings to Make Palindrome
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

def _check_palindrome_formation(x, y)
  i = 0
  j = x.length - 1
  while i < j && x[i] == y[j]
    i += 1
    j -= 1
  end
  mid_x = x[i..j]
  mid_y = y[i..j]
  mid_x == mid_x.reverse || mid_y == mid_y.reverse
end

# @param {String} a
# @param {String} b
# @return {Boolean}
def check_palindrome_formation(a, b)
  _check_palindrome_formation(a, b) || _check_palindrome_formation(b, a)
end
