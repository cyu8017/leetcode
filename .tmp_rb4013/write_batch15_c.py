#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3240_minimum_number_of_flips_to_make_binary_grid_palindromic_ii", r'''
# LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

# @param {Integer[][]} grid
# @return {Integer}
def min_flips(grid)
  m = grid.length
  n = grid[0].length
  ans = 0
  (0...(m / 2)).each do |i|
    (0...(n / 2)).each do |j|
      x = m - i - 1
      y = n - j - 1
      cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y]
      ans += [cnt1, 4 - cnt1].min
    end
  end
  ans += grid[m / 2][n / 2] if m.odd? && n.odd?
  diff = 0
  ones = 0
  if m.odd?
    (0...(n / 2)).each do |j|
      if grid[m / 2][j] == grid[m / 2][n - j - 1]
        ones += grid[m / 2][j] * 2
      else
        diff += 1
      end
    end
  end
  if n.odd?
    (0...(m / 2)).each do |i|
      if grid[i][n / 2] == grid[m - i - 1][n / 2]
        ones += grid[i][n / 2] * 2
      else
        diff += 1
      end
    end
  end
  if ones % 4 == 0 || diff > 0
    ans += diff
  else
    ans += 2
  end
  ans
end
''')

add("3241_time_taken_to_mark_all_nodes", r'''
# LeetCode 3241 - Time Taken to Mark All Nodes
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/

# @param {Integer[][]} edges
# @return {Integer[]}
def time_taken(edges)
  n = edges.length + 1
  ans = Array.new(n, 0)
  tree = Array.new(n) { [] }
  dp = Array.new(n) { { top1: { node: 0, time: 0 }, top2: { node: 0, time: 0 } } }
  edges.each do |e|
    tree[e[0]] << e[1]
    tree[e[1]] << e[0]
  end
  get_time = lambda { |u| u.even? ? 2 : 1 }
  dfs = nil
  dfs = lambda do |u, prev|
    t1 = { node: 0, time: 0 }
    t2 = { node: 0, time: 0 }
    tree[u].each do |v|
      next if v == prev
      t = dfs.call(v, u) + get_time.call(v)
      if t >= t1[:time]
        t2 = t1
        t1 = { node: v, time: t }
      elsif t > t2[:time]
        t2 = { node: v, time: t }
      end
    end
    dp[u][:top1] = t1
    dp[u][:top2] = t2
    t1[:time]
  end
  reroot = nil
  reroot = lambda do |u, prev, max_time|
    ans[u] = max_time
    ans[u] = dp[u][:top1][:time] if dp[u][:top1][:time] > ans[u]
    tree[u].each do |v|
      next if v == prev
      side = dp[u][:top1][:node] == v ? dp[u][:top2][:time] : dp[u][:top1][:time]
      reroot.call(v, u, get_time.call(u) + [max_time, side].max)
    end
  end
  dfs.call(0, -1)
  reroot.call(0, -1, 0)
  ans
end
''')

add("3242_design_neighbor_sum_service", r'''
# LeetCode 3242 - Design Neighbor Sum Service
# https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum
  def initialize(grid)
    @grid = grid
    @d = {}
    @dirs = [
      [-1, 0, 1, 0, -1],
      [-1, 1, 1, -1, -1]
    ]
    grid.each_with_index do |row, i|
      row.each_with_index { |v, j| @d[v] = [i, j] }
    end
  end

  def cal(value, k)
    p = @d[value]
    s = 0
    4.times do |q|
      x = p[0] + @dirs[k][q]
      y = p[1] + @dirs[k][q + 1]
      s += @grid[x][y] if x >= 0 && x < @grid.length && y >= 0 && y < @grid[0].length
    end
    s
  end

  def adjacent_sum(value)
    cal(value, 0)
  end

  def diagonal_sum(value)
    cal(value, 1)
  end
