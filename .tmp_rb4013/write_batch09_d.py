#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


HEAP = r'''
class MinHeap
  def initialize(arr = [])
    @a = arr.dup
    ((@a.length / 2) - 1).downto(0) { |i| down(i) }
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] >= @a[p]

      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && @a[l] < @a[s]
      s = r if r < n && @a[r] < @a[s]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end
'''

add("2595_number_of_even_and_odd_bits", r'''
# LeetCode 2595 - Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/

# @param {Integer} n
# @return {Integer[]}
def even_odd_bit(n)
  even = 0
  odd = 0
  i = 0
  while n > 0
    if (n & 1) != 0
      if i.even?
        even += 1
      else
        odd += 1
      end
    end
    i += 1
    n >>= 1
  end
  [even, odd]
end
''')

add("2596_check_knight_tour_configuration", r'''
# LeetCode 2596 - Check Knight Tour Configuration
# https://leetcode.com/problems/check-knight-tour-configuration/

# @param {Integer[][]} grid
# @return {Boolean}
def check_valid_grid(grid)
  n = grid.length
  return false if grid[0][0] != 0

  pos = Array.new(n * n)
  n.times do |i|
    n.times do |j|
      pos[grid[i][j]] = [i, j]
    end
  end
  dirs = [
    [1, 2], [1, -2], [-1, 2], [-1, -2],
    [2, 1], [2, -1], [-2, 1], [-2, -1]
  ]
  (n * n - 1).times do |v|
    r, c = pos[v]
    ok = false
    dirs.each do |dr, dc|
      if r + dr == pos[v + 1][0] && c + dc == pos[v + 1][1]
        ok = true
        break
      end
    end
    return false unless ok
  end
  true
end
''')

add("2597_the_number_of_beautiful_subsets", r'''
# LeetCode 2597 - The Number of Beautiful Subsets
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def beautiful_subsets(nums, k)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  groups = {}
  freq.each_key do |key|
    rem = key % k
    groups[rem] ||= []
    groups[rem] << key
  end
  ans = 1
  groups.each_value do |vals|
    vals.sort!
    prev_take = 0
    prev_skip = 1
    prev_val = -10**18
    vals.each do |v|
      ways = 1
      freq[v].times { ways *= 2 }
      ways -= 1
      skip = prev_take + prev_skip
      take = ways * prev_skip
      take += ways * prev_take if prev_val + k != v
      prev_take = take
      prev_skip = skip
      prev_val = v
    end
    ans *= prev_take + prev_skip
  end
  ans - 1
end
''')

add("2598_smallest_missing_non_negative_integer_after_operations", r'''
# LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

# @param {Integer[]} nums
# @param {Integer} value
# @return {Integer}
def find_smallest_integer(nums, value)
  cnt = Array.new(value, 0)
  nums.each do |x|
    r = x % value
    r += value if r < 0
    cnt[r] += 1
  end
  mex = 0
  while cnt[mex % value] > 0
    cnt[mex % value] -= 1
    mex += 1
  end
  mex
end
''')

add("2599_make_the_prefix_sum_non_negative", '''
# LeetCode 2599 - Make the Prefix Sum Non-negative
# https://leetcode.com/problems/make-the-prefix-sum-non-negative/
''' + HEAP + r'''
# @param {Integer[]} nums
# @return {Integer}
def make_pref_sum_non_negative(nums)
  h = MinHeap.new
  s = 0
  ans = 0
  nums.each do |x|
    s += x
    h.push(x) if x < 0
    if s < 0
      worst = h.pop
      s -= worst
      ans += 1
    end
  end
  ans
end
''')

add("2600_k_items_with_the_maximum_sum", r'''
# LeetCode 2600 - K Items With the Maximum Sum
# https://leetcode.com/problems/k-items-with-the-maximum-sum/

# @param {Integer} num_ones
# @param {Integer} num_zeros
# @param {Integer} num_neg_ones
# @param {Integer} k
# @return {Integer}
def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k)
  ans = 0
  take = [num_ones, k].min
  ans += take
  k -= take
  take = [num_zeros, k].min
  k -= take
  take = [num_neg_ones, k].min
  ans -= take
  ans
end
''')

