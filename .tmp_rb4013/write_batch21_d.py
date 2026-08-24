#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3898_find_the_degree_of_each_vertex", r'''
# LeetCode 3898 - Find the Degree of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/

# @param {Integer[][]} matrix
# @return {Integer[]}
def find_degrees(matrix)
  ans = Array.new(matrix.length, 0)
  matrix.each_with_index do |row, i|
    row.each { |x| ans[i] += x }
  end
  ans
end
''')

add("3899_angles_of_a_triangle", r'''
# LeetCode 3899 - Angles of a Triangle
# https://leetcode.com/problems/angles-of-a-triangle/

# @param {Float[]} sides
# @return {Float[]}
def internal_angles(sides)
  sides = sides.sort
  a, b, c = sides[0], sides[1], sides[2]
  return [] if a + b <= c
  pi = Math.acos(-1.0)
  aa = Math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / pi
  bb = Math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / pi
  cc = 180.0 - aa - bb
  [aa, bb, cc]
end
''')

add("3900_longest_balanced_substring_after_one_swap", r'''
# LeetCode 3900 - Longest Balanced Substring After One Swap
# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  cnt0 = s.count("0")
  cnt1 = s.length - cnt0
  pos = {}
  pos[0] = [-1]
  ans = 0
  pre = 0
  s.length.times do |i|
    pre += s[i] == "1" ? 1 : -1
    pos[pre] ||= []
    pos[pre] << i
    ans = [ans, i - pos[pre][0]].max
    if pos.key?(pre - 2)
      p = pos[pre - 2]
      if (i - p[0] - 2) / 2 < cnt0
        ans = [ans, i - p[0]].max
      elsif p.length > 1
        ans = [ans, i - p[1]].max
      end
    end
    if pos.key?(pre + 2)
      p = pos[pre + 2]
      if (i - p[0] - 2) / 2 < cnt1
        ans = [ans, i - p[0]].max
      elsif p.length > 1
        ans = [ans, i - p[1]].max
      end
    end
  end
  ans
end
''')

add("3901_good_subsequence_queries", r'''
# LeetCode 3901 - Good Subsequence Queries
# https://leetcode.com/problems/good-subsequence-queries/

