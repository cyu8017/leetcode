#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3504_longest_palindrome_after_substring_concatenation_ii", r'''
# LeetCode 3504 - Longest Palindrome After Substring Concatenation II
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_palindrome(s, t)
  expand = lambda do |str, g, l, r|
    while l >= 0 && r < str.length && str[l] == str[r]
      g[l] = [g[l], r - l + 1].max
      l -= 1
      r += 1
    end
  end
  calc = lambda do |str|
    n = str.length
    g = Array.new(n, 0)
    (0...n).each do |i|
      expand.call(str, g, i, i)
      expand.call(str, g, i, i + 1)
    end
    g
  end
  m = s.length
  n = t.length
  t = t.reverse
  g1 = calc.call(s)
  g2 = calc.call(t)
  ans = 0
  g1.each { |v| ans = [ans, v].max }
  g2.each { |v| ans = [ans, v].max }
  f = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each do |i|
    (1..n).each do |j|
      next unless s[i - 1] == t[j - 1]
      f[i][j] = f[i - 1][j - 1] + 1
      a = i < m ? g1[i] : 0
      b = j < n ? g2[j] : 0
      ans = [ans, f[i][j] * 2 + a].max
      ans = [ans, f[i][j] * 2 + b].max
    end
  end
  ans
end
''')

add("3505_minimum_operations_to_make_elements_within_k_subarrays_equal", r'''
# LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

# @param {Integer[]} nums
# @param {Integer} x
# @param {Integer} k
# @return {Integer}
def min_operations(nums, x, k)
  n = nums.length
  min_ops = Array.new(n - x + 1, 0)
  (0..(n - x)).each do |i|
    w = nums[i, x].sort
    med = w[(x - 1) / 2]
    ops = 0
    w.each { |v| ops += (v - med).abs }
    min_ops[i] = ops
  end
  inf = 10**18
  dp = Array.new(n + 1) { Array.new(k + 1, inf) }
  dp[n][0] = 0
  (n - 1).downto(0) do |i|
    (0..k).each do |j|
      dp[i][j] = dp[i + 1][j]
      if j > 0 && i + x <= n && min_ops[i] + dp[i + x][j - 1] < dp[i][j]
        dp[i][j] = min_ops[i] + dp[i + x][j - 1]
      end
    end
  end
  dp[0][k]
end
''')

add("3506_find_time_required_to_eliminate_bacterial_strains", r'''
# LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

