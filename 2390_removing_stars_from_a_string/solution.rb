# LeetCode 2390 - Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/

# @param {String} s
# @return {String}
def remove_stars(s)
  stack = []
  s.each_char do |c|
    if c == "*"
      stack.pop
    else
      stack << c
    end
  end
  stack.join
end
