#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3365_rearrange_k_substrings_to_form_target_string", r'''
# LeetCode 3365 - Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Boolean}
def is_possible_to_rearrange(s, t, k)
  n = s.length
  sz = n / k
  cnt = {}
  (0...n).step(sz) do |i|
    a = s[i, sz]
    b = t[i, sz]
    cnt[a] = (cnt[a] || 0) + 1
    cnt[b] = (cnt[b] || 0) - 1
  end
  cnt.values.all?(&:zero?)
end
''')

add("3366_minimum_array_sum", r'''
# LeetCode 3366 - Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/

# @param {Float[][]} ndp
# @param {Float} base
# @param {Integer} na
# @param {Integer} nb
# @param {Integer} v
# @return {void}
def try_cand(ndp, base, na, nb, v)
  ndp[na][nb] = base + v if base + v < ndp[na][nb]
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} op1
# @param {Integer} op2
# @return {Integer}
def min_array_sum(nums, k, op1, op2)
  inf = 1e18
  dp = Array.new(op1 + 1) { Array.new(op2 + 1, inf) }
  dp[0][0] = 0
  nums.each do |x|
    ndp = Array.new(op1 + 1) { Array.new(op2 + 1, inf) }
    (0..op1).each do |a|
      (0..op2).each do |b|
        next if dp[a][b] == inf

        try_cand(ndp, dp[a][b], a, b, x)
        try_cand(ndp, dp[a][b], a + 1, b, (x + 1) / 2) if a < op1
        try_cand(ndp, dp[a][b], a, b + 1, x - k) if b < op2 && x >= k
        if a < op1 && b < op2
          v1 = (x + 1) / 2
          try_cand(ndp, dp[a][b], a + 1, b + 1, v1 - k) if v1 >= k
          try_cand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2) if x >= k
        end
      end
    end
    dp = ndp
  end
  ans = inf
  (0..op1).each do |a|
    (0..op2).each { |b| ans = dp[a][b] if dp[a][b] < ans }
  end
  ans.to_i
end
''')

add("3367_maximize_sum_of_weights_after_edge_removals", r'''
# LeetCode 3367 - Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def maximize_sum_of_weights(edges, k)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  dfs = lambda do |u, p|
    base = 0
    gains = []
    g[u].each do |to, w|
      next if to == p

      child = dfs.call(to, u)
      base += child[1]
      gain = child[0] + w - child[1]
      gains << gain if gain > 0
    end
    gains.sort!.reverse!
    with_p = base
    without = base
    [gains.length, k - 1].min.times { |i| with_p += gains[i] }
    [gains.length, k].min.times { |i| without += gains[i] }
    [with_p, without]
  end
  dfs.call(0, -1)[1]
end
''')

add("3369_design_an_array_statistics_tracker", r'''
# LeetCode 3369 - Design an Array Statistics Tracker
# https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker
  def initialize
    @arr = []
    @sum = 0
    @freq = {}
    @mode_freq = 0
    @modes = {}
  end

  def add_number(num)
    @arr << num
    @sum += num
    f = (@freq[num] || 0) + 1
    @freq[num] = f
    if f > @mode_freq
      @mode_freq = f
      @modes.clear
      @modes[num] = true
    elsif f == @mode_freq
      @modes[num] = true
    end
    nil
  end

  def remove_first
    return if @arr.empty?

    num = @arr.shift
    @sum -= num
    f = @freq[num] - 1
    if f == 0
      @freq.delete(num)
    else
      @freq[num] = f
    end
    @mode_freq = 0
    @modes.clear
    @freq.each do |v, ff|
      if ff > @mode_freq
        @mode_freq = ff
        @modes.clear
        @modes[v] = true
      elsif ff == @mode_freq
        @modes[v] = true
      end
    end
    nil
  end

  def get_mean
    return 0 if @arr.empty?

    @sum / @arr.length
  end

  def get_median
    n = @arr.length
    tmp = @arr.sort
    return tmp[n / 2] if n.odd?

    tmp[n / 2 - 1]
  end

  def get_mode
    best = 9_007_199_254_740_991
    @modes.each_key { |v| best = v if v < best }
    best == 9_007_199_254_740_991 ? 0 : best
  end
