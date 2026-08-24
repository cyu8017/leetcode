#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3449_maximize_the_minimum_game_score", r'''
# LeetCode 3449 - Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/

# @param {Integer[]} points
# @param {Integer} m
# @return {Integer}
def max_score(points, m)
  ok = lambda do |mid|
    need = 0
    extra = 0
    points.each do |p|
      req = (mid + p - 1) / p
      if req > extra
        visits = req - extra
        need += 2 * visits - 1
        extra = visits - 1
      else
        need += 1
        extra = 0
      end
      return false if need > m
    end
    need <= m
  end
  lo = 0
  hi = 10**18
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

add("3450_maximum_students_on_a_single_bench", r'''
# LeetCode 3450 - Maximum Students on a Single Bench
# https://leetcode.com/problems/maximum-students-on-a-single-bench/

# @param {Integer[][]} students
# @return {Integer}
def max_students_on_bench(students)
  bench = {}
  students.each do |s|
    bench[s[1]] ||= {}
    bench[s[1]][s[0]] = true
  end
  ans = 0
  bench.each_value do |st|
    ans = st.length if st.length > ans
  end
  ans
end
''')

add("3452_sum_of_good_numbers", r'''
# LeetCode 3452 - Sum of Good Numbers
# https://leetcode.com/problems/sum-of-good-numbers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_good_numbers(nums, k)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    x = nums[i]
    good = true
    good = false if i - k >= 0 && x <= nums[i - k]
    good = false if i + k < n && x <= nums[i + k]
    ans += x if good
  end
  ans
end
''')

add("3453_separate_squares_i", r'''
# LeetCode 3453 - Separate Squares I
# https://leetcode.com/problems/separate-squares-i/

# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
  total = 0
  squares.each do |sq|
    l = sq[2]
    total += l * l
  end
  area_below = lambda do |y|
    below = 0.0
    squares.each do |sq|
      yi = sq[1]
      l = sq[2]
      top = yi + l
      if y <= yi
        next
      elsif y >= top
        below += l * l
      else
        below += l * (y - yi)
      end
    end
    below
  end
  lo = 0.0
  hi = 2e9
  60.times do
    mid = (lo + hi) / 2.0
    if area_below.call(mid) * 2 < total
      lo = mid
    else
      hi = mid
    end
  end
  hi
end
''')

add("3454_separate_squares_ii", r'''
# LeetCode 3454 - Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/

# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
  total = 0
  squares.each do |sq|
    l = sq[2]
    total += l * l
  end
  area_below = lambda do |y|
    below = 0.0
    squares.each do |sq|
      yi = sq[1]
      l = sq[2]
      top = yi + l
      if y <= yi
        next
      elsif y >= top
        below += l * l
      else
        below += l * (y - yi)
      end
    end
    below
  end
  lo = 0.0
  hi = 2e9
  60.times do
    mid = (lo + hi) / 2.0
    if area_below.call(mid) * 2 < total
      lo = mid
    else
      hi = mid
    end
  end
  hi
end
''')

add("3455_shortest_matching_substring", r'''
# LeetCode 3455 - Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/

# @param {String} s
# @param {String} p
# @return {Integer}
def shortest_matching_substring(s, p)
  parts = []
  cur = ""
  p.each_char do |c|
    if c == "*"
      parts << cur
      cur = ""
    else
      cur += c
    end
  end
  parts << cur
  parts << "" while parts.length < 3
  a = parts[0]
  b = parts[1]
  c = parts[2]
  n = s.length
  find_all = lambda do |sub|
    res = []
    if sub.length == 0
      (0..n).each { |i| res << i }
      return res
    end
    (0..(n - sub.length)).each do |i|
      res << i if s[i, sub.length] == sub
    end
    res
  end
  sort_search = lambda do |arr, x|
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
  pos_a = find_all.call(a)
  pos_b = find_all.call(b)
  pos_c = find_all.call(c)
  ans = n + 1
  pos_a.each do |ia|
    end_a = ia + a.length
    bi = sort_search.call(pos_b, end_a)
    while bi < pos_b.length
      end_b = pos_b[bi] + b.length
      ci = sort_search.call(pos_c, end_b)
      if ci < pos_c.length
        length = pos_c[ci] + c.length - ia
        ans = length if length < ans
      end
      break
    end
  end
  ans == n + 1 ? -1 : ans
end
''')