end
''')

add("3243_shortest_distance_after_road_addition_queries_i", r'''
# LeetCode 3243 - Shortest Distance After Road Addition Queries I
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  g = Array.new(n) { [] }
  (0...n - 1).each { |i| g[i] << i + 1 }
  bfs = lambda do
    q = [0]
    vis = Array.new(n, false)
    vis[0] = true
    d = 0
    loop do
      k = q.length
      while k > 0
        u = q.shift
        return d if u == n - 1
        g[u].each do |v|
          unless vis[v]
            vis[v] = true
            q << v
          end
        end
        k -= 1
      end
      d += 1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    g[q[0]] << q[1]
    ans[i] = bfs.call
  end
  ans
end
''')

add("3244_shortest_distance_after_road_addition_queries_ii", r'''
# LeetCode 3244 - Shortest Distance After Road Addition Queries II
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  nxt = (1...n).to_a
  cnt = n - 1
  ans = []
  queries.each do |q|
    u = q[0]
    v = q[1]
    if nxt[u] && nxt[u] > 0 && nxt[u] < v
      i = nxt[u]
      while i < v
        cnt -= 1
        ni = nxt[i]
        nxt[i] = 0
        i = ni
      end
      nxt[u] = v
    end
    ans << cnt
  end
  ans
end
''')

add("3245_alternating_groups_iii", r'''
# LeetCode 3245 - Alternating Groups III
# https://leetcode.com/problems/alternating-groups-iii/

class SegTree
  def initialize(n_)
    @n = n_
    @tree_interval_counts = Array.new(4 * n_, 0)
    @tree_interval_lengths = Array.new(4 * n_, 0)
  end

  def add(i, val)
    add_rec(0, 0, @n - 1, i, val)
  end

  def add_rec(tree_index, lo, hi, i, val)
    if lo == hi
      @tree_interval_counts[tree_index] += val
      @tree_interval_lengths[tree_index] = @tree_interval_counts[tree_index] * i
      return
    end
    mid = (lo + hi) >> 1
    if i <= mid
      add_rec(2 * tree_index + 1, lo, mid, i, val)
    else
      add_rec(2 * tree_index + 2, mid + 1, hi, i, val)
    end
    @tree_interval_counts[tree_index] = @tree_interval_counts[2 * tree_index + 1] + @tree_interval_counts[2 * tree_index + 2]
    @tree_interval_lengths[tree_index] = @tree_interval_lengths[2 * tree_index + 1] + @tree_interval_lengths[2 * tree_index + 2]
  end

  def query_interval_counts(i)
    query(@tree_interval_counts, 0, 0, @n - 1, i, @n - 1)
  end

  def query_interval_lengths(i)
    query(@tree_interval_lengths, 0, 0, @n - 1, i, @n - 1)
  end

  def query(tree, tree_index, lo, hi, i, j)
    return tree[tree_index] if i <= lo && hi <= j
    return 0 if j < lo || hi < i
    mid = (lo + hi) >> 1
    query(tree, tree_index * 2 + 1, lo, mid, i, j) + query(tree, tree_index * 2 + 2, mid + 1, hi, i, j)
  end
end

