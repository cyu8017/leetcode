#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3585_find_weighted_median_node_in_tree", r'''
# LeetCode 3585 - Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def find_median(n, edges, queries)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    u, v = q[0], q[1]
    parent = Array.new(n, -2)
    pw = Array.new(n, 0)
    parent[u] = -1
    dq = [u]
    until dq.empty?
      x = dq.shift
      break if x == v
      g[x].each do |to, w|
        if parent[to] == -2
          parent[to] = x
          pw[to] = w
          dq << to
        end
      end
    end
    nodes = [v]
    weights = []
    cur = v
    while cur != u
      weights << pw[cur]
      cur = parent[cur]
      nodes << cur
    end
    nodes.reverse!
    weights.reverse!
    total = 0
    weights.each { |w| total += w }
    need = (total + 1) / 2
    sm = 0
    med = u
    weights.each_with_index do |w, i|
      sm += w
      med = nodes[i + 1]
      break if sm >= need
    end
    ans[qi] = med
  end
  ans
end
''')

add("3587_minimum_adjacent_swaps_to_alternate_parity", r'''
# LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  calc = lambda do |pos, n, k|
    res = 0
    (0...n).step(2) { |i| res += (pos[k][i / 2] - i).abs }
    res
  end
  pos = [[], []]
  nums.each_with_index { |x, i| pos[x & 1] << i }
  return -1 if (pos[0].length - pos[1].length).abs > 1
  return calc.call(pos, nums.length, 0) if pos[0].length > pos[1].length
  return calc.call(pos, nums.length, 1) if pos[0].length < pos[1].length
  [calc.call(pos, nums.length, 0), calc.call(pos, nums.length, 1)].min
end
''')

add("3588_find_maximum_area_of_a_triangle", r'''
# LeetCode 3588 - Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/

# @param {Integer[][]} coords
# @return {Integer}
def max_area(coords)
  calc = lambda do |cs|
    mn = 10**9
    mx = 0
    f = {}
    g = {}
    cs.each do |c|
      x, y = c[0], c[1]
      mn = [mn, x].min
      mx = [mx, x].max
      if f.key?(x)
        f[x] = [f[x], y].min
        g[x] = [g[x], y].max
      else
        f[x] = y
        g[x] = y
      end
    end
    ans = 0
    f.each do |x, y|
      d = g[x] - y
      ans = [ans, d * [mx - x, x - mn].max].max
    end
    ans
  end
  ans = calc.call(coords)
  coords.each { |c| c[0], c[1] = c[1], c[0] }
  ans = [ans, calc.call(coords)].max
  ans > 0 ? ans : -1
end
''')

add("3589_count_prime_gap_balanced_subarrays", r'''
# LeetCode 3589 - Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def prime_subarray(nums, k)
  mx = nums.max
  is_prime = Array.new(mx + 1, false)
  (2..mx).each { |i| is_prime[i] = true }
  i = 2
  while i * i <= mx
    if is_prime[i]
      (i * i).step(mx, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  n = nums.length
  ans = 0
  (0...n).each do |l|
    primes = []
    (l...n).each do |r|
      primes << nums[r] if is_prime[nums[r]]
      if primes.length >= 2
        mn = primes[0]
        mxp = primes[0]
        primes.each do |p|
          mn = [mn, p].min
          mxp = [mxp, p].max
        end
        ans += 1 if mxp - mn <= k
      end
    end
  end
  ans
end
''')

add("3590_kth_smallest_path_xor_sum", r'''
# LeetCode 3590 - Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/

# @param {Integer[]} par
# @param {Integer[]} vals
# @param {Integer[][]} queries
# @return {Integer[]}
def kth_smallest(par, vals, queries)
  n = par.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[par[i]] << i }
  xor_path = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |u|
    xor_path[u] ^= vals[u]
    g[u].each do |v|
      xor_path[v] = xor_path[u]
      dfs.call(v)
    end
  end
  dfs.call(0)
  in_t = Array.new(n, 0)
  out_t = Array.new(n, 0)
  order = []
  dfs2 = nil
  dfs2 = lambda do |u|
    in_t[u] = order.length
    order << xor_path[u]
    g[u].each { |v| dfs2.call(v) }
    out_t[u] = order.length
  end
  dfs2.call(0)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    u, k = q[0], q[1]
    sub = order[in_t[u]...out_t[u]].sort
    uniq = []
    sub.each { |x| uniq << x if uniq.empty? || uniq[-1] != x }
    ans[i] = k > uniq.length ? -1 : uniq[k - 1]
  end
  ans
