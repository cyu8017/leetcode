# LeetCode 1931 - Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def color_the_grid(m, n)
  mod = 10**9 + 7
  valid_column = lambda do |mask|
    prev = -1
    x = mask
    m.times do
      c = x % 3
      return false if c == prev
      prev = c
      x /= 3
    end
    true
  end
  get_colors = lambda do |mask|
    cols = []
    x = mask
    m.times do
      cols << x % 3
      x /= 3
    end
    cols
  end
  states = (0...(3**m)).select { |s| valid_column.call(s) }
  compat = {}
  states.each { |s| compat[s] = [] }
  states.each do |a|
    ca = get_colors.call(a)
    states.each do |b|
      cb = get_colors.call(b)
      compat[a] << b if ca.each_with_index.all? { |x, i| x != cb[i] }
    end
  end
  memo = {}
  dp = lambda do |col, prev|
    key = [col, prev]
    return memo[key] if memo.key?(key)
    return 1 if col == n
    total = 0
    options = prev == -1 ? states : compat[prev]
    options.each { |cur| total = (total + dp.call(col + 1, cur)) % mod }
    memo[key] = total
  end
  dp.call(0, -1)
end
