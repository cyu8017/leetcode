# LeetCode 3776 - Minimum Moves to Balance Circular Array
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

# @param {Integer[]} balance
# @return {Integer}
def min_moves(balance)
  total = balance.sum
  return -1 if total < 0
  n = balance.length
  mn = balance[0]
  idx = 0
  (1...n).each do |i|
    if balance[i] < mn
      mn = balance[i]
      idx = i
    end
  end
  return 0 if mn >= 0
  need = -mn
  ans = 0
  (1...n).each do |j|
    a = balance[(idx - j + n) % n]
    b = balance[(idx + j) % n]
    c1 = [a, need].min
    need -= c1
    ans += c1 * j
    c2 = [b, need].min
    need -= c2
    ans += c2 * j
  end
  ans
end