add("3456_find_special_substring_of_length_k", r'''
# LeetCode 3456 - Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/

# @param {String} s
# @param {Integer} k
# @return {Boolean}
def has_special_substring(s, k)
  n = s.length
  (0..(n - k)).each do |i|
    ok = true
    ((i + 1)...(i + k)).each do |j|
      if s[j] != s[i]
        ok = false
        break
      end
    end
    next unless ok
    next if i > 0 && s[i - 1] == s[i]
    next if i + k < n && s[i + k] == s[i]

    return true
  end
  false
end
''')

add("3457_eat_pizzas", r'''
# LeetCode 3457 - Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/

# @param {Integer[]} pizzas
# @return {Integer}
def max_weight(pizzas)
  pizzas = pizzas.sort
  n = pizzas.length
  days = n / 4
  ans = 0
  odd_days = (days + 1) / 2
  even_days = days / 2
  idx = n - 1
  odd_days.times do
    ans += pizzas[idx]
    idx -= 1
  end
  even_days.times do
    idx -= 1
    ans += pizzas[idx]
    idx -= 1
  end
  ans
end
''')

add("3458_select_k_disjoint_special_substrings", r'''
# LeetCode 3458 - Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/

# @param {String} s
# @param {Integer} k
# @return {Boolean}
def max_substring_length(s, k)
  n = s.length
  first = Array.new(26, n)
  last = Array.new(26, -1)
  s.each_char.with_index do |ch, i|
    ci = ch.ord - 97
    first[ci] = i if first[ci] == n
    last[ci] = i
  end
  segs = []
  (0...26).each do |c|
    next if last[c] == -1

    l = first[c]
    r = last[c]
    i = l
    while i <= r
      ci = s[i].ord - 97
      if first[ci] < l
        l = first[ci]
        i = l - 1
        i += 1
        next
      end
      r = last[ci] if last[ci] > r
      i += 1
    end
    segs << [l, r] unless l == 0 && r == n - 1
  end
  uniq = {}
  arr = []
  segs.each do |sg|
    key = (sg[0] << 32) | (sg[1] & 0xFFFFFFFF)
    next if uniq[key]

    uniq[key] = true
    arr << sg
  end
  arr.sort_by! { |x| x[1] }
  cnt = 0
  last_end = -1
  arr.each do |sg|
    if sg[0] > last_end
      cnt += 1
      last_end = sg[1]
    end
  end
  cnt >= k
end
''')

add("3459_length_of_longest_v_shaped_diagonal_segment", r'''
# LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

# @param {Integer[][]} grid
# @return {Integer}
def len_of_v_diagonal(grid)
  m = grid.length
  n = grid[0].length
  dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
  next_dir = [1, 2, 3, 0]
  memo = {}
  key_fn = lambda do |i, j, d, turned, expect|
    ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)
  end
  dfs = nil
  dfs = lambda do |i, j, d, turned, expect|
    return 0 if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect

    k = key_fn.call(i, j, d, turned, expect)
    return memo[k] if memo.key?(k)

    ni = i + dirs[d][0]
    nj = j + dirs[d][1]
    nx = expect == 2 ? 0 : 2
    best = 1 + dfs.call(ni, nj, d, turned, nx)
    if turned == 0
      nd = next_dir[d]
      ti = i + dirs[nd][0]
      tj = j + dirs[nd][1]
      cand = 1 + dfs.call(ti, tj, nd, 1, nx)
      best = cand if cand > best
    end
    memo[k] = best
    best
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] != 1

      (0...4).each do |d|
        ni = i + dirs[d][0]
        nj = j + dirs[d][1]
        best = 1 + dfs.call(ni, nj, d, 0, 2)
        ans = best if best > ans
      end
      ans = 1 if ans < 1
    end
  end
  ans
end
''')

add("3460_longest_common_prefix_after_at_most_one_removal", r'''
# LeetCode 3460 - Longest Common Prefix After at Most One Removal
# https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_common_prefix(s, t)
  i = 0
  j = 0
  removed = false
  while i < s.length && j < t.length
    if s[i] == t[j]
      i += 1
      j += 1
      next
    end
    break if removed

    removed = true
    i += 1
  end
  j
end
''')

