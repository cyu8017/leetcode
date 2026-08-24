#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3873_maximum_points_activated_with_one_addition", r'''
# LeetCode 3873 - Maximum Points Activated with One Addition
# https://leetcode.com/problems/maximum-points-activated-with-one-addition/

# @param {Integer[][]} points
# @return {Integer}
def max_activated(points)
  p = {}
  size = {}
  find = nil
  find = lambda do |x|
    unless p.key?(x)
      p[x] = x
      size[x] = 1
    end
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end
  unite = lambda do |a, b|
    pa = find.call(a)
    pb = find.call(b)
    return false if pa == pb
    if size[pa] > size[pb]
      p[pb] = pa
      size[pa] = size[pa] + size[pb]
    else
      p[pa] = pb
      size[pb] = size[pb] + size[pa]
    end
    true
  end
  m = 3_000_000_000
  points.each { |pt| unite.call(pt[0], pt[1] + m) }
  cnt = Hash.new(0)
  points.each { |pt| cnt[find.call(pt[0])] += 1 }
  mx1 = 0
  mx2 = 0
  cnt.each_value do |x|
    if mx1 < x
      mx2 = mx1
      mx1 = x
    elsif mx2 < x
      mx2 = x
    end
  end
  mx1 + mx2 + 1
end
''')

add("3874_valid_subarrays_with_exactly_one_peak", r'''
# LeetCode 3874 - Valid Subarrays With Exactly One Peak
# https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def valid_subarrays(nums, k)
  n = nums.length
  peaks = []
  (1...(n - 1)).each do |i|
    peaks << i if nums[i] > nums[i - 1] && nums[i] > nums[i + 1]
  end
  ans = 0
  peaks.each_with_index do |p, j|
    left_min = [p - k, 0].max
    left_min = [left_min, peaks[j - 1] + 1].max if j > 0
    right_max = [p + k, n - 1].min
    right_max = [right_max, peaks[j + 1] - 1].min if j < peaks.length - 1
    ans += (p - left_min + 1) * (right_max - p + 1)
  end
  ans
end
''')

add("3875_construct_uniform_parity_array_i", r'''
# LeetCode 3875 - Construct Uniform Parity Array I
# https://leetcode.com/problems/construct-uniform-parity-array-i/

# @param {Integer[]} nums1
# @return {Boolean}
def uniform_array(_nums1)
  true
end
''')

add("3876_construct_uniform_parity_array_ii", r'''
# LeetCode 3876 - Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

# @param {Integer[]} nums1
# @return {Boolean}
def uniform_array(nums1)
  mn = Float::INFINITY
  nums1.each { |x| mn = x if x.odd? && x < mn }
  nums1.each { |x| return false if x.even? && mn != Float::INFINITY && x < mn }
  true
end
''')

add("3877_minimum_removals_to_achieve_target_xor", r'''
# LeetCode 3877 - Minimum Removals to Achieve Target XOR
# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_removals(nums, target)
  mx = nums.max
  m = 0
  if mx > 0
    u = mx
    while u != 0
      m += 1
      u >>= 1
    end
  end
  return -1 if (1 << m) <= target
  n = nums.length
  nmask = 1 << m
  neg = -Float::INFINITY
  f = Array.new(n + 1) { Array.new(nmask, neg) }
  f[0][0] = 0
  (1..n).each do |i|
    x = nums[i - 1]
    nmask.times do |j|
      f[i][j] = f[i - 1][j]
      f[i][j] = [f[i][j], f[i - 1][j ^ x] + 1].max if f[i - 1][j ^ x] != neg
    end
  end
  return -1 if f[n][target] < 0
  n - f[n][target].to_i
end
''')

add("3878_count_good_subarrays", r'''
# LeetCode 3878 - Count Good Subarrays
# https://leetcode.com/problems/count-good-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_good_subarrays(nums)
  n = nums.length
  l = Array.new(n, -1)
  stk = []
  n.times do |i|
    x = nums[i]
    stk.pop while !stk.empty? && nums[stk[-1]] < x && (nums[stk[-1]] | x) == x
    l[i] = stk[-1] unless stk.empty?
    stk << i
  end
  r = Array.new(n, n)
  stk = []
  (n - 1).downto(0) do |i|
    stk.pop while !stk.empty? && (nums[stk[-1]] | nums[i]) == nums[i]
    r[i] = stk[-1] unless stk.empty?
    stk << i
  end
  ans = 0
  n.times { |i| ans += (i - l[i]) * (r[i] - i) }
  ans
