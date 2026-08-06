# LeetCode 1444 - Number Of Ways Of Cutting A Pizza
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

def ways(pizza, k)
  mod = 1_000_000_007
  rows = pizza.length
  cols = pizza[0].length
  apples = Array.new(rows + 1) { Array.new(cols + 1, 0) }
  (rows - 1).downto(0) do |r|
    (cols - 1).downto(0) do |c|
      apples[r][c] = (pizza[r][c] == 'A' ? 1 : 0) + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
    end
  end
  dp = Array.new(rows) { |r| Array.new(cols) { |c| apples[r][c] > 0 ? 1 : 0 } }
  (1...k).each do
    nxt = Array.new(rows) { Array.new(cols, 0) }
    rows.times do |r|
      cols.times do |c|
        ((r + 1)...rows).each do |nr|
          nxt[r][c] += dp[nr][c] if apples[r][c] > apples[nr][c]
        end
        ((c + 1)...cols).each do |nc|
          nxt[r][c] += dp[r][nc] if apples[r][c] > apples[r][nc]
        end
        nxt[r][c] %= mod
      end
    end
    dp = nxt
  end
  dp[0][0]
end
