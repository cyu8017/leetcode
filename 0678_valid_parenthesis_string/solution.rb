# LeetCode 0678 - Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/

# @param {String} s
# @return {Boolean}
def check_valid_string(s)
  lo = 0
  hi = 0
  s.each_char do |ch|
    if ch == "("
      lo += 1
      hi += 1
    elsif ch == ")"
      lo = [lo - 1, 0].max
      hi -= 1
      return false if hi < 0
    else
      lo = [lo - 1, 0].max
      hi += 1
    end
  end
  lo.zero?
end
