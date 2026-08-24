#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3000_maximum_area_of_longest_diagonal_rectangle", r'''
# LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

# @param {Integer[][]} dimensions
# @return {Integer}
def area_of_max_diagonal(dimensions)
  ans = 0
  mx = 0
  dimensions.each do |d|
    l = d[0]
    w = d[1]
    t = l * l + w * w
    if mx < t
      mx = t
      ans = l * w
    elsif mx == t
      area = l * w
      ans = area if area > ans
    end
  end
  ans
end
''')

add("3001_minimum_moves_to_capture_the_queen", r'''
# LeetCode 3001 - Minimum Moves to Capture The Queen
# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @param {Integer} d
# @param {Integer} e
# @param {Integer} f
# @return {Integer}
def min_moves_to_capture_the_queen(a, b, c, d, e, f)
  return 1 if a == e && (c != a || (d - b) * (d - f) > 0)
  return 1 if b == f && (d != b || (c - a) * (c - e) > 0)
  return 1 if c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0)
  return 1 if c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0)

  2
end
''')

add("3002_maximum_size_of_a_set_after_removals", r'''
# LeetCode 3002 - Maximum Size of a Set After Removals
# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximum_set_size(nums1, nums2)
  s1 = {}
  s2 = {}
  nums1.each { |x| s1[x] = true }
  nums2.each { |x| s2[x] = true }
  a = 0
  b = 0
  c = 0
  s1.each_key { |x| a += 1 unless s2[x] }
  s2.each_key do |x|
    if s1[x]
      c += 1
    else
      b += 1
    end
  end
  n = nums1.length
  a = [a, n / 2].min
  b = [b, n / 2].min
  [a + b + c, n].min
end
''')

add("3003_maximize_the_number_of_partitions_after_operations", r'''
# LeetCode 3003 - Maximize the Number of Partitions After Operations
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_partitions_after_operations(s, k)
  n = s.length
  memo = {}
  popcount = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  dfs = lambda do |i, cur, t|
    return 1 if i >= n

    kkey = (i << 32) | (cur << 1) | t
    return memo[kkey] if memo.key?(kkey)

    v = 1 << (s[i].ord - 97)
    nxt = cur | v
    ans = if popcount.call(nxt) > k
            dfs.call(i + 1, v, t) + 1
          else
            dfs.call(i + 1, nxt, t)
          end
    if t > 0
      26.times do |j|
        nxt2 = cur | (1 << j)
        ans = if popcount.call(nxt2) > k
                [ans, dfs.call(i + 1, 1 << j, 0) + 1].max
              else
                [ans, dfs.call(i + 1, nxt2, 0)].max
              end
      end
    end
    memo[kkey] = ans
    ans
  end
  dfs.call(0, 0, 1)
end
''')

add("3004_maximum_subtree_of_the_same_color", r'''
# LeetCode 3004 - Maximum Subtree of the Same Color
# https://leetcode.com/problems/maximum-subtree-of-the-same-color/

# @param {Integer[][]} edges
# @param {Integer[]} colors
# @return {Integer}
def maximum_subtree_size(edges, colors)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  size = Array.new(n, 0)
  ans = 0
  dfs = lambda do |a, fa|
    size[a] = 1
    ok = true
    g[a].each do |b|
      next if b == fa

      t = dfs.call(b, a)
      ok = ok && t && colors[a] == colors[b]
      size[a] += size[b]
    end
    ans = size[a] if ok && size[a] > ans
    ok
  end
  dfs.call(0, -1)
  ans
end
''')

add("3005_count_elements_with_maximum_frequency", r'''
# LeetCode 3005 - Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/

# @param {Integer[]} nums
# @return {Integer}
def max_frequency_elements(nums)
  cnt = Array.new(101, 0)
  nums.each { |x| cnt[x] += 1 }
  mx = -1
  ans = 0
  cnt.each do |x|
    if mx < x
      mx = x
      ans = x
    elsif mx == x
      ans += x
    end
  end
  ans
