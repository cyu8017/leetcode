# LeetCode 0008 - String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

# @param {String} s
# @return {Integer}
def my_atoi(s)
  int_max = 2**31 - 1
  int_min = -2**31
  i = 0
  i += 1 while i < s.length && s[i] == " "

  return 0 if i >= s.length

  sign = 1
  if s[i] == "-"
    sign = -1
    i += 1
  elsif s[i] == "+"
    i += 1
  end

  result = 0
  while i < s.length && s[i] >= "0" && s[i] <= "9"
    digit = s[i].ord - "0".ord
    return int_min if sign == -1 && result > (int_max - digit) / 10
    return int_max if sign == 1 && result > (int_max - digit) / 10
    result = result * 10 + digit
    i += 1
  end

  sign * result
end