end
''')

add("3879_maximum_distinct_path_sum_in_a_binary_tree", r'''
# LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
# https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

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
def max_sum(root)
  g = {}
  vis = {}
  dfs = nil
  dfs = lambda do |node, p|
    return if node.nil?
    g[node] = [p, node.left, node.right]
    dfs.call(node.left, node)
    dfs.call(node.right, node)
  end
  dfs2 = nil
  dfs2 = lambda do |node|
    return 0 if node.nil? || vis[node.val] == true
    vis[node.val] = true
    res = node.val
    best = 0
    g[node].each { |nxt| best = [best, dfs2.call(nxt)].max }
    vis[node.val] = false
    res + best
  end
  g.clear
  vis.clear
  dfs.call(root, nil)
  ans = -Float::INFINITY
  g.each_key do |node|
    ans = [ans, dfs2.call(node)].max
    vis.clear
  end
  ans.to_i
end
''')

add("3880_minimum_absolute_difference_between_two_values", r'''
# LeetCode 3880 - Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

# @param {Integer[]} nums
# @return {Integer}
def min_absolute_difference(nums)
  n = nums.length
  ans = n + 1
  last = [-ans, -ans, -ans]
  n.times do |i|
    x = nums[i]
    if x != 0
      ans = [ans, i - last[3 - x]].min
      last[x] = i
    end
  end
  return -1 if ans > n
  ans
end
''')

add("3881_direction_assignments_with_exactly_k_visible_people", r'''
# LeetCode 3881 - Direction Assignments with Exactly K Visible People
# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

N3881 = 100001
MOD3881 = 1_000_000_007
$fact3881 = nil
$inv_fact3881 = nil
$ready3881 = false

def qmi3881(a, k, p)
  res = 1
  while k != 0
    res = res * a % p if (k & 1) != 0
    k >>= 1
    a = a * a % p
  end
  res
end

def init3881
  return if $ready3881
  $fact3881 = Array.new(N3881, 0)
  $inv_fact3881 = Array.new(N3881, 0)
  $fact3881[0] = $inv_fact3881[0] = 1
  (1...N3881).each do |i|
    $fact3881[i] = $fact3881[i - 1] * i % MOD3881
    $inv_fact3881[i] = qmi3881($fact3881[i], MOD3881 - 2, MOD3881)
  end
  $ready3881 = true
end

def comb3881(n, k)
  $fact3881[n] * $inv_fact3881[k] % MOD3881 * $inv_fact3881[n - k] % MOD3881
end

# @param {Integer} n
# @param {Integer} pos
# @param {Integer} k
# @return {Integer}
def count_visible_people(n, pos, k)
  init3881
  l = pos
  r = n - pos - 1
  ans = 0
  (0..[k, l].min).each do |a|
    b = k - a
    if b <= r
      ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881
    end
  end
  ans
end
''')

add("3882_minimum_xor_path_in_a_grid", r'''
# LeetCode 3882 - Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def min_xor(grid)
  rows = grid.length
  cols = grid[0].length
  dp = Array.new(cols) { Array.new(1024, false) }
  rows.times do |row|
    left = Array.new(1024, false)
    cols.times do |col|
      nxt = Array.new(1024, false)
      value = grid[row][col]
      if row == 0 && col == 0
        nxt[value] = true
      else
        1024.times do |xorv|
          nxt[xorv ^ value] = true if dp[col][xorv] || left[xorv]
        end
      end
      dp[col] = nxt
      left = nxt
    end
  end
  1024.times { |xorv| return xorv if dp[cols - 1][xorv] }
  -1
end
''')

add("3883_count_non_decreasing_arrays_with_given_digit_sums", r'''
# LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
# https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