# @param {Integer[]} time_req
# @param {Integer} split_time
# @return {Integer}
def min_elimination_time(time_req, split_time)
  pq = time_req.sort
  while pq.length > 1
    pq.shift
    x = pq.shift
    v = x + split_time
    lo = 0
    hi = pq.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pq[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    pq.insert(lo, v)
  end
  pq[0]
end
''')

add("3507_minimum_pair_removal_to_sort_array_i", r'''
# LeetCode 3507 - Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
  is_non_decreasing = lambda do |a|
    (1...a.length).each { |i| return false if a[i] < a[i - 1] }
    true
  end
  arr = nums.dup
  ans = 0
  until is_non_decreasing.call(arr)
    k = 0
    s = arr[0] + arr[1]
    (1...(arr.length - 1)).each do |i|
      t = arr[i] + arr[i + 1]
      if s > t
        s = t
        k = i
      end
    end
    arr[k] = s
    arr.delete_at(k + 1)
    ans += 1
  end
  ans
end
''')

add("3508_implement_router", r'''
# LeetCode 3508 - Implement Router
# https://leetcode.com/problems/implement-router/

class Router
  def initialize(memory_limit)
    @lim = memory_limit
    @vis = {}
    @q = []
    @idx = {}
    @d = {}
  end

  def f(a, b, c)
    (a << 46) | (b << 29) | c
  end

  def add_packet(source, destination, timestamp)
    x = f(source, destination, timestamp)
    return false if @vis[x]
    @vis[x] = true
    forward_packet if @q.length >= @lim
    @q << [source, destination, timestamp]
    @d[destination] ||= []
    @d[destination] << timestamp
    true
  end

  def forward_packet
    return [] if @q.empty?
    packet = @q.shift
    s, dest, t = packet[0], packet[1], packet[2]
    @vis.delete(f(s, dest, t))
    @idx[dest] = (@idx[dest] || 0) + 1
    [s, dest, t]
  end

  def get_count(destination, start_time, end_time)
    ls = @d[destination]
    return 0 unless ls
    k = @idx[destination] || 0
    lower_bound(ls, k, end_time + 1) - lower_bound(ls, k, start_time)
  end

  def lower_bound(a, frm, target)
    lo = frm
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
end
''')

add("3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k", r'''
# LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} limit
# @return {Integer}
def max_product(nums, k, limit)
  minv = -5000
  memo = {}
  sum_all = 0
  nums.each { |v| sum_all += v }
  return -1 if k.abs > sum_all

  dp = nil
  dp = lambda do |i, product, state, kk|
    if i == nums.length
      return (kk == 0 && state != 0 && product <= limit) ? product : minv
    end
    key = [i, product, state, kk]
    return memo[key] if memo.key?(key)
    res = dp.call(i + 1, product, state, kk)
    if state == 0
      res = [res, dp.call(i + 1, nums[i], 1, kk - nums[i])].max
    end
    if state == 1
      np = product * nums[i]
      np = limit + 1 if np > limit + 1
      res = [res, dp.call(i + 1, np, 2, kk + nums[i])].max
    end
    if state == 2
      np = product * nums[i]
      np = limit + 1 if np > limit + 1
      res = [res, dp.call(i + 1, np, 1, kk - nums[i])].max
    end
    memo[key] = res
    res
  end
  ans = dp.call(0, 1, 0, k)
  ans == minv ? -1 : ans
end
''')

add("3510_minimum_pair_removal_to_sort_array_ii", r'''
# LeetCode 3510 - Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
  n = nums.length
  inv = 0
  ans = 0
  sl = []
  idx = {}
  (0...n).each { |i| idx[i] = true }
  sl_map = {}

  key = lambda { |sm, i| sm * 1000000007 + i }

  add_sl = lambda do |sm, i|
    sl_map[key.call(sm, i)] = [sm, i]
    lo = 0
    hi = sl.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sl[mid][0] < sm || (sl[mid][0] == sm && sl[mid][1] < i)
        lo = mid + 1
      else
        hi = mid
      end
    end
    sl.insert(lo, [sm, i])
  end

  rem_sl = lambda do |sm, i|
    k = key.call(sm, i)
    return unless sl_map.key?(k)
    sl_map.delete(k)
    (0...sl.length).each do |t|
      if sl[t][0] == sm && sl[t][1] == i
        sl.delete_at(t)
        break
      end
    end
  end

  ceiling = lambda do |st, x|
    best = nil
    st.each_key do |v|
      best = v if v >= x && (best.nil? || v < best)
    end
    best
  end

  floor = lambda do |st, x|
    best = nil
    st.each_key do |v|
      best = v if v <= x && (best.nil? || v > best)
    end
    best
  end

  (0...(n - 1)).each do |i|
    inv += 1 if nums[i] > nums[i + 1]
    add_sl.call(nums[i] + nums[i + 1], i)
  end
  while inv > 0
    ans += 1
    p = sl.shift
    sl_map.delete(key.call(p[0], p[1]))
    s = p[0]
    i = p[1]
    j = ceiling.call(idx, i + 1)
    inv -= 1 if nums[i] > nums[j]
    h = floor.call(idx, i - 1)
    unless h.nil?
      inv -= 1 if nums[h] > nums[i]
      rem_sl.call(nums[h] + nums[i], h)
      inv += 1 if nums[h] > s
      add_sl.call(nums[h] + s, h)
    end
    kk = ceiling.call(idx, j + 1)
    unless kk.nil?
      inv -= 1 if nums[j] > nums[kk]
      rem_sl.call(nums[j] + nums[kk], j)
      inv += 1 if s > nums[kk]
      add_sl.call(s + nums[kk], i)
    end
    nums[i] = s
    idx.delete(j)
  end
  ans
end
''')

add("3511_make_a_positive_array", r'''
# LeetCode 3511 - Make a Positive Array
# https://leetcode.com/problems/make-a-positive-array/

# @param {Integer[]} nums
# @return {Integer}
def make_array_positive(nums)
  ans = 0
  l = -1
  pre_mx = 0
  s = 0
  (0...nums.length).each do |r|
    s += nums[r]
    if r - l > 2 && s <= pre_mx
      ans += 1
      l = r
      pre_mx = 0
      s = 0
    elsif r - l >= 2
      pre_mx = [pre_mx, s - nums[r] - nums[r - 1]].max
    end
  end
  ans
end
''')

add("3512_minimum_operations_to_make_array_sum_divisible_by_k", r'''
# LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  ans = 0
  nums.each { |x| ans = (ans + x) % k }
  ans
end
''')

add("3513_number_of_unique_xor_triplets_i", r'''
# LeetCode 3513 - Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  n = nums.length
  return n if n <= 2
  x = n
  length = 0
  while x != 0
    length += 1
    x >>= 1
  end
  1 << length
end
''')

add("3514_number_of_unique_xor_triplets_ii", r'''
# LeetCode 3514 - Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  mx = 0
  nums.each { |v| mx = [mx, v].max }
  mx <<= 1
  st = Array.new(mx, false)
  nums.each do |a|
    nums.each { |b| st[a ^ b] = true }
  end
  s = Array.new(mx, 0)
  (0...mx).each do |ab|
    next unless st[ab]
    nums.each { |c| s[ab ^ c] = 1 }
  end
  ans = 0
  s.each { |v| ans += v }
  ans
end
''')

add("3515_shortest_path_in_a_weighted_tree", r'''
# LeetCode 3515 - Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def tree_queries(n, edges, queries)
  g = Array.new(n + 1) { [] }
  weight = {}
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    g[u] << [v, w]
    g[v] << [u, w]
    a = [u, v].min
    b = [u, v].max
    weight[(a << 32) | b] = w
  end
  in_t = Array.new(n + 1, 0)
  out_t = Array.new(n + 1, 0)
  dist = Array.new(n + 1, 0)
  parent = Array.new(n + 1, 0)
  time = [0]
  dfs = nil
  dfs = lambda do |u, p|
    in_t[u] = time[0]
    time[0] += 1
    g[u].each do |to, w|
      next if to == p
      parent[to] = u
      dist[to] = dist[u] + w
      dfs.call(to, u)
    end
    out_t[u] = time[0] - 1
  end
  dfs.call(1, 0)
  bit = Array.new(n + 2, 0)
  add = lambda do |i, v|
    while i <= n
      bit[i] += v
      i += i & -i
    end
  end
  range_add = lambda do |l, r, v|
    add.call(l + 1, v)
    add.call(r + 2, -v)
  end
  point = lambda do |i|
    s = 0
    i += 1
    while i > 0
      s += bit[i]
      i -= i & -i
    end
    s
  end
  (1..n).each { |i| range_add.call(in_t[i], in_t[i], dist[i]) }
  ans = []
  queries.each do |q|
    if q[0] == 1
      u, v, nw = q[1], q[2], q[3]
      a = [u, v].min
      b = [u, v].max
      key = (a << 32) | b
      ow = weight[key]
      delta = nw - ow
      weight[key] = nw
      child = parent[u] == v ? u : v
      range_add.call(in_t[child], out_t[child], delta)
    else
      ans << point.call(in_t[q[1]])
    end
  end
  ans
end
''')

add("3516_find_closest_person", r'''
# LeetCode 3516 - Find Closest Person
# https://leetcode.com/problems/find-closest-person/

# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def find_closest(x, y, z)
  a = (x - z).abs
  b = (y - z).abs
  return 0 if a == b
  a < b ? 1 : 2
end
''')

add("3517_smallest_palindromic_rearrangement_i", r'''
# LeetCode 3517 - Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

# @param {String} s
# @return {String}
def smallest_palindrome(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  t = ""
  ch = ""
  (0...26).each do |i|
    c = (97 + i).chr
    v = cnt[i] / 2
    t += c * v
    cnt[i] -= v * 2
    ch = c if cnt[i] == 1
  end
  sb = t
  sb += ch unless ch.empty?
  (t.length - 1).downto(0) { |i| sb += t[i] }
  sb
end
''')

add("3518_smallest_palindromic_rearrangement_ii", r'''
# LeetCode 3518 - Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_palindrome(s, k)
  maxv = 1000001
  nck = lambda do |n, kk|
    return 0 if kk < 0 || kk > n
    res = 1
    kk = n - kk if kk > n - kk
    (1..kk).each do |i|
      res = res * (n - i + 1) / i
      return maxv if res >= maxv
    end
    res
  end
  count_arr = lambda do |h|
    total = 0
    h.each { |f| total += f }
    res = 1
    h.each do |f|
      res *= nck.call(total, f)
      return maxv if res >= maxv
      total -= f
    end
    res
  end
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  odd = 0
  cnt.each { |c| odd += 1 if c.odd? }
  return "" if odd > 1
  half = Array.new(26, 0)
  mid = ""
  (0...26).each do |i|
    half[i] = cnt[i] / 2
    mid = (97 + i).chr if cnt[i].odd?
  end
  return "" if count_arr.call(half) < k
  half_len = 0
  half.each { |f| half_len += f }
  left = ""
  half_len.times do
    (0...26).each do |i|
      next if half[i] == 0
      half[i] -= 1
      arr = count_arr.call(half)
      if arr >= k
        left += (97 + i).chr
        break
      end
      k -= arr
      half[i] += 1
    end
  end
  res = left
  res += mid unless mid.empty?
  (left.length - 1).downto(0) { |i| res += left[i] }
  res
end
''')

add("3519_count_numbers_with_non_decreasing_digits", r'''
# LeetCode 3519 - Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

# @param {String} l
# @param {String} r
# @param {Integer} b
# @return {Integer}
def count_numbers(l, r, b)
  mod = 1000000007
  to_digits = lambda do |s, base|
    return [0] if s == "0"
    digs = []
    until s.length == 1 && s[0] == "0"
      rem = 0
      q = ""
      s.each_char do |c|
        cur = rem * 10 + (c.ord - 48)
        d = cur / base
        rem = cur % base
        q += d.to_s if q.length > 0 || d != 0
      end
      digs << rem
      s = q.empty? ? "0" : q
    end
    digs.reverse
  end
  dec = lambda do |s|
    a = s.chars
    i = a.length - 1
    while i >= 0 && a[i] == "0"
      a[i] = "9"
      i -= 1
    end
    return "0" if i < 0
    a[i] = (a[i].ord - 49).chr
    t = a.join
    p = 0
    p += 1 while p + 1 < t.length && t[p] == "0"
    t[p..]
  end
  count_upto = lambda do |digs, base|
    m = digs.length
    memo = {}
    dfs = nil
    dfs = lambda do |pos, last, tight|
      return 1 if pos == m
      key = [pos, last, tight ? 1 : 0]
      return memo[key] if memo.key?(key)
      up = tight ? digs[pos] : base - 1
      res = 0
      (last..up).each do |d|
        res = (res + dfs.call(pos + 1, d, tight && d == up)) % mod
      end
      memo[key] = res
      res
    end
    dfs.call(0, 0, true)
  end
  rd = to_digits.call(r, b)
  ld = to_digits.call(dec.call(l), b)
  (count_upto.call(rd, b) - count_upto.call(ld, b) + mod) % mod
end
''')

add("3520_minimum_threshold_for_inversion_pairs_count", r'''
# LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
# https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_threshold(nums, k)
  upper_bound = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  count_inv = lambda do |arr, kk, threshold|
    sorted_arr = []
    inv = 0
    arr.each do |num|
      left = upper_bound.call(sorted_arr, num)
      right = upper_bound.call(sorted_arr, num + threshold)
      inv += right - left
      sorted_arr.insert(upper_bound.call(sorted_arr, num), num)
    end
    inv >= kk
  end
  mx = 0
  nums.each { |v| mx = v if v > mx }
  l = 0
  r = mx + 1
  while l < r
    m = (l + r) >> 1
    if count_inv.call(nums, k, m)
      r = m
    else
      l = m + 1
    end
  end
  l > mx ? -1 : l
end
''')

add("3522_calculate_score_after_performing_instructions", r'''
# LeetCode 3522 - Calculate Score After Performing Instructions
# https://leetcode.com/problems/calculate-score-after-performing-instructions/

# @param {String[]} instructions
# @param {Integer[]} values
# @return {Integer}
def calculate_score(instructions, values)
  n = values.length
  vis = Array.new(n, false)
  ans = 0
  i = 0
  while i >= 0 && i < n && !vis[i]
    vis[i] = true
    if instructions[i][0] == "a"
      ans += values[i]
      i += 1
    else
      i += values[i]
    end
  end
  ans
end
''')

add("3523_make_array_non_decreasing", r'''
# LeetCode 3523 - Make Array Non-decreasing
# https://leetcode.com/problems/make-array-non-decreasing/

# @param {Integer[]} nums
# @return {Integer}
def maximum_possible_size(nums)
  ans = 0
  mx = 0
  nums.each do |x|
    if mx <= x
      ans += 1
      mx = x
    end
  end
  ans
end
''')

add("3524_find_x_value_of_array_i", r'''
# LeetCode 3524 - Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def result_array(nums, k)
  ans = Array.new(k, 0)
  dp = Array.new(k, 0)
  nums.each do |num|
    new_dp = Array.new(k, 0)
    nm = num % k
    new_dp[nm] = 1
    (0...k).each { |i| new_dp[(i * nm) % k] += dp[i] }
    (0...k).each { |i| ans[i] += new_dp[i] }
    dp = new_dp
  end
  ans
end
''')

add("3525_find_x_value_of_array_ii", r'''
# LeetCode 3525 - Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def result_array(nums, k, queries)
  n = nums.length
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    idx, val, start, x = q[0], q[1], q[2], q[3]
    nums[idx] = val
    prod = 1
    cnt = 0
    (start...n).each do |i|
      prod = prod * (nums[i] % k) % k
      cnt += 1 if prod == x
    end
    ans[qi] = cnt
  end
  ans
end
''')

add("3526_range_xor_queries_with_subarray_reversals", r'''
# LeetCode 3526 - Range XOR Queries with Subarray Reversals
# https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def get_results(nums, queries)
  a = nums.dup
  ans = []
  at = lambda { |i| (i >= 0 && i < a.length) ? a[i] : 0 }
  set_at = lambda do |i, val|
    return if i < 0
    a << 0 while a.length <= i
    a[i] = val
  end
  queries.each do |q|
    typ = q[0]
    if typ == 1
      l = q[1]
      r = q[2]
      while l < r
        left = at.call(l)
        right = at.call(r)
        set_at.call(l, right)
        set_at.call(r, left)
        l += 1
        r -= 1
      end
    elsif typ == 2
      x = 0
      (q[1]..q[2]).each { |i| x ^= at.call(i) }
      ans << x
    else
      set_at.call(q[1], q[2])
    end
  end
  ans
end
''')

add("3527_find_the_most_common_response", r'''
# LeetCode 3527 - Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/

# @param {String[][]} responses
# @return {String}
def find_common_response(responses)
  cnt = {}
  responses.each do |ws|
    seen = {}
    ws.each do |w|
      next if seen[w]
      seen[w] = true
      cnt[w] = (cnt[w] || 0) + 1
    end
  end
  ans = responses[0][0]
  cnt.each do |w, v|
    ans = w if cnt[ans] < v || (cnt[ans] == v && w < ans)
  end
  ans
end
''')

add("3528_unit_conversion_i", r'''
# LeetCode 3528 - Unit Conversion I
# https://leetcode.com/problems/unit-conversion-i/

# @param {Integer[][]} conversions
# @return {Integer[]}
def base_unit_conversions(conversions)
  mod = 1000000007
  n = conversions.length + 1
  g = Array.new(n) { [] }
  conversions.each { |e| g[e[0]] << [e[1], e[2]] }
  ans = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |s, mul|
    ans[s] = mul
    g[s].each { |to, w| dfs.call(to, mul * w % mod) }
  end
  dfs.call(0, 1)
  ans
end
''')

add("3529_count_cells_in_overlapping_horizontal_and_vertical_substrings", r'''
# LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

# @param {String[][]} grid
# @param {String} pattern
# @return {Integer}
def count_cells(grid, pattern)
  m = grid.length
  n = grid[0].length
  row = ""
  (0...m).each { |i| (0...n).each { |j| row += grid[i][j] } }
  col = ""
  (0...n).each { |j| (0...m).each { |i| col += grid[i][j] } }
  h_mark = Array.new(m) { Array.new(n, false) }
  v_mark = Array.new(m) { Array.new(n, false) }
  plen = pattern.length
  (0..(row.length - plen)).each do |i|
    next unless row[i, plen] == pattern
    (0...plen).each do |t|
      pos = i + t
      h_mark[pos / n][pos % n] = true
    end
  end
  (0..(col.length - plen)).each do |i|
    next unless col[i, plen] == pattern
    (0...plen).each do |t|
      pos = i + t
      v_mark[pos % m][pos / m] = true
    end
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each { |j| ans += 1 if h_mark[i][j] && v_mark[i][j] }
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
