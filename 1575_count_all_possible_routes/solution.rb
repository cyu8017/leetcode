# LeetCode 1575 - Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/

# @param {Integer[]} locations
# @param {Integer} start
# @param {Integer} finish
# @param {Integer} fuel
# @return {Integer}
def count_routes(locations, start, finish, fuel)
  mod = 1_000_000_007
  memo = {}
  dp = lambda do |city, left|
    key = [city, left]
    return memo[key] if memo.key?(key)
    total = city == finish ? 1 : 0
    locations.each_with_index do |loc, nxt|
      next if nxt == city
      cost = (locations[city] - loc).abs
      total += dp.call(nxt, left - cost) if cost <= left
    end
    memo[key] = total % mod
  end
  dp.call(start, fuel)
end