def gcd3901(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

class SegmentTree3901
  attr_reader :tr

  def initialize(n)
    @tr = Array.new(n << 2) { { l: 0, r: 0, g: 0 } }
    build(1, 1, n)
  end

  def build(u, l, r)
    @tr[u][:l] = l
    @tr[u][:r] = r
    @tr[u][:g] = 0
    return if l == r
    mid = (l + r) >> 1
    build(u << 1, l, mid)
    build(u << 1 | 1, mid + 1, r)
  end

  def pushup(u)
    @tr[u][:g] = gcd3901(@tr[u << 1][:g], @tr[u << 1 | 1][:g])
  end

  def modify(u, x, v)
    if @tr[u][:l] == @tr[u][:r]
      @tr[u][:g] = v
      return
    end
    mid = (@tr[u][:l] + @tr[u][:r]) >> 1
    if x <= mid
      modify(u << 1, x, v)
    else
      modify(u << 1 | 1, x, v)
    end
    pushup(u)
  end

  def query(u, l, r)
    return 0 if l > r
    return @tr[u][:g] if @tr[u][:l] >= l && @tr[u][:r] <= r
    mid = (@tr[u][:l] + @tr[u][:r]) >> 1
    return query(u << 1, l, r) if r <= mid
    return query(u << 1 | 1, l, r) if l > mid
    gcd3901(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
  end
end

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer}
def count_good_subseq(nums, p, queries)
  n = nums.length
  tree = SegmentTree3901.new(n)
  cnt = 0
  n.times do |i|
    if nums[i] % p == 0
      tree.modify(1, i + 1, nums[i])
      cnt += 1
    end
  end
  ans = 0
  queries.each do |q|
    idx, val = q[0], q[1]
    if nums[idx] % p == 0
      tree.modify(1, idx + 1, 0)
      cnt -= 1
    end
    if val % p == 0
      tree.modify(1, idx + 1, val)
      cnt += 1
    end
    nums[idx] = val
    next if tree.tr[1][:g] != p
    if cnt < n || n > 6
      ans += 1
      next
    end
    (1..n).each do |i|
      left_g = tree.query(1, 1, i - 1)
      right_g = tree.query(1, i + 1, n)
      if gcd3901(left_g, right_g) == p
        ans += 1
        break
      end
    end
  end
  ans
end
''')

add("3902_zigzag_level_sum_of_binary_tree", r'''
# LeetCode 3902 - Zigzag Level Sum of Binary Tree
# https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[]}
def zigzag_level_sum(root)
  ans = []
  q = [root]
  left = true
  until q.empty?
    nq = []
    q.each do |node|
      nq << node.left if node.left
      nq << node.right if node.right
    end
    m = q.length
    s = 0
    m.times do |i|
      node = left ? q[i] : q[m - i - 1]
      child = left ? node.left : node.right
      break unless child
      s += node.val
    end
    ans << s
    left = !left
    q = nq
  end
  ans
end
''')

add("3903_smallest_stable_index_i", r'''
# LeetCode 3903 - Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def first_stable_index(nums, k)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [right[i + 1], nums[i]].min }
  left = 0
  n.times do |i|
    left = [left, nums[i]].max
    return i if left - right[i] <= k
  end
  -1
end
''')

add("3904_smallest_stable_index_ii", r'''
# LeetCode 3904 - Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def first_stable_index(nums, k)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [right[i + 1], nums[i]].min }
  left = 0
  n.times do |i|
    left = [left, nums[i]].max
    return i if left - right[i] <= k
  end
  -1
end
''')

add("3905_multi_source_flood_fill", r'''
# LeetCode 3905 - Multi Source Flood Fill
# https://leetcode.com/problems/multi-source-flood-fill/

# @param {Integer} n
# @param {Integer} m
# @param {Integer[][]} sources
# @return {Integer[][]}
def color_grid(n, m, sources)
  ans = Array.new(n) { Array.new(m, 0) }
  q = sources.map(&:dup)
  dirs = [-1, 0, 1, 0, -1]
  q.each { |s| ans[s[0]][s[1]] = s[2] }
  until q.empty?
    vis = {}
    q.each do |curr|
      r, c, color = curr[0], curr[1], curr[2]
      4.times do |i|
        x = r + dirs[i]
        y = c + dirs[i + 1]
        if x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0
          key = (x << 32) | (y & 0xFFFFFFFF)
          vis[key] = color if !vis.key?(key) || color > vis[key]
        end
      end
    end
    q = []
    vis.each do |key, color|
      x = key >> 32
      y = key & 0xFFFFFFFF
      ans[x][y] = color
      q << [x, y, color]
    end
  end
  ans
end
''')

add("3906_count_good_integers_on_a_grid_path", r'''
# LeetCode 3906 - Count Good Integers on a Grid Path
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/

# @param {Integer} l
# @param {Integer} r
# @param {String} directions
# @return {Integer}
def count_good_integers_on_path(l, r, directions)
  key = Array.new(16, false)
  row = 0
  col = 0
  key[0] = true
  directions.each_char do |c|
    if c == "D"
      row += 1
    else
      col += 1
    end
    key[row * 4 + col] = true
  end
  s = ""
  f = []
  dfs = nil
  dfs = lambda do |pos, last, lim|
    return 1 if pos == 16
    return f[pos][last] if !lim && f[pos][last] != -1
    res = 0
    start = key[pos] ? last : 0
    endv = lim ? s[pos].ord - 48 : 9
    (start..endv).each do |i|
      next_last = key[pos] ? i : last
      res += dfs.call(pos + 1, next_last, lim && i == endv)
    end
    f[pos][last] = res unless lim
    res
  end
  calc = lambda do |x|
    return 0 if x < 0
    t = x.to_s
    s = "0" * (16 - t.length) + t
    f = Array.new(16) { Array.new(10, -1) }
    dfs.call(0, 0, true)
  end
  calc.call(r) - calc.call(l - 1)
end
''')

add("3907_count_smaller_elements_with_opposite_parity", r'''
# LeetCode 3907 - Count Smaller Elements With Opposite Parity
# https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class BIT3907
  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
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
# @return {Integer[]}
def count_smaller_opposite_parity(nums)
  n = nums.length
  sorted_nums = nums.sort
  m = 0
  sorted_nums.length.times do |i|
    if i == 0 || sorted_nums[i] != sorted_nums[i - 1]
      sorted_nums[m] = sorted_nums[i]
      m += 1
    end
  end
  sorted_nums = sorted_nums[0, m]
  bits = [BIT3907.new(m), BIT3907.new(m)]
  ans = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    lo = 0
    hi = sorted_nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sorted_nums[mid] < nums[i]
        lo = mid + 1
      else
        hi = mid
      end
    end
    x = lo + 1
    ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1)
    bits[nums[i] & 1].update(x, 1)
  end
  ans
