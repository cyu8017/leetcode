# LeetCode 0591 - Tag Validator
# https://leetcode.com/problems/tag-validator/

# @param {String} code
# @return {Boolean}
def is_valid(code)
  stack = []
  i = 0
  n = code.length

  while i < n
    if code[i, 9] == "<![CDATA["
      return false if stack.empty?

      j = code.index("]]>", i + 9)
      return false if j.nil?

      i = j + 3
    elsif code[i, 2] == "</"
      j = code.index(">", i + 2)
      return false if j.nil?

      tag = code[(i + 2)...j]
      return false if stack.empty? || stack[-1] != tag

      stack.pop
      i = j + 1
      return false if stack.empty? && i < n
    elsif code[i] == "<"
      j = code.index(">", i + 1)
      return false if j.nil?

      tag = code[(i + 1)...j]
      return false if tag.empty? || tag.length > 9 || tag.chars.any? { |ch| ch < "A" || ch > "Z" }

      stack << tag
      i = j + 1
    else
      return false if stack.empty?

      i += 1
    end
  end

  stack.empty?
end
