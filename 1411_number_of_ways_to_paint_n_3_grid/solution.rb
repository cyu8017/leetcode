# LeetCode 1411 - Number Of Ways To Paint N 3 Grid
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

def num_of_ways(n)
  mod = 1_000_000_007
  aba = abc = 6
  (1...n).each do
    aba, abc = (3 * aba + 2 * abc) % mod, (2 * aba + 2 * abc) % mod
  end
  (aba + abc) % mod
end