add("3461_check_if_digits_are_equal_in_string_after_operations_i", r'''
# LeetCode 3461 - Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

# @param {String} s
# @return {Boolean}
def has_same_digits(s)
  b = s.chars
  while b.length > 2
    nb = Array.new(b.length - 1, "")
    (0...(b.length - 1)).each do |i|
      nb[i] = ((b[i].ord - 48 + b[i + 1].ord - 48) % 10).to_s
    end
    b = nb
  end
  b[0] == b[1]
end
''')

add("3462_maximum_sum_with_at_most_k_elements", r'''
# LeetCode 3462 - Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

# @param {Integer[][]} grid
# @param {Integer[]} limits
# @param {Integer} k
# @return {Integer}
def max_sum(grid, limits, k)
  h = []
  s = 0
  (0...grid.length).each do |i|
    r = grid[i].sort
    lim = limits[i]
    lim = r.length if lim > r.length
    (0...lim).each do |j|
      val = r[r.length - 1 - j]
      h << val
      h.sort!
      s += val
      s -= h.shift if h.length > k
    end
  end
  s
end
''')

add("3463_check_if_digits_are_equal_in_string_after_operations_ii", r'''
# LeetCode 3463 - Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

# @param {String} s
# @return {Boolean}
def has_same_digits(s)
  combine_digit_3463(s, 0) == combine_digit_3463(s, 1)
end

def mod_pow_p_3463(a, e, p)
  r = 1
  while e > 0
    r = r * a % p if e.odd?
    a = a * a % p
    e /= 2
  end
  r
end

def mod_inv_prime_3463(a, p)
  mod_pow_p_3463(a, p - 2, p)
end

def binom_mod_3463(n, k, p)
  return 0 if k < 0 || k > n

  num = 1
  den = 1
  (0...k).each do |i|
    num = num * (n - i) % p
    den = den * (i + 1) % p
  end
  num * mod_inv_prime_3463(den, p) % p
end

def crt_3463(a1, m1, a2, m2)
  (0...(m1 * m2)).each do |x|
    return x if x % m1 == a1 && x % m2 == a2
  end
  0
end

def binom_mod10_3463(n, k)
  crt_3463(binom_mod_3463(n, k, 2), 2, binom_mod_3463(n, k, 5), 5)
end

def combine_digit_3463(s, offset)
  n = s.length
  total = 0
  (0...(n - 1)).each do |i|
    total = (total + binom_mod10_3463(n - 2, i) * (s[i + offset].ord - 48)) % 10
  end
  total
end
''')

add("3464_maximize_the_distance_between_points_on_a_square", r'''
# LeetCode 3464 - Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

# @param {Integer} side
# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer}
def max_distance(side, points, k)
  arr = Array.new(points.length, 0)
  points.each_with_index do |(x, y), i|
    arr[i] = if y == 0
               x
             elsif x == side
               side + y
             elsif y == side
               2 * side + (side - x)
             else
               3 * side + (side - y)
             end
  end
  arr.sort!
  perim = 4 * side
  lo = 0
  hi = 2 * side
  while lo < hi
    mid = (lo + hi + 1) / 2
    if can_place_3464(arr, perim, mid, k)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end

def can_place_3464(arr, perim, mid, k)
  n = arr.length
  (0...n).each do |s|
    cnt = 1
    last = arr[s]
    idx = s
    while cnt < k
      target = last + mid
      found = false
      (1...n).each do |step|
        ni = (idx + step) % n
        val = arr[ni]
        add = ni <= idx ? perim : 0
        next unless val + add >= target

        last = val + add
        idx = ni
        cnt += 1
        found = true
        break
      end
      break unless found
    end
    return true if cnt == k && last - arr[s] <= perim - mid
  end
  false
end
''')

