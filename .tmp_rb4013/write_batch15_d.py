#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3260_find_the_largest_palindrome_divisible_by_k", r'''
# LeetCode 3260 - Find the Largest Palindrome Divisible by K
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

# @param {Integer} n
# @param {Integer} k
# @return {String}
def largest_palindrome(n, k)
  digits = Array.new(n, "9")
  half = (n + 1) / 2
  mod7 = lambda do |s|
    r = 0
    s.each_char { |ch| r = (r * 10 + (ch.ord - 48)) % 7 }
    r
  end
  largest_pal7 = lambda do |nn|
    half_len = (nn + 1) / 2
    half_d = Array.new(half_len, "9")
    loop do
      pal = Array.new(nn, "")
      (0...half_len).each { |i| pal[i] = half_d[i] }
      (0...(nn / 2)).each { |i| pal[nn - 1 - i] = pal[i] }
      return pal.join if mod7.call(pal.join) == 0
      idx = half_len - 1
      while idx >= 0 && half_d[idx] == "0"
        half_d[idx] = "9"
        idx -= 1
      end
      break if idx < 0
      half_d[idx] = (half_d[idx].ord - 1).chr
    end
    ""
  end
  return digits.join if [1, 3, 9].include?(k)
  if k == 2
    digits[0] = digits[n - 1] = "8"
    return digits.join
  end
  if k == 4
    return "8" if n == 1
    digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = "8"
    return digits.join
  end
  if k == 5
    digits[0] = digits[n - 1] = "5"
    return digits.join
  end
  if k == 8
    return Array.new(n, "8").join if n <= 2
    digits[0] = digits[1] = digits[2] = "8"
    digits[n - 1] = digits[n - 2] = digits[n - 3] = "8"
    return digits.join
  end
  if k == 6
    return "6" if n == 1
    digits[0] = digits[n - 1] = "8"
    ssum = 16 + 9 * (n - 2)
    need = ssum % 3
    if need != 0
      pos = half - 1
      digits[pos] = (digits[pos].ord - need).chr
      digits[n - 1 - pos] = digits[pos] if n.even? || pos != n - 1 - pos
    end
    return digits.join
  end
  return largest_pal7.call(n) if k == 7
  digits.join
end
''')

add("3261_count_substrings_that_satisfy_k_constraint_ii", r'''
# LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

# @param {String} s
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def count_k_constraint_substrings(s, k, queries)
  n = s.length
  left_most = Array.new(n, 0)
  z = o = l = 0
  (0...n).each do |r|
    if s[r] == "0"
      z += 1
    else
      o += 1
    end
    while z > k && o > k
      if s[l] == "0"
        z -= 1
      else
        o -= 1
      end
      l += 1
    end
    left_most[r] = l
  end
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + (i - left_most[i] + 1) }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    ll = q[0]
    rr = q[1]
    lo = ll
    hi = rr + 1
    while lo < hi
      mid = (lo + hi) >> 1
      if left_most[mid] < ll
        lo = mid + 1
      else
        hi = mid
      end
    end
    res = 0
    if lo > ll
      m = lo - ll
      res += m * (m + 1) / 2
    end
    res += pref[rr + 1] - pref[lo] if lo <= rr
    ans[qi] = res
  end
  ans
end
''')

add("3263_convert_doubly_linked_list_to_array_i", r'''
# LeetCode 3263 - Convert Doubly Linked List to Array I
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Node
  attr_accessor :val, :prev, :next
  def initialize(val = 0, prev = nil, nxt = nil)
    @val = val
    @prev = prev
    @next = nxt
  end
end

# @param {Node} head
# @return {Integer[]}
def to_array(head)
  ans = []
  while head
    ans << head.val
    head = head.next
  end
  ans
end
''')

add("3264_final_array_state_after_k_multiplication_operations_i", r'''
# LeetCode 3264 - Final Array State After K Multiplication Operations I
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class MinHeap
  def initialize
    @a = []
  end

  def cmp(x, y)
    x[0] != y[0] ? x[0] <=> y[0] : x[1] <=> y[1]
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if cmp(@a[i], @a[p]) >= 0
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
      s = l if l < n && cmp(@a[l], @a[s]) < 0
      s = r if r < n && cmp(@a[r], @a[s]) < 0
      break if s == i
      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} multiplier
