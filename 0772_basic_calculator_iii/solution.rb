# LeetCode 0772 - Basic Calculator III
# https://leetcode.com/problems/basic-calculator-iii/

# @param {String} s
# @return {Integer}
def calculate(s)
  parse = lambda do |expr, i|
    stack = []
    num = 0
    sign = "+"
    while i < expr.length
      ch = expr[i]
      num = num * 10 + ch.to_i if ch >= "0" && ch <= "9"
      if ch == "("
        num, i = parse.call(expr, i + 1)
      end
      if "+-*/)".include?(ch) || i == expr.length - 1
        case sign
        when "+"
          stack << num
        when "-"
          stack << -num
        when "*"
          stack << stack.pop * num
        else
          top = stack.pop
          stack << (top.to_f / num).truncate
        end
        return [stack.sum, i] if ch == ")"

        sign = ch
        num = 0
      end
      i += 1
    end
    [stack.sum, i]
  end

  parse.call(s.delete(" "), 0)[0]
end
