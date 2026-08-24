# LeetCode 0656 - Coin Path
# https://leetcode.com/problems/coin-path/

# @param {Integer[]} coins
# @param {Integer} max_jump
# @return {Integer[]}
def cheapest_jump(coins, max_jump)
  n = coins.length
  return [] if coins[-1] == -1

  inf = 10**18
  cost = Array.new(n, inf)
  nxt = Array.new(n, -1)
  cost[-1] = coins[-1]

  (n - 2).downto(0) do |i|
    next if coins[i] == -1

    (1..max_jump).each do |jump|
      j = i + jump
      break if j >= n
      next if cost[j] == inf

      candidate = coins[i] + cost[j]
      if candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))
        cost[i] = candidate
        nxt[i] = j
      end
    end
  end

  return [] if cost[0] == inf

  path = [1]
  i = 0
  while i != n - 1
    i = nxt[i]
    path << i + 1
  end
  path
end
