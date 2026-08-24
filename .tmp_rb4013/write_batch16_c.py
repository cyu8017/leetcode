#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3340_check_balanced_string", r'''
# LeetCode 3340 - Check Balanced String
# https://leetcode.com/problems/check-balanced-string/

# @param {String} num
# @return {Boolean}
def is_balanced(num)
  even = 0
  odd = 0
  num.each_char.with_index do |ch, i|
    if i.even?
      even += ch.ord - 48
    else
      odd += ch.ord - 48
    end
  end
  even == odd
end
''')

add("3341_find_minimum_time_to_reach_last_room_i", r'''
# LeetCode 3341 - Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

# @param {Integer[][]} move_time
# @return {Integer}
def min_time_to_reach(move_time)
  m = move_time.length
  n = move_time[0].length
  dist = Array.new(m) { Array.new(n, 1 << 30) }
  h = [[0, 0, 0]]
  dist[0][0] = 0
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until h.empty?
    h.sort_by! { |a| a[0] }
    t, r, c = h.shift
    next if t != dist[r][c]
    return t if r == m - 1 && c == n - 1

    dirs.each do |d|
      nr = r + d[0]
      nc = c + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      start = [t, move_time[nr][nc]].max
      nt = start + 1
      if nt < dist[nr][nc]
        dist[nr][nc] = nt
        h << [nt, nr, nc]
      end
    end
  end
  -1
end
''')

add("3342_find_minimum_time_to_reach_last_room_ii", r'''
# LeetCode 3342 - Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

# @param {Integer[][]} move_time
# @return {Integer}
def min_time_to_reach(move_time)
  m = move_time.length
  n = move_time[0].length
  inf = 1 << 30
  dist = Array.new(m) { Array.new(n) { [inf, inf] } }
  pq = [[0, 0, 0, 0]]
  dist[0][0][0] = 0
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    t, r, c, parity = pq.shift
    next if t != dist[r][c][parity]
    return t if r == m - 1 && c == n - 1

    cost = parity == 1 ? 2 : 1
    dirs.each do |d|
      nr = r + d[0]
      nc = c + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      start = [t, move_time[nr][nc]].max
      nt = start + cost
      np = 1 - parity
      if nt < dist[nr][nc][np]
        dist[nr][nc][np] = nt
        pq << [nt, nr, nc, np]
      end
    end
  end
  -1
end
''')

add("3343_count_number_of_balanced_permutations", r'''
# LeetCode 3343 - Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/

# @param {Integer} a
# @param {Integer} e
# @param {Integer} mod
# @return {Integer}
def mod_pow(a, e, mod)
  r = 1
  a %= mod
  while e > 0
    r = r * a % mod if (e & 1) != 0
    a = a * a % mod
    e >>= 1
  end
  r
end

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def pack_key(a, b)
  (a << 32) | (b & 0xFFFFFFFF)
end

# @param {String} num
# @return {Integer}
def count_balanced_permutations(num)
  mod = 1_000_000_007
  cnt = Array.new(10, 0)
  ssum = 0
  num.each_char do |c|
    d = c.ord - 48
    cnt[d] += 1
    ssum += d
  end
  return 0 if ssum.odd?

  n = num.length
  half_n = n / 2
  half_s = ssum / 2
  fact = Array.new(n + 1, 0)
  inv_f = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_f[n] = mod_pow(fact[n], mod - 2, mod)
  n.downto(1) { |i| inv_f[i - 1] = inv_f[i] * i % mod }
  dp = { pack_key(0, 0) => 1 }
  10.times do |d|
    ndp = {}
    dp.each do |st, ways|
      used = st >> 32
      s = st & 0xFFFFFFFF
      (0..cnt[d]).each do |take|
        nu = used + take
        ns = s + take * d
        next if nu > half_n || ns > half_s

        w = ways * inv_f[take] % mod * inv_f[cnt[d] - take] % mod
        nk = pack_key(nu, ns)
        ndp[nk] = ((ndp[nk] || 0) + w) % mod
      end
    end
    dp = ndp
  end
  ans = dp[pack_key(half_n, half_s)] || 0
  ans = ans * fact[half_n] % mod * fact[n - half_n] % mod
  10.times { |d| ans = ans * fact[cnt[d]] % mod }
  ans
