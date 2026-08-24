# LeetCode 3990 - Create Grid With Exactly K Paths II
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

# @param {Integer} k
# @return {String[]}
def create_grid(k)
  return [] if k <= 0
  w = 0
  kk = k
  while kk != 0
    w += 1
    kk >>= 1
  end
  l = w
  m = 2 * l
  n = l + 3
  result = Array.new(m) { Array.new(n, "#") }
  l.times do |i|
    r = 2 * i
    result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = "."
    if (k & (1 << i)) != 0
      ((i + 2)...n).each { |c| result[r][c] = "." }
    end
  end
  m.times { |r| result[r][n - 1] = "." }
  result.map(&:join)
end