end
''')

add("3370_smallest_number_with_all_set_bits", r'''
# LeetCode 3370 - Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/

# @param {Integer} n
# @return {Integer}
def smallest_number(n)
  x = 1
  x = x * 2 + 1 while x < n
  x
end
''')

add("3371_identify_the_largest_outlier_in_an_array", r'''
# LeetCode 3371 - Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def get_largest_outlier(nums)
  total = 0
  freq = {}
  nums.each do |x|
    total += x
    freq[x] = (freq[x] || 0) + 1
  end
  ans = -2_147_483_648
  nums.each do |x|
    freq[x] -= 1
    rem = total - x
    if rem.even?
      cand = rem / 2
      ans = x if (freq[cand] || 0) > 0 && x > ans
    end
    freq[x] += 1
  end
  ans
end
''')

add("3372_maximize_the_number_of_target_nodes_after_connecting_trees_i", r'''
# LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def build_tree(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  g
end

# @param {Integer[][]} g
# @param {Integer} start
# @param {Integer} k
# @return {Integer}
def count_within(g, start, k)
  return 0 if k < 0

  n = g.length
  vis = Array.new(n, false)
  q = [[start, 0]]
  vis[start] = true
  cnt = 0
  qi = 0
  while qi < q.length
    u, d = q[qi]
    qi += 1
    cnt += 1
    next if d == k

    g[u].each do |v|
      unless vis[v]
        vis[v] = true
        q << [v, d + 1]
      end
    end
  end
  cnt
end

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @param {Integer} k
# @return {Integer[]}
def max_target_nodes(edges1, edges2, k)
  n = edges1.length + 1
  m = edges2.length + 1
  g1 = build_tree(n, edges1)
  g2 = build_tree(m, edges2)
  cnt1 = n.times.map { |i| count_within(g1, i, k) }
  best2 = 0
  if k > 0
    m.times do |i|
      c = count_within(g2, i, k - 1)
      best2 = c if c > best2
    end
  end
  n.times.map { |i| cnt1[i] + best2 }
end
''')

add("3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii", r'''
# LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def build_tree(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  g
end

# @param {Integer[][]} g
# @param {Integer[]} color
# @return {Integer[]}
def bipartite_count(g, color)
  color.length.times { |i| color[i] = -1 }
  q = [0]
  color[0] = 0
  cnt = [1, 0]
  qi = 0
  while qi < q.length
    u = q[qi]
    qi += 1
    g[u].each do |v|
      if color[v] == -1
        color[v] = color[u] ^ 1
        cnt[color[v]] += 1
        q << v
      end
    end
  end
  cnt
end

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @return {Integer[]}
def max_target_nodes(edges1, edges2)
  n = edges1.length + 1
  m = edges2.length + 1
  g1 = build_tree(n, edges1)
  g2 = build_tree(m, edges2)
  color1 = Array.new(n, 0)
  color2 = Array.new(m, 0)
  c1 = bipartite_count(g1, color1)
  c2 = bipartite_count(g2, color2)
  best2 = [c2[0], c2[1]].max
  n.times.map { |i| c1[color1[i]] + best2 }
end
''')

add("3375_minimum_operations_to_make_array_values_equal_to_k", r'''
# LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  seen = {}
  nums.each do |x|
    return -1 if x < k

    seen[x] = true if x > k
  end
  seen.length
end
''')

add("3376_minimum_time_to_break_locks_i", r'''
# LeetCode 3376 - Minimum Time to Break Locks I
# https://leetcode.com/problems/minimum-time-to-break-locks-i/

# @param {Integer} x
# @return {Integer}
def bits_ones(x)
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end

# @param {Integer[]} strength
# @param {Integer} k
# @return {Integer}
def find_minimum_time(strength, k)
  n = strength.length
  inf = 1_000_000_000
  nn = 1 << n
  dp = Array.new(nn, inf)
  dp[0] = 0
  nn.times do |mask|
    next if dp[mask] == inf

    opened = bits_ones(mask)
    x = 1 + opened * k
    n.times do |i|
      next if (mask & (1 << i)) != 0

      t = (strength[i] + x - 1) / x
      nmask = mask | (1 << i)
      dp[nmask] = dp[mask] + t if dp[mask] + t < dp[nmask]
    end
  end
  dp[nn - 1]