# @return {Integer[]}
def get_final_state(nums, k, multiplier)
  h = MinHeap.new
  nums.each_with_index { |v, i| h.push([v, i]) }
  k.times do
    cur = h.pop
    v = cur[0] * multiplier
    i = cur[1]
    nums[i] = v
    h.push([v, i])
  end
  nums
end
''')

add("3265_count_almost_equal_pairs_i", r'''
# LeetCode 3265 - Count Almost Equal Pairs I
# https://leetcode.com/problems/count-almost-equal-pairs-i/

# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
  almost_equal = lambda do |a, b|
    sa = a.to_s
    sb = b.to_s
    sa = "0" + sa while sa.length < sb.length
    sb = "0" + sb while sb.length < sa.length
    diff = []
    (0...sa.length).each { |i| diff << i if sa[i] != sb[i] }
    return true if diff.empty?
    return false if diff.length != 2
    i0 = diff[0]
    j = diff[1]
    sa[i0] == sb[j] && sa[j] == sb[i0]
  end
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if almost_equal.call(nums[i], nums[j]) }
  end
  ans
end
''')

add("3266_final_array_state_after_k_multiplication_operations_ii", r'''
# LeetCode 3266 - Final Array State After K Multiplication Operations II
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

class MinHeap
  def initialize
    @a = []
  end

  def cmp(x, y)
    x[0] != y[0] ? x[0] <=> y[0] : x[1] <=> y[1]
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def size
    @a.length
  end

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if cmp(@a[i], @a[p]) >= 0
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
      s = l if l < n && cmp(@a[l], @a[s]) < 0
      s = r if r < n && cmp(@a[r], @a[s]) < 0
      break if s == i
      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} multiplier
# @return {Integer[]}
def get_final_state(nums, k, multiplier)
  mod = 1_000_000_007
  mod_pow = lambda do |a, e, md|
    r = 1
    a %= md
    while e > 0
      r = (r * a) % md if (e & 1) != 0
      a = (a * a) % md
      e >>= 1
    end
    r
  end
  return nums if multiplier == 1
  h = MinHeap.new
  max_v = 0
  nums.each_with_index do |v, i|
    h.push([v, i])
    max_v = v if v > max_v
  end
  while k > 0 && h.size > 0
    cur = h.pop
    v = cur[0]
    i = cur[1]
    if v * multiplier > max_v && k >= nums.length
      h.push([v, i])
      break
    end
    nv = v * multiplier
    nums[i] = nv
    max_v = nv if nv > max_v
    h.push([nv, i])
    k -= 1
  end
  if k > 0
    nn = nums.length
    full = k / nn
    rem = k % nn
    pow_full = mod_pow.call(multiplier, full, mod)
    (0...nn).each { |i| nums[i] = (nums[i] * pow_full) % mod }
    hh = MinHeap.new
    nums.each_with_index { |v, i| hh.push([v, i]) }
    rem.times do
      cur = hh.pop
      v = (cur[0] * multiplier) % mod
      i = cur[1]
      nums[i] = v
      hh.push([v, i])
    end
    (0...nn).each { |i| nums[i] %= mod }
  else
    nums.each_index { |i| nums[i] %= mod }
  end
  nums
end
''')

add("3267_count_almost_equal_pairs_ii", r'''
# LeetCode 3267 - Count Almost Equal Pairs II
# https://leetcode.com/problems/count-almost-equal-pairs-ii/

# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
  sa = sb = ""
  dfs = nil
  dfs = lambda do |arr, start, left|
    return true if arr.join == sb
    return false if left == 0
    (start...arr.length).each do |i|
      next if arr[i] == sb[i]
      ((i + 1)...arr.length).each do |j|
        next unless arr[j] == sb[i]
        arr[i], arr[j] = arr[j], arr[i]
        return true if dfs.call(arr, i + 1, left - 1)
        arr[i], arr[j] = arr[j], arr[i]
      end
      return false
    end
    arr.join == sb
  end
  almost_equal = lambda do |a, b|
    sa = a.to_s
    sb = b.to_s
    sa = "0" + sa while sa.length < sb.length
    sb = "0" + sb while sb.length < sa.length
    return true if sa == sb
    dfs.call(sa.chars, 0, 2)
  end
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if almost_equal.call(nums[i], nums[j]) }
  end
  ans
