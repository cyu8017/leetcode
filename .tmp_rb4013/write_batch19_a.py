#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3612_process_string_with_special_operations_i", r'''
# LeetCode 3612 - Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/

# @param {String} s
# @return {String}
def process_str(s)
  result = []
  s.each_char do |c|
    if c =~ /[a-zA-Z]/
      result << c
    elsif c == "*"
      result.pop unless result.empty?
    elsif c == "#"
      result += result
    elsif c == "%"
      result.reverse!
    end
  end
  result.join
end
''')

add("3613_minimize_maximum_component_cost", r'''
# LeetCode 3613 - Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_cost(n, edges, k)
  p = (0...n).to_a
  find = nil
  find = lambda do |x|
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end
  return 0 if k == n

  edges = edges.sort_by { |e| e[2] }
  cnt = n
  edges.each do |e|
    pu = find.call(e[0])
    pv = find.call(e[1])
    if pu != pv
      p[pu] = pv
      cnt -= 1
      return e[2] if cnt <= k
    end
  end
  0
end
''')

add("3614_process_string_with_special_operations_ii", r'''
# LeetCode 3614 - Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def process_str(s, k)
  m = 0
  s.each_char do |c|
    if c == "*"
      m = m > 0 ? m - 1 : 0
    elsif c == "#"
      m <<= 1
    elsif c != "%"
      m += 1
    end
  end
  k2 = k
  return "." if k2 >= m

  i = s.length - 1
  loop do
    c = s[i]
    if c == "*"
      m += 1
    elsif c == "#"
      m /= 2
      k2 -= m if k2 >= m
    elsif c == "%"
      k2 = m - 1 - k2
    else
      m -= 1
      return c if k2 == m
    end
    i -= 1
  end
end
''')

add("3615_longest_palindromic_path_in_graph", r'''
# LeetCode 3615 - Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} label
# @return {Integer}
def max_len(n, edges, label)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end

  pack = lambda { |a, b| (a << 32) | (b & 0xFFFFFFFF) }

  expand_pal = lambda do |l, r|
    vis = {}
    q = []
    len0 = l != r ? 2 : 1
    q << [l, r, len0]
    best = len0
    vis[pack.call([l, r].min, [l, r].max)] = true
    until q.empty?
      cur0, cur1, cur2 = q.shift
      g[cur0].each do |a|
        g[cur1].each do |b|
          next if a == b || label[a] != label[b]

          p = pack.call([a, b].min, [a, b].max)
          next if vis[p]

          vis[p] = true
          nl = cur2 + 2
          best = nl if nl > best
          q << [a, b, nl]
        end
      end
    end
    best
  end

  ans = 1
  (0...n).each do |i|
    v = expand_pal.call(i, i)
    ans = v if v > ans
    g[i].each do |j|
      if i < j && label[i] == label[j]
        v = expand_pal.call(i, j)
        ans = v if v > ans
      end
    end
  end
  ans
end
''')

add("3616_number_of_student_replacements", r'''
# LeetCode 3616 - Number of Student Replacements
# https://leetcode.com/problems/number-of-student-replacements/

# @param {Integer[]} ranks
# @return {Integer}
def total_replacements(ranks)
  ans = 0
  cur = ranks[0]
  ranks.each do |x|
    if x < cur
      cur = x
      ans += 1
    end
  end
  ans
end
''')

add("3618_split_array_by_prime_indices", r'''
# LeetCode 3618 - Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/

# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)
  pr = primes3618
  ans = 0
  nums.each_with_index do |x, i|
    ans += pr[i] ? x : -x
  end
  ans.abs
end

def primes3618
  return $primes3618 if defined?($primes3618) && $primes3618

  m = 100010
  primes = Array.new(m, true)
  primes[0] = primes[1] = false
  (2...m).each do |i|
    next unless primes[i]

    (i + i...m).step(i) { |j| primes[j] = false }
  end
  $primes3618 = primes
end
''')

add("3619_count_islands_with_total_value_divisible_by_k", r'''
# LeetCode 3619 - Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_islands(grid, k)
  m = grid.length
  n = grid[0].length
  dirs = [-1, 0, 1, 0, -1]
  dfs = nil
  dfs = lambda do |i, j|
    s = grid[i][j]
    grid[i][j] = 0
    4.times do |d|
      x = i + dirs[d]
      y = j + dirs[d + 1]
      s += dfs.call(x, y) if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0
    end
    s
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      ans += 1 if grid[i][j] > 0 && dfs.call(i, j) % k == 0
    end
  end
  ans
