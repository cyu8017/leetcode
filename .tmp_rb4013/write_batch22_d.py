#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3993_maximum_value_of_an_alternating_sequence", r'''
# LeetCode 3993 - Maximum Value of an Alternating Sequence
# https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

# @param {Integer} n
# @param {Integer} s
# @param {Integer} m
# @return {Integer}
def maximum_value(n, s, m)
  return s if n == 1
  s + (n / 2) * (m - 1) + 1
end
''')

add("3994_minimum_adjacent_swaps_to_partition_array", r'''
# LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def min_adjacent_swaps(nums, a, b)
  mod = 1_000_000_007
  result = 0
  cnt1 = 0
  cnt2 = 0
  nums.each do |x|
    if x < a
      result = (result + cnt1 + cnt2) % mod
    elsif x <= b
      cnt1 += 1
      result = (result + cnt2) % mod
    else
      cnt2 += 1
    end
  end
  result
end
''')

add("3995_minimum_cost_to_convert_string_iii", r'''
# LeetCode 3995 - Minimum Cost to Convert String III
# https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

# @param {String} source
# @param {String} target
# @param {String[][]} rules
# @param {Integer[]} costs
# @return {Integer}
def min_cost(source, target, rules, costs)
  n = source.length
  return -1 if target.length != n
  inf = 2_147_483_647
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  n.times do |i|
    next if dp[i] == inf
    dp[i + 1] = dp[i] if source[i] == target[i] && dp[i] < dp[i + 1]
    rules.each_with_index do |rule, j|
      p = rule[0]
      r = rule[1]
      plen = p.length
      next if i + plen > n
      c = costs[j]
      ok = true
      plen.times do |k|
        if r[k] != target[i + k]
          ok = false
          break
        end
        if p[k] == "*"
          c += 1
        elsif p[k] != source[i + k]
          ok = false
          break
        end
      end
      dp[i + plen] = dp[i] + c if ok && dp[i] <= inf - c && dp[i] + c < dp[i + plen]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
''')

add("3996_even_number_of_knight_moves", r'''
# LeetCode 3996 - Even Number of Knight Moves
# https://leetcode.com/problems/even-number-of-knight-moves/

# @param {Integer[]} start
# @param {Integer[]} target
# @return {Boolean}
def can_reach(start, target)
  ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2)
end
''')

add("3997_count_dominant_nodes_in_a_binary_tree", r'''
# LeetCode 3997 - Count Dominant Nodes in a Binary Tree
# https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def count_dominant_nodes(root)
  ans = 0
  dfs = nil
  dfs = lambda do |node|
    return -2_147_483_648 if node.nil?
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    mx = [l, r, node.val].max
    ans += 1 if mx == node.val
    mx
  end
  dfs.call(root)
  ans
end
''')

add("3998_transform_binary_string_using_subsequence_sort", r'''
# LeetCode 3998 - Transform Binary String Using Subsequence Sort
# https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

# @param {String} s
# @param {String[]} strs
# @return {Boolean[]}
def transform_str(s, strs)
  n = s.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + (s[i] == "1" ? 1 : 0) }
  result = Array.new(strs.length, false)
  strs.each_with_index do |t, i|
    left = 0
    right = 0
    ok = true
    n.times do |j|
      left += 1 if t[j] == "1"
      add = t[j] != "0" ? 1 : 0
      right += add
      right = prefix[j + 1] if right > prefix[j + 1]
      if left > right
        ok = false
        break
      end
    end
    result[i] = ok && left <= prefix[n] && prefix[n] <= right
  end
  result
end
''')

add("3999_minimum_number_of_string_groups_through_transformations", r'''
# LeetCode 3999 - Minimum Number of String Groups Through Transformations
# https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

