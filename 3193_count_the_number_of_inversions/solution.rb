# LeetCode 3193 - Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/

# @param {Integer} n
# @param {Integer[][]} requirements
# @return {Integer}
def number_of_permutations(n, requirements)
  req = Array.new(n, -1)
  requirements.each { |r| req[r[0]] = r[1] }
  return 0 if req[0] > 0
  req[0] = 0
  m = req.max
  mod = 1_000_000_007
  f = Array.new(n) { Array.new(m + 1, 0) }
  f[0][0] = 1
  (1...n).each do |i|
    l = 0
    r = m
    if req[i] >= 0
      l = r = req[i]
    end
    (l..r).each do |j|
      (0..[i, j].min).each do |k|
        f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
      end
    end
  end
  f[n - 1][req[n - 1]]
end
