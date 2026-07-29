# LeetCode 1016 - Binary String With Substrings Representing 1 To N
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

# @param {String} s
# @param {Integer} n
# @return {Boolean}
def query_string(s, n)
  n.downto(n / 2 + 1) do |i|
    return false unless s.include?(i.to_s(2))
  end
  true
end
