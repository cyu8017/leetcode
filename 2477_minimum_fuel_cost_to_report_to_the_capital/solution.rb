# LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

# @param {Integer[][]} roads
# @param {Integer} seats
# @return {Integer}
def minimum_fuel_cost(roads, seats)
  n = roads.length + 1
  g = Array.new(n) { [] }
  roads.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = [0]

  dfs = lambda do |u, p|
    people = 1
    g[u].each { |v| people += dfs.call(v, u) if v != p }
    ans[0] += (people + seats - 1) / seats if u != 0
    people
  end

  dfs.call(0, -1)
  ans[0]
end