# @param {Integer[]} colors
# @param {Integer[][]} queries
# @return {Integer[]}
def number_of_alternating_groups(colors, queries)
  n = colors.length
  ans = []
  arr = Array.new(2 * n - 1, 0)
  (0...n).each { |i| arr[i] = colors[i] }
  (0...n - 1).each { |i| arr[n + i] = colors[i] }
  pack = lambda { |l, r| (l << 32) | (r & 0xFFFFFFFF) }
  unpack_l = lambda { |v| v >> 32 }
  unpack_r = lambda { |v| v & 0xFFFFFFFF }
  tree = SegTree.new(2 * n - 1)
  intervals = {}
  insert = lambda do |l, r|
    intervals[pack.call(l, r)] = true
    tree.add(r - l + 1, 1) if l < n
  end
  remove = lambda do |l, r|
    intervals.delete(pack.call(l, r))
    tree.add(r - l + 1, -1) if l < n
  end
  find_interval = lambda do |target|
    best_l = best_r = -1
    intervals.each_key do |k|
      kl = unpack_l.call(k)
      kr = unpack_r.call(k)
      if kl <= target && target <= kr && kl > best_l
        best_l = kl
        best_r = kr
      end
    end
    [best_l, best_r]
  end
  get_num = lambda do |sz|
    num_intervals = tree.query_interval_counts(sz)
    sum_intervals = tree.query_interval_lengths(sz)
    num_alternating_groups = sum_intervals - num_intervals * sz + num_intervals
    l, r = find_interval.call(n)
    return num_alternating_groups if l < 0 || l >= n || r - l + 1 < sz
    if r >= n
      non_duplicate_groups = n - l
      num_groups = (r - l + 1) - sz + 1
      extra = num_groups - non_duplicate_groups
      num_alternating_groups -= extra if extra > 0
    end
    num_alternating_groups
  end
  update = lambda do |index, color|
    return if arr[index] == color
    arr[index] = color
    start, end_ = find_interval.call(index)
    remove.call(start, end_)
    if start < index && index < end_
      insert.call(start, index - 1)
      insert.call(index, index)
      insert.call(index + 1, end_)
      return
    end
    insert.call(start + 1, end_) if start == index && index < end_
    insert.call(start, end_ - 1) if start < index && index == end_
    ns = ne = index
    loop do
      merged = false
      intervals.keys.each do |k|
        kl = unpack_l.call(k)
        kr = unpack_r.call(k)
        if kr + 1 == ns && arr[kr] != arr[ns]
          remove.call(kl, kr)
          ns = kl
          merged = true
          break
        end
      end
      break unless merged
    end
    loop do
      merged = false
      intervals.keys.each do |k|
        kl = unpack_l.call(k)
        kr = unpack_r.call(k)
        if kl == ne + 1 && arr[kl] != arr[ne]
          remove.call(kl, kr)
          ne = kr
          merged = true
          break
        end
      end
      break unless merged
    end
    insert.call(ns, ne)
  end
  st = 0
  (1...(2 * n - 1)).each do |i|
    if arr[i] == arr[i - 1]
      insert.call(st, i - 1)
      st = i
    end
  end
  insert.call(st, 2 * n - 2)
  queries.each do |query|
    if query[0] == 1
      ans << get_num.call(query[1])
    else
      index = query[1]
      color = query[2]
      if arr[index] != color
        update.call(index, color)
        update.call(index + n, color) if index < n - 1
      end
    end
  end
  ans
end
''')

add("3247_number_of_subsequences_with_odd_sum", r'''
# LeetCode 3247 - Number of Subsequences with Odd Sum
# https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

# @param {Integer[]} nums
# @return {Integer}
def subsequence_count(nums)
  mod = 1_000_000_007
  f = [0, 0]
  nums.each do |x|
    g = [0, 0]
    if x.odd?
      g[0] = (f[0] + f[1]) % mod
      g[1] = (f[0] + f[1] + 1) % mod
    else
      g[0] = (f[0] + f[0] + 1) % mod
      g[1] = (f[1] + f[1]) % mod
    end
    f = g
  end
  f[1]
end
''')

add("3248_snake_in_matrix", r'''
# LeetCode 3248 - Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix/

# @param {Integer} n
# @param {String[]} commands
# @return {Integer}
def final_position_of_snake(n, commands)
  x = y = 0
  commands.each do |c|
    case c[0]
    when "U" then x -= 1
    when "D" then x += 1
    when "L" then y -= 1
    when "R" then y += 1
    end
  end
  x * n + y
end
''')

add("3249_count_the_number_of_good_nodes", r'''
# LeetCode 3249 - Count the Number of Good Nodes
# https://leetcode.com/problems/count-the-number-of-good-nodes/