end
''')

add("3269_constructing_two_increasing_arrays", r'''
# LeetCode 3269 - Constructing Two Increasing Arrays
# https://leetcode.com/problems/constructing-two-increasing-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_largest(nums1, nums2)
  n = nums1.length
  m = nums2.length
  inf = 1_000_000_000
  dp = Array.new(n + 1) { Array.new(m + 1, inf) }
  dp[0][0] = 0
  (0..n).each do |i|
    (0..m).each do |j|
      next if dp[i][j] == inf
      prev = dp[i][j]
      if i < n
        need = prev + 1
        if nums1[i] == 0
          need += 1 if need.odd?
        else
          need += 1 if need.even?
        end
        dp[i + 1][j] = need if need < dp[i + 1][j]
      end
      if j < m
        need = prev + 1
        if nums2[j] == 0
          need += 1 if need.odd?
        else
          need += 1 if need.even?
        end
        dp[i][j + 1] = need if need < dp[i][j + 1]
      end
    end
  end
  dp[n][m]
end
''')

add("3270_find_the_key_of_the_numbers", r'''
# LeetCode 3270 - Find the Key of the Numbers
# https://leetcode.com/problems/find-the-key-of-the-numbers/

# @param {Integer} num1
# @param {Integer} num2
# @param {Integer} num3
# @return {Integer}
def generate_key(num1, num2, num3)
  ans = 0
  mul = 1
  4.times do
    d = [num1 % 10, num2 % 10, num3 % 10].min
    ans += d * mul
    mul *= 10
    num1 /= 10
    num2 /= 10
    num3 /= 10
  end
  ans
end
''')

add("3271_hash_divided_string", r'''
# LeetCode 3271 - Hash Divided String
# https://leetcode.com/problems/hash-divided-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def string_hash(s, k)
  out = []
  (0...s.length).step(k) do |i|
    ssum = 0
    (i...(i + k)).each { |j| ssum += s[j].ord - 97 }
    out << (97 + ssum % 26).chr
  end
  out.join
end
''')

add("3272_find_the_count_of_good_integers", r'''
# LeetCode 3272 - Find the Count of Good Integers
# https://leetcode.com/problems/find-the-count-of-good-integers/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def count_good_integers(n, k)
  half = (n + 1) / 2
  start = 1
  (1...half).each { start *= 10 }
  last = start * 10
  seen = {}
  ans = 0
  fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i }
  (start...last).each do |h|
    s = h.to_s
    pal = s.dup
    rev_start = s.length - 1
    rev_start -= 1 if n.odd?
    rev_start.downto(0) { |i| pal += s[i] }
    next if pal.to_i % k != 0
    chars = pal.chars.sort.join
    next if seen[chars]
    seen[chars] = true
    cnt = Array.new(10, 0)
    chars.each_char { |c| cnt[c.ord - 48] += 1 }
    total = fact[n]
    cnt.each { |c| total /= fact[c] }
    if cnt[0] > 0
      bad = fact[n - 1]
      cnt[0] -= 1
      cnt.each { |c| bad /= fact[c] }
      cnt[0] += 1
      total -= bad
    end
    ans += total
  end
  ans
end
''')

add("3273_minimum_amount_of_damage_dealt_to_bob", r'''
# LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

# @param {Integer} power
# @param {Integer[]} damage
# @param {Integer[]} health
# @return {Integer}
def min_damage(power, damage, health)
  n = damage.length
  arr = []
  total_dmg = 0
  (0...n).each do |i|
    hits = (health[i] + power - 1) / power
    arr << { dmg: damage[i], hits: hits }
    total_dmg += damage[i]
  end
  arr.sort! { |a, b| a[:hits] * b[:dmg] <=> b[:hits] * a[:dmg] }
  ans = 0
  cur = total_dmg
  arr.each do |e|
    ans += cur * e[:hits]
    cur -= e[:dmg]
  end
  ans
