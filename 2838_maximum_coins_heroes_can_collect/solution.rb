# LeetCode 2838 - Maximum Coins Heroes Can Collect
# https://leetcode.com/problems/maximum-coins-heroes-can-collect/

# @param {Integer[]} heroes
# @param {Integer[]} monsters
# @param {Integer[]} coins
# @return {Integer[]}
def maximum_coins(heroes, monsters, coins)
  n = monsters.length
  idx = (0...n).to_a
  idx.sort_by! { |i| monsters[i] }
  pref = Array.new(n + 1, 0)
  ms = Array.new(n, 0)
  (0...n).each do |i|
    ms[i] = monsters[idx[i]]
    pref[i + 1] = pref[i] + coins[idx[i]]
  end

  upper_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  heroes.map { |h| pref[upper_bound.call(ms, h)] }
end
