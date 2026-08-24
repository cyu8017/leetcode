# LeetCode 3916 - Number of ZigZag Arrays III
# https://leetcode.com/problems/number-of-zigzag-arrays-iii/

def powm3916(a, e, mod)
  res = 1
  while e > 0
    res = res * a % mod if e.odd?
    a = a * a % mod
    e >>= 1
  end
  res
end

# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  points = n + 1
  values = Array.new(points + 1, 0)
  (1..points).each do |m|
    up = Array.new(m, 0)
    down = Array.new(m, 0)
    m.times do |value|
      up[value] = value
      down[value] = m - 1 - value
    end
    (3..n).each do |_length|
      next_up = Array.new(m, 0)
      next_down = Array.new(m, 0)
      prefix = 0
      m.times do |value|
        next_up[value] = prefix
        prefix = (prefix + down[value]) % mod
      end
      suffix = 0
      (m - 1).downto(0) do |value|
        next_down[value] = suffix
        suffix = (suffix + up[value]) % mod
      end
      up = next_up
      down = next_down
    end
    m.times { |value| values[m] = (values[m] + up[value] + down[value]) % mod }
  end
  x = (r - l + 1) % mod
  return values[r - l + 1] if r - l + 1 <= points
  prefix_a = Array.new(points + 2, 0)
  suffix_a = Array.new(points + 2, 0)
  prefix_a[0] = 1
  (1..points).each { |i| prefix_a[i] = prefix_a[i - 1] * ((x - i + mod) % mod) % mod }
  suffix_a[points + 1] = 1
  points.downto(1) { |i| suffix_a[i] = suffix_a[i + 1] * ((x - i + mod) % mod) % mod }
  factorial = Array.new(points + 1, 0)
  factorial[0] = 1
  (1..points).each { |i| factorial[i] = factorial[i - 1] * i % mod }
  answer = 0
  (1..points).each do |i|
    numerator = prefix_a[i - 1] * suffix_a[i + 1] % mod
    denominator = factorial[i - 1] * factorial[points - i] % mod
    term = values[i] * numerator % mod * powm3916(denominator, mod - 2, mod) % mod
    if (points - i).odd?
      answer -= term
    else
      answer += term
    end
    answer %= mod
  end
  answer += mod if answer < 0
  answer
end
