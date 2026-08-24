#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3969_valid_subarrays_with_matching_sum_digits_i", r'''
# LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def count_valid_subarrays(nums, x)
  n = nums.length
  ans = 0
  n.times do |l|
    s = 0
    (l...n).each do |r|
      s += nums[r]
      if s % 10 == x
        t = s.to_s
        ans += 1 if t[0].ord - 48 == x
      end
    end
  end
  ans
end
''')

add("3970_shortest_path_with_at_most_k_consecutive_identical_characters", r'''
# LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} labels
# @param {Integer} k
# @return {Integer}
def shortest_path(n, edges, labels, k)
  graph = Array.new(n) { [] }
  edges.each { |edge| graph[edge[0]] << [edge[1], edge[2]] }
  infinity = (1 << 53) / 4
  distances = Array.new(n) { Array.new(k + 1, infinity) }
  distances[0][1] = 0
  pq = [[0, 0, 1]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    distance, node, run = pq.shift
    next if distance != distances[node][run]
    return distance if node == n - 1
    graph[node].each do |to, weight|
      next_run = labels[node] == labels[to] ? run + 1 : 1
      next if next_run > k
      next_distance = distance + weight
      if next_distance < distances[to][next_run]
        distances[to][next_run] = next_distance
        pq << [next_distance, to, next_run]
      end
    end
  end
  -1
end
''')

add("3971_maximum_total_value", r'''
# LeetCode 3971 - Maximum Total Value
# https://leetcode.com/problems/maximum-total-value/

# @param {Integer[]} value
# @param {Integer[]} decay
# @param {Integer} m
# @return {Integer}
def maximum_total_value(value, decay, m)
  count_at_least = lambda do |threshold|
    count = 0
    value.each_with_index do |v, i|
      count += (v - threshold) / decay[i] + 1 if v >= threshold
    end
    count
  end
  mod = 1_000_000_007
  if count_at_least.call(1) <= m
    s = 0
    value.each_with_index do |v, i|
      terms = (v - 1) / decay[i] + 1
      s = (s + terms * v - decay[i] * terms * (terms - 1) / 2) % mod
    end
    return s
  end
  high = value.max
  low = 1
  while low < high
    mid = (low + high + 1) / 2
    if count_at_least.call(mid) >= m
      low = mid
    else
      high = mid - 1
    end
  end
  threshold = low
  count = 0
  s = 0
  value.each_with_index do |v, i|
    next if v < threshold
    terms = (v - threshold) / decay[i] + 1
    count += terms
    s = (s + (terms * v - decay[i] * terms * (terms - 1) / 2) % mod) % mod
  end
  s = (s - ((count - m) % mod) * (threshold % mod)) % mod
  s += mod if s < 0
  s
end
''')

add("3972_valid_subarrays_with_matching_sum_digits_ii", r'''
# LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def count_valid_subarrays(nums, x)
  lower_bound = lambda do |a, val|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] < val
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  upper_bound = lambda do |a, val|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] <= val
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  by_remainder = Array.new(10) { [] }
  by_remainder[0] << 0
  prefix = 0
  answer = 0
  nums.each do |value|
    prefix += value
    required = ((prefix - x) % 10 + 10) % 10
    values = by_remainder[required]
    power = 1
    while x * power <= prefix
      low = x * power
      high = (x + 1) * power - 1
      min_prefix = prefix - high
      max_prefix = prefix - low
      left = lower_bound.call(values, min_prefix)
      right = upper_bound.call(values, max_prefix)
      answer += right - left
      break if power > prefix / 10
      power *= 10
    end
    by_remainder[prefix % 10] << prefix
  end
  answer
end
''')

add("3973_distinct_gate_paths_to_lca", r'''
# LeetCode 3973 - Distinct Gate Paths to LCA
# https://leetcode.com/problems/distinct-gate-paths-to-lca/