end
''')

add("3908_valid_digit_number", r'''
# LeetCode 3908 - Valid Digit Number
# https://leetcode.com/problems/valid-digit-number/

# @param {Integer} n
# @param {Integer} x
# @return {Boolean}
def valid_digit(n, x)
  has_x = false
  while n > 9
    has_x ||= n % 10 == x
    n /= 10
  end
  has_x && n != x
end
''')

add("3909_compare_sums_of_bitonic_parts", r'''
# LeetCode 3909 - Compare Sums of Bitonic Parts
# https://leetcode.com/problems/compare-sums-of-bitonic-parts/

# @param {Integer[]} nums
# @return {Integer}
def compare_bitonic_sums(nums)
  l = nums[0]
  r = nums.sum
  (1...nums.length).each do |i|
    break if nums[i - 1] > nums[i]
    l += nums[i]
    r -= nums[i - 1]
  end
  return -1 if l == r
  l > r ? 0 : 1
end
''')

add("3910_count_connected_subgraphs_with_even_node_sum", r'''
# LeetCode 3910 - Count Connected Subgraphs with Even Node Sum
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def even_sum_subgraphs(nums, edges)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  m = (1 << n) - 1
  vis = 0
  dfs = nil
  dfs = lambda do |u|
    vis |= 1 << u
    g[u].each do |v|
      dfs.call(v) if ((vis >> v) & 1) == 0
    end
  end
  ans = 0
  (1..m).each do |sub|
    s = 0
    n.times { |i| s += nums[i] if ((sub >> i) & 1) != 0 }
    next if s.odd?
    vis = m ^ sub
    start = sub.bit_length - 1
    start = 0 if sub == 0
    dfs.call(start)
    ans += 1 if vis == m
  end
  ans
end
''')

add("3911_k_th_smallest_remaining_even_integer_in_subarray_queries", r'''
# LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

def upper_bound3911(a, x)
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

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def kth_smallest_even(nums, queries)
  n = nums.length
  even_prefix = Array.new(n + 1, 0)
  n.times { |i| even_prefix[i + 1] = even_prefix[i] + (nums[i].even? ? 1 : 0) }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    l, r, k = q[0], q[1], q[2]
    lo = 1
    hi = k + (r - l + 1)
    while lo < hi
      mid = (lo + hi) / 2
      pos = upper_bound3911(nums, 2 * mid)
      pos = r + 1 if pos > r + 1
      removed = pos > l ? even_prefix[pos] - even_prefix[l] : 0
      if mid - removed >= k
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans[qi] = 2 * lo
  end
  ans
end
''')

add("3912_valid_elements_in_an_array", r'''
# LeetCode 3912 - Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_valid_elements(nums)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [right[i + 1], nums[i]].max }
  left = 0
  ans = []
  n.times do |i|
    x = nums[i]
    ans << x if x > left || i == n - 1 || x > right[i + 1]
    left = [left, x].max
  end
  ans
end
''')

add("3913_sort_vowels_by_frequency", r'''
# LeetCode 3913 - Sort Vowels by Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/

# @param {String} s
# @return {String}
def sort_vowels(s)
  st = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  vowels = []
  cnt = {}
  s.each_char do |c|
    next unless st[c]
    unless cnt.key?(c)
      vowels << c
      cnt[c] = 0
    end
    cnt[c] += 1
  end
  vowels.sort_by! { |ch| -cnt[ch] }
  ans = s.chars
  i = 0
  s.length.times do |k|
    next unless st[s[k]]
    ch = vowels[i]
    ans[k] = ch
    cnt[ch] -= 1
    i += 1 if cnt[ch] == 0
  end
  ans.join
