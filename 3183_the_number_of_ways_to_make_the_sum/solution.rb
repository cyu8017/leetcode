# LeetCode 3183 - The Number of Ways to Make the Sum
# https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

# @param {Integer} n
# @return {Integer}
def number_of_ways(n)
  mod = 1_000_000_007
  coins = [1, 2, 6]
  f = Array.new(n + 1, 0)
  f[0] = 1
  coins.each do |x|
    (x..n).each { |j| f[j] = (f[j] + f[j - x]) % mod }
  end
  ans = f[n]
  ans = (ans + f[n - 4]) % mod if n >= 4
  ans = (ans + f[n - 8]) % mod if n >= 8
  ans
end
