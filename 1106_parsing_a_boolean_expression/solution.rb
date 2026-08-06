# LeetCode 1106 - Parsing A Boolean Expression
# https://leetcode.com/problems/parsing-a-boolean-expression/

# @param {String} expression
# @return {Boolean}
def parse_bool_expr(expression)
  stack = []
  expression.each_char do |ch|
    if ch == ")"
      values = []
      while !stack.empty? && !"&|!".include?(stack[-1])
        token = stack.pop
        values << (token == "t") if "tf".include?(token)
      end
      op = stack.pop
      if op == "!"
        stack << (values[0] ? "f" : "t")
      elsif op == "&"
        stack << (values.all? ? "t" : "f")
      else
        stack << (values.any? ? "t" : "f")
      end
    elsif ch != ","
      stack << ch
    end
  end
  stack[-1] == "t"
end