# @param {Integer[][]} edges
# @return {Integer}
def count_good_nodes(edges)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0
  dfs = nil
  dfs = lambda do |a, fa|
    pre = -1
    cnt = 1
    ok = 1
    g[a].each do |b|
      next if b == fa
      cur = dfs.call(b, a)
      cnt += cur
      if pre < 0
        pre = cur
      elsif pre != cur
        ok = 0
      end
    end
    ans += ok
    cnt
  end
  dfs.call(0, -1)
  ans
end
''')

add("3250_find_the_count_of_monotonic_pairs_i", r'''
# LeetCode 3250 - Find the Count of Monotonic Pairs I
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

# @param {Integer[]} nums
# @return {Integer}
def count_of_pairs(nums)
  mod = 1_000_000_007
  n = nums.length
  dp = Array.new(51, 0)
  (0..nums[0]).each { |a| dp[a] = 1 }
  (1...n).each do |i|
    ndp = Array.new(51, 0)
    pref = Array.new(52, 0)
    (0...51).each { |a| pref[a + 1] = (pref[a] + dp[a]) % mod }
    (0..nums[i]).each do |a2|
      b2 = nums[i] - a2
      max_a1 = a2
      lim = nums[i - 1] - b2
      max_a1 = lim if lim < max_a1
      next if max_a1 < 0
      max_a1 = 50 if max_a1 > 50
      ndp[a2] = pref[max_a1 + 1]
    end
    dp = ndp
  end
  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ans
end
''')

add("3251_find_the_count_of_monotonic_pairs_ii", r'''
# LeetCode 3251 - Find the Count of Monotonic Pairs II
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

# @param {Integer[]} nums
# @return {Integer}
def count_of_pairs(nums)
  mod = 1_000_000_007
  n = nums.length
  max_v = nums.max
  dp = Array.new(max_v + 1, 0)
  (0..nums[0]).each { |a| dp[a] = 1 }
  (1...n).each do |i|
    ndp = Array.new(max_v + 1, 0)
    pref = Array.new(max_v + 2, 0)
    (0..max_v).each { |a| pref[a + 1] = (pref[a] + dp[a]) % mod }
    (0..nums[i]).each do |a2|
      b2 = nums[i] - a2
      max_a1 = a2
      lim = nums[i - 1] - b2
      max_a1 = lim if lim < max_a1
      next if max_a1 < 0
      max_a1 = max_v if max_a1 > max_v
      ndp[a2] = pref[max_a1 + 1]
    end
    dp = ndp
  end
  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ans
end
''')

add("3253_construct_string_with_minimum_cost_easy", r'''
# LeetCode 3253 - Construct String with Minimum Cost (Easy)
# https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

# @param {String} target
# @param {String[]} words
# @param {Integer[]} costs
# @return {Integer}
def minimum_cost(target, words, costs)
  inf = 10**18
  n = target.length
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  best = {}
  words.each_with_index do |w, i|
    best[w] = costs[i] if !best.key?(w) || costs[i] < best[w]
  end
  (0...n).each do |i|
    next if dp[i] == inf
    best.each do |w, c|
      l = w.length
      dp[i + l] = dp[i] + c if i + l <= n && target[i, l] == w && dp[i] + c < dp[i + l]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
''')

add("3254_find_the_power_of_k_size_subarrays_i", r'''
# LeetCode 3254 - Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def results_array(nums, k)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  (0...(n - k + 1)).each do |i|
    ok = true
    ((i + 1)...(i + k)).each do |j|
      if nums[j] != nums[j - 1] + 1
        ok = false
        break
      end
    end
    ans[i] = ok ? nums[i + k - 1] : -1
  end
  ans