end
''')

add("3344_maximum_sized_array", r'''
# LeetCode 3344 - Maximum Sized Array
# https://leetcode.com/problems/maximum-sized-array/

# @param {Integer} n
# @param {Integer} s
# @return {Boolean}
def sized_array_ok(n, s)
  total = 0
  n.times do |i|
    n.times do |j|
      ij = i | j
      total += ij * (n - 1) * n / 2
      return false if total > s
    end
  end
  total <= s
end

# @param {Integer} s
# @return {Integer}
def max_sized_array(s)
  lo = 1
  hi = 2000
  while lo < hi
    mid = (lo + hi + 1) / 2
    if sized_array_ok(mid, s)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("3345_smallest_divisible_digit_product_i", r'''
# LeetCode 3345 - Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/

# @param {Integer} n
# @param {Integer} t
# @return {Integer}
def smallest_number(n, t)
  x = n
  loop do
    p = 1
    y = x
    while y > 0
      p *= y % 10
      y /= 10
    end
    return x if p % t == 0

    x += 1
  end
end
''')

add("3346_maximum_frequency_of_an_element_after_performing_operations_i", r'''
# LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def lower_bound(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) >> 1
    if a[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def upper_bound(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) >> 1
    if a[mid] <= x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} num_operations
# @return {Integer}
def max_frequency(nums, k, num_operations)
  nums.sort!
  n = nums.length
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  ans = 1
  freq.each do |t, f|
    lo = lower_bound(nums, t - k)
    hi = upper_bound(nums, t + k)
    can = hi - lo
    use = [can, f + num_operations].min
    ans = use if use > ans
  end
  l = 0
  n.times do |r|
    l += 1 while nums[r] - nums[l] > 2 * k
    window = [r - l + 1, num_operations].min
    ans = window if window > ans
  end
  ans
end
''')

add("3347_maximum_frequency_of_an_element_after_performing_operations_ii", r'''
# LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def lower_bound(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) >> 1
    if a[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def upper_bound(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) >> 1
    if a[mid] <= x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} num_operations
# @return {Integer}
def max_frequency(nums, k, num_operations)
  nums.sort!
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  ans = 1
  candidates = []
  seen = {}
  nums.each do |x|
    [x - k, x, x + k].each do |t|
      unless seen[t]
        seen[t] = true
        candidates << t
      end
    end
  end
  candidates.each do |t|
    lo = lower_bound(nums, t - k)
    hi = upper_bound(nums, t + k)
    can = hi - lo
    f = freq[t] || 0
    use = [can, f + num_operations].min
    ans = use if use > ans
  end
  ans
end
''')

add("3348_smallest_divisible_digit_product_ii", r'''
# LeetCode 3348 - Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

# @param {String[]} res
# @param {Integer} i
# @param {Boolean} tight
# @param {Boolean} same_len
# @param {String} num
# @param {Integer} t
# @return {Boolean}
def digit_product_dfs(res, i, tight, same_len, num, t)
  if i == res.length
    prod = 1
    res.each do |c|
      prod *= c.ord - 48
      break if prod == 0
    end
    return prod % t == 0 && prod > 0
  end
  start = i == 0 ? "1" : "0"
  start = num[i] if tight && same_len && i < num.length
  (start.ord...58).each do |cc|
    c = cc.chr
    res[i] = c
    nt = tight && same_len && i < num.length && c == num[i]
    return true if digit_product_dfs(res, i + 1, nt, same_len, num, t)
  end
  false
end

# @param {String} num
# @param {Integer} t
# @return {String}
def smallest_number(num, t)
  tt = t
  9.downto(2) do |d|
    tt /= d while tt % d == 0
  end
  return "-1" if tt > 1

  61.times do |extra|
    len = num.length + extra
    res = Array.new(len, "")
    return res.join if digit_product_dfs(res, 0, true, extra == 0, num, t)
  end
  "-1"
end
''')

