# LeetCode 3498 - Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/

# @param {String} s
# @return {Integer}
def reverse_degree(s)
  ans = 0
  s.each_char.with_index do |c, i|
    ans += (26 - (c.ord - 97)) * (i + 1)
  end
  ans
end