add("3466_maximum_coin_collection", r'''
# LeetCode 3466 - Maximum Coin Collection
# https://leetcode.com/problems/maximum-coin-collection/

# @param {Integer[]} lane1
# @param {Integer[]} lane2
# @return {Integer}
def max_coins(lane1, lane2)
  n = lane1.length
  neg = -(10**18)
  dp = [[lane1[0], neg], [lane2[0], neg]]
  ans = [dp[0][0], dp[1][0]].max
  (1...n).each do |i|
    ndp = [[0, 0], [0, 0]]
    ndp[0][0] = [dp[0][0], 0].max + lane1[i]
    ndp[1][0] = [dp[1][0], 0].max + lane2[i]
    ndp[0][1] = [dp[0][1], dp[1][0]].max + lane1[i]
    ndp[1][1] = [dp[1][1], dp[0][0]].max + lane2[i]
    ndp[0][0] = lane1[i] if lane1[i] > ndp[0][0]
    ndp[1][0] = lane2[i] if lane2[i] > ndp[1][0]
    (0...2).each do |a|
      (0...2).each do |b|
        dp[a][b] = ndp[a][b]
        ans = dp[a][b] if dp[a][b] > ans
      end
    end
  end
  ans
end
''')

add("3467_transform_array_by_parity", r'''
# LeetCode 3467 - Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/

# @param {Integer[]} nums
# @return {Integer[]}
def transform_array(nums)
  (0...nums.length).each { |i| nums[i] %= 2 }
  j = 0
  (0...nums.length).each do |i|
    if nums[i] == 0
      nums[i], nums[j] = nums[j], nums[i]
      j += 1
    end
  end
  nums
end
''')

add("3468_find_the_number_of_copy_arrays", r'''
# LeetCode 3468 - Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/

# @param {Integer[]} original
# @param {Integer[][]} bounds
# @return {Integer}
def count_arrays(original, bounds)
  n = original.length
  lo = bounds[0][0]
  hi = bounds[0][1]
  (1...n).each do |i|
    diff = original[i] - original[i - 1]
    lo2 = bounds[i][0]
    hi2 = bounds[i][1]
    nlo = lo + diff
    nhi = hi + diff
    nlo = lo2 if nlo < lo2
    nhi = hi2 if nhi > hi2
    return 0 if nlo > nhi

    lo = nlo
    hi = nhi
  end
  hi - lo + 1
end
''')

add("3469_find_minimum_cost_to_remove_array_elements", r'''
# LeetCode 3469 - Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

# @param {Integer[]} nums
# @return {Integer}
def min_cost(nums)
  n = nums.length
  memo = {}
  dfs = nil
  dfs = lambda do |i, prev|
    return prev == -1 ? 0 : nums[prev] if i >= n

    k = (i << 32) | (prev & 0xFFFFFFFF)
    return memo[k] if memo.key?(k)

    res = if prev == -1
            if i + 1 >= n
              nums[i]
            elsif i + 2 >= n
              [nums[i], nums[i + 1]].max
            else
              a = nums[i]
              b = nums[i + 1]
              c = nums[i + 2]
              [
                [b, c].max + dfs.call(i + 3, i),
                [a, c].max + dfs.call(i + 3, i + 1),
                [a, b].max + dfs.call(i + 3, i + 2)
              ].min
            end
          elsif i + 1 >= n
            [nums[prev], nums[i]].max
          else
            a = nums[prev]
            b = nums[i]
            c = nums[i + 1]
            [
              [b, c].max + dfs.call(i + 2, prev),
              [a, c].max + dfs.call(i + 2, i),
              [a, b].max + dfs.call(i + 2, i + 1)
            ].min
          end
    memo[k] = res
    res
  end
  dfs.call(0, -1)
end
''')

add("3470_permutations_iv", r'''
# LeetCode 3470 - Permutations IV
# https://leetcode.com/problems/permutations-iv/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def permute(n, k)
  fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each do |i|
    fact[i] = fact[i - 1] * i
    fact[i] = 10**18 + 1 if fact[i] > 10**18
  end
  used = Array.new(n + 1, false)
  ans = []
  kk = k
  dfs = nil
  dfs = lambda do |pos|
    return true if pos == n

    (1..n).each do |x|
      next if used[x]
      next if pos > 0 && (ans[pos - 1] % 2 == x % 2)

      rem = n - pos - 1
      cnt = fact[rem]
      if cnt >= kk
        used[x] = true
        ans << x
        return true if dfs.call(pos + 1)

        ans.pop
        used[x] = false
      else
        kk -= cnt
      end
    end
    false
  end
  return [] unless dfs.call(0)

  ans
end
''')

