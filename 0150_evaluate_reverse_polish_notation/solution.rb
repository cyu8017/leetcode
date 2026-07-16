# @param {String[]} tokens
# @return {Integer}
def eval_rpn(tokens)
  stack = []
  tokens.each do |token|
    if %w[+ - * /].include?(token)
      right = stack.pop
      left = stack.pop
      stack << case token
               when "+" then left + right
               when "-" then left - right
               when "*" then left * right
               else
                 (left.to_f / right).truncate
               end
    else
      stack << token.to_i
    end
  end
  stack[-1]
end