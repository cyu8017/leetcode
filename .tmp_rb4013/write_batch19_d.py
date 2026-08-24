#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3691_maximum_total_subarray_value_ii", r'''
# LeetCode 3691 - Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

class SparseTableRMQ
  def initialize(data)
    @n = data.length
    max_log = 0
    max_log += 1 while (1 << max_log) <= @n
    max_log += 1
    @f_max = Array.new(@n) { Array.new(max_log, 0) }
    @f_min = Array.new(@n) { Array.new(max_log, 0) }
    @lg = Array.new(@n + 1, 0)
    (2..@n).each { |i| @lg[i] = @lg[i >> 1] + 1 }
    (0...@n).each do |i|
      @f_max[i][0] = data[i]
      @f_min[i][0] = data[i]
    end
    (1...max_log).each do |j|
      (0..(@n - (1 << j))).each do |i|
        @f_max[i][j] = [@f_max[i][j - 1], @f_max[i + (1 << (j - 1))][j - 1]].max
        @f_min[i][j] = [@f_min[i][j - 1], @f_min[i + (1 << (j - 1))][j - 1]].min
      end
    end
  end

  def query_max(l, r)
    k = @lg[r - l + 1]
    [@f_max[l][k], @f_max[r - (1 << k) + 1][k]].max
  end

  def query_min(l, r)
    k = @lg[r - l + 1]
    [@f_min[l][k], @f_min[r - (1 << k) + 1][k]].min
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_total_value(nums, k)
  n = nums.length
  st = SparseTableRMQ.new(nums)
  pq = []
  (0...n).each do |l|
    val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
    pq << [-val, l, n - 1]
  end
  ans = 0
  k.times do
    pq.sort_by! { |x| x[0] }
    val, l, r = pq.shift
    val = -val
    ans += val
    if r > l
      next_val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
      pq << [-next_val, l, r - 1]
    end
  end
  ans
end
''')

add("3692_majority_frequency_characters", r'''
# LeetCode 3692 - Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/

