# LeetCode 3538 - Merge Operations for Minimum Travel Time
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

# @param {Integer} l
# @param {Integer} n
# @param {Integer} k
# @param {Integer[]} position
# @param {Integer[]} time
# @return {Integer}
def min_travel_time(l, n, k, position, time)
  prefix = Array.new(n, 0)
  prefix[0] = time[0]
  (1...n).each { |i| prefix[i] = prefix[i - 1] + time[i] }
  memo = {}
  inf = 10**18
  dp = nil
  dp = lambda do |i, skips, last|
    return skips == 0 ? 0 : inf if i == n - 1
    key = [i, skips, last]
    return memo[key] if memo.key?(key)
    rate = prefix[i]
    rate -= prefix[last - 1] if last > 0
    res = inf
    last_end = n - 1
    last_end = i + skips + 1 if i + skips + 1 < last_end
    ((i + 1)..last_end).each do |j|
      cand = (position[j] - position[i]) * rate + dp.call(j, skips - (j - i - 1), i + 1)
      res = cand if cand < res
    end
    memo[key] = res
    res
  end
  dp.call(0, k, 0)
end