end
''')

add("3591_check_if_any_element_has_prime_frequency", r'''
# LeetCode 3591 - Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

# @param {Integer[]} nums
# @return {Boolean}
def check_prime_frequency(nums)
  is_prime = lambda do |x|
    return false if x < 2
    i = 2
    while i * i <= x
      return false if x % i == 0
      i += 1
    end
    true
  end
  cnt = {}
  nums.each { |x| cnt[x] = (cnt[x] || 0) + 1 }
  cnt.each_value { |v| return true if is_prime.call(v) }
  false
end
''')

add("3592_inverse_coin_change", r'''
# LeetCode 3592 - Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/

# @param {Integer[]} num_ways
# @return {Integer[]}
def find_coins(num_ways)
  n = num_ways.length
  dp = Array.new(n + 1, 0)
  coins = []
  dp[0] = 1
  (1..n).each do |amt|
    ways = num_ways[amt - 1]
    next if dp[amt] == ways
    if dp[amt] + 1 == ways
      coins << amt
      (amt..n).each { |x| dp[x] += dp[x - amt] }
      return [] if dp[amt] != ways
      next
    end
    return []
  end
  coins
end
''')

add("3593_minimum_increments_to_equalize_leaf_paths", r'''
# LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} cost
# @return {Integer}
def min_increase(n, edges, cost)
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  ans = [0]
  dfs = nil
  dfs = lambda do |u, p|
    return cost[u] if graph[u].length == 1 && p != -1
    child_vals = []
    graph[u].each do |v|
      next if v == p
      child_vals << dfs.call(v, u)
    end
    return cost[u] if child_vals.empty?
    mx = child_vals.max
    child_vals.each { |c| ans[0] += 1 if c < mx }
    mx + cost[u]
  end
  dfs.call(0, -1)
  ans[0]
end
''')

add("3594_minimum_time_to_transport_all_individuals", r'''
# LeetCode 3594 - Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} m
# @param {Integer[]} time
# @param {Float[]} mul
# @return {Float}
def min_time(n, k, m, time, mul)
  t = time.sort
  total = 0.0
  stage = 0
  left = n
  while left > 0
    take = [k, left].min
    slow = t[left - 1]
    total += slow * mul[stage % m]
    left -= take
    stage += 1
    if left > 0
      total += t[0] * mul[stage % m]
      stage += 1
    end
  end
  total
end
''')

add("3595_once_twice", r'''
# LeetCode 3595 - Once Twice
# https://leetcode.com/problems/once-twice/

# @param {Integer[]} nums
# @return {Integer[]}
def once_twice(nums)
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  a = 0
  b = 0
  freq.each do |key, v|
    if v == 1
      a = key
    elsif v == 2
      b = key
    end
  end
  [a, b]
end
''')

add("3596_minimum_cost_path_with_alternating_directions_i", r'''
# LeetCode 3596 - Minimum Cost Path with Alternating Directions I
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def min_cost(m, n)
  return 1 if m == 1 && n == 1
  return 3 if m == 1 && n == 2
  return 3 if m == 2 && n == 1
  -1
end
''')

add("3597_partition_string", r'''
# LeetCode 3597 - Partition String
# https://leetcode.com/problems/partition-string/

# @param {String} s
# @return {String[]}
def partition_string(s)
  vis = {}
  ans = []
  t = ""
  s.each_char do |c|
    t += c
    unless vis[t]
      vis[t] = true
      ans << t
      t = ""
    end
  end
  ans
