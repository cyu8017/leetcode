# LeetCode 3675 - Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/

# @param {String} s
# @return {Integer}
def min_operations(s)
  ans = 0
  s.each_char do |c|
    next if c == "a"

    v = 26 - (c.ord - 97)
    ans = v if v > ans
  end
  ans
end
