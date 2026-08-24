# LeetCode 0770 - Basic Calculator IV
# https://leetcode.com/problems/basic-calculator-iv/

# @param {String} expression
# @param {String[]} evalvars
# @param {Integer[]} evalints
# @return {String[]}
def basic_calculator_iv(expression, evalvars, evalints)
  values = evalvars.zip(evalints).to_h
  tokens = expression.gsub("(", " ( ").gsub(")", " ) ").split
  pos = 0

  clean = lambda do |poly|
    poly.reject { |_k, v| v == 0 }
  end

  add = lambda do |left, right|
    result = left.dup
    right.each { |key, coef| result[key] = (result[key] || 0) + coef }
    clean.call(result)
  end

  negate = lambda do |poly|
    poly.transform_values { |v| -v }
  end

  mul = lambda do |left, right|
    result = {}
    left.each do |lk, lv|
      right.each do |rk, rv|
        key = (lk + rk).sort
        result[key] = (result[key] || 0) + lv * rv
      end
    end
    clean.call(result)
  end

  atom = lambda do |token|
    poly = {}
    if token.match?(/\A[A-Za-z]+\z/)
      if values.key?(token)
        poly[[]] = values[token]
      else
        poly[[token]] = 1
      end
    else
      poly[[]] = token.to_i
    end
    poly
  end

  parse_expr = nil
  parse_term = nil
  parse_factor = nil

  parse_factor = lambda do
    token = tokens[pos]
    if token == "("
      pos += 1
      poly = parse_expr.call
      pos += 1
      return poly
    end
    pos += 1
    atom.call(token)
  end

  parse_term = lambda do
    poly = parse_factor.call
    while pos < tokens.length && tokens[pos] == "*"
      pos += 1
      poly = mul.call(poly, parse_factor.call)
    end
    poly
  end

  parse_expr = lambda do
    poly = parse_term.call
    while pos < tokens.length && ["+", "-"].include?(tokens[pos])
      op = tokens[pos]
      pos += 1
      right = parse_term.call
      poly = op == "+" ? add.call(poly, right) : add.call(poly, negate.call(right))
    end
    poly
  end

  poly = parse_expr.call
  keys = poly.keys.sort_by { |k| [-k.length, k] }
  keys.map do |key|
    coef = poly[key]
    key.empty? ? coef.to_s : ([coef.to_s] + key).join("*")
  end
end