end
''')

add("3255_find_the_power_of_k_size_subarrays_ii", r'''
# LeetCode 3255 - Find the Power of K-Size Subarrays II
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def results_array(nums, k)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  return nums.dup if k == 1
  streak = 1
  (1...n).each do |i|
    if nums[i] == nums[i - 1] + 1
      streak += 1
    else
      streak = 1
    end
    ans[i - k + 1] = streak >= k ? nums[i] : -1 if i >= k - 1
  end
  ans
end
''')

add("3256_maximum_value_sum_by_placing_three_rooks_i", r'''
# LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

# @param {Integer[][]} board
# @return {Integer}
def maximum_value_sum(board)
  m = board.length
  n = board[0].length
  tops = []
  (0...m).each do |i|
    row = []
    (0...n).each do |j|
      cur = { v: board[i][j], c: j }
      placed = false
      row.each_index do |t|
        if cur[:v] > row[t][:v]
          row.insert(t, cur)
          placed = true
          break
        end
      end
      row << cur unless placed
      row = row[0, 3] if row.length > 3
    end
    tops << row
  end
  ans = -(10**18)
  (0...m).each do |i|
    tops[i].each do |a|
      ((i + 1)...m).each do |j|
        tops[j].each do |b|
          next if a[:c] == b[:c]
          ((j + 1)...m).each do |k|
            tops[k].each do |c|
              next if c[:c] == a[:c] || c[:c] == b[:c]
              s = a[:v] + b[:v] + c[:v]
              ans = s if s > ans
            end
          end
        end
      end
    end
  end
  ans
end
''')

add("3257_maximum_value_sum_by_placing_three_rooks_ii", r'''
# LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

# @param {Integer[][]} board
# @return {Integer}
def maximum_value_sum(board)
  m = board.length
  n = board[0].length
  tops = []
  (0...m).each do |i|
    row = []
    (0...n).each do |j|
      cur = { v: board[i][j], c: j }
      placed = false
      row.each_index do |t|
        if cur[:v] > row[t][:v]
          row.insert(t, cur)
          placed = true
          break
        end
      end
      row << cur unless placed
      row = row[0, 3] if row.length > 3
    end
    tops << row
  end
  ans = -(10**18)
  (0...m).each do |i|
    tops[i].each do |a|
      ((i + 1)...m).each do |j|
        tops[j].each do |b|
          next if a[:c] == b[:c]
          ((j + 1)...m).each do |k|
            tops[k].each do |c|
              next if c[:c] == a[:c] || c[:c] == b[:c]
              s = a[:v] + b[:v] + c[:v]
              ans = s if s > ans
            end
          end
        end
      end
    end
  end
  ans
end
''')

add("3258_count_substrings_that_satisfy_k_constraint_i", r'''
# LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_constraint_substrings(s, k)
  ans = 0
  n = s.length
  (0...n).each do |i|
    z = o = 0
    (i...n).each do |j|
      if s[j] == "0"
        z += 1
      else
        o += 1
      end
      if z <= k || o <= k
        ans += 1
      else
        break
      end
    end
  end
  ans
end
''')

add("3259_maximum_energy_boost_from_two_drinks", r'''
# LeetCode 3259 - Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

# @param {Integer[]} energy_drink_a
# @param {Integer[]} energy_drink_b
# @return {Integer}
def max_energy_boost(energy_drink_a, energy_drink_b)
  n = energy_drink_a.length
  dp_a = Array.new(n, 0)
  dp_b = Array.new(n, 0)
  dp_a[0] = energy_drink_a[0]
  dp_b[0] = energy_drink_b[0]
  return [dp_a[0], dp_b[0]].max if n == 1
  dp_a[1] = energy_drink_a[1] + dp_a[0]
  dp_b[1] = energy_drink_b[1] + dp_b[0]
  (2...n).each do |i|
    dp_a[i] = energy_drink_a[i] + [dp_a[i - 1], dp_b[i - 2]].max
    dp_b[i] = energy_drink_b[i] + [dp_b[i - 1], dp_a[i - 2]].max
  end
  [dp_a[n - 1], dp_b[n - 1]].max
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
