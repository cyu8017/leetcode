# LeetCode 0241 - Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/

# @param {String} expression
# @return {Integer[]}
def diff_ways_to_compute(expression)
  return [expression.to_i] if expression.match?(/^\d+$/)

  result = []
  expression.each_char.with_index do |char, index|
    next unless ['+', '-', '*'].include?(char)

    left = diff_ways_to_compute(expression[0...index])
    right = diff_ways_to_compute(expression[(index + 1)..])
    left.each do |left_value|
      right.each do |right_value|
        result << case char
                  when '+' then left_value + right_value
                  when '-' then left_value - right_value
                  else left_value * right_value
                  end
      end
    end
  end
  result
end
