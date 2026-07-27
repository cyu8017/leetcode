# LeetCode 1698 - Number of Distinct Substrings in a String
# https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

# @param {String} s
# @return {Integer}
def count_distinct(s)
  root = {}
  ans = 0
  s.length.times do |i|
    node = root
    s[i..].each_char do |c|
      unless node.key?(c)
        node[c] = {}
        ans += 1
      end
      node = node[c]
    end
  end
  ans
end
