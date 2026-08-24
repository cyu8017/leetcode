# LeetCode 3207 - Maximum Points After Enemy Battles
# https://leetcode.com/problems/maximum-points-after-enemy-battles/

# @param {Integer[]} enemy_energies
# @param {Integer} current_energy
# @return {Integer}
def maximum_points(enemy_energies, current_energy)
  enemy_energies.sort!
  return 0 if current_energy < enemy_energies[0]
  ans = 0
  (enemy_energies.length - 1).downto(0) do |i|
    ans += current_energy / enemy_energies[0]
    current_energy %= enemy_energies[0]
    current_energy += enemy_energies[i]
  end
  ans
end
