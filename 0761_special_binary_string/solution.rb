# LeetCode 0761 - Special Binary String
# https://leetcode.com/problems/special-binary-string/

# @param {String} s
# @return {String}
def make_largest_special(s)
  parts = []
  balance = 0
  start = 0
  s.chars.each_with_index do |ch, i|
    balance += ch == "1" ? 1 : -1
    if balance == 0
      parts << "1" + make_largest_special(s[(start + 1)...i]) + "0"
      start = i + 1
    end
  end
  parts.sort.reverse.join
end
