# LeetCode 2578 - Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/

# @param {Integer} num
# @return {Integer}
def split_num(num)
  digits = []
  while num > 0
    digits << (num % 10)
    num /= 10
  end
  digits.sort!
  a = b = 0
  digits.each_with_index do |d, i|
    if i.even?
      a = a * 10 + d
    else
      b = b * 10 + d
    end
  end
  a + b
end
