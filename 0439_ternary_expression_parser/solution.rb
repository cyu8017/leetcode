# LeetCode 0439 - Ternary Expression Parser
# https://leetcode.com/problems/ternary-expression-parser/

class Solution
  def parse_ternary(expression)
    return expression unless expression.include?("?")

    separator = 2
    depth = 0
    (2...expression.length).each do |index|
      case expression[index]
      when "?"
        depth += 1
      when ":"
        if depth.zero?
          separator = index
          break
        end
        depth -= 1
      end
    end

    if expression[0] == "T"
      parse_ternary(expression[2...separator])
    else
      parse_ternary(expression[(separator + 1)..])
    end
  end

  alias_method :parseTernary, :parse_ternary
end
