# LeetCode 1659 - Maximize Grid Happiness
# https://leetcode.com/problems/maximize-grid-happiness/

def _pair_happiness(a, b)
  return 0 if a.zero? || b.zero?

  (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20)
end

# @param {Integer} m
# @param {Integer} n
# @param {Integer} introverts_count
# @param {Integer} extroverts_count
# @return {Integer}
def get_max_grid_happiness(m, n, introverts_count, extroverts_count)
  states = 3**n
  cells = []
  intro = []
  extro = []
  row = []
  states.times do |s|
    x = s
    a = []
    n.times do
      a << (x % 3)
      x /= 3
    end
    cells << a
    ic = a.count(1)
    ec = a.count(2)
    intro << ic
    extro << ec
    val = a.sum { |z| z == 1 ? 120 : z == 2 ? 40 : 0 }
    (1...n).each { |j| val += _pair_happiness(a[j - 1], a[j]) }
    row << val
  end
  compat = Array.new(states) do |a|
    Array.new(states) do |b|
      (0...n).sum { |j| _pair_happiness(cells[a][j], cells[b][j]) }
    end
  end
  memo = {}
  dp = lambda do |r, prev, i, e|
    return 0 if r == m

    key = [r, prev, i, e]
    return memo[key] if memo.key?(key)

    best = 0
    states.times do |s|
      next if intro[s] > i || extro[s] > e

      best = [best, row[s] + compat[prev][s] + dp.call(r + 1, s, i - intro[s], e - extro[s])].max
    end
    memo[key] = best
  end
  dp.call(0, 0, introverts_count, extroverts_count)
end