# @param {Integer[]} digit_sum
# @return {Integer}
def count_non_decreasing_arrays(digit_sum)
  mod = 1_000_000_007
  groups = Array.new(51) { [] }
  (0..5000).each do |x|
    s = 0
    y = x
    while y > 0
      s += y % 10
      y /= 10
    end
    groups[s] << x
  end
  prev_vals = groups[digit_sum[0]]
  dp = Array.new(prev_vals.length, 1)
  (1...digit_sum.length).each do |pos|
    cur_vals = groups[digit_sum[pos]]
    nxt = Array.new(cur_vals.length, 0)
    j = 0
    prefix = 0
    cur_vals.each_with_index do |x, i|
      while j < prev_vals.length && prev_vals[j] <= x
        prefix += dp[j]
        prefix -= mod if prefix >= mod
        j += 1
      end
      nxt[i] = prefix
    end
    prev_vals = cur_vals
    dp = nxt
  end
  ans = 0
  dp.each do |x|
    ans += x
    ans -= mod if ans >= mod
  end
  ans
end
''')

add("3884_first_matching_character_from_both_ends", r'''
# LeetCode 3884 - First Matching Character From Both Ends
# https://leetcode.com/problems/first-matching-character-from-both-ends/

# @param {String} s
# @return {Integer}
def first_matching_index(s)
  n = s.length
  (0..(n / 2)).each { |i| return i if s[i] == s[n - i - 1] }
  -1
end
''')

add("3885_design_event_manager", r'''
# LeetCode 3885 - Design Event Manager
# https://leetcode.com/problems/design-event-manager/

class EventManager
  def initialize(events)
    @sl = []
    @d = {}
    events.each do |e|
      event_id, priority = e[0], e[1]
      @sl << [-priority, event_id]
      @d[event_id] = priority
    end
    _sort
  end

  def update_priority(event_id, new_priority)
    old = @d[event_id]
    @sl.reject! { |x| x[0] == -old && x[1] == event_id }
    @sl << [-new_priority, event_id]
    @d[event_id] = new_priority
    _sort
    nil
  end

  def poll_highest
    return -1 if @sl.empty?
    top = @sl.shift
    event_id = top[1]
    @d.delete(event_id)
    event_id
  end

  def _sort
    @sl.sort_by! { |a| [a[0], a[1]] }
  end
end
''')

add("3886_sum_of_sortable_integers", r'''
# LeetCode 3886 - Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-sortable-integers/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_sortable_integers(nums)
  rotation_matches = lambda do |block, target|
    k = block.length
    prefix = Array.new(k, 0)
    (1...k).each do |i|
      j = prefix[i - 1]
      while j > 0 && target[i] != target[j]
        j = prefix[j - 1]
      end
      j += 1 if target[i] == target[j]
      prefix[i] = j
    end
    matched = 0
    (0...(2 * k - 1)).each do |i|
      x = block[i % k]
      matched = prefix[matched - 1] while matched > 0 && x != target[matched]
      matched += 1 if x == target[matched]
      return true if matched == k
    end
    false
  end
  n = nums.length
  sorted_nums = nums.sort
  divisors = []
  d = 1
  while d * d <= n
    if n % d == 0
      divisors << d
      divisors << n / d if d * d != n
    end
    d += 1
  end
  answer = 0
  divisors.each do |k|
    ok = true
    (0...n).step(k) do |start|
      block = nums[start, k]
      target = sorted_nums[start, k]
      unless rotation_matches.call(block, target)
        ok = false
        break
      end
    end
    answer += k if ok
  end
  answer
end
''')

add("3887_incremental_even_weighted_cycle_queries", r'''
# LeetCode 3887 - Incremental Even-Weighted Cycle Queries
# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_valid_edges(n, edges)
  parent = (0...n).to_a
  size = Array.new(n, 1)
  parity = Array.new(n, 0)
  find = nil
  find = lambda do |x|
    return [x, 0] if parent[x] == x
    root, p = find.call(parent[x])
    parity[x] ^= p
    parent[x] = root
    [root, parity[x]]
  end
  ans = 0
  edges.each do |e|
    ru, pu = find.call(e[0])
    rv, pv = find.call(e[1])
    if ru == rv
      ans += 1 if (pu ^ pv) == e[2]
      next
    end
    if size[ru] < size[rv]
      ru, rv = rv, ru
      pu, pv = pv, pu
    end
    parent[rv] = ru
    parity[rv] = pu ^ pv ^ e[2]
    size[ru] += size[rv]
    ans += 1
  end
  ans
