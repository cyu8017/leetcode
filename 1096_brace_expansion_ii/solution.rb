# LeetCode 1096 - Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/

# @param {String} expression
# @return {String[]}
def brace_expansion_ii(expression)
  parse = lambda do |expr, i|
    union = {}
    cur = { "" => true }
    while i < expr.length && expr[i] != "}"
      if expr[i] == "{"
        nested, i = parse.call(expr, i + 1)
        nxt = {}
        cur.each_key do |a|
          nested.each_key { |b| nxt[a + b] = true }
        end
        cur = nxt
      elsif expr[i] == ","
        cur.each_key { |k| union[k] = true }
        cur = { "" => true }
        i += 1
      else
        j = i
        j += 1 while j < expr.length && expr[j].match?(/[a-zA-Z]/)
        token = expr[i...j]
        nxt = {}
        cur.each_key { |a| nxt[a + token] = true }
        cur = nxt
        i = j
      end
    end
    cur.each_key { |k| union[k] = true }
    [union, i + 1]
  end

  result, = parse.call(expression, 0)
  result.keys.sort
end
