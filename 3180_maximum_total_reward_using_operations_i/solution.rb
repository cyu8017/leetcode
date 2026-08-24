# LeetCode 3180 - Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

# @param {Integer[]} reward_values
# @return {Integer}
def max_total_reward(reward_values)
  reward_values.sort!
  n = reward_values.length
  f = Array.new(reward_values[n - 1] << 1, -1)
  dfs = lambda do |x|
    return f[x] if f[x] != -1
    idx = reward_values.bsearch_index { |v| v > x } || n
    f[x] = 0
    (idx...n).each do |it|
      f[x] = [f[x], reward_values[it] + dfs.call(x + reward_values[it])].max
    end
    f[x]
  end
  dfs.call(0)
end
