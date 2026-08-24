# LeetCode 3155 - Maximum Number of Upgradable Servers
# https://leetcode.com/problems/maximum-number-of-upgradable-servers/

# @param {Integer[]} count
# @param {Integer[]} upgrade
# @param {Integer[]} sell
# @param {Integer[]} money
# @return {Integer[]}
def max_upgrades(count, upgrade, sell, money)
  count.each_index.map do |i|
    cnt = count[i]
    [cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i])].min
  end
end