end
''')

add("3620_network_recovery_pathways", r'''
# LeetCode 3620 - Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/

# @param {Integer[][]} edges
# @param {Boolean[]} online
# @param {Integer} k
# @return {Integer}
def find_max_path_score(edges, online, k)
  n = online.length
  g = Array.new(n) { [] }
  l = 2147483647
  r = 0
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    next if !online[u] || !online[v]

    g[u] << [v, w]
    l = w if w < l
    r = w if w > r
  end
  return -1 if l == 2147483647

  check = lambda do |mid|
    inf = 1073741823
    dist = Array.new(n, inf)
    dist[0] = 0
    pq = [[0, 0]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      return false if d > k
      return true if u == n - 1
      next if dist[u] < d

      g[u].each do |v, w|
        next if w < mid

        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          pq << [nd, v]
        end
      end
    end
    false
  end

  while l < r
    mid = (l + r + 1) >> 1
    if check.call(mid)
      l = mid
    else
      r = mid - 1
    end
  end
  check.call(l) ? l : -1
end
''')

add("3621_number_of_integers_with_popcount_depth_equal_to_k_i", r'''
# LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def popcount_depth(n, k)
  return n >= 1 ? 1 : 0 if k == 0

  bit_count = lambda do |x|
    c = 0
    while x > 0
      c += x & 1
      x >>= 1
    end
    c
  end

  depth = lambda do |x|
    return 100 if x <= 0

    d = 0
    while x > 1
      x = bit_count.call(x)
      d += 1
    end
    d
  end

  bits = []
  x = n
  while x > 0
    bits << (x & 1).to_s
    x /= 2
  end
  s = bits.empty? ? "0" : bits.reverse.join
  memo = {}
  dfs = nil
  dfs = lambda do |pos, tight, started, pc|
    if pos == s.length
      return 0 if started == 0
      return k == 1 ? 1 : 0 if pc == 1

      return depth.call(pc) == k - 1 ? 1 : 0
    end
    key = [pos, tight, started, pc]
    return memo[key] if memo.key?(key)

    up = tight == 1 ? s[pos].to_i : 1
    res = 0
    (0..up).each do |dig|
      nt = tight == 1 && dig == up ? 1 : 0
      res += if started == 0 && dig == 0
               dfs.call(pos + 1, nt, 0, 0)
             else
               dfs.call(pos + 1, nt, 1, pc + dig)
             end
    end
    memo[key] = res
    res
  end
  dfs.call(0, 1, 0, 0)
end
''')

add("3622_check_divisibility_by_digit_sum_and_product", r'''
# LeetCode 3622 - Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

# @param {Integer} n
# @return {Boolean}
def check_divisibility(n)
  s = 0
  p = 1
  x = n
  while x != 0
    v = x % 10
    x /= 10
    s += v
    p *= v
  end
  n % (s + p) == 0
end
''')

add("3623_count_number_of_trapezoids_i", r'''
# LeetCode 3623 - Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/

# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
  mod = 1_000_000_007
  cnt = Hash.new(0)
  points.each { |p| cnt[p[1]] += 1 }
  ans = 0
  pre = 0
  cnt.each_value do |c|
    lines = c * (c - 1) / 2
    ans = (ans + pre * lines) % mod
    pre = (pre + lines) % mod
  end
  ans
end
''')

add("3624_number_of_integers_with_popcount_depth_equal_to_k_ii", r'''
# LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def popcount_depth(nums, queries)
  bit_count = lambda do |x|
    c = 0
    v = x
    while v > 0
      c += v & 1
      v >>= 1
    end
    c
  end
  depth = lambda do |x|
    v = x
    return 0 if v == 1

    d = 0
    while v > 1
      v = bit_count.call(v)
      d += 1
    end
    d
  end
  a = nums.dup
  ans = []
  queries.each do |q|
    if q[0] == 1
      l, r, k = q[1], q[2], q[3]
      cnt = 0
      (l..r).each { |i| cnt += 1 if depth.call(a[i]) == k }
      ans << cnt
    else
      a[q[1]] = q[2]
    end
  end
  ans
end
''')

add("3625_count_number_of_trapezoids_ii", r'''
# LeetCode 3625 - Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii/

# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
  n = points.length
  cnt1 = {}
  cnt2 = {}
  get_or = lambda do |m, k|
    m[k] ||= {}
    m[k]
  end
  (0...n).each do |i|
    x1, y1 = points[i][0], points[i][1]
    (0...i).each do |j|
      x2, y2 = points[j][0], points[j][1]
      dx = x2 - x1
      dy = y2 - y1
      if dx == 0
        k = 1e9
        b = x1
      else
        k = dy.to_f / dx
        b = (y1 * dx - x1 * dy).to_f / dx
      end
      m1 = get_or.call(cnt1, k)
      m1[b] = (m1[b] || 0) + 1
      p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
      m2 = get_or.call(cnt2, p)
      m2[k] = (m2[k] || 0) + 1
    end
  end
  ans = 0
  cnt1.each_value do |e|
    s = 0
    e.each_value do |t|
      ans += s * t
      s += t
    end
  end
  cnt2.each_value do |e|
    s = 0
    e.each_value do |t|
      ans -= s * t
      s += t
    end
  end
  ans
end
''')

add("3627_maximum_median_sum_of_subsequences_of_size_3", r'''
# LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

# @param {Integer[]} nums
# @return {Integer}
def maximum_median_sum(nums)
  nums = nums.sort
  n = nums.length
  ans = 0
  (n / 3...n).step(2) { |i| ans += nums[i] }
  ans
end
''')

add("3628_maximum_number_of_subsequences_after_one_inserting", r'''
# LeetCode 3628 - Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

# @param {String} s
# @return {Integer}
def num_of_subsequences(s)
  calc = lambda do |st, t|
    cnt = 0
    a = 0
    st.each_char do |c|
      cnt += a if c == t[1]
      a += 1 if c == t[0]
    end
    cnt
  end
  l = 0
  r = 0
  s.each_char { |c| r += 1 if c == "T" }
  ans = 0
  mx = 0
  s.each_char do |c|
    r -= 1 if c == "T"
    ans += l * r if c == "C"
    l += 1 if c == "L"
    mx = l * r if l * r > mx
  end
  mx = [mx, calc.call(s, "LC"), calc.call(s, "CT")].max
  ans + mx
end
''')

add("3629_minimum_jumps_to_reach_end_via_prime_teleportation", r'''
# LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

# @param {Integer[]} nums
# @return {Integer}
def min_jumps(nums)
  fac = factors3629
  n = nums.length
  g = {}
  nums.each_with_index do |v, i|
    fac[v].each do |p|
      (g[p] ||= []) << i
    end
  end
  ans = 0
  vis = Array.new(n, false)
  vis[0] = true
  q = [0]
  loop do
    nq = []
    q.each do |i|
      return ans if i == n - 1

      idx = (g[nums[i]] || []).dup
      idx << i + 1
      idx << i - 1 if i > 0
      idx.each do |j|
        if j >= 0 && j < n && !vis[j]
          vis[j] = true
          nq << j
        end
      end
      g[nums[i]] = []
    end
    q = nq
    ans += 1
  end
end

def factors3629
  return $factors3629 if defined?($factors3629) && $factors3629

  mx = 1_000_001
  factors = Array.new(mx) { [] }
  (2...mx).each do |i|
    next unless factors[i].empty?

    i.step(mx - 1, i) { |j| factors[j] << i }
  end
  $factors3629 = factors
end
''')

add("3630_partition_array_for_maximum_xor_and_and", r'''
# LeetCode 3630 - Partition Array for Maximum XOR and AND
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

# @param {Integer[]} nums
# @return {Integer}
def maximize_xor_and_xor(nums)
  n = nums.length
  best = 0
  (0...(1 << n)).each do |mask|
    and_val = -1
    xor_rest = 0
    (0...n).each do |i|
      if ((mask >> i) & 1) != 0
        and_val = and_val < 0 ? nums[i] : (and_val & nums[i])
      else
        xor_rest ^= nums[i]
      end
    end
    and_val = 0 if and_val < 0
    comp = ((1 << n) - 1) ^ mask
    sub = comp
    loop do
      x1 = 0
      (0...n).each { |i| x1 ^= nums[i] if ((sub >> i) & 1) != 0 }
      x2 = xor_rest ^ x1
      v = and_val + x1 + x2
      best = v if v > best
      break if sub == 0

      sub = (sub - 1) & comp
    end
  end
  best
end
''')

add("3631_sort_threats_by_severity_and_exploitability", r'''
# LeetCode 3631 - Sort Threats by Severity and Exploitability
# https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

# @param {Integer[][]} threats
# @return {Integer[][]}
def sort_threats(threats)
  threats.sort_by { |a| [-(2 * a[1] + a[2]), a[0]] }
end
''')

add("3632_subarrays_with_xor_at_least_k", r'''
# LeetCode 3632 - Subarrays With XOR At Least K
# https://leetcode.com/problems/subarrays-with-xor-at-least-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_with_xor_at_least_k(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    x = 0
    (i...n).each do |j|
      x ^= nums[j]
      ans += 1 if x >= k
    end
  end
  ans
end
''')

add("3633_earliest_finish_time_for_land_and_water_rides_i", r'''
# LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

# @param {Integer[]} land_start_time
# @param {Integer[]} land_duration
# @param {Integer[]} water_start_time
# @param {Integer[]} water_duration
# @return {Integer}
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  calc = lambda do |a1, t1, a2, t2|
    min_end = (0...a1.length).map { |i| a1[i] + t1[i] }.min
    (0...a2.length).map { |i| [min_end, a2[i]].max + t2[i] }.min
  end
  [
    calc.call(land_start_time, land_duration, water_start_time, water_duration),
    calc.call(water_start_time, water_duration, land_start_time, land_duration)
  ].min
end
''')

add("3634_minimum_removals_to_balance_array", r'''
# LeetCode 3634 - Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_removal(nums, k)
  nums = nums.sort
  n = nums.length
  lower_bound = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  cnt = 0
  (0...n).each do |i|
    j = n
    if nums[i] * k <= nums[n - 1]
      target = nums[i] * k + 1
      j = lower_bound.call(nums, target)
    end
    cnt = j - i if j - i > cnt
  end
  n - cnt
end
''')

add("3635_earliest_finish_time_for_land_and_water_rides_ii", r'''
# LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

# @param {Integer[]} land_start_time
# @param {Integer[]} land_duration
# @param {Integer[]} water_start_time
# @param {Integer[]} water_duration
# @return {Integer}
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  calc = lambda do |a1, t1, a2, t2|
    min_end = (0...a1.length).map { |i| a1[i] + t1[i] }.min
    (0...a2.length).map { |i| [min_end, a2[i]].max + t2[i] }.min
  end
  [
    calc.call(land_start_time, land_duration, water_start_time, water_duration),
    calc.call(water_start_time, water_duration, land_start_time, land_duration)
  ].min
end
''')

add("3636_threshold_majority_queries", r'''
# LeetCode 3636 - Threshold Majority Queries
# https://leetcode.com/problems/threshold-majority-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def subarray_majority(nums, queries)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r, t), qi|
    cnt = Hash.new(0)
    (l..r).each { |i| cnt[nums[i]] += 1 }
    best = -1
    best_c = 0
    cnt.each do |v, c|
      if c >= t && (c > best_c || (c == best_c && (best == -1 || v < best)))
        best_c = c
        best = v
      end
    end
    ans[qi] = best
  end
  ans
end
''')

add("3637_trionic_array_i", r'''
# LeetCode 3637 - Trionic Array I
# https://leetcode.com/problems/trionic-array-i/

# @param {Integer[]} nums
# @return {Boolean}
def is_trionic(nums)
  n = nums.length
  p = 0
  p += 1 while p < n - 2 && nums[p] < nums[p + 1]
  return false if p == 0

  q = p
  q += 1 while q < n - 1 && nums[q] > nums[q + 1]
  return false if q == p || q == n - 1

  q += 1 while q < n - 1 && nums[q] < nums[q + 1]
  q == n - 1
end
''')

add("3638_maximum_balanced_shipments", r'''
# LeetCode 3638 - Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/

# @param {Integer[]} weight
# @return {Integer}
def max_balanced_shipments(weight)
  ans = 0
  mx = 0
  weight.each do |x|
    mx = x if x > mx
    if x < mx
      ans += 1
      mx = 0
    end
  end
  ans
end
''')

if __name__ == "__main__":
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch A written={written}")