# @param {String[]} words
# @return {Integer}
def minimum_groups(words)
  least_rotation = lambda do |s|
    n = s.length
    i = 0
    j = 1
    k = 0
    while i < n && j < n && k < n
      a = s[(i + k) % n]
      b = s[(j + k) % n]
      if a == b
        k += 1
      else
        if a > b
          i += k + 1
        else
          j += k + 1
        end
        j += 1 if i == j
        k = 0
      end
    end
    i < j ? i : j
  end
  canonical_rotate = lambda do |s|
    n = s.length
    return s if n <= 1
    r = least_rotation.call(s)
    return s if r == 0
    s[r..] + s[0...r]
  end
  keys = words.map do |w|
    even = +""
    odd = +""
    w.length.times do |i|
      if i.even?
        even << w[i]
      else
        odd << w[i]
      end
    end
    canonical_rotate.call(even) + "#" + canonical_rotate.call(odd)
  end
  keys.sort!
  groups = 0
  keys.each_with_index do |key, i|
    groups += 1 if i == 0 || key != keys[i - 1]
  end
  groups
end
''')

add("4000_largest_integer_with_given_digit_sum", r'''
# LeetCode 4000 - Largest Integer With Given Digit Sum
# https://leetcode.com/problems/largest-integer-with-given-digit-sum/

# @param {Integer} n
# @param {Integer} s
# @return {Integer}
def largest_integer(n, s)
  return -1 if n * 9 < s
  ans = 0
  n.times do
    x = s < 9 ? s : 9
    ans = ans * 10 + x
    s -= x
  end
  ans
end
''')

add("4001_aggregate_two_time_series", r'''
# LeetCode 4001 - Aggregate Two Time Series
# https://leetcode.com/problems/aggregate-two-time-series/

# @param {Integer[][]} series1
# @param {Integer[][]} series2
# @return {Integer[][]}
def aggregate_time_series(series1, series2)
  m = series1.length
  n = series2.length
  i = 0
  j = 0
  ans = []
  while i < m && j < n
    t1, v1 = series1[i][0], series1[i][1]
    t2, v2 = series2[j][0], series2[j][1]
    if t1 == t2
      ans << [t1, v1 + v2]
      i += 1
      j += 1
    elsif t1 < t2
      ans << [t1, v1 + v2]
      i += 1
    else
      ans << [t2, v1 + v2]
      j += 1
    end
  end
  while i < m
    ans << [series1[i][0], series1[i][1]]
    i += 1
  end
  while j < n
    ans << [series2[j][0], series2[j][1]]
    j += 1
  end
  ans
end
''')

add("4002_count_valid_sequences", r'''
# LeetCode 4002 - Count Valid Sequences
# https://leetcode.com/problems/count-valid-sequences/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def count_valid_sequences(n, k)
  mx = 500001
  mod = 1_000_000_007
  unless defined?($count_valid_sequences_f)
    $count_valid_sequences_f = Array.new(mx, 0)
    $count_valid_sequences_g = Array.new(mx, 0)
    $count_valid_sequences_f[0] = 1
    $count_valid_sequences_g[0] = 1
    mod_pow = lambda do |a, b|
      res = 1
      a %= mod
      while b > 0
        res = res * a % mod if (b & 1) != 0
        a = a * a % mod
        b >>= 1
      end
      res
    end
    (1...mx).each do |i|
      $count_valid_sequences_f[i] = $count_valid_sequences_f[i - 1] * i % mod
      $count_valid_sequences_g[i] = mod_pow.call($count_valid_sequences_f[i], mod - 2)
    end
  end
  comb = lambda do |nn, kk|
    return 0 if kk < 0 || kk > nn
    $count_valid_sequences_f[nn] * $count_valid_sequences_g[kk] % mod * $count_valid_sequences_g[nn - kk] % mod
  end
  ans = comb.call(n - 1, k - 1)
  ans = (ans - comb.call((n + k) / 2 - 1, k - 1) + mod) % mod if (n + k).even?
  ans
