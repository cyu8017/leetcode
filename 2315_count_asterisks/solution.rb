# LeetCode 2315 - Count Asterisks
# https://leetcode.com/problems/count-asterisks/

# @param {String} s
# @return {Integer}
def count_asterisks(s)
  ans = 0
  inside = false
  s.each_char do |c|
    if c == "|"
      inside = !inside
    elsif c == "*" && !inside
      ans += 1
    end
  end
  ans
end
