#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3116_kth_smallest_amount_with_single_denomination_combination", r'''
# LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def find_kth_smallest(coins, k)
  gcdll = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  lcmll = lambda { |a, b| a / gcdll.call(a, b) * b }
  bit_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  n = coins.length

  check = lambda do |mx|
    cnt = 0
    (1...(1 << n)).each do |i|
      v = 1
      n.times do |j|
        if ((i >> j) & 1) != 0
          v = lcmll.call(v, coins[j])
          break if v > mx
        end
      end
      m = bit_count.call(i)
      if m.odd?
        cnt += mx / v
      else
        cnt -= mx / v
      end
    end
    cnt >= k
  end

  lo = 1
  hi = 100_000_000_000
  while lo < hi
    mid = lo + (hi - lo) / 2
    if check.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3117_minimum_sum_of_values_by_dividing_array", r'''
# LeetCode 3117 - Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

# @param {Integer[]} nums
# @param {Integer[]} and_values
# @return {Integer}
def minimum_value_sum(nums, and_values)
  inf = 1 << 29
  n = nums.length
  m = and_values.length
  f = {}

  dfs = lambda do |i, j, a|
    return inf if n - i < m - j
    return i == n ? 0 : inf if j == m
    a &= nums[i]
    return inf if a < and_values[j]
    key = [i, j, a]
    return f[key] if f.key?(key)
    ans = dfs.call(i + 1, j, a)
    ans = [ans, dfs.call(i + 1, j + 1, -1) + nums[i]].min if a == and_values[j]
    f[key] = ans
    ans
  end

  ans = dfs.call(0, 0, -1)
  ans < inf ? ans : -1
end
''')

add("3119_maximum_number_of_potholes_that_can_be_fixed", r'''
# LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
# https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

# @param {String} road
# @param {Integer} budget
# @return {Integer}
def max_potholes(road, budget)
  road = road + "."
  n = road.length
  cnt = Array.new(n, 0)
  k = 0
  ans = 0
  road.each_char do |c|
    if c == "x"
      k += 1
    elsif k > 0
      cnt[k] += 1
      k = 0
    end
  end
  k = n - 1
  while k > 0 && budget > 0
    t = [budget / (k + 1), cnt[k]].min
    ans += t * k
    budget -= t * (k + 1)
    cnt[k - 1] += cnt[k] - t
    k -= 1
  end
  ans
end
''')

add("3120_count_the_number_of_special_characters_i", r'''
# LeetCode 3120 - Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
  s = Array.new(128, false)
  word.each_char { |ch| s[ch.ord] = true }
  ans = 0
  26.times { |i| ans += 1 if s[97 + i] && s[65 + i] }
  ans
end
''')

add("3121_count_the_number_of_special_characters_ii", r'''
# LeetCode 3121 - Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
  first = Array.new(128, 0)
  last = Array.new(128, 0)
  word.each_char.with_index do |ch, i|
    c = ch.ord
    first[c] = i + 1 if first[c] == 0
    last[c] = i + 1
  end
  ans = 0
  26.times { |i| ans += 1 if last[97 + i] > 0 && last[97 + i] < first[65 + i] }
  ans
end
''')

add("3122_minimum_number_of_operations_to_satisfy_conditions", r'''
# LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  inf = 1 << 29
  f = Array.new(n) { Array.new(10, inf) }
  n.times do |i|
    cnt = Array.new(10, 0)
    m.times { |j| cnt[grid[j][i]] += 1 }
    if i == 0
      10.times { |j| f[i][j] = m - cnt[j] }
    else
      10.times do |j|
        10.times do |k|
          f[i][j] = [f[i][j], f[i - 1][k] + m - cnt[j]].min if j != k
        end
      end
    end
  end
  f[n - 1].min