end
''')

add("3377_digit_operations_to_make_two_integers_equal", r'''
# LeetCode 3377 - Digit Operations to Make Two Integers Equal
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

# @param {Integer} n
# @return {Boolean[]}
def sieve_primes(n)
  is_p = Array.new(n, false)
  (2...n).each { |i| is_p[i] = true }
  i = 2
  while i * i < n
    if is_p[i]
      j = i * i
      while j < n
        is_p[j] = false
        j += i
      end
    end
    i += 1
  end
  is_p
end

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def min_operations(n, m)
  is_prime = sieve_primes(100_000)
  return -1 if is_prime[n]

  dist = Array.new(100_000, -1)
  pq = [[n, n]]
  dist[n] = n
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    cost, val = pq.shift
    next if cost != dist[val]
    return cost if val == m

    s = val.to_s.chars
    s.length.times do |i|
      orig = s[i]
      [-1, 1].each do |d|
        nd = (orig.ord - 48) + d
        next if nd < 0 || nd > 9
        next if i == 0 && nd == 0 && s.length > 1

        s[i] = nd.to_s
        nv = s.join.to_i
        s[i] = orig
        next if is_prime[nv]

        nc = cost + nv
        if dist[nv] == -1 || nc < dist[nv]
          dist[nv] = nc
          pq << [nc, nv]
        end
      end
    end
  end
  -1
end
''')

add("3378_count_connected_components_in_lcm_graph", r'''
# LeetCode 3378 - Count Connected Components in LCM Graph
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def count_components(nums, threshold)
  n = nums.length
  parent = n.times.to_a
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  idx = {}
  nums.each_with_index { |v, i| idx[v] = i }
  (1..threshold).each do |d|
    first = -1
    m = d
    while m <= threshold
      if idx.key?(m)
        i = idx[m]
        if first == -1
          first = i
        elsif nums[first] * nums[i] / gcd_int(nums[first], nums[i]) <= threshold
          unite.call(first, i)
        end
      end
      m += d
    end
  end
  n.times do |i|
    ((i + 1)...n).each do |j|
      a = nums[i]
      b = nums[j]
      g = gcd_int(a, b)
      unite.call(i, j) if (a / g) * b <= threshold
    end
  end
  n.times.map { |i| find.call(i) }.uniq.length
end
''')

add("3379_transformed_array", r'''
# LeetCode 3379 - Transformed Array
# https://leetcode.com/problems/transformed-array/

# @param {Integer[]} nums
# @return {Integer[]}
def construct_transformed_array(nums)
  n = nums.length
  ans = Array.new(n, 0)
  n.times do |i|
    j = ((i + nums[i]) % n + n) % n
    ans[i] = nums[j]
  end
  ans
end
''')

add("3380_maximum_area_rectangle_with_point_constraints_i", r'''
# LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def pack_point(x, y)
  (x << 32) ^ (y & 0xFFFFFFFF)
end

# @param {Integer[][]} points
# @return {Integer}
def max_rectangle_area(points)
  s = {}
  points.each { |p| s[pack_point(p[0], p[1])] = true }
  ans = -1
  n = points.length
  n.times do |i|
    ((i + 1)...n).each do |j|
      x1 = points[i][0]
      y1 = points[i][1]
      x2 = points[j][0]
      y2 = points[j][1]
      next if x1 == x2 || y1 == y2
      next unless s[pack_point(x1, y2)] && s[pack_point(x2, y1)]

      min_x = [x1, x2].min
      max_x = [x1, x2].max
      min_y = [y1, y2].min
      max_y = [y1, y2].max
      good = true
      points.each do |p|
        x = p[0]
        y = p[1]
        if x > min_x && x < max_x && y > min_y && y < max_y
          good = false
          break
        end
        on_border = ((x == min_x || x == max_x) && y >= min_y && y <= max_y) ||
                    ((y == min_y || y == max_y) && x >= min_x && x <= max_x)
        next unless on_border

        is_corner = (x == min_x || x == max_x) && (y == min_y || y == max_y)
        unless is_corner
          good = false
          break
        end
      end
      if good
        area = (max_x - min_x) * (max_y - min_y)
        ans = area if area > ans
      end
    end
  end
  ans
