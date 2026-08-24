# LeetCode 4006 - Count Valid Prefixes
# https://leetcode.com/problems/count-valid-prefixes/

# @param {String} s
# @return {Integer}
def count_valid_prefixes(s)
  ans = 0
  t = 0
  s.each_char do |ch|
    t += ch == "1" ? 1 : -1
    ans += 1 if t >= -1 && t <= 1
  end
  ans
end
