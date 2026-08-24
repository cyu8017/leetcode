# LeetCode 3109 - Find the Index of Permutation
# https://leetcode.com/problems/find-the-index-of-permutation/

class BIT
  def initialize(n)
    @n = n
    @c = Array.new(n + 1, 0)
  end

  def update(x, delta)
    while x <= @n
      @c[x] += delta
      x += x & -x
    end
  end

  def query(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} perm
# @return {Integer}
def get_permutation_index(perm)
  mod = 1_000_000_007
  n = perm.length
  tree = BIT.new(n + 1)
  f = Array.new(n, 0)
  f[0] = 1
  (1...n).each { |i| f[i] = f[i - 1] * i % mod }
  ans = 0
  n.times do |i|
    x = perm[i]
    cnt = x - 1 - tree.query(x)
    ans = (ans + cnt * f[n - 1 - i]) % mod
    tree.update(x, 1)
  end
  ans
end
