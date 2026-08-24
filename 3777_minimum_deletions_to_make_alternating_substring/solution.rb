# LeetCode 3777 - Minimum Deletions to Make Alternating Substring
# https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class AltBit
  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
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

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def min_deletions(s, queries)
  n = s.length
  nums = Array.new(n, 0)
  bit = AltBit.new(n)
  (1...n).each do |i|
    if s[i] == s[i - 1]
      nums[i] = 1
      bit.update(i + 1, 1)
    end
  end
  ans = []
  queries.each do |q|
    if q[0] == 1
      j = q[1]
      delta = (nums[j] ^ 1) - nums[j]
      nums[j] ^= 1
      bit.update(j + 1, delta)
      if j + 1 < n
        delta = (nums[j + 1] ^ 1) - nums[j + 1]
        nums[j + 1] ^= 1
        bit.update(j + 2, delta)
      end
    else
      l = q[1]
      r = q[2]
      ans << bit.query(r + 1) - bit.query(l + 1)
    end
  end
  ans
end
