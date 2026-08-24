# LeetCode 3259 - Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

# @param {Integer[]} energy_drink_a
# @param {Integer[]} energy_drink_b
# @return {Integer}
def max_energy_boost(energy_drink_a, energy_drink_b)
  n = energy_drink_a.length
  dp_a = Array.new(n, 0)
  dp_b = Array.new(n, 0)
  dp_a[0] = energy_drink_a[0]
  dp_b[0] = energy_drink_b[0]
  return [dp_a[0], dp_b[0]].max if n == 1
  dp_a[1] = energy_drink_a[1] + dp_a[0]
  dp_b[1] = energy_drink_b[1] + dp_b[0]
  (2...n).each do |i|
    dp_a[i] = energy_drink_a[i] + [dp_a[i - 1], dp_b[i - 2]].max
    dp_b[i] = energy_drink_b[i] + [dp_b[i - 1], dp_a[i - 2]].max
  end
  [dp_a[n - 1], dp_b[n - 1]].max
end
