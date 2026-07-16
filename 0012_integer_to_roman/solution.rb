# LeetCode 0012 - Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

# @param {Integer} num
# @return {String}
def int_to_roman(num)
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symbols = %w[M CM D CD C XC L XL X IX V IV I]
  result = +""
  value = num

  values.each_with_index do |v, i|
    while value >= v
      result << symbols[i]
      value -= v
    end
  end

  result
end
