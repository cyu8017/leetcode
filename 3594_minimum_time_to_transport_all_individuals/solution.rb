# LeetCode 3594 - Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} m
# @param {Integer[]} time
# @param {Float[]} mul
# @return {Float}
def min_time(n, k, m, time, mul)
  t = time.sort
  total = 0.0
  stage = 0
  left = n
  while left > 0
    take = [k, left].min
    slow = t[left - 1]
    total += slow * mul[stage % m]
    left -= take
    stage += 1
    if left > 0
      total += t[0] * mul[stage % m]
      stage += 1
    end
  end
  total
end