end
''')

add("3598_longest_common_prefix_between_adjacent_strings_after_removals", r'''
# LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

# @param {String[]} words
# @return {Integer[]}
def longest_common_prefix(words)
  n = words.length
  tm = {}
  keys = []
  calc = lambda do |s, t|
    m = [s.length, t.length].min
    (0...m).each { |k| return k if s[k] != t[k] }
    m
  end
  add_key = lambda do |x|
    unless tm.key?(x)
      tm[x] = 0
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) >> 1
        if keys[mid] < x
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, x)
    end
    tm[x] += 1
  end
  rem_key = lambda do |x|
    c = tm[x] - 1
    if c == 0
      tm.delete(x)
      ix = keys.index(x)
      keys.delete_at(ix) if ix
    else
      tm[x] = c
    end
  end
  add = lambda do |i, j|
    add_key.call(calc.call(words[i], words[j])) if i >= 0 && i < n && j >= 0 && j < n
  end
  remove = lambda do |i, j|
    rem_key.call(calc.call(words[i], words[j])) if i >= 0 && i < n && j >= 0 && j < n
  end
  (0...(n - 1)).each { |i| add.call(i, i + 1) }
  ans = Array.new(n, 0)
  (0...n).each do |i|
    remove.call(i, i + 1)
    remove.call(i - 1, i)
    add.call(i - 1, i + 1)
    ans[i] = keys[-1] if !keys.empty? && keys[-1] > 0
    remove.call(i - 1, i + 1)
    add.call(i - 1, i)
    add.call(i, i + 1)
  end
  ans
end
''')

add("3599_partition_array_to_minimize_xor", r'''
# LeetCode 3599 - Partition Array to Minimize XOR
# https://leetcode.com/problems/partition-array-to-minimize-xor/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_xor(nums, k)
  n = nums.length
  g = Array.new(n + 1, 0)
  (1..n).each { |i| g[i] = g[i - 1] ^ nums[i - 1] }
  inf = 2147483647 / 2
  f = Array.new(n + 1) { Array.new(k + 1, inf) }
  f[0][0] = 0
  (1..n).each do |i|
    (1..[i, k].min).each do |j|
      ((j - 1)...i).each do |h|
        f[i][j] = [f[i][j], [f[h][j - 1], g[i] ^ g[h]].max].min
      end
    end
  end
  f[n][k]
end
''')

add("3600_maximize_spanning_tree_stability_with_upgrades", r'''
# LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class UnionFind3600
  attr_reader :cnt

  def initialize(n)
    @p = (0...n).to_a
    @size = Array.new(n, 1)
    @cnt = n
  end

  def find(x)
    @p[x] = find(@p[x]) if @p[x] != x
    @p[x]
  end

  def unite(a, b)
    pa = find(a)
    pb = find(b)
    return false if pa == pb
    if @size[pa] > @size[pb]
      @p[pb] = pa
      @size[pa] += @size[pb]
    else
      @p[pa] = pb
      @size[pb] += @size[pa]
    end
    @cnt -= 1
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def max_stability(n, edges, k)
  check = lambda do |lim|
    uf = UnionFind3600.new(n)
    edges.each { |e| uf.unite(e[0], e[1]) if e[2] >= lim }
    rem = k
    edges.each do |e|
      if e[2] * 2 >= lim && rem > 0
        rem -= 1 if uf.unite(e[0], e[1])
      end
    end
    uf.cnt == 1
  end
  uf = UnionFind3600.new(n)
  mn = 1000000
  edges.each do |e|
    if e[3] == 1
      mn = [mn, e[2]].min
      return -1 unless uf.unite(e[0], e[1])
    end
  end
  edges.each { |e| uf.unite(e[0], e[1]) }
  return -1 if uf.cnt > 1
  l = 1
  r = mn
  while l < r
    mid = (l + r + 1) >> 1
    if check.call(mid)
      l = mid
    else
      r = mid - 1
    end
  end
  l