end
''')

add("3006_find_beautiful_indices_in_the_given_array_i", r'''
# LeetCode 3006 - Find Beautiful Indices in the Given Array I
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

# @param {String} s
# @param {String} a
# @param {String} b
# @param {Integer} k
# @return {Integer[]}
def beautiful_indices(s, a, b, k)
  lps_a = Array.new(a.length, 0)
  lps_b = Array.new(b.length, 0)
  a_index = []
  b_index = []
  result = []
  build_lps(lps_a, a)
  build_lps(lps_b, b)
  kmp_collect(s, a, lps_a, a_index)
  kmp_collect(s, b, lps_b, b_index)
  i = 0
  j = 0
  while i < a_index.length && j < b_index.length
    if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]
      result << a_index[i]
      i += 1
    elsif a_index[i] - k > b_index[j]
      j += 1
    else
      i += 1
    end
  end
  result
end

def build_lps(lps, pattern)
  l = 0
  i = 1
  s_l = pattern.length
  lps[0] = 0
  while i < s_l
    if pattern[i] == pattern[l]
      l += 1
      lps[i] = l
      i += 1
    elsif l != 0
      l = lps[l - 1]
    else
      lps[i] = l
      i += 1
    end
  end
end

def kmp_collect(s, pat, lps, index)
  s_len = s.length
  pat_l = pat.length
  i = 0
  j = 0
  while s_len - i >= pat_l - j
    if s[i] == pat[j]
      i += 1
      j += 1
    end
    if j == pat_l
      index << i - pat_l
      j = lps[j - 1]
    elsif i < s_len && s[i] != pat[j]
      if j != 0
        j = lps[j - 1]
      else
        i += 1
      end
    end
  end
end
''')

add("3007_maximum_number_that_sum_of_the_prices_is_less_than_or_equal_to_k", r'''
# LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

# @param {Integer} k
# @param {Integer} x
# @return {Integer}
def find_maximum_number(k, x)
  l = 1
  r = 10**17
  while l < r
    mid = (l + r + 1) >> 1
    if price_sum(mid, x) <= k
      l = mid
    else
      r = mid - 1
    end
  end
  l
end

def price_sum(num, x)
  m = 0
  t = num
  while t > 0
    m += 1
    t >>= 1
  end
  f = Array.new(65) { Array.new(65, -1) }
  dfs = lambda do |pos, cnt, limit|
    return cnt if pos == 0
    return f[pos][cnt] if !limit && f[pos][cnt] != -1

    ans = 0
    up = limit ? ((num >> (pos - 1)) & 1) : 1
    (0..up).each do |i|
      v = cnt
      v += 1 if i == 1 && pos % x == 0
      ans += dfs.call(pos - 1, v, limit && i == up)
    end
    f[pos][cnt] = ans unless limit
    ans
  end
  dfs.call(m, 0, true)
end
''')

add("3008_find_beautiful_indices_in_the_given_array_ii", r'''
# LeetCode 3008 - Find Beautiful Indices in the Given Array II
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

# @param {String} s
# @param {String} a
# @param {String} b
# @param {Integer} k
# @return {Integer[]}
def beautiful_indices(s, a, b, k)
  lps_a = Array.new(a.length, 0)
  lps_b = Array.new(b.length, 0)
  a_index = []
  b_index = []
  result = []
  build_lps(lps_a, a)
  build_lps(lps_b, b)
  kmp_collect(s, a, lps_a, a_index)
  kmp_collect(s, b, lps_b, b_index)
  i = 0
  j = 0
  while i < a_index.length && j < b_index.length
    if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]
      result << a_index[i]
      i += 1
    elsif a_index[i] - k > b_index[j]
      j += 1
    else
      i += 1
    end
  end
  result
end

