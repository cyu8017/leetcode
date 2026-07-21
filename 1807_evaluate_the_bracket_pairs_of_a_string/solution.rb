
# @param {String} s
# @param {String[][]} knowledge
# @return {String}
def evaluate(s, knowledge)
  lookup = {}
  knowledge.each { |key, value| lookup[key] = value }
  result = []
  i = 0
  while i < s.length
    if s[i] == '('
      j = s.index(')', i + 1)
      key = s[(i + 1)...j]
      result << (lookup[key] || '?')
      i = j + 1
    else
      result << s[i]
      i += 1
    end
  end
  result.join
end