add("3471_find_the_largest_almost_missing_integer", r'''
# LeetCode 3471 - Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_integer(nums, k)
  n = nums.length
  cnt = Hash.new(0)
  (0..(n - k)).each do |i|
    seen = {}
    (i...(i + k)).each { |j| seen[nums[j]] = true }
    seen.each_key { |x| cnt[x] += 1 }
  end
  ans = -1
  cnt.each do |key, value|
    ans = key if value == 1 && key > ans
  end
  ans
end
''')

add("3472_longest_palindromic_subsequence_after_at_most_k_operations", r'''
# LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_palindromic_subsequence(s, k)
  n = s.length
  dp = Array.new(n) { Array.new(n) { Array.new(k + 1, -1) } }
  dist_circ = lambda do |a, b|
    d = (a.ord - b.ord).abs
    [d, 26 - d].min
  end
  dfs = nil
  dfs = lambda do |i, j, ops|
    return 0 if i > j
    return 1 if i == j
    return dp[i][j][ops] if dp[i][j][ops] != -1

    best = dfs.call(i + 1, j, ops)
    best = [best, dfs.call(i, j - 1, ops)].max
    cost = dist_circ.call(s[i], s[j])
    best = [best, 2 + dfs.call(i + 1, j - 1, ops - cost)].max if cost <= ops
    dp[i][j][ops] = best
    best
  end
  dfs.call(0, n - 1, k)
end
''')

add("3473_sum_of_k_subarrays_with_length_at_least_m", r'''
# LeetCode 3473 - Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def max_sum(nums, k, m)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }
  neg = -(10**18)
  dp = Array.new(k + 1) { Array.new(n + 1, neg) }
  (0..(n)).each { |i| dp[0][i] = 0 }
  (1..k).each do |t|
    best = neg
    ((t * m)..n).each do |i|
      j = i - m
      best = [best, dp[t - 1][j] - pref[j]].max
      dp[t][i] = best + pref[i]
    end
    (1..n).each { |i| dp[t][i] = [dp[t][i], dp[t][i - 1]].max }
  end
  dp[k][n]
end
''')

add("3474_lexicographically_smallest_generated_string", r'''
# LeetCode 3474 - Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/

# @param {String} str1
# @param {String} str2
# @return {String}
def generate_string(str1, str2)
  n = str1.length
  m = str2.length
  len = n + m - 1
  ans = Array.new(len, "?")
  (0...n).each do |i|
    next unless str1[i] == "T"

    (0...m).each do |j|
      return "" if ans[i + j] != "?" && ans[i + j] != str2[j]

      ans[i + j] = str2[j]
    end
  end
  (0...len).each { |i| ans[i] = "a" if ans[i] == "?" }
  (0...n).each do |i|
    next unless str1[i] == "F"

    match = true
    (0...m).each do |j|
      if ans[i + j] != str2[j]
        match = false
        break
      end
    end
    next unless match

    changed = false
    (m - 1).downto(0) do |j|
      pos = i + j
      forced = false
      (0...n).each do |t|
        if str1[t] == "T" && pos >= t && pos < t + m
          forced = true
          break
        end
      end
      next if forced

      ans[pos] = "b"
      changed = true
      break
    end
    return "" unless changed
  end
  (0...n).each do |i|
    match = true
    (0...m).each do |j|
      if ans[i + j] != str2[j]
        match = false
        break
      end
    end
    return "" if str1[i] == "T" && !match
    return "" if str1[i] == "F" && match
  end
  ans.join
end
''')

add("3476_maximize_profit_from_task_assignment", r'''
# LeetCode 3476 - Maximize Profit from Task Assignment
# https://leetcode.com/problems/maximize-profit-from-task-assignment/

# @param {Integer[]} workers
# @param {Integer[][]} tasks
# @return {Integer}
def max_profit(workers, tasks)
  workers = workers.sort
  tasks = tasks.sort_by { |t| t[0] }
  ans = 0
  used = Array.new(tasks.length, false)
  workers.each do |w|
    best = -1
    bi = -1
    (0...tasks.length).each do |i|
      next if used[i]
      break if tasks[i][0] > w

      if tasks[i][1] > best
        best = tasks[i][1]
        bi = i
      end
    end
    if bi >= 0
      used[bi] = true
      ans += best
    end
  end
  ans
end
''')

written = 0
failed = []
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    try:
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print("OK", name)
    except Exception as e:
        failed.append((name, str(e)))
        print("FAIL", name, e)
print(f"written={written} failed={len(failed)}")