end
''')

add("3914_minimum_operations_to_make_array_non_decreasing", r'''
# LeetCode 3914 - Minimum Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  (1...nums.length).each { |i| ans += [0, nums[i - 1] - nums[i]].max }
  ans
end
''')

add("3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k", r'''
# LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Fenwick3915
  def initialize(n)
    @f = Array.new(n, 0)
  end

  def update(i, val)
    while i < @f.length
      @f[i] = [@f[i], val].max
      i += i & -i
    end
  end

  def pre_max(i)
    res = 0
    while i > 0
      res = [res, @f[i]].max
      i &= i - 1
    end
    res
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_alternating_sum(nums, k)
  sorted_nums = nums.sort
  m = 0
  sorted_nums.length.times do |i|
    if i == 0 || sorted_nums[i] != sorted_nums[i - 1]
      sorted_nums[m] = sorted_nums[i]
      m += 1
    end
  end
  sorted_nums = sorted_nums[0, m]
  n = nums.length
  f_inc = Array.new(n, 0)
  f_dec = Array.new(n, 0)
  inc = Fenwick3915.new(m + 1)
  dec = Fenwick3915.new(m + 1)
  ans = 0
  ranks = Array.new(n, 0)
  n.times do |i|
    x = nums[i]
    if i >= k
      j = ranks[i - k]
      inc.update(m - j, f_inc[i - k])
      dec.update(j + 1, f_dec[i - k])
    end
    lo = 0
    hi = sorted_nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sorted_nums[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    ranks[i] = lo
    f_inc[i] = dec.pre_max(lo) + x
    f_dec[i] = inc.pre_max(m - 1 - lo) + x
    ans = [ans, [f_inc[i], f_dec[i]].max].max
  end
  ans
end
''')

add("3916_number_of_zigzag_arrays_iii", r'''
# LeetCode 3916 - Number of ZigZag Arrays III
# https://leetcode.com/problems/number-of-zigzag-arrays-iii/

def powm3916(a, e, mod)
  res = 1
  while e > 0
    res = res * a % mod if e.odd?
    a = a * a % mod
    e >>= 1
  end
  res
end

# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  points = n + 1
  values = Array.new(points + 1, 0)
  (1..points).each do |m|
    up = Array.new(m, 0)
    down = Array.new(m, 0)
    m.times do |value|
      up[value] = value
      down[value] = m - 1 - value
    end
    (3..n).each do |_length|
      next_up = Array.new(m, 0)
      next_down = Array.new(m, 0)
      prefix = 0
      m.times do |value|
        next_up[value] = prefix
        prefix = (prefix + down[value]) % mod
      end
      suffix = 0
      (m - 1).downto(0) do |value|
        next_down[value] = suffix
        suffix = (suffix + up[value]) % mod
      end
      up = next_up
      down = next_down
    end
    m.times { |value| values[m] = (values[m] + up[value] + down[value]) % mod }
  end
  x = (r - l + 1) % mod
  return values[r - l + 1] if r - l + 1 <= points
  prefix_a = Array.new(points + 2, 0)
  suffix_a = Array.new(points + 2, 0)
  prefix_a[0] = 1
  (1..points).each { |i| prefix_a[i] = prefix_a[i - 1] * ((x - i + mod) % mod) % mod }
  suffix_a[points + 1] = 1
  points.downto(1) { |i| suffix_a[i] = suffix_a[i + 1] * ((x - i + mod) % mod) % mod }
  factorial = Array.new(points + 1, 0)
  factorial[0] = 1
  (1..points).each { |i| factorial[i] = factorial[i - 1] * i % mod }
  answer = 0
  (1..points).each do |i|
    numerator = prefix_a[i - 1] * suffix_a[i + 1] % mod
    denominator = factorial[i - 1] * factorial[points - i] % mod
    term = values[i] * numerator % mod * powm3916(denominator, mod - 2, mod) % mod
    if (points - i).odd?
      answer -= term
    else
      answer += term
    end
    answer %= mod
  end
  answer += mod if answer < 0
  answer
end
''')

add("3917_count_indices_with_opposite_parity", r'''
# LeetCode 3917 - Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/

# @param {Integer[]} nums
# @return {Integer[]}
def count_opposite_parity(nums)
  cnt = [0, 0]
  nums.each { |x| cnt[x & 1] += 1 }
  n = nums.length
  ans = Array.new(n, 0)
  n.times do |i|
    x = nums[i]
    cnt[x & 1] -= 1
    ans[i] = cnt[(x & 1) ^ 1]
  end
  ans
end
''')

add("3918_sum_of_primes_between_number_and_its_reverse", r'''
# LeetCode 3918 - Sum of Primes Between Number and Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

$is_prime3918 = nil

def init3918
  return unless $is_prime3918.nil?
  $is_prime3918 = Array.new(1001, true)
  $is_prime3918[0] = $is_prime3918[1] = false
  i = 2
  while i * i <= 1000
    if $is_prime3918[i]
      j = i * i
      while j <= 1000
        $is_prime3918[j] = false
        j += i
      end
    end
    i += 1
  end
end

# @param {Integer} n
# @return {Integer}
def sum_of_primes_in_range(n)
  init3918
  r = 0
  x = n
  while x > 0
    r = r * 10 + x % 10
    x /= 10
  end
  low = [n, r].min
  high = [n, r].max
  ans = 0
  (low..high).each { |v| ans += v if $is_prime3918[v] }
  ans
end
''')

add("3919_minimum_cost_to_move_between_indices", r'''
# LeetCode 3919 - Minimum Cost to Move Between Indices
# https://leetcode.com/problems/minimum-cost-to-move-between-indices/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def min_cost(nums, queries)
  n = nums.length
  s1 = Array.new(n, 0)
  s2 = Array.new(n, 0)
  (1...n).each do |i|
    c1 = 1
    c1 = nums[i] - nums[i - 1] if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]
    c2 = 1
    c2 = nums[i] - nums[i - 1] if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]
    s1[i] = s1[i - 1] + c1
    s2[i] = s2[i - 1] + c2
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    l, r = q[0], q[1]
    ans[i] = l < r ? s1[r] - s1[l] : s2[l] - s2[r]
  end
  ans