end
''')

add("4003_minimum_cost_path_with_alternating_directions_iii", r'''
# LeetCode 4003 - Minimum Cost Path with Alternating Directions III
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} penalty
# @return {Integer}
def min_cost(m, n, penalty)
  inf = 2**60
  dist = Array.new(m) { Array.new(n) { [inf, inf] } }
  dist[0][0][1] = 1
  pq = [[1, 0, 0, 1]]
  dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    d, i, j, k = pq.shift
    return d if i == m - 1 && j == n - 1
    next if d > dist[i][j][k]
    p = penalty[i][j]
    nd = d + p
    if nd < dist[i][j][k ^ 1]
      dist[i][j][k ^ 1] = nd
      pq << [nd, i, j, k ^ 1]
    end
    4.times do |idx|
      x = i + dirs[idx][0]
      y = j + dirs[idx][1]
      next unless x >= 0 && x < m && y >= 0 && y < n
      nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p))
      if nd < dist[x][y][k ^ 1]
        dist[x][y][k ^ 1] = nd
        pq << [nd, x, y, k ^ 1]
      end
    end
  end
  -1
end
''')

add("4004_minimum_moves_to_balance_circular_array_ii", r'''
# LeetCode 4004 - Minimum Moves to Balance Circular Array II
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

class Edge
  attr_accessor :to, :cap, :cost, :rev

  def initialize(to, cap, cost, rev)
    @to = to
    @cap = cap
    @cost = cost
    @rev = rev
  end
end

class MinCostMaxFlow
  def initialize(n_)
    @n = n_
    @graph = Array.new(n_) { [] }
  end

  def add_edge(u, v, cap, cost)
    @graph[u] << Edge.new(v, cap, cost, @graph[v].length)
    @graph[v] << Edge.new(u, 0, -cost, @graph[u].length - 1)
  end

  def min_cost_flow(source, sink, max_flow)
    inf = 1_000_000_000
    total_cost = 0
    current_flow = 0
    n = @n
    graph = @graph
    while current_flow < max_flow
      dist = Array.new(n, inf)
      parent_node = Array.new(n, -1)
      parent_edge = Array.new(n, -1)
      in_queue = Array.new(n, false)
      q = [source]
      dist[source] = 0
      in_queue[source] = true
      qi = 0
      while qi < q.length
        u = q[qi]
        qi += 1
        in_queue[u] = false
        graph[u].each_with_index do |e, i|
          if e.cap > 0 && dist[e.to] > dist[u] + e.cost
            dist[e.to] = dist[u] + e.cost
            parent_node[e.to] = u
            parent_edge[e.to] = i
            unless in_queue[e.to]
              in_queue[e.to] = true
              q << e.to
            end
          end
        end
      end
      return -1 if dist[sink] == inf
      push_flow = max_flow - current_flow
      cur = sink
      while cur != source
        e = graph[parent_node[cur]][parent_edge[cur]]
        push_flow = e.cap if e.cap < push_flow
        cur = parent_node[cur]
      end
      cur = sink
      while cur != source
        p = parent_node[cur]
        idx = parent_edge[cur]
        rev = graph[p][idx].rev
        graph[p][idx].cap -= push_flow
        graph[cur][rev].cap += push_flow
        cur = parent_node[cur]
      end
      current_flow += push_flow
      total_cost += push_flow * dist[sink]
    end
    total_cost
  end
end

# @param {Integer[]} balance
# @return {Integer}
def min_moves(balance)
  inf = 1_000_000_000
  total_balance = 0
  total_deficit = 0
  balance.each do |x|
    total_balance += x
    total_deficit += -x if x < 0
  end
  return -1 if total_balance < 0
  return 0 if total_deficit == 0
  n = balance.length
  source = n
  sink = n + 1
  mcmf = MinCostMaxFlow.new(n + 2)
  n.times do |i|
    x = balance[i]
    if x > 0
      mcmf.add_edge(source, i, x, 0)
    elsif x < 0
      mcmf.add_edge(i, sink, -x, 0)
    end
    mcmf.add_edge(i, (i + 1) % n, inf, 1)
    mcmf.add_edge(i, (i - 1 + n) % n, inf, 1)
  end
  mcmf.min_cost_flow(source, sink, total_deficit)
