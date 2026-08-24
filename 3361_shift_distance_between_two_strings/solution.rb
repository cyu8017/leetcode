# LeetCode 3361 - Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/

# @param {String} s
# @param {String} t
# @param {Integer[]} next_cost
# @param {Integer[]} previous_cost
# @return {Integer}
def shift_distance(s, t, next_cost, previous_cost)
  ans = 0
  s.length.times do |i|
    a = s[i].ord - 97
    b = t[i].ord - 97
    next if a == b

    fwd = 0
    x = a
    while x != b
      fwd += next_cost[x]
      x = (x + 1) % 26
    end
    bwd = 0
    x = a
    while x != b
      bwd += previous_cost[x]
      x = (x + 25) % 26
    end
    ans += fwd < bwd ? fwd : bwd
  end
  ans
end