# @param {String} s
# @return {String}
def majority_frequency_group(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  f = {}
  (0...26).each do |i|
    f[cnt[i]] = (f[cnt[i]] || "") + (97 + i).chr if cnt[i] > 0
  end
  mx = 0
  mv = 0
  ans = ""
  f.each do |v, cs|
    if cs.length > mx || (cs.length == mx && v > mv)
      mx = cs.length
      mv = v
      ans = cs
    end
  end
  ans
end
''')

add("3693_climbing_stairs_ii", r'''
# LeetCode 3693 - Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/

# @param {Integer} n
# @param {Integer[]} costs
# @return {Integer}
def climb_stairs(n, costs)
  inf = 10**9
  f = Array.new(n + 1, inf)
  f[0] = 0
  (1..n).each do |i|
    x = costs[i - 1]
    ([0, i - 3].max...i).each do |j|
      v = f[j] + x + (i - j) * (i - j)
      f[i] = v if v < f[i]
    end
  end
  f[n]
end
''')

add("3694_distinct_points_reachable_after_substring_removal", r'''
# LeetCode 3694 - Distinct Points Reachable After Substring Removal
# https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def distinct_points(s, k)
  n = s.length
  f = Array.new(n + 1, 0)
  g = Array.new(n + 1, 0)
  x = 0
  y = 0
  (1..n).each do |i|
    c = s[i - 1]
    if c == "U"
      y += 1
    elsif c == "D"
      y -= 1
    elsif c == "L"
      x -= 1
    else
      x += 1
    end
    f[i] = x
    g[i] = y
  end
  st = {}
  (k..n).each do |i|
    a = f[n] - (f[i] - f[i - k])
    b = g[n] - (g[i] - g[i - k])
    st[[a, b]] = true
  end
  st.length
end
''')

add("3695_maximize_alternating_sum_using_swaps", r'''
# LeetCode 3695 - Maximize Alternating Sum Using Swaps
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

# @param {Integer[]} nums
# @param {Integer[][]} swaps
# @return {Integer}
def max_alternating_sum(nums, swaps)
  n = nums.length
  parent = (0...n).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  swaps.each do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  comp_vals = {}
  comp_idx = {}
  (0...n).each do |i|
    r = find.call(i)
    (comp_vals[r] ||= []) << nums[i]
    (comp_idx[r] ||= []) << i
  end
  arr = Array.new(n, 0)
  comp_vals.each do |r, vals|
    idxs = comp_idx[r]
    vals.sort!.reverse!
    even = idxs.select { |i| i.even? }.sort
    odd = idxs.select { |i| i.odd? }.sort
    ei = 0
    vals.each do |v|
      if ei < even.length
        arr[even[ei]] = v
      else
        arr[odd[ei - even.length]] = v
      end
      ei += 1
    end
  end
  ans = 0
  (0...n).each { |i| ans += i.even? ? arr[i] : -arr[i] }
  ans
end
''')

add("3696_maximum_distance_between_unequal_words_in_array_i", r'''
# LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

# @param {String[]} words
# @return {Integer}
def max_distance(words)
  n = words.length
  ans = 0
  (0...n).each do |i|
    ans = i + 1 if words[i] != words[0] && i + 1 > ans
    ans = n - i if words[i] != words[n - 1] && n - i > ans
  end
  ans
end
''')

add("3697_compute_decimal_representation", r'''
# LeetCode 3697 - Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/

# @param {Integer} n
# @return {Integer[]}
def decimal_representation(n)
  ans = []
  p = 1
  while n > 0
    v = n % 10
    n /= 10
    ans << p * v if v != 0
    p *= 10
  end
  ans.reverse
end
''')

add("3698_split_array_with_minimum_difference", r'''
# LeetCode 3698 - Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/

# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)
  n = nums.length
  s = Array.new(n, 0)
  f = Array.new(n, true)
  g = Array.new(n, true)
  s[0] = nums[0]
  (1...n).each do |i|
    s[i] = s[i - 1] + nums[i]
    f[i] = f[i - 1]
    f[i] = false if nums[i] <= nums[i - 1]
  end
  (n - 2).downto(0) do |i|
    g[i] = g[i + 1]
    g[i] = false if nums[i] <= nums[i + 1]
  end
  inf = 10**18
  ans = inf
  (0...(n - 1)).each do |i|
    next unless f[i] && g[i + 1]

    s1 = s[i]
    s2 = s[n - 1] - s[i]
    d = (s1 - s2).abs
    ans = d if d < ans
  end
  ans < inf ? ans : -1
end
''')

add("3699_number_of_zigzag_arrays_i", r'''
# LeetCode 3699 - Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/

# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  m = r - l + 1
  return m % mod if n == 1

  up = Array.new(m, 1)
  down = Array.new(m, 1)
  (2..n).each do
    pref_down = Array.new(m + 1, 0)
    (0...m).each { |j| pref_down[j + 1] = (pref_down[j] + down[j]) % mod }
    nup = (0...m).map { |j| pref_down[j] }
    suf_up = Array.new(m + 1, 0)
    (m - 1).downto(0) { |j| suf_up[j] = (suf_up[j + 1] + up[j]) % mod }
    ndown = (0...m).map { |j| suf_up[j + 1] }
    up = nup
    down = ndown
  end
  ans = 0
  (0...m).each do |j|
    ans = (ans + up[j]) % mod
    ans = (ans + down[j]) % mod
  end
  ans
end
''')

add("3700_number_of_zigzag_arrays_ii", r'''
# LeetCode 3700 - Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  m = r - l + 1
  return m % mod if n == 1

  up = Array.new(m, 1)
  down = Array.new(m, 1)
  (2..n).each do
    pref = Array.new(m + 1, 0)
    (0...m).each { |j| pref[j + 1] = (pref[j] + down[j]) % mod }
    nup = (0...m).map { |j| pref[j] }
    suf = Array.new(m + 1, 0)
    (m - 1).downto(0) { |j| suf[j] = (suf[j + 1] + up[j]) % mod }
    ndown = (0...m).map { |j| suf[j + 1] }
    up = nup
    down = ndown
  end
  ans = 0
  (0...m).each do |j|
    ans = (ans + up[j]) % mod
    ans = (ans + down[j]) % mod
  end
  ans
end
''')

add("3701_compute_alternating_sum", r'''
# LeetCode 3701 - Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/

# @param {Integer[]} nums
# @return {Integer}
def alternating_sum(nums)
  ans = 0
  nums.each_with_index { |x, i| ans += i.even? ? x : -x }
  ans
end
''')

add("3702_longest_subsequence_with_non_zero_bitwise_xor", r'''
# LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  xorv = 0
  cnt0 = 0
  nums.each do |x|
    xorv ^= x
    cnt0 += 1 if x == 0
  end
  n = nums.length
  return n if xorv != 0
  return 0 if cnt0 == n

  n - 1
end
''')

add("3703_remove_k_balanced_substrings", r'''
# LeetCode 3703 - Remove K-Balanced Substrings
# https://leetcode.com/problems/remove-k-balanced-substrings/

# @param {String} s
# @param {Integer} k
# @return {String}
def remove_substring(s, k)
  stk = []
  s.each_char do |c|
    if !stk.empty? && stk[-1][0] == c
      stk[-1][1] += 1
    else
      stk << [c, 1]
    end
    next unless c == ")" && stk.length > 1

    top = stk[-1]
    prev = stk[-2]
    if top[1] == k && prev[1] >= k
      stk.pop
      prev[1] -= k
      stk.pop if prev[1] == 0
    end
  end
  stk.map { |p| p[0] * p[1] }.join
end
''')

add("3704_count_no_zero_pairs_that_sum_to_n", r'''
# LeetCode 3704 - Count No-Zero Pairs That Sum to N
# https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

# @param {Integer} n
# @return {Integer}
def count_no_zero_pairs(n)
  s = n.to_s
  m = s.length
  digits = Array.new(m + 1, 0)
  (0...m).each { |i| digits[i] = s[m - 1 - i].ord - 48 }
  dp = Array.new(2) { Array.new(2) { Array.new(2, 0) } }
  dp[0][1][1] = 1
  (0..m).each do |pos|
    ndp = Array.new(2) { Array.new(2) { Array.new(2, 0) } }
    target = digits[pos]
    (0...2).each do |carry|
      (0...2).each do |alive_a|
        (0...2).each do |alive_b|
          ways = dp[carry][alive_a][alive_b]
          next if ways == 0

          a_opts = []
          if alive_a == 1
            (1..9).each { |d| a_opts << [d, 1] }
            a_opts << [0, 0] if pos > 0
          else
            a_opts << [0, 0]
          end
          b_opts = []
          if alive_b == 1
            (1..9).each { |d| b_opts << [d, 1] }
            b_opts << [0, 0] if pos > 0
          else
            b_opts << [0, 0]
          end
          a_opts.each do |da, na|
            b_opts.each do |db, nb|
              sm = da + db + carry
              next if sm % 10 != target

              ncarry = sm / 10
              ndp[ncarry][na][nb] += ways
            end
          end
        end
      end
    end
    dp = ndp
  end
  dp[0][0][0]
end
''')

add("3706_maximum_distance_between_unequal_words_in_array_ii", r'''
# LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

# @param {String[]} words
# @return {Integer}
def max_distance(words)
  n = words.length
  ans = 0
  (0...n).each do |i|
    ans = i + 1 if words[i] != words[0] && i + 1 > ans
    ans = n - i if words[i] != words[n - 1] && n - i > ans
  end
  ans
end
''')

add("3707_equal_score_substrings", r'''
# LeetCode 3707 - Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/

# @param {String} s
# @return {Boolean}
def score_balance(s)
  l = 0
  r = 0
  s.each_char { |c| r += (c.ord - 97) + 1 }
  (0...(s.length - 1)).each do |i|
    x = (s[i].ord - 97) + 1
    l += x
    r -= x
    return true if l == r
  end
  false
end
''')

add("3708_longest_fibonacci_subarray", r'''
# LeetCode 3708 - Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  f = 2
  ans = f
  (2...nums.length).each do |i|
    if nums[i] == nums[i - 1] + nums[i - 2]
      f += 1
      ans = f if f > ans
    else
      f = 2
    end
  end
  ans
end
''')

add("3709_design_exam_scores_tracker", r'''
# LeetCode 3709 - Design Exam Scores Tracker
# https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker
  def initialize
    @times = [0]
    @pre = [0]
  end

  def record(time, score)
    @times << time
    @pre << @pre[-1] + score
  end

  def total_score(start_time, end_time)
    l = bisect_left(@times, start_time) - 1
    r = bisect_left(@times, end_time + 1) - 1
    @pre[r] - @pre[l]
  end

  private

  def bisect_left(a, target)
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
end
''')

add("3710_maximum_partition_factor", r'''
# LeetCode 3710 - Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/

# @param {Integer[][]} points
# @return {Integer}
def max_partition_factor(points)
  n = points.length
  return 0 if n == 2

  dist = lambda do |i, j|
    (points[i][0] - points[j][0]).abs + (points[i][1] - points[j][1]).abs
  end
  ok = lambda do |d|
    g = Array.new(n) { [] }
    (0...n).each do |i|
      ((i + 1)...n).each do |j|
        if dist.call(i, j) < d
          g[i] << j
          g[j] << i
        end
      end
    end
    color = Array.new(n, -1)
    (0...n).each do |i|
      next if color[i] != -1

      q = [i]
      color[i] = 0
      until q.empty?
        u = q.shift
        g[u].each do |v|
          if color[v] == -1
            color[v] = color[u] ^ 1
            q << v
          elsif color[v] == color[u]
            return false
          end
        end
      end
    end
    true
  end
  lo = 0
  hi = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      d = dist.call(i, j)
      hi = d if d > hi
    end
  end
  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("3711_maximum_transactions_without_negative_balance", r'''
# LeetCode 3711 - Maximum Transactions Without Negative Balance
# https://leetcode.com/problems/maximum-transactions-without-negative-balance/

# @param {Integer[]} transactions
# @return {Integer}
def max_transactions(transactions)
  tm = Hash.new(0)
  ans = transactions.length
  s = 0
  heap = []
  transactions.each do |x|
    s += x
    tm[x] += 1
    heap << x
    heap.sort!
    while s < 0
      heap.shift while !heap.empty? && tm[heap[0]] == 0
      y = heap[0]
      s -= y
      ans -= 1
      c = tm[y]
      if c == 1
        tm.delete(y)
        heap.shift
      else
        tm[y] = c - 1
        heap.shift
      end
    end
  end
  ans
end
''')

add("3712_sum_of_elements_with_frequency_divisible_by_k", r'''
# LeetCode 3712 - Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_divisible_by_k(nums, k)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ans = 0
  cnt.each { |key, val| ans += key * val if val % k == 0 }
  ans
end
''')

add("3713_longest_balanced_substring_i", r'''
# LeetCode 3713 - Longest Balanced Substring I
# https://leetcode.com/problems/longest-balanced-substring-i/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  n = s.length
  ans = 0
  (0...n).each do |i|
    cnt = Array.new(26, 0)
    mx = 0
    v = 0
    (i...n).each do |j|
      c = s[j].ord - 97
      cnt[c] += 1
      v += 1 if cnt[c] == 1
      mx = cnt[c] if cnt[c] > mx
      ans = j - i + 1 if mx * v == j - i + 1 && j - i + 1 > ans
    end
  end
  ans
end
''')

add("3714_longest_balanced_substring_ii", r'''
# LeetCode 3714 - Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  calc1 = lambda do |st|
    res = 0
    n = st.length
    i = 0
    while i < n
      j = i + 1
      j += 1 while j < n && st[j] == st[i]
      res = j - i if j - i > res
      i = j
    end
    res
  end
  calc2 = lambda do |st, a, b|
    res = 0
    n = st.length
    i = 0
    while i < n
      i += 1 while i < n && st[i] != a && st[i] != b
      pos = { 0 => i - 1 }
      d = 0
      while i < n && (st[i] == a || st[i] == b)
        d += st[i] == a ? 1 : -1
        if pos.key?(d)
          res = i - pos[d] if i - pos[d] > res
        else
          pos[d] = i
        end
        i += 1
      end
    end
    res
  end
  calc3 = lambda do |st|
    pos = { "0,0" => -1 }
    cnt = [0, 0, 0]
    res = 0
    st.each_char.with_index do |ch, i|
      cnt[ch.ord - 97] += 1
      x = cnt[0] - cnt[1]
      y = cnt[1] - cnt[2]
      k = "#{x},#{y}"
      if pos.key?(k)
        res = i - pos[k] if i - pos[k] > res
      else
        pos[k] = i
      end
    end
    res
  end
  x = calc1.call(s)
  y = [calc2.call(s, "a", "b"), calc2.call(s, "b", "c"), calc2.call(s, "a", "c")].max
  z = calc3.call(s)
  [x, y, z].max
end
''')

add("3715_sum_of_perfect_square_ancestors", r'''
# LeetCode 3715 - Sum of Perfect Square Ancestors
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} nums
# @return {Integer}
def sum_of_ancestors(n, edges, nums)
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end
  kernel = lambda do |x|
    res = 1
    p = 2
    while p * p <= x
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
      end
      res *= p if cnt.odd?
      p += 1
    end
    res *= x if x > 1
    res
  end
  ks = (0...n).map { |i| kernel.call(nums[i]) }
  freq = Hash.new(0)
  ans = 0
  dfs = nil
  dfs = lambda do |u, p|
    ans += freq[ks[u]]
    freq[ks[u]] += 1
    graph[u].each { |v| dfs.call(v, u) if v != p }
    freq[ks[u]] -= 1
  end
  dfs.call(0, -1)
  ans
end
''')

add("3717_minimum_operations_to_make_the_array_beautiful", r'''
# LeetCode 3717 - Minimum Operations to Make the Array Beautiful
# https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  f = { nums[0] => 0 }
  (1...nums.length).each do |i|
    x = nums[i]
    g = {}
    f.each do |pre, s|
      cur = ((x + pre - 1) / pre) * pre
      while cur <= 100
        val = s + (cur - x)
        old = g[cur]
        g[cur] = val if old.nil? || old > val
        cur += pre
      end
    end
    f = g
  end
  f.empty? ? 0 : f.values.min
end
''')

add("3718_smallest_missing_multiple_of_k", r'''
# LeetCode 3718 - Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def missing_multiple(nums, k)
  s = {}
  nums.each { |x| s[x] = true }
  i = 1
  loop do
    x = k * i
    return x unless s[x]

    i += 1
  end
end
''')

if __name__ == "__main__":
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch D written={written}")