end
''')

add("4005_minimum_operations_to_make_array_equal_iii", r'''
# LeetCode 4005 - Minimum Operations to Make Array Equal III
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  cost = lambda do |x, t|
    return 0 if x == t
    return 1 if x % t == 0 || t % x == 0
    2
  end
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  return 0 if n <= 1
  g = nums[0]
  mn = nums[0]
  (1...n).each do |i|
    g = gcd.call(g, nums[i])
    mn = nums[i] if nums[i] < mn
  end
  cands = {}
  nums.each { |x| cands[x] = true }
  d = 1
  while d * d <= mn
    if mn % d == 0
      cands[d] = true
      cands[mn / d] = true
    end
    d += 1
  end
  cands[g] = true
  ans = 2_147_483_647
  cands.keys.each do |t|
    s = 0
    nums.each do |x|
      s += cost.call(x, t)
      break if s >= ans
    end
    ans = s if s < ans
  end
  ans
end
''')

add("4006_count_valid_prefixes", r'''
# LeetCode 4006 - Count Valid Prefixes
# https://leetcode.com/problems/count-valid-prefixes/

# @param {String} s
# @return {Integer}
def count_valid_prefixes(s)
  ans = 0
  t = 0
  s.each_char do |ch|
    t += ch == "1" ? 1 : -1
    ans += 1 if t >= -1 && t <= 1
  end
  ans
end
''')

add("4007_widest_possible_fence", r'''
# LeetCode 4007 - Widest Possible Fence
# https://leetcode.com/problems/widest-possible-fence/

# @param {Integer[]} planks
# @return {Integer}
def maximum_width(planks)
  cnt = {}
  planks.each { |x| cnt[x] = cnt.fetch(x, 0) + 1 }
  t = {}
  ans = 0
  cnt.each do |x, v1|
    t[x] = t.fetch(x, 0) + v1
    ans = t[x] if t[x] > ans
    t[x * 2] = t.fetch(x * 2, 0) + v1 / 2
    ans = t[x * 2] if t[x * 2] > ans
    cnt.each do |y, v2|
      next unless y > x
      key = x + y
      t[key] = t.fetch(key, 0) + [v1, v2].min
      ans = t[key] if t[key] > ans
    end
  end
  ans
end
''')

add("4008_minimum_initial_strength_to_defeat_all_monsters", r'''
# LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
# https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

# @param {Integer[]} monsters
# @param {Integer[][]} boosts
# @return {Integer}
def min_initial_strength(monsters, boosts)
  n = monsters.length
  d = Array.new(n + 1, 0)
  boosts.each do |b|
    d[b[0]] += b[2]
    d[b[1] + 1] -= b[2]
  end
  check = lambda do |v|
    bonus = 0
    monsters.each_with_index do |m, i|
      bonus += d[i]
      return false if v + bonus < m
      v -= m
      v = 0 if v < 0
    end
    true
  end
  left = 0
  right = 1_000_000_000_000_000
  while left < right
    mid = (left + right) / 2
    if check.call(mid)
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
''')

add("4009_minimum_possible_maximum_waiting_time", r'''
# LeetCode 4009 - Minimum Possible Maximum Waiting Time
# https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

# @param {Integer[]} demand
# @param {Integer[]} fuel
# @return {Integer}
def min_max_waiting_time(demand, fuel)
  pack_key = lambda { |i, f0, f1, d0, d1| ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1) }
  dem = demand
  n = dem.length
  f0, f1 = fuel[0], fuel[1]
  return -1 if f0 < demand[0] && f1 < demand[0]
  memo = {}
  max_serve = nil
  max_serve = lambda do |i, ff0, ff1, d0, d1|
    return i if i == n
    key = pack_key.call(i, ff0, ff1, d0, d1)
    return memo[key] if memo.key?(key)
    need = dem[i]
    can0 = ff0 >= need
    can1 = ff1 >= need
    best = i
    if !can0 && !can1
      memo[key] = best
      return best
    end
    if can0
      nd1 = d1 > d0 ? d1 - d0 : 0
      v = max_serve.call(i + 1, ff0 - need, ff1, need, nd1)
      best = v if v > best
    end
    if can1
      nd0 = d0 > d1 ? d0 - d1 : 0
      v = max_serve.call(i + 1, ff0, ff1 - need, nd0, need)
      best = v if v > best
    end
    memo[key] = best
    best
  end
  best_serve = max_serve.call(0, f0, f1, 0, 0)
  return -1 if best_serve == 0
  can_with_w = nil
  w = 0
  can_with_w = lambda do |i, ff0, ff1, d0, d1|
    return true if i >= best_serve || i == n
    key = pack_key.call(i, ff0, ff1, d0, d1)
    return memo[key] == 2 if memo.key?(key)
    need = dem[i]
    can0 = ff0 >= need
    can1 = ff1 >= need
    ok = false
    if !can0 && !can1
      memo[key] = 1
      return false
    end
    if can0 && d0 <= w
      nd1 = d1 > d0 ? d1 - d0 : 0
      ok = true if can_with_w.call(i + 1, ff0 - need, ff1, need, nd1)
    end
    if !ok && can1 && d1 <= w
      nd0 = d0 > d1 ? d0 - d1 : 0
      ok = true if can_with_w.call(i + 1, ff0, ff1 - need, nd0, need)
    end
    memo[key] = ok ? 2 : 1
    ok
  end
  lo = 0
  hi = demand.sum
  ans = hi
  while lo <= hi
    mid = (lo + hi) / 2
    w = mid
    memo = {}
    if can_with_w.call(0, f0, f1, 0, 0)
      ans = mid
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  ans
end
''')

add("4010_maximize_pair_strength_using_gcd", r'''
# LeetCode 4010 - Maximize Pair Strength Using GCD
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/