end
''')

add("3888_minimum_operations_to_make_all_grid_elements_equal", r'''
# LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def min_operations(grid, k)
  m = grid.length
  n = grid[0].length
  max_val = grid[0][0]
  grid.each { |row| row.each { |x| max_val = [max_val, x].max } }
  check = lambda do |target|
    diff = Array.new(m + 2) { Array.new(n + 2, 0) }
    total_ops = 0
    (1..m).each do |i|
      (1..n).each do |j|
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        cur_val = grid[i - 1][j - 1] + diff[i][j]
        return -1 if cur_val > target
        if cur_val < target
          return -1 if i + k - 1 > m || j + k - 1 > n
          needed = target - cur_val
          total_ops += needed
          diff[i][j] += needed
          diff[i + k][j] -= needed
          diff[i][j + k] -= needed
          diff[i + k][j + k] += needed
        end
      end
    end
    total_ops
  end
  (max_val..(max_val + 1)).each do |t|
    res = check.call(t)
    return res if res != -1
  end
  -1
end
''')

add("3889_mirror_frequency_distance", r'''
# LeetCode 3889 - Mirror Frequency Distance
# https://leetcode.com/problems/mirror-frequency-distance/

# @param {String} s
# @return {Integer}
def mirror_frequency(s)
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  ans = 0
  vis = {}
  freq.each do |c, v|
    m = if c >= "a" && c <= "z"
          (97 + 25 - (c.ord - 97)).chr
        else
          (48 + (9 - (c.ord - 48))).chr
        end
    next if vis[m] == true
    vis[c] = true
    ans += (v - freq[m]).abs
  end
  ans
end
''')

add("3890_integers_with_multiple_sum_of_two_cubes", r'''
# LeetCode 3890 - Integers With Multiple Sum of Two Cubes
# https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

$good3890 = nil

def init3890
  return unless $good3890.nil?
  limit = 1_000_000_000
  cnt = Hash.new(0)
  cubes = Array.new(1001, 0)
  1001.times { |i| cubes[i] = i * i * i }
  (1..1000).each do |a|
    (a..1000).each do |b|
      x = cubes[a] + cubes[b]
      break if x > limit
      cnt[x] += 1
    end
  end
  $good3890 = []
  cnt.each { |k, v| $good3890 << k if v > 1 }
  $good3890.sort!
end

# @param {Integer} n
# @return {Integer[]}
def find_good_integers(n)
  init3890
  lo = 0
  hi = $good3890.length
  while lo < hi
    mid = (lo + hi) / 2
    if $good3890[mid] <= n
      lo = mid + 1
    else
      hi = mid
    end
  end
  $good3890[0, lo]
end
''')

add("3891_minimum_increase_to_maximize_special_indices", r'''
# LeetCode 3891 - Minimum Increase to Maximize Special Indices
# https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

# @param {Integer[]} nums
# @return {Integer}
def min_increase(nums)
  n = nums.length
  f = Array.new(n) { [-1, -1] }
  dfs = nil
  dfs = lambda do |i, j|
    return 0 if i >= n - 1
    return f[i][j] if f[i][j] != -1
    cost = [0, [nums[i - 1], nums[i + 1]].max + 1 - nums[i]].max
    ans = cost + dfs.call(i + 2, j)
    ans = [ans, dfs.call(i + 1, 0)].min if j > 0
    f[i][j] = ans
    ans
  end
  dfs.call(1, (n & 1) ^ 1)
end
''')

add("3892_minimum_operations_to_achieve_at_least_k_peaks", r'''
# LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

INF3892 = (1 << 53) / 4

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  n = nums.length
  return 0 if k == 0
  return -1 if k > n / 2
  cost = Array.new(n, 0)
  n.times do |i|
    left = nums[(i + n - 1) % n]
    right = nums[(i + 1) % n]
    need = [left, right].max
    cost[i] = need - nums[i] + 1 if need >= nums[i]
  end
  line = lambda do |left, right, choose|
    return 0 if choose == 0
    return INF3892 if left > right || choose > (right - left + 2) / 2
    prev2 = Array.new(choose + 1, INF3892)
    prev1 = Array.new(choose + 1, INF3892)
    prev2[0] = prev1[0] = 0
    (left..right).each do |i|
      current = prev1.dup
      (1..choose).each do |j|
        if prev2[j - 1] != INF3892 && prev2[j - 1] + cost[i] < current[j]
          current[j] = prev2[j - 1] + cost[i]
        end
      end
      prev2 = prev1
      prev1 = current
    end
    prev1[choose]
  end
  answer = line.call(1, n - 1, k)
  with_first = line.call(2, n - 2, k - 1)
  if with_first != INF3892
    with_first += cost[0]
    answer = [answer, with_first].min
  end
  return -1 if answer == INF3892
  answer
