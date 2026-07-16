# LeetCode 0058 - Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# @param {String} s
# @return {Integer}
def length_of_last_word(s)
  length = 0
  i = s.length - 1

  while i >= 0 && s[i] == ' '
    i -= 1
  end

  while i >= 0 && s[i] != ' '
    length += 1
    i -= 1
  end

  length
end