# @param {Integer[]} nums
# @return {Integer}
def max_pair_strength(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  ans = 0
  n.times do |i|
    ((i + 1)...n).each do |j|
      g = gcd.call(nums[i], nums[j])
      x = nums[i] * nums[j] / (g * g)
      ans = x if x > ans
    end
  end
  ans
end
''')

add("4011_count_subarrays_with_even_odd_ratio_i", r'''
# LeetCode 4011 - Count Subarrays With Even Odd Ratio I
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def count_ratio_subarrays(nums, a, b)
  n = nums.length
  ans = 0
  n.times do |i|
    y = 0
    (i...n).each do |j|
      y += nums[j] % 2
      x = j - i + 1 - y
      ans += 1 if y > 0 && x * b <= y * a
    end
  end
  ans
end
''')

add("4012_count_of_unfinished_tasks_after_each_shift", r'''
# LeetCode 4012 - Count of Unfinished Tasks After Each Shift
# https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

# @param {Integer[]} tasks
# @param {Integer[]} shifts
# @return {Integer[]}
def count_tasks(tasks, shifts)
  m = tasks.length
  n = shifts.length
  s = Array.new(m + 1, 0)
  m.times { |i| s[i + 1] = s[i] + tasks[i] }
  ans = Array.new(n, 0)
  i_idx = 0
  cur = 0
  n.times do |j|
    if shifts[j] < tasks[i_idx] - cur
      cur += shifts[j]
      ans[j] = m - i_idx
    else
      t = shifts[j] - (tasks[i_idx] - cur)
      if t >= s[m] - s[i_idx + 1]
        i_idx = 0
        cur = 0
      else
        l = i_idx + 1
        r = m
        while l < r
          mid = (l + r) >> 1
          if t < s[mid + 1] - s[i_idx + 1]
            r = mid
          else
            l = mid + 1
          end
        end
        cur = t - (s[l] - s[i_idx + 1])
        i_idx = l
        ans[j] = m - i_idx
      end
    end
  end
  ans
end
''')

add("4013_count_subarrays_with_even_odd_ratio_ii", r'''
# LeetCode 4013 - Count Subarrays With Even Odd Ratio II
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

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

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def count_ratio_subarrays(nums, a, b)
  n = nums.length
  s = Array.new(n + 1, 0)
  n.times do |i|
    s[i + 1] = if nums[i].odd?
                 s[i] + a
               else
                 s[i] - b
               end
  end
  st = s.sort
  uniq = 0
  st.each_with_index do |v, i|
    if uniq == 0 || v != st[uniq - 1]
      st[uniq] = v
      uniq += 1
    end
  end
  st = st[0...uniq]
  lower_bound = lambda do |arr, x|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  bit = BIT.new(st.length + 1)
  ans = 0
  s.each do |v|
    x = lower_bound.call(st, v) + 1
    ans += bit.query(x)
    bit.update(x, 1)
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
