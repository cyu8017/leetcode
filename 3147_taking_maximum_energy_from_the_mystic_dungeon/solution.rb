# LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

# @param {Integer[]} energy
# @param {Integer} k
# @return {Integer}
def maximum_energy(energy, k)
  ans = -(1 << 30)
  n = energy.length
  (n - k...n).each do |i|
    s = 0
    j = i
    while j >= 0
      s += energy[j]
      ans = [ans, s].max
      j -= k
    end
  end
  ans
end