def build_lps(lps, pattern)
  l = 0
  i = 1
  s_l = pattern.length
  lps[0] = 0
  while i < s_l
    if pattern[i] == pattern[l]
      l += 1
      lps[i] = l
      i += 1
    elsif l != 0
      l = lps[l - 1]
    else
      lps[i] = l
      i += 1
    end
  end
end

def kmp_collect(s, pat, lps, index)
  s_len = s.length
  pat_l = pat.length
  i = 0
  j = 0
  while s_len - i >= pat_l - j
    if s[i] == pat[j]
      i += 1
      j += 1
    end
    if j == pat_l
      index << i - pat_l
      j = lps[j - 1]
    elsif i < s_len && s[i] != pat[j]
      if j != 0
        j = lps[j - 1]
      else
        i += 1
      end
    end
  end
end
''')

add("3009_maximum_number_of_intersections_on_the_chart", r'''
# LeetCode 3009 - Maximum Number of Intersections on the Chart
# https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

# @param {Integer[]} y
# @return {Integer}
def max_intersection_count(y)
  n = y.length
  line = Hash.new(0)
  (1...n).each do |i|
    start = 2 * y[i - 1]
    finish = 2 * y[i]
    unless i == n - 1
      if y[i] > y[i - 1]
        finish -= 1
      else
        finish += 1
      end
    end
    a = start
    b = finish
    a, b = b, a if a > b
    line[a] += 1
    line[b + 1] -= 1
  end
  keys = line.keys.sort
  ans = 0
  cur = 0
  keys.each do |key|
    cur += line[key]
    ans = cur if cur > ans
  end
  ans
end
''')

add("3010_divide_an_array_into_subarrays_with_minimum_cost_i", r'''
# LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  a = nums[0]
  b = 100
  c = 100
  (1...nums.length).each do |i|
    x = nums[i]
    if x < b
      c = b
      b = x
    elsif x < c
      c = x
    end
  end
  a + b + c
end
''')

add("3011_find_if_array_can_be_sorted", r'''
# LeetCode 3011 - Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/

# @param {Integer[]} nums
# @return {Boolean}
def can_sort_array(nums)
  pre_mx = 0
  i = 0
  n = nums.length
  while i < n
    cnt = popcount(nums[i])
    j = i + 1
    mi = nums[i]
    mx = nums[i]
    while j < n && popcount(nums[j]) == cnt
      mi = nums[j] if nums[j] < mi
      mx = nums[j] if nums[j] > mx
      j += 1
    end
    return false if pre_mx > mi

    pre_mx = mx
    i = j
  end
  true
end

def popcount(x)
  c = 0
  while x != 0
    c += x & 1
    x >>= 1
  end
  c
end
''')

add("3012_minimize_length_of_array_using_operations", r'''
# LeetCode 3012 - Minimize Length of Array Using Operations
# https://leetcode.com/problems/minimize-length-of-array-using-operations/

# @param {Integer[]} nums
# @return {Integer}
def minimum_array_length(nums)
  mi = nums.min
  cnt = 0
  nums.each do |x|
    return 1 if x % mi != 0

    cnt += 1 if x == mi
  end
  (cnt + 1) / 2
