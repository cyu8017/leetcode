# LeetCode 3181 - Maximum Total Reward Using Operations II
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

# @param {Integer[]} reward_values
# @return {Integer}
def max_total_reward(reward_values)
  reward_values.sort!
  uniq = 0
  reward_values.each_index do |i|
    if uniq == 0 || reward_values[i] != reward_values[uniq - 1]
      reward_values[uniq] = reward_values[i]
      uniq += 1
    end
  end
  f = 1
  (0...uniq).each do |i|
    v = reward_values[i]
    mask = f & ((1 << v) - 1)
    f |= mask << v
  end
  100000.downto(0) { |i| return i if ((f >> i) & 1) != 0 }
  0
end
