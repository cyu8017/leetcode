#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3086_minimum_moves_to_pick_k_ones", r'''
# LeetCode 3086 - Minimum Moves to Pick K Ones
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} max_changes
# @return {Integer}
def minimum_moves(nums, k, max_changes)
  n = nums.length
  cnt = Array.new(n + 1, 0)
  s = Array.new(n + 1, 0)
  (1..n).each do |i|
    cnt[i] = cnt[i - 1] + nums[i - 1]
    s[i] = s[i - 1] + i * nums[i - 1]
  end
  ans = 10**18
  (1..n).each do |i|
    t = 0
    need = k - nums[i - 1]
    [i - 1, i + 1].each do |j|
      if need > 0 && j >= 1 && j <= n && nums[j - 1] == 1
        need -= 1
        t += 1
      end
    end
    c = [need, max_changes].min
    need -= c
    t += c * 2
    if need <= 0
      ans = [ans, t].min
      next
    end
    l = 2
    r = [i - 1, n - i].max
    while l <= r
      mid = (l + r) >> 1
      l1 = [1, i - mid].max
      r1 = [0, i - 2].max
      l2 = [n + 1, i + 2].min
      r2 = [n, i + mid].min
      c1 = cnt[r1] - cnt[l1 - 1]
      c2 = cnt[r2] - cnt[l2 - 1]
      if c1 + c2 >= need
        t1 = c1 * i - (s[r1] - s[l1 - 1])
        t2 = s[r2] - s[l2 - 1] - c2 * i
        ans = [ans, t + t1 + t2].min
        r = mid - 1
      else
        l = mid + 1
      end
    end
  end
  ans
end
''')

add("3088_make_string_anti_palindrome", r'''
# LeetCode 3088 - Make String Anti-palindrome
# https://leetcode.com/problems/make-string-anti-palindrome/

# @param {String} s
# @return {String}
def make_anti_palindrome(s)
  arr = s.chars.sort
  n = arr.length
  m = n / 2
  if arr[m] == arr[m - 1]
    i = m
    i += 1 while i < n && arr[i] == arr[i - 1]
    j = m
    while j < n && arr[j] == arr[n - j - 1]
      return "-1" if i >= n
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j += 1
    end
  end
  arr.join
end
''')

add("3090_maximum_length_substring_with_two_occurrences", r'''
# LeetCode 3090 - Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

# @param {String} s
# @return {Integer}
def maximum_length_substring(s)
  l = 0
  ans = 0
  cnt = Array.new(26, 0)
  s.each_char.with_index do |ch, r|
    idx = ch.ord - 97
    cnt[idx] += 1
    while cnt[idx] > 2
      cnt[s[l].ord - 97] -= 1
      l += 1
    end
    ans = [ans, r - l + 1].max
  end
  ans
end
''')

add("3091_apply_operations_to_make_sum_of_array_greater_than_or_equal_to_k", r'''
# LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

# @param {Integer} k
# @return {Integer}
def min_operations(k)
  ans = k
  k.times do |a|
    x = a + 1
    b = (k + x - 1) / x - 1
    ans = [ans, a + b].min
  end
  ans
end
''')

add("3092_most_frequent_ids", r'''
# LeetCode 3092 - Most Frequent IDs
# https://leetcode.com/problems/most-frequent-ids/

# @param {Integer[]} nums
# @param {Integer[]} freq
# @return {Integer[]}
def most_frequent_i_ds(nums, freq)
  n = nums.length
  cnt = {}
  lazy = Hash.new(0)
  ans = Array.new(n, 0)
  pq = []
  n.times do |i|
    x = nums[i]
    f = freq[i]
    old = cnt.fetch(x, 0)
    lazy[old] += 1
    neu = old + f
    cnt[x] = neu
    heap_push_neg(pq, -neu)
    while !pq.empty? && lazy[-pq[0]] > 0
      top = -heap_pop_neg(pq)
      lazy[top] -= 1
    end
    ans[i] = pq.empty? ? 0 : -pq[0]
  end
  ans
end

