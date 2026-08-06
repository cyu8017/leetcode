# LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

# @param {Integer[][]} cost
# @return {Integer}
def connect_two_groups(cost)
  m = cost.length
  n = cost[0].length
  full = 1 << n
  inf = 10**9
  dp = Array.new(full, inf)
  dp[0] = 0
  cost.each do |row|
    nxt = Array.new(full, inf)
    (0...full).each do |mask|
      row.each_with_index do |value, j|
        new_mask = mask | (1 << j)
        nxt[new_mask] = [nxt[new_mask], dp[mask] + value, nxt[mask] + value].min
      end
    end
    dp = nxt
  end
  minimum = (0...n).map { |j| (0...m).map { |i| cost[i][j] }.min }
  (0...full).map do |mask|
    extra = (0...n).sum { |j| (mask >> j) & 1 == 0 ? minimum[j] : 0 }
    dp[mask] + extra
  end.min
end