end
''')

add("3123_find_edges_in_shortest_paths", r'''
# LeetCode 3123 - Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean[]}
def find_answer(n, edges)
  g = Array.new(n) { [] }
  edges.each_with_index do |(a, b, w), i|
    g[a] << [b, w, i]
    g[b] << [a, w, i]
  end
  inf = 1 << 30
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    da, a = heap_pop_pair(pq)
    next if da > dist[a]
    g[a].each do |b, w, _|
      if dist[b] > dist[a] + w
        dist[b] = dist[a] + w
        heap_push_pair(pq, [dist[b], b])
      end
    end
  end
  ans = Array.new(edges.length, false)
  return ans if dist[n - 1] == inf
  q = [n - 1]
  until q.empty?
    a = q.shift
    g[a].each do |b, w, i|
      if dist[a] == dist[b] + w
        ans[i] = true
        q << b
      end
    end
  end
  ans
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

add("3125_maximum_number_that_makes_result_of_bitwise_and_zero", r'''
# LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
# https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

# @param {Integer} n
# @return {Integer}
def max_number(n)
  length = 0
  x = n
  while x > 0
    length += 1
    x >>= 1
  end
  (1 << (length - 1)) - 1
end
''')

add("3127_make_a_square_with_the_same_color", r'''
# LeetCode 3127 - Make a Square with the Same Color
# https://leetcode.com/problems/make-a-square-with-the-same-color/

# @param {String[][]} grid
# @return {Boolean}
def can_make_square(grid)
  dirs = [0, 0, 1, 1, 0]
  2.times do |i|
    2.times do |j|
      cnt1 = 0
      cnt2 = 0
      4.times do |k|
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if grid[x][y] == "W"
          cnt1 += 1
        else
          cnt2 += 1
        end
      end
      return true if cnt1 != cnt2
    end
  end
  false
end
''')

add("3128_right_triangles", r'''
# LeetCode 3128 - Right Triangles
# https://leetcode.com/problems/right-triangles/

# @param {Integer[][]} grid
# @return {Integer}
def number_of_right_triangles(grid)
  m = grid.length
  n = grid[0].length
  rows = Array.new(m, 0)
  cols = Array.new(n, 0)
  m.times do |i|
    n.times do |j|
      rows[i] += grid[i][j]
      cols[j] += grid[i][j]
    end
  end
  ans = 0
  m.times do |i|
    n.times do |j|
      ans += (rows[i] - 1) * (cols[j] - 1) if grid[i][j] == 1
    end
  end
  ans
end
''')

add("3129_find_all_possible_stable_binary_arrays_i", r'''
# LeetCode 3129 - Find All Possible Stable Binary Arrays I
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

# @param {Integer} zero
# @param {Integer} one
# @param {Integer} limit
# @return {Integer}
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  f = Array.new(zero + 1) { Array.new(one + 1) { [-1, -1] } }

  dfs = lambda do |i, j, k|
    return 0 if i < 0 || j < 0
    return (k == 1 && j <= limit) ? 1 : 0 if i == 0
    return (k == 0 && i <= limit) ? 1 : 0 if j == 0
    return f[i][j][k] if f[i][j][k] != -1
    res = if k == 0
            (dfs.call(i - 1, j, 0) + dfs.call(i - 1, j, 1) - dfs.call(i - limit - 1, j, 1) + mod) % mod
          else
            (dfs.call(i, j - 1, 0) + dfs.call(i, j - 1, 1) - dfs.call(i, j - limit - 1, 0) + mod) % mod
          end
    f[i][j][k] = res
    res
  end

  (dfs.call(zero, one, 0) + dfs.call(zero, one, 1)) % mod
end
''')

add("3130_find_all_possible_stable_binary_arrays_ii", r'''
# LeetCode 3130 - Find All Possible Stable Binary Arrays II
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

# @param {Integer} zero
# @param {Integer} one
# @param {Integer} limit
# @return {Integer}
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  f = Array.new(zero + 1) { Array.new(one + 1) { [-1, -1] } }

  dfs = lambda do |i, j, k|
    return 0 if i < 0 || j < 0
    return (k == 1 && j <= limit) ? 1 : 0 if i == 0
    return (k == 0 && i <= limit) ? 1 : 0 if j == 0
    return f[i][j][k] if f[i][j][k] != -1
    res = if k == 0
            (dfs.call(i - 1, j, 0) + dfs.call(i - 1, j, 1) - dfs.call(i - limit - 1, j, 1) + mod) % mod
          else
            (dfs.call(i, j - 1, 0) + dfs.call(i, j - 1, 1) - dfs.call(i, j - limit - 1, 0) + mod) % mod
          end
    f[i][j][k] = res
    res
  end

  (dfs.call(zero, one, 0) + dfs.call(zero, one, 1)) % mod
end
''')