def heap_push_neg(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_neg(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] < a[s]
      s = r if r < n && a[r] < a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end
''')

add("3093_longest_common_suffix_queries", r'''
# LeetCode 3093 - Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/

class Trie
  attr_accessor :children, :length, :idx
  def initialize
    @children = Array.new(26)
    @length = 1 << 30
    @idx = 1 << 30
  end
end

# @param {String[]} words_container
# @param {String[]} words_query
# @return {Integer[]}
def string_indices(words_container, words_query)
  insert = lambda do |t, w, i|
    node = t
    if node.length > w.length
      node.length = w.length
      node.idx = i
    end
    (w.length - 1).downto(0) do |k|
      cid = w[k].ord - 97
      node.children[cid] ||= Trie.new
      node = node.children[cid]
      if node.length > w.length
        node.length = w.length
        node.idx = i
      end
    end
  end

  query = lambda do |t, w|
    node = t
    (w.length - 1).downto(0) do |k|
      cid = w[k].ord - 97
      break if node.children[cid].nil?
      node = node.children[cid]
    end
    node.idx
  end

  trie = Trie.new
  words_container.each_with_index { |w, i| insert.call(trie, w, i) }
  words_query.map { |w| query.call(trie, w) }
end
''')

add("3094_guess_the_number_using_bitwise_questions_ii", r'''
# LeetCode 3094 - Guess the Number Using Bitwise Questions II
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

# The commonBits API is provided by the judge.

# @return {Integer}
def find_number
  n = 0
  32.times do |i|
    count1 = common_bits(1 << i)
    count2 = common_bits(1 << i)
    n |= 1 << i if count1 > count2
  end
  n
end
''')

add("3095_shortest_subarray_with_or_at_least_k_i", r'''
# LeetCode 3095 - Shortest Subarray With OR at Least K I
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_subarray_length(nums, k)
  n = nums.length
  cnt = Array.new(32, 0)
  ans = n + 1
  s = 0
  i = 0
  n.times do |j|
    x = nums[j]
    s |= x
    32.times { |h| cnt[h] += 1 if ((x >> h) & 1) != 0 }
    while s >= k && i <= j
      ans = [ans, j - i + 1].min
      32.times do |h|
        if ((nums[i] >> h) & 1) != 0
          cnt[h] -= 1
          s ^= 1 << h if cnt[h] == 0
        end
      end
      i += 1
    end
  end
  ans == n + 1 ? -1 : ans
end
''')

add("3096_minimum_levels_to_gain_more_points", r'''
# LeetCode 3096 - Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

# @param {Integer[]} possible
# @return {Integer}
def minimum_levels(possible)
  s = possible.sum { |x| x == 0 ? -1 : x }
  t = 0
  (0...possible.length - 1).each do |i|
    x = possible[i] == 0 ? -1 : possible[i]
    t += x
    return i + 1 if t > s - t
  end
  -1
end
''')

add("3097_shortest_subarray_with_or_at_least_k_ii", r'''
# LeetCode 3097 - Shortest Subarray With OR at Least K II
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_subarray_length(nums, k)
  n = nums.length
  cnt = Array.new(32, 0)
  ans = n + 1
  s = 0
  i = 0
  n.times do |j|
    x = nums[j]
    s |= x
    32.times { |h| cnt[h] += 1 if ((x >> h) & 1) != 0 }
    while s >= k && i <= j
      ans = [ans, j - i + 1].min
      32.times do |h|
        if ((nums[i] >> h) & 1) != 0
          cnt[h] -= 1
          s ^= 1 << h if cnt[h] == 0
        end
      end
      i += 1
    end
  end
  ans == n + 1 ? -1 : ans
end
''')

add("3098_find_the_sum_of_subsequence_powers", r'''
# LeetCode 3098 - Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_powers(nums, k)
  mod = 1_000_000_007
  nums = nums.sort
  n = nums.length
  f = {}

  dfs = lambda do |i, j, kk, mi|
    return mi if i >= n && kk == 0
    return 0 if i >= n
    return 0 if n - i < kk
    key = [mi, i, j, kk]
    return f[key] if f.key?(key)
    ans = dfs.call(i + 1, j, kk, mi)
    if j == n
      ans = (ans + dfs.call(i + 1, i, kk - 1, mi)) % mod
    else
      ans = (ans + dfs.call(i + 1, i, kk - 1, [mi, nums[i] - nums[j]].min)) % mod
    end
    f[key] = ans
    ans
  end

  dfs.call(0, n, k, 10**18)
end
''')

add("3099_harshad_number", r'''
# LeetCode 3099 - Harshad Number
# https://leetcode.com/problems/harshad-number/

# @param {Integer} x
# @return {Integer}
def sum_of_the_digits_of_harshad_number(x)
  s = 0
  y = x
  while y > 0
    s += y % 10
    y /= 10
  end
  x % s == 0 ? s : -1
end
''')

add("3100_water_bottles_ii", r'''
# LeetCode 3100 - Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/

# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def max_bottles_drunk(num_bottles, num_exchange)
  ans = num_bottles
  while num_bottles >= num_exchange
    num_bottles -= num_exchange
    num_exchange += 1
    ans += 1
    num_bottles += 1
  end
  ans
end
''')

add("3101_count_alternating_subarrays", r'''
# LeetCode 3101 - Count Alternating Subarrays
# https://leetcode.com/problems/count-alternating-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_alternating_subarrays(nums)
  ans = 1
  s = 1
  (1...nums.length).each do |i|
    if nums[i] != nums[i - 1]
      s += 1
    else
      s = 1
    end
    ans += s
  end
  ans
end
''')

add("3102_minimize_manhattan_distances", r'''
# LeetCode 3102 - Minimize Manhattan Distances
# https://leetcode.com/problems/minimize-manhattan-distances/

class MultiSet
  def initialize
    @m = Hash.new(0)
    @keys = []
  end

  def merge(x, v)
    nv = @m[x] + v
    if nv == 0
      @m.delete(x)
      i = bisect_left(@keys, x)
      @keys.delete_at(i) if i < @keys.length && @keys[i] == x
    else
      if !@m.key?(x) || @m[x] == 0
        i = bisect_left(@keys, x)
        @keys.insert(i, x) unless i < @keys.length && @keys[i] == x
      end
      @m[x] = nv
    end
  end

  def first
    @keys[0]
  end

  def last
    @keys[-1]
  end

  def bisect_left(a, x)
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end

# @param {Integer[][]} points
# @return {Integer}
def minimum_distance(points)
  st1 = MultiSet.new
  st2 = MultiSet.new
  points.each do |p|
    st1.merge(p[0] + p[1], 1)
    st2.merge(p[0] - p[1], 1)
  end
  ans = 10**18
  points.each do |p|
    x = p[0]
    y = p[1]
    st1.merge(x + y, -1)
    st2.merge(x - y, -1)
    ans = [ans, [st1.last - st1.first, st2.last - st2.first].max].min
    st1.merge(x + y, 1)
    st2.merge(x - y, 1)
  end
  ans
end
''')

add("3104_find_longest_self_contained_substring", r'''
# LeetCode 3104 - Find Longest Self-Contained Substring
# https://leetcode.com/problems/find-longest-self-contained-substring/

# @param {String} s
# @return {Integer}
def max_substring_length(s)
  first = Array.new(26, -1)
  last = Array.new(26, 0)
  n = s.length
  s.each_char.with_index do |ch, i|
    j = ch.ord - 97
    first[j] = i if first[j] == -1
    last[j] = i
  end
  ans = -1
  26.times do |k|
    i = first[k]
    next if i == -1
    mx = last[k]
    (i...n).each do |j|
      a = first[s[j].ord - 97]
      b = last[s[j].ord - 97]
      break if a < i
      mx = [mx, b].max
      ans = [ans, j - i + 1].max if mx == j && j - i + 1 < n
    end
  end
  ans
end
''')

add("3105_longest_strictly_increasing_or_strictly_decreasing_subarray", r'''
# LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_monotonic_subarray(nums)
  ans = 1
  t = 1
  (1...nums.length).each do |i|
    if nums[i - 1] < nums[i]
      t += 1
      ans = [ans, t].max
    else
      t = 1
    end
  end
  t = 1
  (1...nums.length).each do |i|
    if nums[i - 1] > nums[i]
      t += 1
      ans = [ans, t].max
    else
      t = 1
    end
  end
  ans
end
''')

add("3106_lexicographically_smallest_string_after_operations_with_constraint", r'''
# LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

# @param {String} s
# @param {Integer} k
# @return {String}
def get_smallest_string(s, k)
  arr = s.chars
  arr.each_index do |i|
    c1 = arr[i].ord
    (97...c1).each do |c2|
      d = [c1 - c2, 26 - (c1 - c2)].min
      if d <= k
        arr[i] = c2.chr
        k -= d
        break
      end
    end
  end
  arr.join
end
''')

add("3107_minimum_operations_to_make_median_of_array_equal_to_k", r'''
# LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations_to_make_median_k(nums, k)
  nums = nums.sort
  n = nums.length
  m = n >> 1
  ans = (nums[m] - k).abs
  if nums[m] > k
    i = m - 1
    while i >= 0 && nums[i] > k
      ans += nums[i] - k
      i -= 1
    end
  else
    i = m + 1
    while i < n && nums[i] < k
      ans += k - nums[i]
      i += 1
    end
  end
  ans
end
''')

add("3108_minimum_cost_walk_in_weighted_graph", r'''
# LeetCode 3108 - Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} query
# @return {Integer[]}
def minimum_cost(n, edges, query)
  p = (0...n).to_a
  size = Array.new(n, 1)

  find = lambda do |x|
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end

  unite = lambda do |a, b|
    pa = find.call(a)
    pb = find.call(b)
    return if pa == pb
    if size[pa] > size[pb]
      p[pb] = pa
      size[pa] += size[pb]
    else
      p[pa] = pb
      size[pb] += size[pa]
    end
  end

  g = Array.new(n, -1)
  edges.each { |e| unite.call(e[0], e[1]) }
  edges.each do |e|
    root = find.call(e[0])
    g[root] &= e[2]
  end
  query.map do |u, v|
    if u == v
      0
    else
      a = find.call(u)
      b = find.call(v)
      a == b ? g[a] : -1
    end
  end
end
''')

add("3109_find_the_index_of_permutation", r'''
# LeetCode 3109 - Find the Index of Permutation
# https://leetcode.com/problems/find-the-index-of-permutation/

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

# @param {Integer[]} perm
# @return {Integer}
def get_permutation_index(perm)
  mod = 1_000_000_007
  n = perm.length
  tree = BIT.new(n + 1)
  f = Array.new(n, 0)
  f[0] = 1
  (1...n).each { |i| f[i] = f[i - 1] * i % mod }
  ans = 0
  n.times do |i|
    x = perm[i]
    cnt = x - 1 - tree.query(x)
    ans = (ans + cnt * f[n - 1 - i]) % mod
    tree.update(x, 1)
  end
  ans
end
''')

add("3110_score_of_a_string", r'''
# LeetCode 3110 - Score of a String
# https://leetcode.com/problems/score-of-a-string/

# @param {String} s
# @return {Integer}
def score_of_string(s)
  ans = 0
  (1...s.length).each { |i| ans += (s[i - 1].ord - s[i].ord).abs }
  ans
end
''')

add("3111_minimum_rectangles_to_cover_points", r'''
# LeetCode 3111 - Minimum Rectangles to Cover Points
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

# @param {Integer[][]} points
# @param {Integer} w
# @return {Integer}
def min_rectangles_to_cover_points(points, w)
  points = points.sort_by { |p| p[0] }
  ans = 0
  x1 = -1
  points.each do |p|
    if p[0] > x1
      ans += 1
      x1 = p[0] + w
    end
  end
  ans
end
''')

add("3112_minimum_time_to_visit_disappearing_nodes", r'''
# LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} disappear
# @return {Integer[]}
def minimum_time(n, edges, disappear)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  inf = 1 << 30
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    du, u = heap_pop_pair(pq)
    next if du > dist[u]
    g[u].each do |v, w|
      if dist[v] > dist[u] + w && dist[u] + w < disappear[v]
        dist[v] = dist[u] + w
        heap_push_pair(pq, [dist[v], v])
      end
    end
  end
  n.times.map { |i| dist[i] < disappear[i] ? dist[i] : -1 }
end

def heap_push_pair(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if cmp_pair(a[i], a[p]) >= 0
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_pair(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp_pair(a[l], a[s]) < 0
      s = r if r < n && cmp_pair(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end

def cmp_pair(a, b)
  a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
end
''')

add("3113_find_the_number_of_subarrays_where_boundary_elements_are_maximum", r'''
# LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

# @param {Integer[]} nums
# @return {Integer}
def number_of_subarrays(nums)
  stk = []
  ans = 0
  nums.each do |x|
    stk.pop while !stk.empty? && stk[-1][0] < x
    if stk.empty? || stk[-1][0] > x
      stk << [x, 1]
    else
      stk[-1][1] += 1
    end
    ans += stk[-1][1]
  end
  ans
end
''')

add("3114_latest_time_you_can_obtain_after_replacing_characters", r'''
# LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

# @param {String} s
# @return {String}
def find_latest_time(s)
  h = 11
  loop do
    59.downto(0) do |m|
      t = format("%02d:%02d", h, m)
      ok = true
      5.times do |i|
        if s[i] != "?" && s[i] != t[i]
          ok = false
          break
        end
      end
      return t if ok
    end
    h -= 1
  end
end
''')

add("3115_maximum_prime_difference", r'''
# LeetCode 3115 - Maximum Prime Difference
# https://leetcode.com/problems/maximum-prime-difference/

# @param {Integer[]} nums
# @return {Integer}
def maximum_prime_difference(nums)
  is_prime = lambda do |n|
    return false if n < 2
    i = 2
    while i * i <= n
      return false if n % i == 0
      i += 1
    end
    true
  end

  i = 0
  loop do
    if is_prime.call(nums[i])
      j = nums.length - 1
      loop do
        return j - i if is_prime.call(nums[j])
        j -= 1
      end
    end
    i += 1
  end
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        written += 1
        print(f"wrote {name}")
    print(f"batch_b written={written}")


if __name__ == "__main__":
    main()
