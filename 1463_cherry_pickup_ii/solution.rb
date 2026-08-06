# LeetCode 1463 - Cherry Pickup Ii
# https://leetcode.com/problems/cherry-pickup-ii/

def cherry_pickup(grid)
  m = grid.length
  n = grid[0].length
  dp = { [0, n - 1] => grid[0][0] + (n > 1 ? grid[0][n - 1] : 0) }
  (1...m).each do |r|
    nxt = {}
    dp.each do |(a, b), score|
      [a - 1, a, a + 1].each do |na|
        [b - 1, b, b + 1].each do |nb|
          next unless na >= 0 && na < n && nb >= 0 && nb < n
          val = score + grid[r][na] + (na != nb ? grid[r][nb] : 0)
          nxt[[na, nb]] = [nxt.fetch([na, nb], -1), val].max
        end
      end
    end
    dp = nxt
  end
  dp.values.max
end
