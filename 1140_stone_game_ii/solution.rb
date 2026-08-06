# LeetCode 1140 - Stone Game II
# https://leetcode.com/problems/stone-game-ii/

# @param {Integer[]} piles
# @return {Integer}
def stone_game_ii(piles)
  n = piles.length
  suffix = Array.new(n + 1, 0)
  (n - 1).downto(0) { |i| suffix[i] = suffix[i + 1] + piles[i] }
  memo = {}
  dfs = lambda do |i, m|
    return 0 if i >= n
    return suffix[i] if m + i >= n
    key = [i, m]
    return memo[key] if memo.key?(key)
    best = Float::INFINITY
    (1..[m * 2, n - i].min).each do |x|
      best = [best, dfs.call(i + x, [x, m].max)].min
    end
    memo[key] = suffix[i] - best
  end
  dfs.call(0, 1)
end
