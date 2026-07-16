# LeetCode 0065 - Valid Number
# https://leetcode.com/problems/valid-number/

# @param {String} s
# @return {Boolean}
def is_number(s)
  seen_digit = false
  seen_dot = false
  seen_exp = false

  s.each_char.with_index do |ch, i|
    if ch.match?(/\d/)
      seen_digit = true
    elsif ch == '+' || ch == '-'
      return false if i.positive? && !%w[e E].include?(s[i - 1])
    elsif ch == 'e' || ch == 'E'
      return false if seen_exp || !seen_digit

      seen_exp = true
      seen_digit = false
      seen_dot = false
    elsif ch == '.'
      return false if seen_dot || seen_exp

      seen_dot = true
    else
      return false
    end
  end

  seen_digit
end
