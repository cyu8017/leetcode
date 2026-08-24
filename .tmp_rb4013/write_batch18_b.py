#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3530_maximum_profit_from_valid_topological_order_in_dag", r'''
# LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} score
# @return {Integer}
def max_profit(n, edges, score)
  popcount = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  need = Array.new(n, 0)
  dp = Array.new(1 << n, -1)
  dp[0] = 0
  edges.each { |e| need[e[1]] |= 1 << e[0] }
  (0...(1 << n)).each do |mask|
    next if dp[mask] < 0
    pos = popcount.call(mask) + 1
    (0...n).each do |i|
      next if ((mask >> i) & 1) != 0
      next unless (mask & need[i]) == need[i]
      nm = mask | (1 << i)
      v = dp[mask] + score[i] * pos
      dp[nm] = v if v > dp[nm]
    end
  end
  dp[(1 << n) - 1]
end
''')

add("3531_count_covered_buildings", r'''
# LeetCode 3531 - Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/

# @param {Integer} n
# @param {Integer[][]} buildings
# @return {Integer}
def count_covered_buildings(n, buildings)
  g1 = {}
  g2 = {}
  buildings.each do |b|
    (g1[b[0]] ||= []) << b[1]
    (g2[b[1]] ||= []) << b[0]
  end
  g1.each_value(&:sort!)
  g2.each_value(&:sort!)
  ans = 0
  buildings.each do |b|
    x, y = b[0], b[1]
    l1 = g1[x]
    l2 = g2[y]
    ans += 1 if l2[0] < x && x < l2[-1] && l1[0] < y && y < l1[-1]
  end
  ans
end
''')

add("3532_path_existence_queries_in_a_graph_i", r'''
# LeetCode 3532 - Path Existence Queries in a Graph I
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

# @param {Integer} n
# @param {Integer[]} nums
# @param {Integer} max_diff
# @param {Integer[][]} queries
# @return {Boolean[]}
def path_existence_queries(n, nums, max_diff, queries)
  g = Array.new(n, 0)
  cnt = 0
  (1...n).each do |i|
    cnt += 1 if nums[i] - nums[i - 1] > max_diff
    g[i] = cnt
  end
  queries.map { |q| g[q[0]] == g[q[1]] }
end
''')

add("3533_concatenated_divisibility", r'''
# LeetCode 3533 - Concatenated Divisibility
# https://leetcode.com/problems/concatenated-divisibility/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def concatenated_divisibility(nums, k)
  nums = nums.sort
  n = nums.length
  pows = Array.new(n, 0)
  (0...n).each do |i|
    p = 1
    num = nums[i]
    if num == 0
      p = 10 % k
    else
      x = num
      while x > 0
        p = p * 10 % k
        x /= 10
      end
    end
    pows[i] = p
  end
  memo = {}
  dp = nil
  dp = lambda do |mask, mod|
    return mod == 0 if mask == (1 << n) - 1
    key = (mask << 32) | mod
    return memo[key] if memo.key?(key)
    (0...n).each do |i|
      next unless ((mask >> i) & 1) == 0
      nm = (mod * pows[i] + nums[i]) % k
      if dp.call(mask | (1 << i), nm)
        memo[key] = true
        return true
      end
    end
    memo[key] = false
    false
  end
  reconstruct = nil
  reconstruct = lambda do |mask, mod|
    (0...n).each do |i|
      next unless ((mask >> i) & 1) == 0
      nm = (mod * pows[i] + nums[i]) % k
      if dp.call(mask | (1 << i), nm)
        rest = reconstruct.call(mask | (1 << i), nm)
        rest.unshift(nums[i])
        return rest
      end
    end
    []
  end
  return [] unless dp.call(0, 0)
  reconstruct.call(0, 0)
end
''')

add("3534_path_existence_queries_in_a_graph_ii", r'''
# LeetCode 3534 - Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