end
''')

add("3893_maximum_team_size_with_overlapping_intervals", r'''
# LeetCode 3893 - Maximum Team Size with Overlapping Intervals
# https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def maximum_team_size(start_time, end_time)
  upper_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  n = start_time.length
  st = start_time.sort
  en = end_time.sort
  ans = 0
  n.times do |t|
    l = start_time[t]
    r = end_time[t]
    i = upper_bound.call(en, l - 1)
    j = upper_bound.call(st, r)
    ans = [ans, j - i].max
  end
  ans
end
''')

add("3894_traffic_signal_color", r'''
# LeetCode 3894 - Traffic Signal Color
# https://leetcode.com/problems/traffic-signal-color/

# @param {Integer} timer
# @return {String}
def traffic_signal(timer)
  return "Green" if timer == 0
  return "Orange" if timer == 30
  return "Red" if timer > 30 && timer <= 90
  "Invalid"
end
''')

add("3895_count_digit_appearances", r'''
# LeetCode 3895 - Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/

# @param {Integer[]} nums
# @param {Integer} digit
# @return {Integer}
def count_digit_occurrences(nums, digit)
  ans = 0
  nums.each do |num|
    x = num
    while x > 0
      ans += 1 if x % 10 == digit
      x /= 10
    end
  end
  ans
end
''')

add("3896_minimum_operations_to_transform_array_into_alternating_prime", r'''
# LeetCode 3896 - Minimum Operations to Transform Array into Alternating Prime
# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

MX3896 = 200000
$is_prime3896 = nil
$primes3896 = nil

def init3896
  return unless $is_prime3896.nil?
  $is_prime3896 = Array.new(MX3896 + 1, true)
  $is_prime3896[0] = $is_prime3896[1] = false
  i = 2
  while i * i <= MX3896
    if $is_prime3896[i]
      j = i * i
      while j <= MX3896
        $is_prime3896[j] = false
        j += i
      end
    end
    i += 1
  end
  $primes3896 = []
  (2..MX3896).each { |x| $primes3896 << x if $is_prime3896[x] }
end

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  init3896
  ans = 0
  nums.each_with_index do |x, i|
    if i.even?
      lo = 0
      hi = $primes3896.length
      while lo < hi
        mid = (lo + hi) >> 1
        if $primes3896[mid] < x
          lo = mid + 1
        else
          hi = mid
        end
      end
      ans += $primes3896[lo] - x
    elsif $is_prime3896[x]
      ans += x == 2 ? 2 : 1
    end
  end
  ans
end
''')

add("3897_maximum_value_of_concatenated_binary_segments", r'''
# LeetCode 3897 - Maximum Value of Concatenated Binary Segments
# https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

MOD3897 = 1_000_000_007

def group3897(p)
  return 0 if p[1] == 0
  p[0] > 0 ? 1 : 2
end

# @param {Integer[]} nums1
# @param {Integer[]} nums0
# @return {Integer}
def max_value(nums1, nums0)
  n = nums1.length
  pairs = n.times.map { |i| [nums1[i], nums0[i]] }
  b = 0
  n.times { |i| b += nums1[i] + nums0[i] }
  pairs.sort_by! do |a|
    g = group3897(a)
    second = if g == 0
               -a[0]
             elsif g == 1
               -a[0]
             else
               a[1]
             end
    third = g == 1 ? a[1] : 0
    [g, second, third]
  end
  p = Array.new(b, 0)
  p[0] = 1
  (1...b).each { |i| p[i] = (2 * p[i - 1]) % MOD3897 }
  ans = 0
  b -= 1
  pairs.each do |pr|
    cnt1, cnt0 = pr[0], pr[1]
    while cnt1 > 0
      ans = (ans + p[b]) % MOD3897
      b -= 1
      cnt1 -= 1
    end
    b -= cnt0
  end
  ans
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch21_c written={written}")


if __name__ == "__main__":
    main()
