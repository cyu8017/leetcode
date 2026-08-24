# LeetCode 0640 - Solve the Equation
# https://leetcode.com/problems/solve-the-equation/

# @param {String} equation
# @return {String}
def solve_equation(equation)
  parse = lambda do |expr|
    coef = 0
    const = 0
    expr.scan(/[+-]?(?:\d+x|x|\d+)/).each do |token|
      if token.include?("x")
        raw = token.delete("x")
        if raw.empty? || raw == "+"
          coef += 1
        elsif raw == "-"
          coef -= 1
        else
          coef += raw.to_i
        end
      else
        const += token.to_i
      end
    end
    [coef, const]
  end

  left, right = equation.split("=")
  left_coef, left_const = parse.call(left)
  right_coef, right_const = parse.call(right)
  coef = left_coef - right_coef
  const = right_const - left_const

  return const.zero? ? "Infinite solutions" : "No solution" if coef.zero?

  "x=#{const / coef}"
end
