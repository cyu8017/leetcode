# LeetCode 0736 - Parse Lisp Expression
# https://leetcode.com/problems/parse-lisp-expression/

# @param {String} expression
# @return {Integer}
def evaluate(expression)
  tokens = expression.gsub("(", " ( ").gsub(")", " ) ").split
  pos = 0

  parse = lambda do |env|
    token = tokens[pos]
    if token != "("
      pos += 1
      return token.to_i if token.match?(/^-?\d+$/)

      env.reverse_each do |scope|
        return scope[token] if scope.key?(token)
      end
      raise KeyError, token
    end

    pos += 1
    op = tokens[pos]
    pos += 1

    if op == "let"
      env << {}
      while tokens[pos] != ")"
        if tokens[pos] == "(" || tokens[pos + 1] == ")"
          value = parse.call(env)
          pos += 1
          env.pop
          return value
        end
        var = tokens[pos]
        pos += 1
        env[-1][var] = parse.call(env)
      end
    end

    if op == "add"
      left = parse.call(env)
      right = parse.call(env)
      pos += 1
      return left + right
    end

    if op == "mult"
      left = parse.call(env)
      right = parse.call(env)
      pos += 1
      return left * right
    end

    raise ArgumentError, op
  end

  parse.call([])
end
