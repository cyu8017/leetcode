# LeetCode 3337 - Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

# @param {Integer[][]} a
# @param {Integer[][]} b
# @param {Integer} mod
# @return {Integer[][]}
def mat_mul(a, b, mod)
  n = a.length
  c = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    n.times do |k|
      next if a[i][k] == 0

      n.times { |j| c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod }
    end
  end
  c
end

# @param {Integer[][]} a
# @param {Integer} e
# @param {Integer} mod
# @return {Integer[][]}
def mat_pow(a, e, mod)
  n = a.length
  r = Array.new(n) { Array.new(n, 0) }
  n.times { |i| r[i][i] = 1 }
  while e > 0
    r = mat_mul(r, a, mod) if (e & 1) != 0
    a = mat_mul(a, a, mod)
    e >>= 1
  end
  r
end

# @param {String} s
# @param {Integer} t
# @param {Integer[]} nums
# @return {Integer}
def length_after_transformations(s, t, nums)
  mod = 1_000_000_007
  mat = Array.new(26) { Array.new(26, 0) }
  26.times do |i|
    (1..nums[i]).each { |j| mat[i][(i + j) % 26] = 1 }
  end
  mat = mat_pow(mat, t, mod)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  ans = 0
  26.times do |i|
    26.times { |j| ans = (ans + cnt[i] * mat[i][j] % mod) % mod }
  end
  ans
end
