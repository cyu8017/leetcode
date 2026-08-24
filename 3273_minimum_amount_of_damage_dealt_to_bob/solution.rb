# LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

# @param {Integer} power
# @param {Integer[]} damage
# @param {Integer[]} health
# @return {Integer}
def min_damage(power, damage, health)
  n = damage.length
  arr = []
  total_dmg = 0
  (0...n).each do |i|
    hits = (health[i] + power - 1) / power
    arr << { dmg: damage[i], hits: hits }
    total_dmg += damage[i]
  end
  arr.sort! { |a, b| a[:hits] * b[:dmg] <=> b[:hits] * a[:dmg] }
  ans = 0
  cur = total_dmg
  arr.each do |e|
    ans += cur * e[:hits]
    cur -= e[:dmg]
  end
  ans
end