end
''')

add("3013_divide_an_array_into_subarrays_with_minimum_cost_ii", r'''
# LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class BITI
  attr_reader :c, :n

  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
  end

  def upd(x, d)
    while x <= @n
      @c[x] += d
      x += x & -x
    end
  end

  def qry(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

class BITL
  attr_reader :c, :n

  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
  end

  def upd(x, d)
    while x <= @n
      @c[x] += d
      x += x & -x
    end
  end

  def qry(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} dist
# @return {Integer}
def minimum_cost(nums, k, dist)
  k -= 1
  n = nums.length
  uniq = nums.sort
  write = 0
  uniq.each do |v|
    if write == 0 || v != uniq[write - 1]
      uniq[write] = v
      write += 1
    end
  end
  uniq = uniq[0...write]
  m = uniq.length
  cnt = BITI.new(m + 2)
  sbit = BITL.new(m + 2)
  (1..[dist + 1, n - 1].min).each do |i|
    r = lower_bound(uniq, nums[i]) + 1
    cnt.upd(r, 1)
    sbit.upd(r, nums[i])
  end
  finish = [dist + 1, n - 1].min
  kk = [k, finish].min
  ans = nums[0] + sum_smallest(cnt, sbit, uniq, m, kk)
  (dist + 2...n).each do |i|
    rem = nums[i - dist - 1]
    r1 = lower_bound(uniq, rem) + 1
    cnt.upd(r1, -1)
    sbit.upd(r1, -rem)
    add = nums[i]
    r2 = lower_bound(uniq, add) + 1
    cnt.upd(r2, 1)
    sbit.upd(r2, add)
    kk = [k, dist + 1].min
    cand = nums[0] + sum_smallest(cnt, sbit, uniq, m, kk)
    ans = cand if cand < ans
  end
  ans
end

def bit_kth(cnt, m, k)
  idx = 0
  bit = 1 << 20
  while bit != 0
    nidx = idx + bit
    if nidx <= m && cnt.c[nidx] < k
      k -= cnt.c[nidx]
      idx = nidx
    end
    bit >>= 1
  end
  idx + 1
end

def sum_smallest(cnt, sbit, uniq, m, kk)
  return 0 if kk <= 0

  r = bit_kth(cnt, m, kk)
  before = cnt.qry(r - 1)
  s = sbit.qry(r - 1)
  s += (kk - before) * uniq[r - 1]
  s
end

def lower_bound(arr, x)
  lo = 0
  hi = arr.length
  while lo < hi
    mid = (lo + hi) >> 1
    if arr[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
''')

add("3014_minimum_number_of_pushes_to_type_word_i", r'''
# LeetCode 3014 - Minimum Number of Pushes to Type Word I
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  n = word.length
  ans = 0
  k = 1
  (n / 8).times do
    ans += k * 8
    k += 1
  end
  ans + k * (n % 8)
end
''')

add("3015_count_the_number_of_houses_at_a_certain_distance_i", r'''
# LeetCode 3015 - Count the Number of Houses at a Certain Distance I
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer[]}
def count_of_pairs(n, x, y)
  ans = Array.new(n, 0)
  x -= 1
  y -= 1
  n.times do |i|
    (i + 1...n).each do |j|
      a = j - i
      b = (x - i).abs + (y - j).abs + 1
      c = (x - j).abs + (y - i).abs + 1
      ans[[a, b, c].min - 1] += 2
    end
  end
  ans
end
''')

add("3016_minimum_number_of_pushes_to_type_word_ii", r'''
# LeetCode 3016 - Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  cnt = Array.new(26, 0)
  word.each_char { |ch| cnt[ch.ord - 97] += 1 }
  cnt.sort!
  ans = 0
  26.times { |i| ans += (i / 8 + 1) * cnt[26 - i - 1] }
  ans
end
''')

add("3017_count_the_number_of_houses_at_a_certain_distance_ii", r'''
# LeetCode 3017 - Count the Number of Houses at a Certain Distance II
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer[]}
def count_of_pairs(n, x, y)
  x, y = y, x if x > y
  a = Array.new(n, 0)
  (1..n).each do |i|
    a[0] += 2
    a[[i - 1, (i - y).abs + x].min] -= 1
    a[[n - i, (i - x).abs + 1 + (n - y)].min] -= 1
    a[[(i - x).abs, (y - i).abs + 1].min] += 1
    a[[(i - x).abs + 1, (y - i).abs].min] += 1
    r = [x - i, 0].max + [i - y, 0].max
    a[r + ((y - x) / 2)] -= 1
    a[r + ((y - x + 1) / 2)] -= 1
  end
  (1...n).each { |i| a[i] += a[i - 1] }
  a
