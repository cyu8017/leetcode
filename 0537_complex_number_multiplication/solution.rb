# LeetCode 0537 - Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/

class Solution
  def complex_number_multiply(num1, num2)
    a, b = parse(num1)
    c, d = parse(num2)
    real = a * c - b * d
    imag = a * d + b * c
    "#{real}+#{imag}i"
  end

  alias_method :complexNumberMultiply, :complex_number_multiply

  private

  def parse(num)
    real, imag = num.split("+")
    [real.to_i, imag[0...-1].to_i]
  end
end
