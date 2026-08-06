# LeetCode 1573 - Number of Ways to Split a String
# https://leetcode.com/problems/number-of-ways-to-split-a-string/

# @param {String} s
# @return {Integer}
def num_ways(s)
  mod = 1_000_000_007
  ones = s.count('1')
  return 0 if ones % 3 != 0
  if ones == 0
    gaps = s.length - 1
    return gaps * (gaps - 1) / 2 % mod
  end
  target = ones / 3
  positions = []
  s.each_char.with_index { |ch, i| positions << i if ch == '1' }
  (positions[target] - positions[target - 1]) * (positions[2 * target] - positions[2 * target - 1]) % mod
end