add("2601_prime_subtraction_operation", r'''
# LeetCode 2601 - Prime Subtraction Operation
# https://leetcode.com/problems/prime-subtraction-operation/

# @param {Integer[]} nums
# @return {Boolean}
def prime_sub_operation(nums)
  max_v = 0
  nums.each { |x| max_v = x if x > max_v }
  is_p = Array.new(max_v + 1, true)
  is_p[0] = false if max_v >= 0
  is_p[1] = false if max_v >= 1
  i = 2
  while i * i <= max_v
    if is_p[i]
      j = i * i
      while j <= max_v
        is_p[j] = false
        j += i
      end
    end
    i += 1
  end
  primes = (2..max_v).select { |x| is_p[x] }
  prev = 0
  nums.each do |x|
    need = x - prev
    best = -1
    primes.each do |p|
      break if p >= need

      best = p
    end
    cur = best < 0 ? x : x - best
    return false if cur <= prev

    prev = cur
  end
  true
end
''')

add("2602_minimum_operations_to_make_all_array_elements_equal", r'''
# LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def min_operations(nums, queries)
  nums = nums.sort
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }

  lower_bound = lambda do |x|
    lo = 0
    hi = n
    while lo < hi
      mid = (lo + hi) >> 1
      if nums[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  queries.map do |q|
    i = lower_bound.call(q)
    left = q * i - pref[i]
    right = pref[n] - pref[i] - q * (n - i)
    left + right
  end
end
''')

add("2603_collect_coins_in_a_tree", r'''
# LeetCode 2603 - Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/

# @param {Integer[]} coins
# @param {Integer[][]} edges
# @return {Integer}
def collect_the_coins(coins, edges)
  n = coins.length
  g = Array.new(n) { {} }
  edges.each do |a, b|
    g[a][b] = true
    g[b][a] = true
  end
  deg = Array.new(n) { |i| g[i].size }
  q = []
  n.times { |i| q << i if deg[i] == 1 && coins[i] == 0 }
  until q.empty?
    u = q.shift
    g[u].keys.each do |v|
      g[v].delete(u)
      deg[v] -= 1
      q << v if deg[v] == 1 && coins[v] == 0
    end
    g[u].clear
    deg[u] = 0
  end
  2.times do
    leaves = (0...n).select { |i| deg[i] == 1 }
    leaves.each do |u|
      g[u].keys.each do |v|
        g[v].delete(u)
        deg[v] -= 1
      end
      g[u].clear
      deg[u] = 0
    end
  end
  remain = 0
  n.times { |i| remain += g[i].size }
  remain
end
''')