end
''')

add("3381_maximum_subarray_sum_with_length_divisible_by_k", r'''
# LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  inf = 9_007_199_254_740_991
  best = Array.new(k, inf)
  best[0] = 0
  ans = -inf
  (1..n).each do |i|
    r = i % k
    if best[r] != inf
      cand = pref[i] - best[r]
      ans = cand if cand > ans
    end
    best[r] = pref[i] if pref[i] < best[r]
  end
  ans
end
''')

add("3382_maximum_area_rectangle_with_point_constraints_ii", r'''
# LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def pack_point(x, y)
  (x << 32) ^ (y & 0xFFFFFFFF)
end

# @param {Integer[]} x_coord
# @param {Integer[]} y_coord
# @return {Integer}
def max_rectangle_area(x_coord, y_coord)
  n = x_coord.length
  points = n.times.map { |i| [x_coord[i], y_coord[i]] }
  s = {}
  points.each { |p| s[pack_point(p[0], p[1])] = true }
  ans = -1
  n.times do |i|
    ((i + 1)...n).each do |j|
      x1 = points[i][0]
      y1 = points[i][1]
      x2 = points[j][0]
      y2 = points[j][1]
      next if x1 == x2 || y1 == y2
      next unless s[pack_point(x1, y2)] && s[pack_point(x2, y1)]

      min_x = [x1, x2].min
      max_x = [x1, x2].max
      min_y = [y1, y2].min
      max_y = [y1, y2].max
      good = true
      points.each do |p|
        x = p[0]
        y = p[1]
        if x > min_x && x < max_x && y > min_y && y < max_y
          good = false
          break
        end
        on_border = ((x == min_x || x == max_x) && y >= min_y && y <= max_y) ||
                    ((y == min_y || y == max_y) && x >= min_x && x <= max_x)
        next unless on_border

        is_corner = (x == min_x || x == max_x) && (y == min_y || y == max_y)
        unless is_corner
          good = false
          break
        end
      end
      if good
        area = (max_x - min_x) * (max_y - min_y)
        ans = area if area > ans
      end
    end
  end
  ans
end
''')

add("3383_minimum_runes_to_add_to_cast_spell", r'''
# LeetCode 3383 - Minimum Runes to Add to Cast Spell
# https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

# @param {Integer} n
# @param {Integer[]} crystals
# @param {Integer[]} flow_from
# @param {Integer[]} flow_to
# @return {Integer}
def min_runes_to_add(n, crystals, flow_from, flow_to)
  g = Array.new(n) { [] }
  rg = Array.new(n) { [] }
  flow_from.length.times do |i|
    a = flow_from[i]
    b = flow_to[i]
    g[a] << b
    rg[b] << a
  end
  vis = Array.new(n, false)
  order = []
  dfs1 = lambda do |u|
    vis[u] = true
    g[u].each { |v| dfs1.call(v) unless vis[v] }
    order << u
  end
  n.times { |i| dfs1.call(i) unless vis[i] }
  comp = Array.new(n, -1)
  cid = 0
  dfs2 = lambda do |u|
    comp[u] = cid
    rg[u].each { |v| dfs2.call(v) if comp[v] == -1 }
  end
  (n - 1).downto(0) do |i|
    u = order[i]
    if comp[u] == -1
      dfs2.call(u)
      cid += 1
    end
  end
  has_crystal = Array.new(cid, false)
  crystals.each { |c| has_crystal[comp[c]] = true }
  indeg = Array.new(cid, 0)
  n.times do |u|
    g[u].each { |v| indeg[comp[v]] += 1 if comp[u] != comp[v] }
  end
  ans = 0
  cid.times { |i| ans += 1 if indeg[i] == 0 && !has_crystal[i] }
  ans
