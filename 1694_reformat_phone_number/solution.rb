# LeetCode 1694 - Reformat Phone Number
# https://leetcode.com/problems/reformat-phone-number/

# @param {String} number
# @return {String}
def reformat_number(number)
  s = number.chars.select { |c| c.match?(/\d/) }.join
  out = []
  while s.length > 4
    out << s[0, 3]
    s = s[3..]
  end
  if s.length == 4
    out << s[0, 2]
    out << s[2, 2]
  elsif !s.empty?
    out << s
  end
  out.join("-")
end