# @param {Integer} n
# @param {Integer[]} nums
# @param {Integer} max_diff
# @param {Integer[][]} queries
# @return {Integer[]}
def path_existence_queries(n, nums, max_diff, queries)
  pairs = (0...n).map { |i| [nums[i], i] }
  pairs.sort_by! { |x| x[0] }
  m = 20
  f = Array.new(n) { Array.new(m, 0) }
  r = n - 1
  (n - 1).downto(0) do |l|
    r -= 1 while pairs[r][0] - pairs[l][0] > max_diff
    i = pairs[l][1]
    j = pairs[r][1]
    f[i][0] = j
    (1...m).each { |k| f[i][k] = f[f[i][k - 1]][k - 1] }
  end
  ans = []
  queries.each do |q|
    i = q[0]
    j = q[1]
    i, j = j, i if nums[i] > nums[j]
    if i == j
      ans << 0
      next
    end
    if nums[i] == nums[j]
      ans << 1
      next
    end
    d = 0
    (m - 1).downto(0) do |k|
      if nums[f[i][k]] < nums[j]
        d |= 1 << k
        i = f[i][k]
      end
    end
    ans << (nums[f[i][0]] < nums[j] ? -1 : d + 1)
  end
  ans
end
''')

add("3535_unit_conversion_ii", r'''
# LeetCode 3535 - Unit Conversion II
# https://leetcode.com/problems/unit-conversion-ii/

# @param {Integer[][]} conversions
# @param {Integer[][]} queries
# @return {Integer[]}
def query_conversions(conversions, queries)
  mod = 1000000007
  qpow = lambda do |x, nn|
    res = 1
    bx = x
    bn = nn
    while bn > 0
      res = res * bx % mod if (bn & 1) != 0
      bx = bx * bx % mod
      bn >>= 1
    end
    res
  end
  n = conversions.length + 1
  g = Array.new(n) { [] }
  conversions.each { |e| g[e[0]] << [e[1], e[2]] }
  res = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |s, mul|
    res[s] = mul
    g[s].each { |to, w| dfs.call(to, mul * w % mod) }
  end
  dfs.call(0, 1)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    ans[i] = res[q[1]] * qpow.call(res[q[0]], mod - 2) % mod
  end
  ans
end
''')

add("3536_maximum_product_of_two_digits", r'''
# LeetCode 3536 - Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/

# @param {Integer} n
# @return {Integer}
def max_product(n)
  a = 0
  b = 0
  while n > 0
    x = n % 10
    n /= 10
    if a < x
      b = a
      a = x
    elsif b < x
      b = x
    end
  end
  a * b
end
''')

add("3537_fill_a_special_grid", r'''
# LeetCode 3537 - Fill a Special Grid
# https://leetcode.com/problems/fill-a-special-grid/

# @param {Integer} n
# @return {Integer[][]}
def special_grid(n)
  m = 1 << n
  ans = Array.new(m) { Array.new(m, 0) }
  val = [0]
  dfs = nil
  dfs = lambda do |x, y, k|
    if k == 1
      ans[x][y] = val[0]
      val[0] += 1
      return
    end
    h = k >> 1
    dfs.call(x, y, h)
    dfs.call(x + h, y, h)
    dfs.call(x + h, y - h, h)
    dfs.call(x, y - h, h)
  end
  dfs.call(0, m - 1, m)
  ans
end
''')

add("3538_merge_operations_for_minimum_travel_time", r'''
# LeetCode 3538 - Merge Operations for Minimum Travel Time
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

# @param {Integer} l
# @param {Integer} n
# @param {Integer} k
# @param {Integer[]} position
# @param {Integer[]} time
# @return {Integer}
def min_travel_time(l, n, k, position, time)
  prefix = Array.new(n, 0)
  prefix[0] = time[0]
  (1...n).each { |i| prefix[i] = prefix[i - 1] + time[i] }
  memo = {}
  inf = 10**18
  dp = nil
  dp = lambda do |i, skips, last|
    return skips == 0 ? 0 : inf if i == n - 1
    key = [i, skips, last]
    return memo[key] if memo.key?(key)
    rate = prefix[i]
    rate -= prefix[last - 1] if last > 0
    res = inf
    last_end = n - 1
    last_end = i + skips + 1 if i + skips + 1 < last_end
    ((i + 1)..last_end).each do |j|
      cand = (position[j] - position[i]) * rate + dp.call(j, skips - (j - i - 1), i + 1)
      res = cand if cand < res
    end
    memo[key] = res
    res
  end
  dp.call(0, k, 0)