end
''')

add("3385_minimum_time_to_break_locks_ii", r'''
# LeetCode 3385 - Minimum Time to Break Locks II
# https://leetcode.com/problems/minimum-time-to-break-locks-ii/

# @param {Integer} x
# @return {Integer}
def bits_ones(x)
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end

# @param {Integer[]} strength
# @return {Integer}
def find_minimum_time(strength)
  n = strength.length
  nn = 1 << n
  inf = 1e18
  dp = Array.new(nn, inf)
  dp[0] = 0
  k = 1
  nn.times do |mask|
    next if dp[mask] == inf

    opened = bits_ones(mask)
    x = 1 + opened * k
    n.times do |i|
      next if (mask & (1 << i)) != 0

      t = (strength[i] + x - 1) / x
      nmask = mask | (1 << i)
      dp[nmask] = dp[mask] + t if dp[mask] + t < dp[nmask]
    end
  end
  dp[nn - 1].to_i
end
''')

add("3386_button_with_longest_push_time", r'''
# LeetCode 3386 - Button with Longest Push Time
# https://leetcode.com/problems/button-with-longest-push-time/

# @param {Integer[][]} events
# @return {Integer}
def button_with_longest_time(events)
  best_t = events[0][1]
  best_i = events[0][0]
  (1...events.length).each do |i|
    t = events[i][1] - events[i - 1][1]
    if t > best_t || (t == best_t && events[i][0] < best_i)
      best_t = t
      best_i = events[i][0]
    end
  end
  best_i
end
''')

add("3387_maximize_amount_after_two_days_of_conversions", r'''
# LeetCode 3387 - Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

# @param {String[][]} pairs
# @param {Float[]} rates
# @return {Hash}
def build_rate_graph(pairs, rates)
  g = {}
  pairs.length.times do |i|
    a = pairs[i][0]
    b = pairs[i][1]
    g[a] ||= {}
    g[b] ||= {}
    g[a][b] = rates[i]
    g[b][a] = 1.0 / rates[i]
  end
  g
end

# @param {String} start
# @param {String[][]} pairs
# @param {Float[]} rates
# @return {Hash}
def bellman_rates(start, pairs, rates)
  g = build_rate_graph(pairs, rates)
  dist = { start => 1.0 }
  100.times do
    updated = false
    g.each do |frm, tos|
      next if !dist.key?(frm) || dist[frm] == 0

      tos.each do |to, rate|
        nv = dist[frm] * rate
        if !dist.key?(to) || nv > dist[to]
          dist[to] = nv
          updated = true
        end
      end
    end
    break unless updated
  end
  dist
end

# @param {String} initial_currency
# @param {String[][]} pairs1
# @param {Float[]} rates1
# @param {String[][]} pairs2
# @param {Float[]} rates2
# @return {Float}
def max_amount(initial_currency, pairs1, rates1, pairs2, rates2)
  amt1 = bellman_rates(initial_currency, pairs1, rates1)
  ans = 1.0
  g2 = build_rate_graph(pairs2, rates2)
  amt1.each do |c, a|
    next if a <= 0

    dist = { c => a }
    updated = true
    it = 0
    while it < 100 && updated
      updated = false
      g2.each do |frm, tos|
        next if !dist.key?(frm) || dist[frm] == 0

        tos.each do |to, rate|
          nv = dist[frm] * rate
          if !dist.key?(to) || nv > dist[to]
            dist[to] = nv
            updated = true
          end
        end
      end
      it += 1
    end
    ans = dist[initial_currency] if dist.key?(initial_currency) && dist[initial_currency] > ans
  end
  ans
end
''')

add("3388_count_beautiful_splits_in_an_array", r'''
# LeetCode 3388 - Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/

# @param {Integer[]} a
# @param {Integer} as_
# @param {Integer} ae
# @param {Integer[]} b
# @param {Integer} bs
# @param {Integer} be
# @return {Boolean}
def ranges_equal(a, as_, ae, b, bs, be)
  return false if ae - as_ != be - bs

  (ae - as_).times { |i| return false if a[as_ + i] != b[bs + i] }
  true
