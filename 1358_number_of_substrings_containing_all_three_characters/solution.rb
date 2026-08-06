# LeetCode 1358 - Number Of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

def number_of_substrings(s)
  last = [-1, -1, -1]
  ans = 0
  s.each_char.with_index do |c, i|
    last[c.ord - 97] = i
    ans += last.min + 1
  end
  ans
end