end
''')

add("3274_check_if_two_chessboard_squares_have_the_same_color", r'''
# LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

# @param {String} coordinate1
# @param {String} coordinate2
# @return {Boolean}
def check_two_chessboards(coordinate1, coordinate2)
  c1 = (coordinate1[0].ord - 97) + (coordinate1[1].ord - 49)
  c2 = (coordinate2[0].ord - 97) + (coordinate2[1].ord - 49)
  c1 % 2 == c2 % 2
end
''')

add("3275_k_th_nearest_obstacle_queries", r'''
# LeetCode 3275 - K-th Nearest Obstacle Queries
# https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class MaxHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def peek
    @a[0]
  end

  def size
    @a.length
  end

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] <= @a[p]
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
      s = l if l < n && @a[l] > @a[s]
      s = r if r < n && @a[r] > @a[s]
      break if s == i
      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[][]} queries
# @param {Integer} k
# @return {Integer[]}
def results_array(queries, k)
  h = MaxHeap.new
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    d = q[0].abs + q[1].abs
    h.push(d)
    h.pop if h.size > k
    ans[i] = h.size < k ? -1 : h.peek
  end
  ans
end
''')

add("3276_select_cells_in_grid_with_maximum_score", r'''
# LeetCode 3276 - Select Cells in Grid With Maximum Score
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

# @param {Integer[][]} grid
# @return {Integer}
def max_score(grid)
  m = grid.length
  vals = {}
  (0...m).each do |i|
    seen = {}
    grid[i].each do |v|
      next if seen[v]
      seen[v] = true
      vals[v] ||= []
      vals[v] << i
    end
  end
  arr = vals.keys.sort.reverse
  nn = 1 << m
  dp = Array.new(nn, 0)
  arr.each do |v|
    ndp = dp.dup
    vals[v].each do |r|
      bit = 1 << r
      (0...nn).each do |mask|
        next if (mask & bit) != 0
        cand = dp[mask] + v
        nmask = mask | bit
        ndp[nmask] = cand if cand > ndp[nmask]
      end
    end
    dp = ndp
  end
  dp.max
end
''')

add("3277_maximum_xor_score_subarray_queries", r'''
# LeetCode 3277 - Maximum XOR Score Subarray Queries
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_subarray_xor(nums, queries)
  n = nums.length
  f = Array.new(n) { Array.new(n, 0) }
  (0...n).each { |i| f[i][i] = nums[i] }
  (2..n).each do |length|
    (0...(n - length + 1)).each do |i|
      j = i + length - 1
      f[i][j] = f[i][j - 1] ^ f[i + 1][j]
    end
  end
  best = Array.new(n) { Array.new(n, 0) }
  (0...n).each { |i| best[i][i] = f[i][i] }
  (2..n).each do |length|
    (0...(n - length + 1)).each do |i|
      j = i + length - 1
      best[i][j] = [f[i][j], best[i][j - 1], best[i + 1][j]].max
    end
  end
  queries.map { |q| best[q[0]][q[1]] }
end
''')

add("3279_maximum_total_area_occupied_by_pistons", r'''
# LeetCode 3279 - Maximum Total Area Occupied by Pistons
# https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

# @param {Integer} height
# @param {Integer[]} positions
# @param {String} directions
# @return {Integer}
def max_area(height, positions, directions)
  n = positions.length
  pos = positions.dup
  dirc = directions.chars
  best = 0
  (0..(2 * height)).each do |_t|
    s = pos.sum
    best = s if s > best
    (0...n).each do |i|
      if dirc[i] == "U"
        if pos[i] == height
          dirc[i] = "D"
          pos[i] -= 1
        else
          pos[i] += 1
        end
      elsif pos[i] == 0
        dirc[i] = "U"
        pos[i] += 1
      else
        pos[i] -= 1
      end
    end
  end
  best
end
''')

add("3280_convert_date_to_binary", r'''
# LeetCode 3280 - Convert Date to Binary
# https://leetcode.com/problems/convert-date-to-binary/

