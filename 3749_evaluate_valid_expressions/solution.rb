# LeetCode 3749 - Evaluate Valid Expressions
# https://leetcode.com/problems/evaluate-valid-expressions/

# @param {String} expression
# @return {Integer}
def evaluate_expression(expression)
  parse = nil
  parse = lambda do |i|
    ch = expression[i]
    if (ch >= "0" && ch <= "9") || ch == "-"
      j = i
      j += 1 if expression[j] == "-"
      j += 1 while j < expression.length && expression[j] >= "0" && expression[j] <= "9"
      return [expression[i...j].to_i, j]
    end
    j = i
    j += 1 while expression[j] != "("
    op = expression[i...j]
    j += 1
    p1 = parse.call(j)
    j = p1[1] + 1
    p2 = parse.call(j)
    j = p2[1] + 1
    res = 0
    case op
    when "add"
      res = p1[0] + p2[0]
    when "sub"
      res = p1[0] - p2[0]
    when "mul"
      res = p1[0] * p2[0]
    when "div"
      res = (p1[0].to_f / p2[0]).to_i
    end
    [res, j]
  end
  parse.call(0)[0]
end
