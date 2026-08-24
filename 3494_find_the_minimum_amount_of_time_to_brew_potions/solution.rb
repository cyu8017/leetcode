# LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

# @param {Integer[]} skill
# @param {Integer[]} mana
# @return {Integer}
def min_time(skill, mana)
  n = skill.length
  m = mana.length
  done = Array.new(n, 0)
  (0...m).each do |j|
    t = 0
    (0...n).each do |i|
      t = done[i] if done[i] > t
      t += skill[i] * mana[j]
      done[i] = t
    end
    (n - 2).downto(0) { |i| done[i] = done[i + 1] - skill[i + 1] * mana[j] }
  end
  done[n - 1]
end