# @param {Integer} n
# @param {Integer[]} parent
# @param {Integer[][]} gates
# @param {Integer[][]} queries
# @return {Integer}
def gate_path_xor(n, parent, gates, queries)
  mod = 1_000_000_007
  multiply = lambda do |a, b|
    c = [[0, 0], [0, 0]]
    2.times do |i|
      2.times do |j|
        2.times do |k|
          c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
        end
      end
    end
    c
  end
  logn = 1
  logn += 1 while (1 << logn) <= n
  up = Array.new(logn) { Array.new(n, 0) }
  product = Array.new(logn) { Array.new(n) }
  children = Array.new(n) { [] }
  (1...n).each { |node| children[parent[node]] << node }
  depth = Array.new(n, 0)
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    children[u].each do |v|
      depth[v] = depth[u] + 1
      order << v
    end
    i += 1
  end
  n.times do |u|
    up[0][u] = u == 0 ? 0 : parent[u]
    product[0][u] = [[gates[u][1], gates[u][2]], [gates[u][2], gates[u][0]]]
  end
  (1...logn).each do |level|
    n.times do |u|
      mid = up[level - 1][u]
      up[level][u] = up[level - 1][mid]
      product[level][u] = multiply.call(product[level - 1][u], product[level - 1][mid])
    end
  end
  lift_node = lambda do |node, distance|
    level = 0
    while distance > 0
      node = up[level][node] if (distance & 1) != 0
      distance >>= 1
      level += 1
    end
    node
  end
  lca = lambda do |a, b|
    if depth[a] > depth[b]
      a = lift_node.call(a, depth[a] - depth[b])
    elsif depth[b] > depth[a]
      b = lift_node.call(b, depth[b] - depth[a])
    end
    return a if a == b
    (logn - 1).downto(0) do |level|
      if up[level][a] != up[level][b]
        a = up[level][a]
        b = up[level][b]
      end
    end
    up[0][a]
  end
  ways = lambda do |node, card, distance|
    vector = [0, 0]
    vector[card] = 1
    level = 0
    while distance > 0
      if (distance & 1) != 0
        matrix = product[level][node]
        vector = [
          (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % mod,
          (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % mod
        ]
        node = up[level][node]
      end
      distance >>= 1
      level += 1
    end
    (vector[0] + vector[1]) % mod
  end
  answer = 0
  queries.each do |query|
    ancestor = lca.call(query[0], query[2])
    alice = ways.call(query[0], query[1], depth[query[0]] - depth[ancestor])
    bob = ways.call(query[2], query[3], depth[query[2]] - depth[ancestor])
    total = (alice * bob) % mod
    answer ^= total
  end
  answer
end
''')

add("3974_maximum_total_sum_of_k_selected_elements", r'''
# LeetCode 3974 - Maximum Total Sum Of K Selected Elements
# https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} mul
# @return {Integer}
def max_sum(nums, k, mul)
  nums = nums.sort
  n = nums.length
  ans = 0
  (n - 1).downto(n - k) do |i|
    m = [1, mul].max
    ans += nums[i] * m
    mul -= 1
  end
  ans
end
''')

add("3975_filter_occupied_intervals", r'''
# LeetCode 3975 - Filter Occupied Intervals
# https://leetcode.com/problems/filter-occupied-intervals/

# @param {Integer[][]} occupied_intervals
# @param {Integer} free_start
# @param {Integer} free_end
# @return {Integer[][]}
def filter_occupied_intervals(occupied_intervals, free_start, free_end)
  occupied_intervals.sort_by! { |a| a[0] }
  busy = [[occupied_intervals[0][0], occupied_intervals[0][1]]]
  (1...occupied_intervals.length).each do |i|
    cur = occupied_intervals[i]
    last = busy[-1]
    if last[1] + 1 < cur[0]
      busy << [cur[0], cur[1]]
    elsif cur[1] > last[1]
      last[1] = cur[1]
    end
  end
  ans = []
  busy.each do |it|
    s, e = it[0], it[1]
    if e < free_start || s > free_end
      ans << [s, e]
    else
      ans << [s, free_start - 1] if s < free_start
      ans << [free_end + 1, e] if e > free_end
    end
  end
  ans
end
''')

add("3976_maximum_subarray_sum_after_multiplier", r'''
# LeetCode 3976 - Maximum Subarray Sum After Multiplier
# https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  n = nums.length
  inf = -(2**53) / 4
  f = Array.new(n + 1) { Array.new(4, inf) }
  f[0][0] = 0
  ans = inf
  (1..n).each do |i|
    x = nums[i - 1]
    f[i][0] = [f[i - 1][0], 0].max + x
    f[i][1] = [[f[i - 1][0], f[i - 1][1]].max, 0].max + x * k
    f[i][2] = [[f[i - 1][0], f[i - 1][2]].max, 0].max + (x.to_f / k).to_i
    f[i][3] = [[f[i - 1][1], f[i - 1][2]].max, f[i - 1][3]].max + x
    v = [[f[i][0], f[i][1]].max, [f[i][2], f[i][3]].max].max
    ans = v if v > ans
  end
  ans
end
''')

add("3977_minimum_time_to_reach_target_with_limited_power", r'''
# LeetCode 3977 - Minimum Time to Reach Target With Limited Power
# https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} power
# @param {Integer[]} cost
# @param {Integer} source
# @param {Integer} target
# @return {Integer[]}
def min_time_max_power(n, edges, power, cost, source, target)
  inf = 2**62
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << [e[1], e[2]] }
  dist = Array.new(n) { Array.new(power + 1, inf) }
  pq = [[0, -power, source]]
  dist[source][power] = 0
  until pq.empty?
    pq.sort_by! { |a| [a[0], a[1]] }
    d, neg_p, u = pq.shift
    p = -neg_p
    return [d, p] if u == target
    next if d > dist[u][p] || p < cost[u]
    p -= cost[u]
    g[u].each do |v, t|
      nd = d + t
      if nd < dist[v][p]
        dist[v][p] = nd
        pq << [nd, -p, v]
      end
    end
  end
  [-1, -1]
end
''')

add("3978_unique_middle_element", r'''
# LeetCode 3978 - Unique Middle Element
# https://leetcode.com/problems/unique-middle-element/

# @param {Integer[]} nums
# @return {Boolean}
def is_middle_element_unique(nums)
  mid = nums[nums.length / 2]
  nums.count(mid) == 1
end
''')

add("3979_maximum_valid_pair_sum", r'''
# LeetCode 3979 - Maximum Valid Pair Sum
# https://leetcode.com/problems/maximum-valid-pair-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_valid_pair_sum(nums, k)
  ans = 0
  x = 0
  (k...nums.length).each do |j|
    y = nums[j]
    x = nums[j - k] if nums[j - k] > x
    ans = x + y if x + y > ans
  end
  ans
end
''')

add("3980_minimum_operations_to_transform_binary_string", r'''
# LeetCode 3980 - Minimum Operations to Transform Binary String
# https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

# @param {String} s1
# @param {String} s2
# @return {Integer}
def min_operations(s1, s2)
  infinity = 1_000_000_000
  dp = [0, infinity]
  n = s1.length
  n.times do |i|
    nxt = [infinity, infinity]
    2.times do |forced_zero|
      next if dp[forced_zero] == infinity
      current = forced_zero == 1 ? "0" : s1[i]
      direct = dp[forced_zero]
      if current == "0" && s2[i] == "1"
        direct += 1
      elsif current == "1" && s2[i] == "0"
        direct = infinity
      end
      nxt[0] = direct if direct < nxt[0]
      if i + 1 < n
        cost = dp[forced_zero] + 1
        cost += 1 if current == "0"
        cost += 1 if s1[i + 1] == "0"
        cost += 1 if s2[i] == "1"
        nxt[1] = cost if cost < nxt[1]
      end
    end
    dp = nxt
  end
  dp[0] == infinity ? -1 : dp[0]
end
''')

add("3981_count_distinct_ways_to_form_target_from_two_strings", r'''
# LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
# https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

# @param {String} word1
# @param {String} word2
# @param {String} target
# @return {Integer}
def count_ways(word1, word2, target)
  index = lambda { |i, j, mask, n2| ((i * (n2 + 1) + j) * 4) + mask }
  mod = 1_000_000_007
  n1 = word1.length
  n2 = word2.length
  size = (n1 + 1) * (n2 + 1) * 4
  dp = Array.new(size, 0)
  dp[index.call(0, 0, 0, n2)] = 1
  target.each_char do |ch|
    nxt = Array.new(size, 0)
    (0..n2).each do |j|
      prefix = Array.new(4, 0)
      n1.times do |a|
        4.times do |mask|
          prefix[mask] += dp[index.call(a, j, mask, n2)]
          prefix[mask] -= mod if prefix[mask] >= mod
        end
        next unless word1[a] == ch
        4.times do |mask|
          at = index.call(a + 1, j, mask | 1, n2)
          nxt[at] += prefix[mask]
          nxt[at] -= mod if nxt[at] >= mod
        end
      end
    end
    (0..n1).each do |i|
      prefix = Array.new(4, 0)
      n2.times do |b|
        4.times do |mask|
          prefix[mask] += dp[index.call(i, b, mask, n2)]
          prefix[mask] -= mod if prefix[mask] >= mod
        end
        next unless word2[b] == ch
        4.times do |mask|
          at = index.call(i, b + 1, mask | 2, n2)
          nxt[at] += prefix[mask]
          nxt[at] -= mod if nxt[at] >= mod
        end
      end
    end
    dp = nxt
  end
  answer = 0
  (0..n1).each do |i|
    (0..n2).each do |j|
      answer += dp[index.call(i, j, 3, n2)]
      answer -= mod if answer >= mod
    end
  end
  answer
end
''')

add("3982_sum_of_integers_with_maximum_digit_range", r'''
# LeetCode 3982 - Sum of Integers with Maximum Digit Range
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

# @param {Integer[]} nums
# @return {Integer}
def max_digit_range(nums)
  mx = 0
  ans = 0
  nums.each do |x|
    a = 10
    b = 0
    y = x
    while y > 0
      v = y % 10
      a = v if v < a
      b = v if v > b
      y /= 10
    end
    r = b - a
    if mx < r
      mx = r
      ans = x
    elsif mx == r
      ans += x
    end
  end
  ans
end
''')

add("3983_subsequence_after_one_replacement", r'''
# LeetCode 3983 - Subsequence After One Replacement
# https://leetcode.com/problems/subsequence-after-one-replacement/

# @param {String} s
# @param {String} t
# @return {Boolean}
def can_make_subsequence(s, t)
  m = s.length
  n = t.length
  i0 = 0
  i1 = 0
  j = 0
  while i1 < m && j < n
    i1 += 1 if s[i1] == t[j]
    i1 = i0 + 1 if i1 < i0 + 1
    i0 += 1 if s[i0] == t[j]
    j += 1
  end
  i1 == m
end
''')

add("3984_divisible_game", r'''
# LeetCode 3984 - Divisible Game
# https://leetcode.com/problems/divisible-game/

# @param {Integer[]} nums
# @return {Integer}
def divisible_game(nums)
  candidates = { 2 => true }
  nums.each do |value|
    divisor = 2
    while divisor * divisor <= value
      if value % divisor == 0
        candidates[divisor] = true
        candidates[value / divisor] = true
      end
      divisor += 1
    end
    candidates[value] = true if value > 1
  end
  best_score = -(1 << 62)
  best_k = 0
  candidates.keys.each do |k|
    ending = 0
    score = 0
    nums.each_with_index do |value, i|
      contribution = value % k == 0 ? value : -value
      if i == 0 || ending + contribution < contribution
        ending = contribution
      else
        ending += contribution
      end
      score = ending if i == 0 || ending > score
    end
    if score > best_score || (score == best_score && k < best_k)
      best_score = score
      best_k = k
    end
  end
  mod = 1_000_000_007
  answer = (best_score % mod) * best_k % mod
  answer += mod if answer < 0
  answer
end
''')

add("3985_palindromic_subarray_sum", r'''
# LeetCode 3985 - Palindromic Subarray Sum
# https://leetcode.com/problems/palindromic-subarray-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_palindromic_subarray_sum(nums)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  odd = Array.new(n, 0)
  left = 0
  right = -1
  n.times do |i|
    radius = 1
    if i <= right
      mirror = left + right - i
      radius = odd[mirror]
      radius = right - i + 1 if right - i + 1 < radius
    end
    radius += 1 while i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]
    odd[i] = radius
    if i + radius - 1 > right
      left = i - radius + 1
      right = i + radius - 1
    end
  end
  even = Array.new(n, 0)
  left = 0
  right = -1
  n.times do |i|
    radius = 0
    if i <= right
      mirror = left + right - i + 1
      radius = even[mirror]
      radius = right - i + 1 if right - i + 1 < radius
    end
    radius += 1 while i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]
    even[i] = radius
    if i + radius - 1 > right
      left = i - radius
      right = i + radius - 1
    end
  end
  answer = 0
  n.times do |i|
    s = prefix[i + odd[i]] - prefix[i - odd[i] + 1]
    answer = s if s > answer
    if even[i] > 0
      s = prefix[i + even[i]] - prefix[i - even[i]]
      answer = s if s > answer
    end
  end
  answer
