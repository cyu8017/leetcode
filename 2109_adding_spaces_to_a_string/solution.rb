# LeetCode 2109 - Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

# @param {String} s
# @param {Integer[]} spaces
# @return {String}
def add_spaces(s, spaces)
  b = []
  j = 0
  s.chars.each_with_index do |ch, i|
    if j < spaces.length && spaces[j] == i
      b << " "
      j += 1
    end
    b << ch
  end
  b.join
end
