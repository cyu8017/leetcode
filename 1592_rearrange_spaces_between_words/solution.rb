# LeetCode 1592 - Rearrange Spaces Between Words
# https://leetcode.com/problems/rearrange-spaces-between-words/

# @param {String} text
# @return {String}
def reorder_spaces(text)
  words = text.split
  spaces = text.count(' ')
  return words[0] + (' ' * spaces) if words.length == 1
  between, trailing = spaces.divmod(words.length - 1)
  words.join(' ' * between) + (' ' * trailing)
end
