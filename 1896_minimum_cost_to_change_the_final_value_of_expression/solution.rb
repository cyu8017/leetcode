# LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

# @param {String} expression
# @return {Integer}
def min_operations_to_flip(expression)
  combine = lambda do |left, op, right|
    left_val, left_to_zero, left_to_one = left
    right_val, right_to_zero, right_to_one = right
    if op == "&"
      and_val = left_val & right_val
      and_to_zero = [left_to_zero, left_to_one + right_to_zero].min
      and_to_one = left_to_one + right_to_one
      or_to_zero = left_to_zero + right_to_zero
      or_to_one = [left_to_one, left_to_zero + right_to_one, right_to_zero + left_to_one].min
      val = and_val
      to_zero = [and_to_zero, 1 + or_to_zero].min
      to_one = [and_to_one, 1 + or_to_one].min
    else
      or_val = left_val | right_val
      or_to_zero = left_to_zero + right_to_zero
      or_to_one = [left_to_one, left_to_zero + right_to_one, right_to_zero + left_to_one].min
      and_to_zero = [left_to_zero, left_to_one + right_to_zero].min
      and_to_one = left_to_one + right_to_one
      val = or_val
      to_zero = [or_to_zero, 1 + and_to_zero].min
      to_one = [or_to_one, 1 + and_to_one].min
    end
    [val, to_zero, to_one]
  end

  index = 0

  parse_factor = nil
  parse_expr = lambda do
    node = parse_factor.call
    while index < expression.length && "&|".include?(expression[index])
      op = expression[index]
      index += 1
      node = combine.call(node, op, parse_factor.call)
    end
    node
  end

  parse_factor = lambda do
    if "01".include?(expression[index])
      value = expression[index].to_i
      index += 1
      to_zero = value == 0 ? 0 : 1
      to_one = value == 0 ? 1 : 0
      return [value, to_zero, to_one]
    end
    index += 1
    node = parse_expr.call
    index += 1
    node
  end

  value, to_zero, to_one = parse_expr.call
  value == 0 ? to_one : to_zero
end