add("3349_adjacent_increasing_subarrays_detection_i", r'''
# LeetCode 3349 - Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

# @param {Integer[]} nums
# @param {Integer} start
# @param {Integer} k
# @return {Boolean}
def increasing_run?(nums, start, k)
  (start...(start + k - 1)).each do |i|
    return false if nums[i] >= nums[i + 1]
  end
  true
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def has_increasing_subarrays(nums, k)
  n = nums.length
  (0..(n - 2 * k)).each do |i|
    return true if increasing_run?(nums, i, k) && increasing_run?(nums, i + k, k)
  end
  false
end
''')

add("3350_adjacent_increasing_subarrays_detection_ii", r'''
# LeetCode 3350 - Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

# @param {Integer[]} up
# @param {Integer} n
# @param {Integer} k
# @return {Boolean}
def adjacent_inc_ok(up, n, k)
  (0..(n - 2 * k)).each do |i|
    return true if up[i] >= k && up[i + k] >= k
  end
  false
end

# @param {Integer[]} nums
# @return {Integer}
def max_increasing_subarrays(nums)
  n = nums.length
  up = Array.new(n, 0)
  up[n - 1] = 1
  (n - 2).downto(0) do |i|
    up[i] = nums[i] < nums[i + 1] ? up[i + 1] + 1 : 1
  end
  lo = 1
  hi = n / 2
  while lo < hi
    mid = (lo + hi + 1) / 2
    if adjacent_inc_ok(up, n, mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("3351_sum_of_good_subsequences", r'''
# LeetCode 3351 - Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_good_subsequences(nums)
  mod = 1_000_000_007
  cnt = {}
  ssum = {}
  ans = 0
  nums.each do |x|
    c = 1
    s = x
    if (cnt[x - 1] || 0) > 0
      c = (c + cnt[x - 1]) % mod
      s = (s + ssum[x - 1] + cnt[x - 1] * x % mod) % mod
    end
    if (cnt[x + 1] || 0) > 0
      c = (c + cnt[x + 1]) % mod
      s = (s + ssum[x + 1] + cnt[x + 1] * x % mod) % mod
    end
    cnt[x] = ((cnt[x] || 0) + c) % mod
    ssum[x] = ((ssum[x] || 0) + s) % mod
    ans = (ans + s) % mod
  end
  ans
end
''')

add("3352_count_k_reducible_numbers_less_than_n", r'''
# LeetCode 3352 - Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

# @param {Integer} x
# @return {Integer}
def bits_pop(x)
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_reducible_numbers(s, k)
  mod = 1_000_000_007
  red = Array.new(801, 0)
  red[1] = 0
  (2...801).each { |i| red[i] = 1 + red[bits_pop(i)] }
  memo = {}
  dfs = lambda do |pos, tight, ones|
    if pos == s.length
      return 0 if ones == 0
      return red[ones] <= k - 1 ? 1 : 0
    end
    ky = (pos << 32) | ((tight ? 1 : 0) << 16) | ones
    return memo[ky] if memo.key?(ky)

    up = tight ? (s[pos].ord - 48) : 1
    ans = 0
    (0..up).each do |d|
      nt = tight && d == up
      ans = (ans + dfs.call(pos + 1, nt, ones + d)) % mod
    end
    memo[ky] = ans
    ans
  end
  dfs.call(0, true, 0)
end
''')

add("3353_minimum_total_operations", r'''
# LeetCode 3353 - Minimum Total Operations
# https://leetcode.com/problems/minimum-total-operations/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  ops = 0
  (nums.length - 2).downto(0) { |i| ops += 1 if nums[i] != nums[i + 1] }
  ops
end
''')

add("3354_make_array_elements_equal_to_zero", r'''
# LeetCode 3354 - Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def count_valid_selections(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    next unless nums[i] == 0

    [-1, 1].each do |direction|
      a = nums.dup
      cur = i
      d = direction
      while cur >= 0 && cur < n
        if a[cur] == 0
          cur += d
        else
          a[cur] -= 1
          d = -d
          cur += d
        end
      end
      ans += 1 if a.all?(&:zero?)
    end
  end
  ans
end
''')

add("3355_zero_array_transformation_i", r'''
# LeetCode 3355 - Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean}
def is_zero_array(nums, queries)
  n = nums.length
  diff = Array.new(n + 1, 0)
  queries.each do |q|
    diff[q[0]] += 1
    diff[q[1] + 1] -= 1
  end
  cur = 0
  n.times do |i|
    cur += diff[i]
    return false if cur < nums[i]
  end
  true
end
''')

add("3356_zero_array_transformation_ii", r'''
# LeetCode 3356 - Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/

# @param {Integer} k
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @param {Integer} n
# @return {Boolean}
def zero_array_ok(k, nums, queries, n)
  diff = Array.new(n + 1, 0)
  k.times do |i|
    q = queries[i]
    diff[q[0]] += q[2]
    diff[q[1] + 1] -= q[2]
  end
  cur = 0
  n.times do |i|
    cur += diff[i]
    return false if cur < nums[i]
  end
  true
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def min_zero_array(nums, queries)
  n = nums.length
  return 0 if zero_array_ok(0, nums, queries, n)

  lo = 1
  hi = queries.length + 1
  while lo < hi
    mid = (lo + hi) >> 1
    if mid <= queries.length && zero_array_ok(mid, nums, queries, n)
      hi = mid
    else
      lo = mid + 1
    end
  end
  return -1 if lo > queries.length

  lo
end
''')

add("3357_minimize_the_maximum_adjacent_element_difference", r'''
# LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

# @param {Integer} d
# @param {Integer[]} nums
# @param {Integer} n
# @return {Boolean}
def adj_diff_ok(d, nums, n)
  prev = -1
  i = 0
  while i < n
    if nums[i] != -1
      return false if prev != -1 && (nums[i] - prev).abs > d

      prev = nums[i]
      i += 1
      next
    end
    j = i
    j += 1 while j < n && nums[j] == -1
    left = prev
    right = j < n ? nums[j] : -1
    gap = j - i
    return true if left == -1 && right == -1

    if left == -1 || right == -1
      prev = -1
      i = j
      next
    end
    return false if (left - right).abs > d * (gap + 1)

    prev = -1
    i = j
  end
  true
end

# @param {Integer[]} nums
# @return {Integer}
def min_difference(nums)
  n = nums.length
  lo = 0
  hi = 1_000_000_000
  while lo < hi
    mid = (lo + hi) / 2
    if adj_diff_ok(mid, nums, n)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3359_find_sorted_submatrices_with_maximum_element_at_most_k", r'''
# LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
# https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_sorted_matrices(grid, k)
  m = grid.length
  n = grid[0].length
  ans = 0
  m.times do |r1|
    (r1...m).each do |r2|
      n.times do |c1|
        (c1...n).each do |c2|
          good = true
          i = r1
          while i <= r2 && good
            (c1..c2).each do |j|
              if grid[i][j] > k
                good = false
                break
              end
              if j > c1 && grid[i][j] < grid[i][j - 1]
                good = false
                break
              end
              if i > r1 && grid[i][j] < grid[i - 1][j]
                good = false
                break
              end
            end
            i += 1
          end
          ans += 1 if good
        end
      end
    end
  end
  ans
end
''')

add("3360_stone_removal_game", r'''
# LeetCode 3360 - Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/

# @param {Integer} n
# @return {Boolean}
def can_alice_win(n)
  take = 10
  alice = true
  while n >= take && take > 0
    n -= take
    take -= 1
    alice = !alice
  end
  !alice
end
''')

add("3361_shift_distance_between_two_strings", r'''
# LeetCode 3361 - Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/

# @param {String} s
# @param {String} t
# @param {Integer[]} next_cost
# @param {Integer[]} previous_cost
# @return {Integer}
def shift_distance(s, t, next_cost, previous_cost)
  ans = 0
  s.length.times do |i|
    a = s[i].ord - 97
    b = t[i].ord - 97
    next if a == b

    fwd = 0
    x = a
    while x != b
      fwd += next_cost[x]
      x = (x + 1) % 26
    end
    bwd = 0
    x = a
    while x != b
      bwd += previous_cost[x]
      x = (x + 25) % 26
    end
    ans += fwd < bwd ? fwd : bwd
  end
  ans
end
''')

add("3362_zero_array_transformation_iii", r'''
# LeetCode 3362 - Zero Array Transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def max_removal(nums, queries)
  queries.sort_by! { |a| a[0] }
  h = []
  n = nums.length
  diff = Array.new(n + 1, 0)
  j = 0
  used = 0
  cur = 0
  n.times do |i|
    cur += diff[i]
    while j < queries.length && queries[j][0] == i
      h << queries[j][1]
      j += 1
    end
    while cur < nums[i]
      return -1 if h.empty?

      h.sort!.reverse!
      return -1 if h[0] < i

      r = h.shift
      cur += 1
      diff[r + 1] -= 1
      used += 1
    end
  end
  queries.length - used
end
''')

add("3363_find_the_maximum_number_of_fruits_collected", r'''
# LeetCode 3363 - Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

# @param {Integer[][]} fruits
# @return {Integer}
def max_collected_fruits(fruits)
  n = fruits.length
  ans = 0
  n.times do |i|
    ans += fruits[i][i]
    fruits[i][i] = 0
  end
  neg = -(1 << 30)
  dp2 = Array.new(n) { Array.new(n, neg) }
  dp3 = Array.new(n) { Array.new(n, neg) }
  dp2[0][n - 1] = fruits[0][n - 1]
  n.times do |i|
    n.times do |j|
      next if dp2[i][j] == neg

      [-1, 0, 1].each do |dj|
        ni = i + 1
        nj = j + dj
        next unless ni < n && nj >= 0 && nj < n && nj > ni

        v = dp2[i][j] + fruits[ni][nj]
        dp2[ni][nj] = v if v > dp2[ni][nj]
      end
    end
  end
  dp3[n - 1][0] = fruits[n - 1][0]
  n.times do |j|
    n.times do |i|
      next if dp3[i][j] == neg

      [-1, 0, 1].each do |di|
        ni = i + di
        nj = j + 1
        next unless ni >= 0 && ni < n && nj < n && ni > nj

        v = dp3[i][j] + fruits[ni][nj]
        dp3[ni][nj] = v if v > dp3[ni][nj]
      end
    end
  end
  ans + dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
end
''')

add("3364_minimum_positive_sum_subarray", r'''
# LeetCode 3364 - Minimum Positive Sum Subarray
# https://leetcode.com/problems/minimum-positive-sum-subarray/

# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def minimum_sum_subarray(nums, l, r)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 2_147_483_647
  found = false
  n.times do |i|
    length = l
    while length <= r && i + length <= n
      s = pref[i + length] - pref[i]
      if s > 0 && s < ans
        ans = s
        found = true
      end
      length += 1
    end
  end
  found ? ans : -1
end
''')

written = 0
failed = []
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    try:
        path.write_text(body, encoding="utf-8", newline="\n")
        if body.startswith("\ufeff") or "def solve(input)" in body:
            failed.append((name, "bom_or_stub"))
        else:
            written += 1
    except Exception as e:
        failed.append((name, str(e)))
print(f"batch16_c written={written} failed={failed}")
print("keys", len(S))
