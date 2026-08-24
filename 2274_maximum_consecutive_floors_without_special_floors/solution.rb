# LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

# @param {Integer} bottom
# @param {Integer} top
# @param {Integer[]} special
# @return {Integer}
def max_consecutive(bottom, top, special)
  special = special.sort
  ans = special[0] - bottom
  (1...special.length).each { |i| ans = [ans, special[i] - special[i - 1] - 1].max }
  [ans, top - special[-1]].max
end
