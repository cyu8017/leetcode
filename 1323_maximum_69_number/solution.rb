# LeetCode 1323 - Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

def maximum69_number(num)
  num.to_s.sub('6', '9').to_i
end