end
''')

add("3920_maximize_fixed_points_after_deletions", r'''
# LeetCode 3920 - Maximize Fixed Points After Deletions
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/

# @param {Integer[]} nums
# @return {Integer}
def max_fixed_points(nums)
  tails = []
  nums.each_with_index do |val, i|
    next if i < val
    d = i - val
    lo = 0
    hi = tails.length
    while lo < hi
      mid = (lo + hi) >> 1
      if tails[mid] < d
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == tails.length
      tails << d
    else
      tails[lo] = d
    end
  end
  tails.length
end
''')

add("3921_score_validator", r'''
# LeetCode 3921 - Score Validator
# https://leetcode.com/problems/score-validator/

# @param {String[]} events
# @return {Integer[]}
def score_validator(events)
  score = 0
  counter = 0
  events.each do |event_str|
    is_num = !event_str.empty?
    num = 0
    start = 0
    if is_num && event_str[0] == "-"
      start = 1
    end
    (start...event_str.length).each do |i|
      if event_str[i] < "0" || event_str[i] > "9"
        is_num = false
        break
      end
      num = num * 10 + (event_str[i].ord - 48)
    end
    if is_num && !(start == 1 && event_str.length == 1)
      num = -num if start == 1
      score += num
    elsif event_str == "W"
      counter += 1
      break if counter == 10
    else
      score += 1
    end
  end
  [score, counter]
end
''')

add("3922_minimum_flips_to_make_binary_string_coherent", r'''
# LeetCode 3922 - Minimum Flips to Make Binary String Coherent
# https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

# @param {String} s
# @return {Integer}
def min_flips(s)
  ones = s.count("1")
  answer = ones
  answer = ones - 1 if ones > 0
  zeros = s.length - ones
  answer = [answer, zeros].min
  if s.length >= 2
    cost = 0
    s.length.times do |i|
      want = (i == 0 || i == s.length - 1) ? "1" : "0"
      cost += 1 if s[i] != want
    end
    answer = [answer, cost].min
  end
  answer
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch21_d written={written}")


if __name__ == "__main__":
    main()
