# LeetCode 1047 - Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# @param {String} s
# @return {String}
def remove_duplicates(s)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1] == ch
      stack.pop
    else
      stack << ch
    end
  end
  stack.join
end
