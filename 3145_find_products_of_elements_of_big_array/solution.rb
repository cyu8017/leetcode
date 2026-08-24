# LeetCode 3145 - Find Products of Elements of Big Array
# https://leetcode.com/problems/find-products-of-elements-of-big-array/

# @param {Integer[][]} queries
# @return {Integer[]}
def find_products_of_elements(queries)
  m = 50
  cnt = Array.new(m + 1, 0)
  s = Array.new(m + 1, 0)
  p = 1
  (1..m).each do |i|
    cnt[i] = cnt[i - 1] * 2 + p
    s[i] = s[i - 1] * 2 + p * (i - 1)
    p *= 2
  end

  num_idx_and_sum = lambda do |x|
    idx = 0
    total_sum = 0
    while x > 0
      i = 0
      t = x
      while t > 1
        t >>= 1
        i += 1
      end
      idx += cnt[i]
      total_sum += s[i]
      x -= 1 << i
      total_sum += (x + 1) * i
      idx += x + 1
    end
    [idx, total_sum]
  end

  f = lambda do |i|
    l = 0
    r = 1 << m
    while l < r
      mid = (l + r + 1) >> 1
      p0 = num_idx_and_sum.call(mid)
      if p0[0] < i
        l = mid
      else
        r = mid - 1
      end
    end
    p0 = num_idx_and_sum.call(l)
    total_sum = p0[1]
    i -= p0[0]
    x = l + 1
    i.times do
      y = x & -x
      tz = 0
      yy = y
      while (yy & 1) == 0
        tz += 1
        yy >>= 1
      end
      total_sum += tz
      x -= y
    end
    total_sum
  end

  qpow = lambda do |a, n, mod|
    ans = 1 % mod
    a %= mod
    while n > 0
      ans = ans * a % mod if (n & 1) != 0
      a = a * a % mod
      n >>= 1
    end
    ans
  end

  queries.map do |q|
    left, right, mod = q[0], q[1], q[2]
    power = f.call(right + 1) - f.call(left)
    qpow.call(2, power, mod)
  end
end