end

# @param {Integer[]} nums
# @return {Integer}
def beautiful_splits(nums)
  n = nums.length
  ans = 0
  (1...(n - 1)).each do |i|
    ((i + 1)...n).each do |j|
      ok = false
      ok = true if i <= j - i && ranges_equal(nums, 0, i, nums, i, i + i)
      ok = true if !ok && j - i <= n - j && ranges_equal(nums, i, j, nums, j, j + (j - i))
      ans += 1 if ok
    end
  end
  ans
end
''')

add("3389_minimum_operations_to_make_character_frequencies_equal", r'''
# LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

# @param {String} s
# @return {Integer}
def make_string_good(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  ans = s.length
  (1..s.length).each do |t|
    pool = 0
    26.times { |i| pool += freq[i] - t if freq[i] > t }
    deficit = 0
    26.times { |i| deficit += t - freq[i] if freq[i] < t }
    ops = [pool, deficit].max
    ans = ops if ops < ans
  end
  ans = s.length if s.length < ans
  ans
end
''')

add("3391_design_a_3d_binary_matrix_with_efficient_layer_tracking", r'''
# LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
# https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D
  def initialize(n)
    @n = n
    @m = Array.new(n) { Array.new(n) { Array.new(n, 0) } }
    @ones = Array.new(n, 0)
  end

  def set_cell(x, y, z)
    if @m[x][y][z] == 0
      @m[x][y][z] = 1
      @ones[x] += 1
    end
    nil
  end

  def unset_cell(x, y, z)
    if @m[x][y][z] == 1
      @m[x][y][z] = 0
      @ones[x] -= 1
    end
    nil
  end

  def largest_matrix
    best = -1
    idx = 0
    @n.times do |i|
      if @ones[i] >= best
        best = @ones[i]
        idx = i
      end
    end
    idx
  end
end
''')

add("3392_count_subarrays_of_length_three_with_a_condition", r'''
# LeetCode 3392 - Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

# @param {Integer[]} nums
# @return {Integer}
def count_subarrays(nums)
  ans = 0
  (0...(nums.length - 2)).each do |i|
    ans += 1 if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]
  end
  ans
end
''')

add("3393_count_paths_with_the_given_xor_value", r'''
# LeetCode 3393 - Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_paths_with_xor_value(grid, k)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n) { Array.new(16, 0) } }
  dp[0][0][grid[0][0]] = 1
  m.times do |i|
    n.times do |j|
      16.times do |x|
        next if dp[i][j][x] == 0

        if i + 1 < m
          nx = x ^ grid[i + 1][j]
          dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
        end
        if j + 1 < n
          nx = x ^ grid[i][j + 1]
          dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
        end
      end
    end
  end
  dp[m - 1][n - 1][k]
end
''')

add("3394_check_if_grid_can_be_cut_into_sections", r'''
# LeetCode 3394 - Check if Grid can be Cut into Sections
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

# @param {Integer[][]} rects
# @param {Integer} axis
# @return {Boolean}
def check_cut(rects, axis)
  arr = rects.map { |r| axis == 0 ? [r[0], r[2]] : [r[1], r[3]] }
  arr.sort_by! { |x| [x[0], x[1]] }
  cuts = 0
  ending = arr[0][1]
  (1...arr.length).each do |i|
    if arr[i][0] >= ending
      cuts += 1
      ending = arr[i][1]
      return true if cuts >= 2
    elsif arr[i][1] > ending
      ending = arr[i][1]
    end
  end
  false
end

# @param {Integer} n
# @param {Integer[][]} rectangles
# @return {Boolean}
def check_valid_cuts(n, rectangles)
  check_cut(rectangles, 0) || check_cut(rectangles, 1)
end
''')

written = 0
failed = []
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    try:
        path.write_text(body, encoding="utf-8", newline="\n")
        if body.startswith("\ufeff") or "def solve(input)" in body:
            failed.append((name, "bom_or_stub"))
        else:
            written += 1
    except Exception as e:
        failed.append((name, str(e)))
print(f"batch16_d written={written} failed={failed}")
print("keys", len(S))