end
''')

add("3539_find_sum_of_array_product_of_magical_sequences", r'''
# LeetCode 3539 - Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

# @param {Integer} m
# @param {Integer} k
# @param {Integer[]} nums
# @return {Integer}
def magical_sum(m, k, nums)
  nn = 31
  mod = 1000000007
  f = Array.new(nn, 0)
  g = Array.new(nn, 0)
  qpow = lambda do |a, kk|
    res = 1
    ba = a
    bk = kk
    while bk > 0
      res = res * ba % mod if (bk & 1) != 0
      ba = ba * ba % mod
      bk >>= 1
    end
    res
  end
  f[0] = g[0] = 1
  (1...nn).each do |i|
    f[i] = f[i - 1] * i % mod
    g[i] = qpow.call(f[i], mod - 2)
  end
  comb = lambda do |mm, nnn|
    return 0 if nnn < 0 || nnn > mm
    f[mm] * g[nnn] % mod * g[mm - nnn] % mod
  end
  n = nums.length
  dp = Array.new(n + 1) { Array.new(m + 1) { Array.new(k + 1) { Array.new(nn, -1) } } }
  dfs = nil
  dfs = lambda do |i, j, kk, st|
    return 0 if kk < 0 || (i == n && j > 0)
    if i == n
      while st > 0
        kk -= st & 1
        st >>= 1
      end
      return kk == 0 ? 1 : 0
    end
    return dp[i][j][kk][st] if dp[i][j][kk][st] != -1
    res = 0
    (0..j).each do |t|
      nt = t + st
      nk = kk - (nt & 1)
      p = qpow.call(nums[i], t)
      tmp = comb.call(j, t) * p % mod * dfs.call(i + 1, j - t, nk, nt >> 1) % mod
      res = (res + tmp) % mod
    end
    dp[i][j][kk][st] = res
    res
  end
  dfs.call(0, m, k, 0)
end
''')

add("3540_minimum_time_to_visit_all_houses", r'''
# LeetCode 3540 - Minimum Time to Visit All Houses
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

# @param {Integer[]} forward
# @param {Integer[]} backward
# @param {Integer[]} queries
# @return {Integer}
def min_total_time(forward, backward, queries)
  n = forward.length
  sum_b = 0
  backward.each { |x| sum_b += x }
  pf = Array.new(n + 1, 0)
  pb = Array.new(n + 1, 0)
  (0...n).each do |i|
    pf[i + 1] = pf[i] + forward[i]
    pb[i + 1] = pb[i] + backward[i]
  end
  ans = 0
  pos = 0
  queries.each do |q|
    r = 0
    r = pf[n] if q < pos
    r += pf[q] - pf[pos]
    lft = 0
    lft = sum_b if q > pos
    lft += pb[pos] - pb[q]
    ans += [lft, r].min
    pos = q
  end
  ans
end
''')

add("3541_find_most_frequent_vowel_and_consonant", r'''
# LeetCode 3541 - Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