add("3131_find_the_integer_added_to_array_i", r'''
# LeetCode 3131 - Find the Integer Added to Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def added_integer(nums1, nums2)
  nums2.min - nums1.min
end
''')

add("3132_find_the_integer_added_to_array_ii", r'''
# LeetCode 3132 - Find the Integer Added to Array II
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_added_integer(nums1, nums2)
  nums1 = nums1.sort
  nums2 = nums2.sort

  ok = lambda do |x|
    i = 0
    j = 0
    cnt = 0
    while i < nums1.length && j < nums2.length
      if nums2[j] - nums1[i] != x
        cnt += 1
      else
        j += 1
      end
      i += 1
    end
    cnt <= 2
  end

  ans = 1 << 30
  3.times do |t|
    x = nums2[0] - nums1[t]
    ans = [ans, x].min if ok.call(x)
  end
  ans
end
''')

add("3133_minimum_array_end", r'''
# LeetCode 3133 - Minimum Array End
# https://leetcode.com/problems/minimum-array-end/

# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def min_end(n, x)
  n -= 1
  ans = x
  31.times do |i|
    if ((x >> i) & 1) == 0
      ans |= (n & 1) << i
      n >>= 1
    end
  end
  ans |= n << 31
  ans
end
''')

add("3134_find_the_median_of_the_uniqueness_array", r'''
# LeetCode 3134 - Find the Median of the Uniqueness Array
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

# @param {Integer[]} nums
# @return {Integer}
def median_of_uniqueness_array(nums)
  n = nums.length
  m = (1 + n) * n / 2

  check = lambda do |mx|
    cnt = {}
    l = 0
    k = 0
    n.times do |r|
      cnt[nums[r]] = cnt.fetch(nums[r], 0) + 1
      while cnt.length > mx
        y = nums[l]
        l += 1
        nv = cnt[y] - 1
        if nv == 0
          cnt.delete(y)
        else
          cnt[y] = nv
        end
      end
      k += r - l + 1
      return true if k >= (m + 1) / 2
    end
    false
  end

  lo = 1
  hi = n
  while lo < hi
    mid = lo + (hi - lo) / 2
    if check.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3135_equalize_strings_by_adding_or_removing_characters_at_ends", r'''
# LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
# https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

# @param {String} initial
# @param {String} target
# @return {Integer}
def min_operations(initial, target)
  m = initial.length
  n = target.length
  f = Array.new(m + 1) { Array.new(n + 1, 0) }
  mx = 0
  m.times do |i|
    n.times do |j|
      if initial[i] == target[j]
        f[i + 1][j + 1] = f[i][j] + 1
        mx = [mx, f[i + 1][j + 1]].max
      end
    end
  end
  m + n - 2 * mx
end
''')

add("3136_valid_word", r'''
# LeetCode 3136 - Valid Word
# https://leetcode.com/problems/valid-word/

# @param {String} word
# @return {Boolean}
def is_valid(word)
  return false if word.length < 3
  has_vowel = false
  has_consonant = false
  vs = Array.new(26, false)
  "aeiou".each_char { |c| vs[c.ord - 97] = true }
  word.each_char do |c|
    if c =~ /[A-Za-z]/
      lower = c.downcase
      if vs[lower.ord - 97]
        has_vowel = true
      else
        has_consonant = true
      end
    elsif c !~ /\d/
      return false
    end
  end
  has_vowel && has_consonant
end
''')

add("3137_minimum_number_of_operations_to_make_word_k_periodic", r'''
# LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_operations_to_make_k_periodic(word, k)
  cnt = Hash.new(0)
  n = word.length
  mx = 0
  (0...n).step(k) do |i|
    s = word[i, k]
    cnt[s] += 1
    mx = [mx, cnt[s]].max
  end
  n / k - mx
end
''')

add("3138_minimum_length_of_anagram_concatenation", r'''
# LeetCode 3138 - Minimum Length of Anagram Concatenation
# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

# @param {String} s
# @return {Integer}
def min_anagram_length(s)
  n = s.length
  cnt = Array.new(26, 0)
  s.each_char { |ch| cnt[ch.ord - 97] += 1 }

  check = lambda do |k|
    (0...n).step(k) do |i|
      cnt1 = Array.new(26, 0)
      (i...i + k).each { |j| cnt1[s[j].ord - 97] += 1 }
      26.times { |j| return false if cnt1[j] * (n / k) != cnt[j] }
    end
    true
  end

  i = 1
  loop do
    return i if n % i == 0 && check.call(i)
    i += 1
  end
end
''')

add("3139_minimum_cost_to_equalize_array", r'''
# LeetCode 3139 - Minimum Cost to Equalize Array
# https://leetcode.com/problems/minimum-cost-to-equalize-array/

# @param {Integer[]} nums
# @param {Integer} cost1
# @param {Integer} cost2
# @return {Integer}
def min_cost_to_equalize_array(nums, cost1, cost2)
  mod = 1_000_000_007
  n = nums.length
  min_num = nums.min
  max_num = nums.max
  total = nums.sum
  if cost1 * 2 <= cost2 || n < 3
    total_gap = max_num * n - total
    return (cost1 * total_gap) % mod
  end
  ans = 10**18
  (max_num...2 * max_num).each do |target|
    max_gap = target - min_num
    total_gap = target * n - total
    pairs = total_gap / 2
    alt = total_gap - max_gap
    pairs = alt if alt < pairs
    cost = cost1 * (total_gap - 2 * pairs) + cost2 * pairs
    ans = [ans, cost].min
  end
  ans % mod
end
''')

add("3141_maximum_hamming_distances", r'''
# LeetCode 3141 - Maximum Hamming Distances
# https://leetcode.com/problems/maximum-hamming-distances/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer[]}
def max_hamming_distances(nums, m)
  dist = Array.new(1 << m, -1)
  q = []
  nums.each do |x|
    dist[x] = 0
    q << x
  end
  k = 1
  until q.empty?
    t = []
    q.each do |x|
      m.times do |i|
        y = x ^ (1 << i)
        if dist[y] == -1
          dist[y] = k
          t << y
        end
      end
    end
    q = t
    k += 1
  end
  nums.map { |x| m - dist[x ^ ((1 << m) - 1)] }
end
''')

add("3142_check_if_grid_satisfies_conditions", r'''
# LeetCode 3142 - Check if Grid Satisfies Conditions
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

# @param {Integer[][]} grid
# @return {Boolean}
def satisfies_conditions(grid)
  m = grid.length
  n = grid[0].length
  m.times do |i|
    n.times do |j|
      x = grid[i][j]
      return false if i + 1 < m && x != grid[i + 1][j]
      return false if j + 1 < n && x == grid[i][j + 1]
    end
  end
  true
end
''')

add("3143_maximum_points_inside_the_square", r'''
# LeetCode 3143 - Maximum Points Inside the Square
# https://leetcode.com/problems/maximum-points-inside-the-square/

# @param {Integer[][]} points
# @param {String} s
# @return {Integer}
def max_points_inside_square(points, s)
  g = {}
  keys = []
  points.each_with_index do |p, i|
    key = [[p[0], -p[0]].max, [p[1], -p[1]].max].max
    unless g.key?(key)
      g[key] = []
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) / 2
        if keys[mid] < key
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, key)
    end
    g[key] << i
  end
  vis = Array.new(26, false)
  ans = 0
  keys.each do |key|
    lst = g[key]
    lst.each do |i|
      j = s[i].ord - 97
      return ans if vis[j]
      vis[j] = true
    end
    ans += lst.length
  end
  ans
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        written += 1
        print(f"wrote {name}")
    print(f"batch_c written={written}")


if __name__ == "__main__":
    main()
