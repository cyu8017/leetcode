# LeetCode 1717 - Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings/

# @param {String} s
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def maximum_gain(s, x, y)
  remove = lambda do |text, pair, score|
    stack = []
    gained = 0
    text.each_char do |ch|
      if !stack.empty? && stack[-1] == pair[0] && ch == pair[1]
        stack.pop
        gained += score
      else
        stack << ch
      end
    end
    [stack.join, gained]
  end

  if x >= y
    rest, first = remove.call(s, 'ab', x)
    _, second = remove.call(rest, 'ba', y)
  else
    rest, first = remove.call(s, 'ba', y)
    _, second = remove.call(rest, 'ab', x)
  end
  first + second
end