end
''')

add("3602_hexadecimal_and_hexatrigesimal_conversion", r'''
# LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

# @param {Integer} n
# @return {String}
def concat_hex36(n)
  f = lambda do |x, k|
    res = []
    while x > 0
      v = x % k
      res << (v <= 9 ? (48 + v).chr : (65 + v - 10).chr)
      x /= k
    end
    res.reverse.join
  end
  f.call(n * n, 16) + f.call(n * n * n, 36)
end
''')

add("3603_minimum_cost_path_with_alternating_directions_ii", r'''
# LeetCode 3603 - Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} wait_cost
# @return {Integer}
def min_cost(m, n, wait_cost)
  entry = lambda { |i, j| (i + 1) * (j + 1) }
  inf = 10**18
  dp = Array.new(m) { Array.new(n, inf) }
  dp[0][0] = entry.call(0, 0)
  (0...m).each do |i|
    (0...n).each do |j|
      next if i == 0 && j == 0
      if i > 0
        cand = dp[i - 1][j] + entry.call(i, j)
        cand += wait_cost[i - 1][j] unless i - 1 == 0 && j == 0
        dp[i][j] = [dp[i][j], cand].min
      end
      if j > 0
        cand = dp[i][j - 1] + entry.call(i, j)
        cand += wait_cost[i][j - 1] unless i == 0 && j - 1 == 0
        dp[i][j] = [dp[i][j], cand].min
      end
    end
  end
  dp[m - 1][n - 1]
end
''')

add("3604_minimum_time_to_reach_destination_in_directed_graph", r'''
# LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_time(n, edges)
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << [e[1], e[2], e[3]] }
  inf = 10**18
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  push = lambda do |t, u|
    lo = 0
    hi = pq.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pq[mid][0] < t
        lo = mid + 1
      else
        hi = mid
      end
    end
    pq.insert(lo, [t, u])
  end
  until pq.empty?
    t, u = pq.shift
    next if t != dist[u]
    return t if u == n - 1
    g[u].each do |to, start, last|
      nt = t
      next if nt > last
      nt = start if nt < start
      nt += 1
      if nt < dist[to]
        dist[to] = nt
        push.call(nt, to)
      end
    end
  end
  dist[n - 1] == inf ? -1 : dist[n - 1]
end
''')

add("3605_minimum_stability_factor_of_array", r'''
# LeetCode 3605 - Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/