# @param {String} s
# @return {Integer}
def max_freq_sum(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  a = 0
  b = 0
  (0...26).each do |i|
    c = (97 + i).chr
    if "aeiou".include?(c)
      a = [a, cnt[i]].max
    else
      b = [b, cnt[i]].max
    end
  end
  a + b
end
''')

add("3542_minimum_operations_to_convert_all_elements_to_zero", r'''
# LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  stk = []
  ans = 0
  nums.each do |x|
    while !stk.empty? && stk[-1] > x
      ans += 1
      stk.pop
    end
    stk << x if x != 0 && (stk.empty? || stk[-1] != x)
  end
  ans + stk.length
end
''')

add("3543_maximum_weighted_k_edge_path", r'''
# LeetCode 3543 - Maximum Weighted K-Edge Path
# https://leetcode.com/problems/maximum-weighted-k-edge-path/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @param {Integer} t
# @return {Integer}
def max_weight(n, edges, k, t)
  graph = Array.new(n) { [] }
  edges.each { |e| graph[e[0]] << [e[1], e[2]] }
  dp = Array.new(n) { Array.new(k + 1) { {} } }
  (0...n).each { |u| dp[u][0][0] = true }
  (0...k).each do |i|
    (0...n).each do |u|
      dp[u][i].each_key do |sm|
        graph[u].each do |to, w|
          ns = sm + w
          dp[to][i + 1][ns] = true if ns < t
        end
      end
    end
  end
  ans = -1
  (0...n).each do |u|
    dp[u][k].each_key { |sm| ans = sm if sm > ans }
  end
  ans
end
''')

add("3544_subtree_inversion_sum", r'''
# LeetCode 3544 - Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subtree_inversion_sum(edges, nums, k)
  n = edges.length + 1
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  parent = Array.new(n, -1)
  memo = {}
  dp = nil
  dp = lambda do |u, steps, inv|
    key = [u, steps, inv]
    return memo[key] if memo.key?(key)
    num = nums[u]
    num = -num if inv
    neg_num = -num
    graph[u].each do |v|
      next if v == parent[u]
      parent[v] = u
      ns = steps + 1
      ns = k if ns > k
      num += dp.call(v, ns, inv)
      neg_num += dp.call(v, 1, !inv) if steps == k
    end
    res = num
    res = neg_num if steps == k && neg_num > res
    memo[key] = res
    res
  end
  dp.call(0, k, false)
end
''')

add("3545_minimum_deletions_for_at_most_k_distinct_characters", r'''
# LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def min_deletion(s, k)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  cnt.sort!
  ans = 0
  (0...(26 - k)).each { |i| ans += cnt[i] }
  ans
end
''')

add("3546_equal_sum_grid_partition_i", r'''
# LeetCode 3546 - Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/

# @param {Integer[][]} grid
# @return {Boolean}
def can_partition_grid(grid)
  s = 0
  grid.each { |row| row.each { |x| s += x } }
  return false if s.odd?
  m = grid.length
  n = grid[0].length
  pre = 0
  (0...m).each do |i|
    grid[i].each { |x| pre += x }
    return true if pre * 2 == s && i + 1 < m
  end
  pre = 0
  (0...n).each do |j|
    (0...m).each { |i| pre += grid[i][j] }
    return true if pre * 2 == s && j + 1 < n
  end
  false
end
''')

add("3547_maximum_sum_of_edge_values_in_a_graph", r'''
# LeetCode 3547 - Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def max_score(n, edges)
  calc = lambda do |left, right, is_cycle|
    w0 = right
    w1 = right
    score = 0
    (right - 1).downto(left) do |value|
      score += w0 * value
      w0 = w1
      w1 = value
    end
    score += w0 * w1 if is_cycle
    score
  end
  get_comp = lambda do |start, graph, seen|
    comp = [start]
    seen[start] = true
    i = 0
    while i < comp.length
      graph[comp[i]].each do |v|
        unless seen[v]
          seen[v] = true
          comp << v
        end
      end
      i += 1
    end
    comp
  end
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  seen = Array.new(n, false)
  cycle_sizes = []
  path_sizes = []
  (0...n).each do |i|
    next if seen[i]
    comp = get_comp.call(i, graph, seen)
    all_deg2 = comp.all? { |u| graph[u].length == 2 }
    if all_deg2
      cycle_sizes << comp.length
    elsif comp.length > 1
      path_sizes << comp.length
    end
  end
  ans = 0
  cur_n = n
  cycle_sizes.each do |cs|
    ans += calc.call(cur_n - cs + 1, cur_n, true)
    cur_n -= cs
  end
  path_sizes.sort!.reverse!
  path_sizes.each do |ps|
    ans += calc.call(cur_n - ps + 1, cur_n, false)
    cur_n -= ps
  end
  ans
end
''')

add("3548_equal_sum_grid_partition_ii", r'''
# LeetCode 3548 - Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/

# @param {Integer[][]} grid
# @return {Boolean}
def can_partition_grid(grid)
  rotate = lambda do |g|
    m = g.length
    n = g[0].length
    t = Array.new(n) { Array.new(m, 0) }
    (0...m).each { |i| (0...n).each { |j| t[j][i] = g[i][j] } }
    t
  end
  check = lambda do |g|
    m = g.length
    n = g[0].length
    s1 = 0
    s2 = 0
    cnt1 = {}
    cnt2 = {}
    g.each do |row|
      row.each do |x|
        s2 += x
        cnt2[x] = (cnt2[x] || 0) + 1
      end
    end
    (0...(m - 1)).each do |i|
      g[i].each do |x|
        s1 += x
        s2 -= x
        cnt1[x] = (cnt1[x] || 0) + 1
        cnt2[x] = (cnt2[x] || 0) - 1
      end
      return true if s1 == s2
      if s1 < s2
        diff = s2 - s1
        if (cnt2[diff] || 0) > 0
          if (m - i - 1 > 1 && n > 1) ||
             (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
             (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff))
            return true
          end
        end
      else
        diff = s1 - s2
        if (cnt1[diff] || 0) > 0
          if (i + 1 > 1 && n > 1) ||
             (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
             (n == 1 && (g[0][0] == diff || g[i][0] == diff))
            return true
          end
        end
      end
    end
    false
  end
  check.call(grid) || check.call(rotate.call(grid))
end
''')

add("3549_multiply_two_polynomials", r'''
# LeetCode 3549 - Multiply Two Polynomials
# https://leetcode.com/problems/multiply-two-polynomials/

class Complex3549
  attr_accessor :re, :im

  def initialize(re, im)
    @re = re
    @im = im
  end

  def mul(o)
    Complex3549.new(@re * o.re - @im * o.im, @re * o.im + @im * o.re)
  end

  def add(o)
    Complex3549.new(@re + o.re, @im + o.im)
  end

  def sub(o)
    Complex3549.new(@re - o.re, @im - o.im)
  end

  def div(x)
    Complex3549.new(@re / x.to_f, @im / x.to_f)
  end
end

# @param {Integer[]} poly1
# @param {Integer[]} poly2
# @return {Integer[]}
def multiply(poly1, poly2)
  return [] if poly1.empty? || poly2.empty?
  fft = lambda do |a, invert|
    n = a.length
    j = 0
    (1...n).each do |i|
      bit = n >> 1
      while (j & bit) != 0
        j ^= bit
        bit >>= 1
      end
      j ^= bit
      a[i], a[j] = a[j], a[i] if i < j
    end
    length = 2
    while length <= n
      angle = 2 * Math::PI / length * (invert ? -1 : 1)
      wlen = Complex3549.new(Math.cos(angle), Math.sin(angle))
      (0...n).step(length) do |i|
        w = Complex3549.new(1, 0)
        half = length >> 1
        (0...half).each do |jj|
          u = a[i + jj]
          v = a[i + jj + half].mul(w)
          a[i + jj] = u.add(v)
          a[i + jj + half] = u.sub(v)
          w = w.mul(wlen)
        end
      end
      length <<= 1
    end
    (0...n).each { |i| a[i] = a[i].div(n) } if invert
  end
  m = poly1.length + poly2.length - 1
  n = 1
  n <<= 1 while n < m
  fa = Array.new(n) { Complex3549.new(0, 0) }
  fb = Array.new(n) { Complex3549.new(0, 0) }
  (0...n).each do |i|
    fa[i] = Complex3549.new(i < poly1.length ? poly1[i] : 0, 0)
    fb[i] = Complex3549.new(i < poly2.length ? poly2[i] : 0, 0)
  end
  fft.call(fa, false)
  fft.call(fb, false)
  (0...n).each { |i| fa[i] = fa[i].mul(fb[i]) }
  fft.call(fa, true)
  (0...m).map { |i| fa[i].re.round }
end
''')

add("3550_smallest_index_with_digit_sum_equal_to_index", r'''
# LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

# @param {Integer[]} nums
# @return {Integer}
def smallest_index(nums)
  nums.each_with_index do |num, i|
    x = num
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    return i if s == i
  end
  -1
end
''')

add("3551_minimum_swaps_to_sort_by_digit_sum", r'''
# LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  f = lambda do |x|
    s = 0
    while x != 0
      s += x % 10
      x /= 10
    end
    s
  end
  n = nums.length
  arr = (0...n).map { |i| [f.call(nums[i]), nums[i]] }
  arr.sort_by! { |x| [x[0], x[1]] }
  d = {}
  (0...n).each { |i| d[arr[i][1]] = i }
  vis = Array.new(n, false)
  ans = n
  (0...n).each do |i|
    next if vis[i]
    ans -= 1
    j = i
    until vis[j]
      vis[j] = true
      j = d[nums[j]]
    end
  end
  ans
end
''')

add("3552_grid_teleportation_traversal", r'''
# LeetCode 3552 - Grid Teleportation Traversal
# https://leetcode.com/problems/grid-teleportation-traversal/

# @param {String[]} matrix
# @return {Integer}
def min_moves(matrix)
  m = matrix.length
  n = matrix[0].length
  g = {}
  (0...m).each do |i|
    (0...n).each do |j|
      c = matrix[i][j]
      if c.match?(/[A-Za-z]/)
        (g[c] ||= []) << [i, j]
      end
    end
  end
  dirs = [-1, 0, 1, 0, -1]
  inf = 1 << 30
  dist = Array.new(m) { Array.new(n, inf) }
  dist[0][0] = 0
  q = [[0, 0]]
  until q.empty?
    i, j = q.shift
    d = dist[i][j]
    return d if i == m - 1 && j == n - 1
    c = matrix[i][j]
    if g.key?(c)
      g[c].each do |x, y|
        if d < dist[x][y]
          dist[x][y] = d
          q.unshift([x, y])
        end
      end
      g.delete(c)
    end
    (0...4).each do |idx|
      x = i + dirs[idx]
      y = j + dirs[idx + 1]
      if x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] != "#" && d + 1 < dist[x][y]
        dist[x][y] = d + 1
        q << [x, y]
      end
    end
  end
  -1
end
''')

add("3553_minimum_weighted_subgraph_with_the_required_paths_ii", r'''
# LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def minimum_weight(edges, queries)
  log = 17
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  parent = Array.new(log) { Array.new(n, -1) }
  depth = Array.new(n, 0)
  dist = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |u, p|
    parent[0][u] = p
    g[u].each do |to, w|
      next if to == p
      depth[to] = depth[u] + 1
      dist[to] = dist[u] + w
      dfs.call(to, u)
    end
  end
  lca = lambda do |u, v|
    u, v = v, u if depth[u] < depth[v]
    (log - 1).downto(0) do |k|
      u = parent[k][u] if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]
    end
    return u if u == v
    (log - 1).downto(0) do |k|
      if parent[k][u] != -1 && parent[k][u] != parent[k][v]
        u = parent[k][u]
        v = parent[k][v]
      end
    end
    parent[0][u]
  end
  path = lambda do |u, v|
    a = lca.call(u, v)
    dist[u] + dist[v] - 2 * dist[a]
  end
  dfs.call(0, -1)
  (1...log).each do |k|
    (0...n).each do |v|
      parent[k][v] = parent[k - 1][parent[k - 1][v]] if parent[k - 1][v] != -1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    a, b, c = q[0], q[1], q[2]
    ans[i] = (path.call(a, b) + path.call(b, c) + path.call(a, c)) / 2
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
