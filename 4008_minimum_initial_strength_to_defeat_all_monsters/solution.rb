# LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
# https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

# @param {Integer[]} monsters
# @param {Integer[][]} boosts
# @return {Integer}
def min_initial_strength(monsters, boosts)
  n = monsters.length
  d = Array.new(n + 1, 0)
  boosts.each do |b|
    d[b[0]] += b[2]
    d[b[1] + 1] -= b[2]
  end
  check = lambda do |v|
    bonus = 0
    monsters.each_with_index do |m, i|
      bonus += d[i]
      return false if v + bonus < m
      v -= m
      v = 0 if v < 0
    end
    true
  end
  left = 0
  right = 1_000_000_000_000_000
  while left < right
    mid = (left + right) / 2
    if check.call(mid)
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
