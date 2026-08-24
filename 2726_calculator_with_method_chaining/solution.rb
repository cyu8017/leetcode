# LeetCode 2726 - Calculator with Method Chaining
# https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator
  def initialize(value)
    @val = value.to_f
  end

  def add(value)
    @val += value
    self
  end

  def subtract(value)
    @val -= value
    self
  end

  def multiply(value)
    @val *= value
    self
  end

  def divide(value)
    raise "Division by zero is not allowed" if value == 0

    @val /= value
    self
  end

  def power(value)
    @val **= value
    self
  end

  def get_result
    @val
  end
end

# @param {Float} value
# @return {Calculator}
def calculator(value)
  Calculator.new(value)
end

def solve(*args)
  calculator(*args)
end