end
''')

add("3986_number_of_elapsed_seconds_between_two_times", r'''
# LeetCode 3986 - Number of Elapsed Seconds Between Two Times
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

# @param {String} start_time
# @param {String} end_time
# @return {Integer}
def seconds_between_times(start_time, end_time)
  to_seconds = lambda do |s|
    h = (s[0].ord - 48) * 10 + (s[1].ord - 48)
    m = (s[3].ord - 48) * 10 + (s[4].ord - 48)
    sec = (s[6].ord - 48) * 10 + (s[7].ord - 48)
    h * 3600 + m * 60 + sec
  end
  to_seconds.call(end_time) - to_seconds.call(start_time)
end
''')

add("3987_minimum_total_cost_to_process_all_elements", r'''
# LeetCode 3987 - Minimum Total Cost to Process All Elements
# https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_cost(nums, k)
  mod = 1_000_000_007
  cnt = 0
  cur = k
  nums.each do |x0|
    x = x0
    diff = x - cur
    if diff > 0
      m = (diff + k - 1) / k
      cur += m * k
      cnt += m
    end
    cur -= x
  end
  cnt %= mod
  (cnt + 1) * cnt / 2 % mod
end
''')

add("3988_create_grid_with_exactly_k_paths_i", r'''
# LeetCode 3988 - Create Grid With Exactly K Paths I
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {String[]}
def create_grid(m, n, k)
  cands = []
  if k == 1
    cands << ["."]
  elsif k == 2
    cands << ["..", ".."]
  elsif k == 3
    cands << ["..", "..", ".."]
    cands << ["...", "..."]
  elsif k == 4
    cands << ["..", "..", "..", ".."]
    cands << ["....", "...."]
    cands << ["..#", "...", "#.."]
  end
  cands.each do |pat|
    pr = pat.length
    pc = pat[0].length
    next if pr > m || pc > n
    result = Array.new(m) { "#" * n }
    pr.times do |i|
      row = result[i].chars
      pc.times { |j| row[j] = pat[i][j] }
      result[i] = row.join
    end
    (pr...m).each do |i|
      row = result[i].chars
      row[pc - 1] = "."
      result[i] = row.join
    end
    (pc...n).each do |j|
      row = result[m - 1].chars
      row[j] = "."
      result[m - 1] = row.join
    end
    return result
  end
  []