# @param {Integer[]} nums
# @param {Integer} max_c
# @return {Integer}
def min_stable(nums, max_c)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  ok = lambda do |arr, maxc, x|
    n = arr.length
    return true if x >= n
    changes = 0
    i = 0
    while i + x < n
      g = arr[i]
      ((i + 1)..(i + x)).each { |j| g = gcd.call(g, arr[j]) }
      if g > 1
        changes += 1
        i += x + 1
      else
        i += 1
      end
    end
    changes <= maxc
  end
  n = nums.length
  lo = 0
  hi = n
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(nums, max_c, mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3606_coupon_code_validator", r'''
# LeetCode 3606 - Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/

# @param {String[]} code
# @param {String[]} business_line
# @param {Boolean[]} is_active
# @return {String[]}
def validate_coupons(code, business_line, is_active)
  check = lambda do |s|
    return false if s.nil? || s.empty?
    s.each_char { |c| return false unless c.match?(/[A-Za-z0-9_]/) }
    true
  end
  bs = { "electronics" => true, "grocery" => true, "pharmacy" => true, "restaurant" => true }
  idx = []
  (0...code.length).each do |i|
    idx << i if is_active[i] && bs[business_line[i]] && check.call(code[i])
  end
  idx.sort_by! { |i| [business_line[i], code[i]] }
  idx.map { |i| code[i] }
end
''')

add("3607_power_grid_maintenance", r'''
# LeetCode 3607 - Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance/

# @param {Integer} c
# @param {Integer[][]} connections
# @param {Integer[][]} queries
# @return {Integer[]}
def process_queries(c, connections, queries)
  parent = (0..c).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if ra < rb
      parent[rb] = ra
    else
      parent[ra] = rb
    end
  end
  connections.each { |e| unite.call(e[0], e[1]) }
  online = Array.new(c + 1, true)
  comp = {}
  (1..c).each do |i|
    r = find.call(i)
    (comp[r] ||= []) << i
  end
  comp.each_value(&:sort!)
  ptr = {}
  ans = []
  queries.each do |q|
    t, x = q[0], q[1]
    if t == 2
      online[x] = false
      next
    end
    if online[x]
      ans << x
      next
    end
    r = find.call(x)
    ids = comp[r]
    p = ptr[r] || 0
    p += 1 while p < ids.length && !online[ids[p]]
    ptr[r] = p
    ans << (p < ids.length ? ids[p] : -1)
  end
  ans
end
''')

add("3608_minimum_time_for_k_connected_components", r'''
# LeetCode 3608 - Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/

class UnionFind3608
  def initialize(n)
    @p = (0...n).to_a
    @size = Array.new(n, 1)
  end

  def find(x)
    @p[x] = find(@p[x]) if @p[x] != x
    @p[x]
  end

  def unite(a, b)
    pa = find(a)
    pb = find(b)
    return false if pa == pb
    if @size[pa] > @size[pb]
      @p[pb] = pa
      @size[pa] += @size[pb]
    else
      @p[pa] = pb
      @size[pb] += @size[pa]
    end
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_time(n, edges, k)
  edges = edges.sort_by { |e| e[2] }
  uf = UnionFind3608.new(n)
  cnt = n
  (edges.length - 1).downto(0) do |i|
    if uf.unite(edges[i][0], edges[i][1])
      cnt -= 1
      return edges[i][2] if cnt < k
    end
  end
  0
end
''')

add("3609_minimum_moves_to_reach_target_in_grid", r'''
# LeetCode 3609 - Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Integer}
def min_moves(sx, sy, tx, ty)
  ans = 0
  while tx > sx || ty > sy
    return -1 if tx < sx || ty < sy
    return -1 if tx == ty
    if tx > ty
      if ty > sy
        if tx >= 2 * ty
          return -1 if tx.odd?
          tx /= 2
        else
          tx -= ty
        end
        ans += 1
      else
        return -1 if ty != sy
        while tx > sx
          if tx >= 2 * ty
            return -1 if tx.odd?
            tx /= 2
          else
            tx -= ty
          end
          ans += 1
          return -1 if tx < sx
        end
      end
    else
      if tx > sx
        if ty >= 2 * tx
          return -1 if ty.odd?
          ty /= 2
        else
          ty -= tx
        end
        ans += 1
      else
        return -1 if tx != sx
        while ty > sy
          if ty >= 2 * tx
            return -1 if ty.odd?
            ty /= 2
          else
            ty -= tx
          end
          ans += 1
          return -1 if ty < sy
        end
      end
    end
  end
  tx == sx && ty == sy ? ans : -1
end
''')

add("3610_minimum_number_of_primes_to_sum_to_target", r'''
# LeetCode 3610 - Minimum Number of Primes to Sum to Target
# https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

$primes3610 = []

def ensure_primes3610
  return unless $primes3610.empty?
  x = 2
  while $primes3610.length < 1000
    is_prime = true
    $primes3610.each do |p|
      break if p * p > x
      if x % p == 0
        is_prime = false
        break
      end
    end
    $primes3610 << x if is_prime
    x += 1
  end
end

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def min_number_of_primes(n, m)
  ensure_primes3610
  inf = 2147483647 / 2
  f = Array.new(n + 1, inf)
  f[0] = 0
  (0...m).each do |pi|
    x = $primes3610[pi]
    (x..n).each { |i| f[i] = f[i - x] + 1 if f[i - x] + 1 < f[i] }
  end
  f[n] < inf ? f[n] : -1
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
