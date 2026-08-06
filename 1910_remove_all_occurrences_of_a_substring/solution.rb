# LeetCode 1910 - Remove All Occurrences of a Substring
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# @param {String} s
# @param {String} part
# @return {String}
def remove_occurrences(s, part)
  stack = []
  m = part.length
  s.each_char do |ch|
    stack << ch
    if stack.length >= m && stack[-m..].join == part
      m.times { stack.pop }
    end
  end
  stack.join
end