# @param {String} date
# @return {String}
def convert_date_to_binary(date)
  to_binary = lambda do |v|
    return "0" if v == 0
    s = ""
    while v > 0
      s = (v & 1).to_s + s
      v >>= 1
    end
    s
  end
  y, m, d = date.split("-").map(&:to_i)
  "#{to_binary.call(y)}-#{to_binary.call(m)}-#{to_binary.call(d)}"
end
''')

add("3281_maximize_score_of_numbers_in_ranges", r'''
# LeetCode 3281 - Maximize Score of Numbers in Ranges
# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

# @param {Integer[]} start
# @param {Integer} d
# @return {Integer}
def max_possible_score(start, d)
  start.sort!
  n = start.length
  ok = lambda do |mid|
    prev = start[0]
    (1...start.length).each do |i|
      need = prev + mid
      cur = start[i]
      return false if need > cur + d
      prev = need > cur ? need : cur
    end
    true
  end
  lo = 0
  hi = start[n - 1] + d - start[0] + 1
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

add("3282_reach_end_of_array_with_max_score", r'''
# LeetCode 3282 - Reach End of Array With Max Score
# https://leetcode.com/problems/reach-end-of-array-with-max-score/

# @param {Integer[]} nums
# @return {Integer}
def find_maximum_score(nums)
  ans = 0
  max_v = 0
  (0...(nums.length - 1)).each do |i|
    max_v = nums[i] if nums[i] > max_v
    ans += max_v
  end
  ans
end
''')

add("3283_maximum_number_of_moves_to_kill_all_pawns", r'''
# LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

# @param {Integer} kx
# @param {Integer} ky
# @param {Integer[][]} positions
# @return {Integer}
def max_moves(kx, ky, positions)
  dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  knight_dist = lambda do |x, y, pts|
    np = pts.length
    ans = Array.new(np, -1)
    vis = Array.new(50) { Array.new(50, false) }
    q = [[x, y, 0]]
    vis[x][y] = true
    need = {}
    (0...np).each do |i|
      key = (pts[i][0] << 32) | (pts[i][1] & 0xFFFFFFFF)
      need[key] ||= []
      need[key] << i
    end
    found = 0
    while !q.empty? && found < np
      cur = q.shift
      key = (cur[0] << 32) | (cur[1] & 0xFFFFFFFF)
      idxs = need[key]
      if idxs
        idxs.each do |i|
          if ans[i] == -1
            ans[i] = cur[2]
            found += 1
          end
        end
      end
      dirs.each do |d|
        nx = cur[0] + d[0]
        ny = cur[1] + d[1]
        next if nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]
        vis[nx][ny] = true
        q << [nx, ny, cur[2] + 1]
      end
    end
    ans
  end
  n = positions.length
  pts = Array.new(n + 1) { [0, 0] }
  pts[0][0] = kx
  pts[0][1] = ky
  (0...n).each do |i|
    pts[i + 1][0] = positions[i][0]
    pts[i + 1][1] = positions[i][1]
  end
  dist = (0..n).map { |i| knight_dist.call(pts[i][0], pts[i][1], pts) }
  nn = 1 << n
  memo = Array.new(nn) { Array.new(n + 1, -1) }
  dfs = nil
  dfs = lambda do |mask, cur, turn|
    return 0 if mask == nn - 1
    return memo[mask][cur] if memo[mask][cur] != -1
    best = turn == 0 ? -(1 << 30) : (1 << 30)
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      d = dist[cur][i + 1]
      v = d + dfs.call(mask | (1 << i), i + 1, 1 - turn)
      if turn == 0
        best = v if v > best
      elsif v < best
        best = v
      end
    end
    memo[mask][cur] = best
  end
  dfs.call(0, 0, 0)
end
''')

add("3284_sum_of_consecutive_subarrays", r'''
# LeetCode 3284 - Sum of Consecutive Subarrays
# https://leetcode.com/problems/sum-of-consecutive-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def range_sum(nums)
  mod = 1_000_000_007
  n = nums.length
  ans = 0
  i = 0
  while i < n
    j = i
    j += 1 while j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1)
    (i..j).each do |l|
      s = 0
      (l..j).each do |r|
        s += nums[r]
        ans = (ans + s) % mod
      end
    end
    i = j + 1
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
