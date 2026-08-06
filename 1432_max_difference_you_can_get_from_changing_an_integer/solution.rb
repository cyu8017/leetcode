# LeetCode 1432 - Max Difference You Can Get From Changing An Integer
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

def max_diff(num)
  s = num.to_s
  high = s
  s.each_char do |char|
    if char != '9'
      high = s.gsub(char, '9')
      break
    end
  end
  low = s
  if s[0] != '1'
    low = s.gsub(s[0], '1')
  else
    s[1..].each_char do |char|
      if char != '0' && char != '1'
        low = s.gsub(char, '0')
        break
      end
    end
  end
  high.to_i - low.to_i
end