end
''')

add("3989_maximum_consistent_columns_in_a_grid", r'''
# LeetCode 3989 - Maximum Consistent Columns in a Grid
# https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer} limit
# @return {Integer}
def max_consistent_columns(grid, limit)
  m = grid.length
  n = grid[0].length
  dp = Array.new(n, 0)
  ans = 1
  n.times do |j|
    dp[j] = 1
    j.times do |i|
      next if dp[i] + 1 <= dp[j]
      ok = true
      m.times do |r|
        d = (grid[r][j] - grid[r][i]).abs
        if d > limit
          ok = false
          break
        end
      end
      dp[j] = dp[i] + 1 if ok
    end
    ans = dp[j] if dp[j] > ans
  end
  ans
end
''')

add("3990_create_grid_with_exactly_k_paths_ii", r'''
# LeetCode 3990 - Create Grid With Exactly K Paths II
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

# @param {Integer} k
# @return {String[]}
def create_grid(k)
  return [] if k <= 0
  w = 0
  kk = k
  while kk != 0
    w += 1
    kk >>= 1
  end
  l = w
  m = 2 * l
  n = l + 3
  result = Array.new(m) { Array.new(n, "#") }
  l.times do |i|
    r = 2 * i
    result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = "."
    if (k & (1 << i)) != 0
      ((i + 2)...n).each { |c| result[r][c] = "." }
    end
  end
  m.times { |r| result[r][n - 1] = "." }
  result.map(&:join)
end
''')

add("3992_rearrange_string_to_avoid_character_pair", r'''
# LeetCode 3992 - Rearrange String to Avoid Character Pair
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

# @param {String} s
# @param {String} x
# @param {String} y
# @return {String}
def rearrange_string(s, x, y)
  arr = s.chars
  i = 0
  arr.each_index do |j|
    if arr[j] == y
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
    end
  end
  arr.join
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