add("2604_minimum_time_to_eat_all_grains", r'''
# LeetCode 2604 - Minimum Time to Eat All Grains
# https://leetcode.com/problems/minimum-time-to-eat-all-grains/

# @param {Integer[]} hens
# @param {Integer[]} grains
# @return {Integer}
def minimum_time(hens, grains)
  hens = hens.sort
  grains = grains.sort

  ok = lambda do |t|
    j = 0
    hens.each do |h|
      return true if j >= grains.length

      if grains[j] >= h
        j += 1 while j < grains.length && grains[j] - h <= t
      else
        return false if h - grains[j] > t

        left = h - grains[j]
        max_right1 = t - 2 * left
        max_right2 = (t - left) / 2
        reach = h
        if max_right1 > max_right2
          reach = h + max_right1 if max_right1 > 0
        elsif max_right2 > 0
          reach = h + max_right2
        end
        j += 1 while j < grains.length && grains[j] <= reach
      end
    end
    j >= grains.length
  end

  lo = 0
  hi = 2_000_000_000
  while lo < hi
    mid = lo + (hi - lo) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("2605_form_smallest_number_from_two_digit_arrays", r'''
# LeetCode 2605 - Form Smallest Number From Two Digit Arrays
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_number(nums1, nums2)
  s1 = {}
  s2 = {}
  nums1.each { |x| s1[x] = true }
  nums2.each { |x| s2[x] = true }
  common = 10
  s1.each_key { |x| common = x if s2[x] && x < common }
  return common if common < 10

  a = nums1.min
  b = nums2.min
  [a * 10 + b, b * 10 + a].min
end
''')

add("2606_find_the_substring_with_maximum_cost", r'''
# LeetCode 2606 - Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

# @param {String} s
# @param {String} chars
# @param {Integer[]} vals
# @return {Integer}
def maximum_cost_substring(s, chars, vals)
  val = (1..26).to_a
  chars.each_char.with_index { |ch, i| val[ch.ord - 97] = vals[i] }
  best = 0
  cur = 0
  s.each_char do |c|
    cur += val[c.ord - 97]
    cur = 0 if cur < 0
    best = cur if cur > best
  end
  best
end
''')

add("2607_make_k_subarray_sums_equal", r'''
# LeetCode 2607 - Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def make_sub_k_sum_equal(arr, k)
  n = arr.length
  g = n.gcd(k)
  ans = 0
  g.times do |r|
    group = (r...n).step(g).map { |i| arr[i] }
    group.sort!
    med = group[group.length / 2]
    group.each { |x| ans += (x - med).abs }
  end
  ans
end
''')

add("2608_shortest_cycle_in_a_graph", r'''
# LeetCode 2608 - Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_shortest_cycle(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  inf = 1_000_000_000
  ans = inf
  n.times do |start|
    dist = Array.new(n, -1)
    parent = Array.new(n, -1)
    q = [start]
    dist[start] = 0
    until q.empty?
      u = q.shift
      g[u].each do |v|
        if dist[v] < 0
          dist[v] = dist[u] + 1
          parent[v] = u
          q << v
        elsif parent[u] != v
          c = dist[u] + dist[v] + 1
          ans = c if c < ans
        end
      end
    end
  end
  ans == inf ? -1 : ans
end
''')

add("2609_find_the_longest_balanced_substring_of_a_binary_string", r'''
# LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

# @param {String} s
# @return {Integer}
def find_the_longest_balanced_substring(s)
  ans = 0
  zeros = 0
  ones = 0
  s.each_char do |c|
    if c == "0"
      zeros = ones = 0 if ones > 0
      zeros += 1
    else
      ones += 1
      cur = [ones, zeros].min
      ans = 2 * cur if 2 * cur > ans
    end
  end
  ans
end
''')

add("2610_convert_an_array_into_a_2d_array_with_conditions", r'''
# LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

# @param {Integer[]} nums
# @return {Integer[][]}
def find_matrix(nums)
  freq = Hash.new(0)
  ans = []
  nums.each do |x|
    f = freq[x]
    ans << [] if f == ans.length
    ans[f] << x
    freq[x] = f + 1
  end
  ans
end
''')

add("2611_mice_and_cheese", r'''
# LeetCode 2611 - Mice and Cheese
# https://leetcode.com/problems/mice-and-cheese/

# @param {Integer[]} reward1
# @param {Integer[]} reward2
# @param {Integer} k
# @return {Integer}
def mice_and_cheese(reward1, reward2, k)
  n = reward1.length
  diff = Array.new(n, 0)
  ans = 0
  n.times do |i|
    ans += reward2[i]
    diff[i] = reward1[i] - reward2[i]
  end
  diff.sort!.reverse!
  k.times { |i| ans += diff[i] }
  ans
end
''')

add("2612_minimum_reverse_operations", r'''
# LeetCode 2612 - Minimum Reverse Operations
# https://leetcode.com/problems/minimum-reverse-operations/

# @param {Integer} n
# @param {Integer} p
# @param {Integer[]} banned
# @param {Integer} k
# @return {Integer[]}
def min_reverse_operations(n, p, banned, k)
  ban = {}
  banned.each { |x| ban[x] = true }
  ans = Array.new(n, -1)
  ans[p] = 0
  q = [[p, 0]]
  until q.empty?
    i, d = q.shift
    lo = i - (k - 1)
    lo = 0 if lo < 0
    hi = i
    hi = n - k if hi > n - k
    (lo..hi).each do |l|
      r = l + k - 1
      ni = l + r - i
      next if ni < 0 || ni >= n || ban[ni] || ans[ni] != -1

      ans[ni] = d + 1
      q << [ni, d + 1]
    end
  end
  ans
end
''')

add("2613_beautiful_pairs", r'''
# LeetCode 2613 - Beautiful Pairs
# https://leetcode.com/problems/beautiful-pairs/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def beautiful_pair(nums1, nums2)
  n = nums1.length
  best = Float::INFINITY
  ans = [0, 1]
  n.times do |i|
    (i + 1...n).each do |j|
      d = (nums1[i] - nums1[j]).abs + (nums2[i] - nums2[j]).abs
      if d < best || (d == best && (i < ans[0] || (i == ans[0] && j < ans[1])))
        best = d
        ans = [i, j]
      end
    end
  end
  ans
end
''')

add("2614_prime_in_diagonal", r'''
# LeetCode 2614 - Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/

# @param {Integer[][]} nums
# @return {Integer}
def diagonal_prime(nums)
  is_prime = lambda do |x|
    return false if x < 2

    i = 2
    while i * i <= x
      return false if x % i == 0

      i += 1
    end
    true
  end

  n = nums.length
  best = 0
  n.times do |i|
    a = nums[i][i]
    b = nums[i][n - 1 - i]
    best = a if is_prime.call(a) && a > best
    best = b if is_prime.call(b) && b > best
  end
  best
end
''')

add("2615_sum_of_distances", r'''
# LeetCode 2615 - Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

# @param {Integer[]} nums
# @return {Integer[]}
def distance(nums)
  n = nums.length
  ans = Array.new(n, 0)
  pos = {}
  nums.each_with_index do |x, i|
    pos[x] ||= []
    pos[x] << i
  end
  pos.each_value do |idxs|
    m = idxs.length
    pref = Array.new(m + 1, 0)
    m.times { |i| pref[i + 1] = pref[i] + idxs[i] }
    m.times do |j|
      idx = idxs[j]
      left = j * idx - pref[j]
      right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
      ans[idx] = left + right
    end
  end
  ans
end
''')

add("2616_minimize_the_maximum_difference_of_pairs", r'''
# LeetCode 2616 - Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

# @param {Integer[]} nums
# @param {Integer} p
# @return {Integer}
def minimize_max(nums, p)
  nums = nums.sort
  lo = 0
  hi = nums[-1] - nums[0]

  ok = lambda do |d|
    cnt = 0
    i = 0
    while i + 1 < nums.length
      if nums[i + 1] - nums[i] <= d
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    cnt >= p
  end

  while lo < hi
    mid = (lo + hi) >> 1
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("2617_minimum_number_of_visited_cells_in_a_grid", r'''
# LeetCode 2617 - Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_visited_cells(grid)
  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, -1) }
  q = [[0, 0]]
  dist[0][0] = 1
  until q.empty?
    r, c = q.shift
    return dist[r][c] if r == m - 1 && c == n - 1

    nc = c + 1
    while nc <= c + grid[r][c] && nc < n
      if dist[r][nc] == -1
        dist[r][nc] = dist[r][c] + 1
        q << [r, nc]
      end
      nc += 1
    end
    nr = r + 1
    while nr <= r + grid[r][c] && nr < m
      if dist[nr][c] == -1
        dist[nr][c] = dist[r][c] + 1
        q << [nr, c]
      end
      nr += 1
    end
  end
  -1
end
''')

add("2618_check_if_object_instance_of_class", r'''
# LeetCode 2618 - Check if Object Instance of Class
# https://leetcode.com/problems/check-if-object-instance-of-class/

# @param {Object} obj
# @param {Object} class_function
# @return {Boolean}
def check_if_instance_of(obj, class_function)
  return false if obj.nil?
  return false unless class_function.is_a?(Class)

  obj.is_a?(class_function)
rescue TypeError
  false
end
''')

add("2619_array_prototype_last", r'''
# LeetCode 2619 - Array Prototype Last
# https://leetcode.com/problems/array-prototype-last/

# @param {Object[]} nums
# @return {Object}
def last(nums)
  return -1 if nums.empty?

  nums[-1]
end
''')

written = 0
for folder, body in S.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