end
''')

add("3018_maximum_number_of_removal_queries_that_can_be_processed_i", r'''
# LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
# https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer}
def maximum_processable_queries(nums, queries)
  n = nums.length
  f = Array.new(n) { Array.new(n, 0) }
  m = queries.length
  n.times do |i|
    (n - 1).downto(i) do |j|
      if i > 0
        t = f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0
        f[i][j] = [f[i][j], f[i - 1][j] + t].max
      end
      if j + 1 < n
        t = f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0
        f[i][j] = [f[i][j], f[i][j + 1] + t].max
      end
      return m if f[i][j] == m
    end
  end
  ans = 0
  n.times do |i|
    t = f[i][i] < m && nums[i] >= queries[f[i][i]] ? 1 : 0
    ans = [ans, f[i][i] + t].max
  end
  ans
end
''')

add("3019_number_of_changing_keys", r'''
# LeetCode 3019 - Number of Changing Keys
# https://leetcode.com/problems/number-of-changing-keys/

# @param {String} s
# @return {Integer}
def count_key_changes(s)
  s = s.downcase
  ans = 0
  (1...s.length).each { |i| ans += 1 if s[i] != s[i - 1] }
  ans
end
''')

add("3020_find_the_maximum_number_of_elements_in_subset", r'''
# LeetCode 3020 - Find the Maximum Number of Elements in Subset
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ones = cnt[1]
  ans = ones - ((ones % 2) ^ 1)
  cnt.delete(1)
  cnt.each_key do |start|
    x = start
    t = 0
    while cnt[x] > 1
      x *= x
      t += 2
    end
    if cnt[x] > 0
      t += 1
    else
      t -= 1
    end
    ans = t if t > ans
  end
  ans
end
''')

add("3021_alice_and_bob_playing_flower_game", r'''
# LeetCode 3021 - Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game/

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def flower_game(n, m)
  a1 = (n + 1) / 2
  b1 = (m + 1) / 2
  a2 = n / 2
  b2 = m / 2
  a1 * b2 + a2 * b1
end
''')

add("3022_minimize_or_of_remaining_elements_using_operations", r'''
# LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_or_after_operations(nums, k)
  ans = 0
  rans = 0
  29.downto(0) do |i|
    test = ans + (1 << i)
    cnt = 0
    val = 0
    nums.each do |num|
      if val == 0
        val = test & num
      else
        val &= test & num
      end
      cnt += 1 if val != 0
    end
    if cnt > k
      rans += 1 << i
    else
      ans += 1 << i
    end
  end
  rans
end
''')

add("3023_find_pattern_in_infinite_stream_i", r'''
# LeetCode 3023 - Find Pattern in Infinite Stream I
# https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

# @param {Object} stream
# @param {Integer[]} pattern
# @return {Integer}
def find_pattern(stream, pattern)
  a = 0
  b = 0
  m = pattern.length
  half = m >> 1
  mask1 = (1 << half) - 1
  mask2 = (1 << (m - half)) - 1
  half.times { |i| a |= pattern[i] << (half - 1 - i) }
  (half...m).each { |i| b |= pattern[i] << (m - 1 - i) }
  x = 0
  y = 0
  i = 1
  loop do
    v = stream.next
    y = y << 1 | v
    v = (y >> (m - half)) & 1
    y &= mask2
    x = x << 1 | v
    x &= mask1
    return i - m if i >= m && a == x && b == y

    i += 1
  end
end
''')

add("3024_type_of_triangle", r'''
# LeetCode 3024 - Type of Triangle
# https://leetcode.com/problems/type-of-triangle/

# @param {Integer[]} nums
# @return {String}
def triangle_type(nums)
  nums = nums.sort
  return "none" if nums[0] + nums[1] <= nums[2]
  return "equilateral" if nums[0] == nums[2]
  return "isosceles" if nums[0] == nums[1] || nums[1] == nums[2]

  "scalene"
end
''')

written = 0
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body)
    written += 1
    print(f"wrote {name}")

print(f"written={written}")
