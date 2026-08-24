# LeetCode 3174 - Clear Digits
# https://leetcode.com/problems/clear-digits/

# @param {String} s
# @return {String}
def clear_digits(s)
  stk = []
  s.each_char do |c|
    if c >= "0" && c <= "9"
      stk.pop
    else
      stk << c
    end
  end
  stk.join
end
