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

  def peek
    @a[0]
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  def sum
    @a.sum
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

add("2520_count_the_digits_that_divide_a_number", r'''
# LeetCode 2520 - Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

# @param {Integer} num
# @return {Integer}
def count_digits(num)
  ans = 0
  x = num
  while x > 0
    d = x % 10
    ans += 1 if d != 0 && num % d == 0
    x /= 10
  end
  ans
end
''')

add("2521_distinct_prime_factors_of_product_of_array", r'''
# LeetCode 2521 - Distinct Prime Factors of Product of Array
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

# @param {Integer[]} nums
# @return {Integer}
def distinct_prime_factors(nums)
  seen = {}
  nums.each do |num|
    x = num
    p = 2
    while p * p <= x
      if x % p == 0
        seen[p] = true
        x /= p while x % p == 0
      end
      p += 1
    end
    seen[x] = true if x > 1
  end
  seen.size
end
''')

add("2522_partition_string_into_substrings_with_values_at_most_k", r'''
# LeetCode 2522 - Partition String Into Substrings With Values At Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_partition(s, k)
  ans = 1
  cur = 0
  s.each_char do |ch|
    d = ch.ord - 48
    return -1 if d > k

    nxt = cur * 10 + d
    if nxt > k
      ans += 1
      cur = d
    else
      cur = nxt
    end
  end
  ans
end
''')

add("2523_closest_prime_numbers_in_range", r'''
# LeetCode 2523 - Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range/

# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def closest_primes(left, right)
  is_prime = Array.new(right + 1, true)
  is_prime[0] = false if right >= 0
  is_prime[1] = false if right >= 1
  i = 2
  while i * i <= right
    if is_prime[i]
      j = i * i
      while j <= right
        is_prime[j] = false
        j += i
      end
    end
    i += 1
  end
  primes = (left..right).select { |x| is_prime[x] }
  return [-1, -1] if primes.length < 2

  best_diff = 10**18
  best = [-1, -1]
  (0...primes.length - 1).each do |i|
    d = primes[i + 1] - primes[i]
    if d < best_diff
      best_diff = d
      best = [primes[i], primes[i + 1]]
    end
  end
  best
end
''')

add("2524_maximum_frequency_score_of_a_subarray", r'''
# LeetCode 2524 - Maximum Frequency Score of a Subarray
# https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency_score(nums, k)
  mod = 1_000_000_007
  freq = Hash.new(0)

  mod_pow = lambda do |a, e|
    res = 1
    a %= mod
    while e > 0
      res = res * a % mod if e.odd?
      a = a * a % mod
      e >>= 1
    end
    res
  end

  add = lambda do |score, x|
    c = freq[x]
    score = (score - mod_pow.call(x, c) + mod) % mod if c > 0
    freq[x] = c + 1
    (score + mod_pow.call(x, c + 1)) % mod
  end

  remove = lambda do |score, x|
    c = freq[x]
    score = (score - mod_pow.call(x, c) + mod) % mod
    if c == 1
      freq.delete(x)
    else
      freq[x] = c - 1
      score = (score + mod_pow.call(x, c - 1)) % mod
    end
    score
  end

  score = 0
  best = 0
  nums.each_with_index do |num, i|
    score = add.call(score, num)
    score = remove.call(score, nums[i - k]) if i >= k
    best = score if i >= k - 1 && score > best
  end
  best
end
''')

add("2525_categorize_box_according_to_criteria", r'''
# LeetCode 2525 - Categorize Box According to Criteria
# https://leetcode.com/problems/categorize-box-according-to-criteria/

# @param {Integer} length
# @param {Integer} width
# @param {Integer} height
# @param {Integer} mass
# @return {String}
def categorize_box(length, width, height, mass)
  bulky = length >= 10_000 || width >= 10_000 || height >= 10_000 ||
          length * width * height >= 1_000_000_000
  heavy = mass >= 100
  return "Both" if bulky && heavy
  return "Bulky" if bulky
  return "Heavy" if heavy

  "Neither"
end
''')

add("2526_find_consecutive_integers_from_a_data_stream", r'''
# LeetCode 2526 - Find Consecutive Integers from a Data Stream
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream
  def initialize(value, k)
    @value = value
    @k = k
    @streak = 0
  end

  def consec(num)
    if num == @value
      @streak += 1
    else
      @streak = 0
    end
    @streak >= @k
  end
end
''')

add("2527_find_xor_beauty_of_array", r'''
# LeetCode 2527 - Find Xor-Beauty of Array
# https://leetcode.com/problems/find-xor-beauty-of-array/

# @param {Integer[]} nums
# @return {Integer}
def xor_beauty(nums)
  ans = 0
  nums.each { |x| ans ^= x }
  ans
end
''')

add("2528_maximize_the_minimum_powered_city", r'''
# LeetCode 2528 - Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

# @param {Integer[]} stations
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def max_power(stations, r, k)
  n = stations.length
  diff = Array.new(n + 1, 0)
  n.times do |i|
    left = [0, i - r].max
    right = [n - 1, i + r].min
    diff[left] += stations[i]
    diff[right + 1] -= stations[i]
  end
  power = Array.new(n, 0)
  cur = 0
  n.times do |i|
    cur += diff[i]
    power[i] = cur
  end
  lo = 0
  hi = k
  power.each { |p| hi = p if p > hi }
  hi += k

  ok = lambda do |x|
    extra = Array.new(n + 1, 0)
    have = 0
    used = 0
    n.times do |i|
      have += extra[i]
      need = x - (power[i] + have)
      if need > 0
        used += need
        return false if used > k

        have += need
        endi = i + 2 * r
        extra[endi + 1] -= need if endi + 1 <= n
      end
    end
    true
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

add("2529_maximum_count_of_positive_integer_and_negative_integer", r'''
# LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

# @param {Integer[]} nums
# @return {Integer}
def maximum_count(nums)
  pos = 0
  neg = 0
  nums.each do |x|
    if x > 0
      pos += 1
    elsif x < 0
      neg += 1
    end
  end
  [pos, neg].max
end
''')

add("2530_maximal_score_after_applying_k_operations", HEAP + r'''
# LeetCode 2530 - Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_kelements(nums, k)
  h = MinHeap.new(nums.map { |x| -x })
  ans = 0
  k.times do
    x = -h.pop
    ans += x
    h.push(-((x + 2) / 3))
  end
  ans
end
''')

add("2531_make_number_of_distinct_characters_equal", r'''
# LeetCode 2531 - Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

# @param {String} word1
# @param {String} word2
# @return {Boolean}
def is_it_possible(word1, word2)
  c1 = Array.new(26, 0)
  c2 = Array.new(26, 0)
  word1.each_byte { |b| c1[b - 97] += 1 }
  word2.each_byte { |b| c2[b - 97] += 1 }
  d1 = d2 = 0
  26.times do |i|
    d1 += 1 if c1[i] > 0
    d2 += 1 if c2[i] > 0
  end
  26.times do |a|
    next if c1[a] == 0

    26.times do |b|
      next if c2[b] == 0

      nd1 = d1
      nd2 = d2
      if a == b
        return true if nd1 == nd2

        next
      end
      nd1 -= 1 if c1[a] == 1
      nd1 += 1 if c1[b] == 0
      nd2 -= 1 if c2[b] == 1
      nd2 += 1 if c2[a] == 0
      return true if nd1 == nd2
    end
  end
  false
end
''')

add("2532_time_to_cross_a_bridge", HEAP + r'''
# LeetCode 2532 - Time to Cross a Bridge
# https://leetcode.com/problems/time-to-cross-a-bridge/

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} time
# @return {Integer}
def find_crossing_time(n, k, time)
  left = MinHeap.new
  right = MinHeap.new
  events = MinHeap.new
  ws = []
  k.times do |i|
    t = time[i]
    w = {
      idx: i,
      left_to_right: t[0],
      pick_old: t[1],
      right_to_left: t[2],
      put_new: t[3],
      efficiency: t[0] + t[2]
    }
    ws << w
    left.push([-w[:efficiency], -w[:idx], i])
  end
  cur = 0
  bridge_free = 0
  remain = n
  done = 0
  while done < n
    while !events.empty? && events.peek[0] <= cur
      _et, side, idx = events.pop
      w = ws[idx]
      if side == 0
        left.push([-w[:efficiency], -w[:idx], idx])
      else
        right.push([-w[:efficiency], -w[:idx], idx])
      end
    end
    if cur < bridge_free
      cur = bridge_free
      next
    end
    if !right.empty?
      _e, _id, idx = right.pop
      w = ws[idx]
      cur += w[:right_to_left]
      bridge_free = cur
      events.push([cur + w[:put_new], 0, w[:idx]])
      done += 1
      next
    end
    if !left.empty? && remain > 0
      _e, _id, idx = left.pop
      w = ws[idx]
      cur += w[:left_to_right]
      bridge_free = cur
      remain -= 1
      events.push([cur + w[:pick_old], 1, w[:idx]])
      next
    end
    break if events.empty?

    cur = events.peek[0]
  end
  cur
end
''')

add("2533_number_of_good_binary_strings", r'''
# LeetCode 2533 - Number of Good Binary Strings
# https://leetcode.com/problems/number-of-good-binary-strings/

# @param {Integer} min_length
# @param {Integer} max_length
# @param {Integer} one_group
# @param {Integer} zero_group
# @return {Integer}
def good_binary_strings(min_length, max_length, one_group, zero_group)
  mod = 1_000_000_007
  dp = Array.new(max_length + 1, 0)
  dp[0] = 1
  (0..max_length).each do |i|
    next if dp[i] == 0

    dp[i + one_group] = (dp[i + one_group] + dp[i]) % mod if i + one_group <= max_length
    dp[i + zero_group] = (dp[i + zero_group] + dp[i]) % mod if i + zero_group <= max_length
  end
  ans = 0
  (min_length..max_length).each { |i| ans = (ans + dp[i]) % mod }
  ans
end
''')

add("2534_time_taken_to_cross_the_door", r'''
# LeetCode 2534 - Time Taken to Cross the Door
# https://leetcode.com/problems/time-taken-to-cross-the-door/

# @param {Integer[]} arrival
# @param {Integer[]} state
# @return {Integer[]}
def time_taken(arrival, state)
  n = arrival.length
  ans = Array.new(n, 0)
  enter = []
  exitq = []
  i = 0
  t = 0
  prev = 1
  while i < n || !enter.empty? || !exitq.empty?
    while i < n && arrival[i] <= t
      if state[i] == 0
        enter << i
      else
        exitq << i
      end
      i += 1
    end
    if enter.empty? && exitq.empty?
      if i < n
        t = arrival[i]
        prev = 1
      end
      next
    end
    if prev == 1
      if !exitq.empty?
        ans[exitq.shift] = t
        prev = 1
      else
        ans[enter.shift] = t
        prev = 0
      end
    elsif !enter.empty?
      ans[enter.shift] = t
      prev = 0
    else
      ans[exitq.shift] = t
      prev = 1
    end
    t += 1
  end
  ans
end
''')

add("2535_difference_between_element_sum_and_digit_sum_of_an_array", r'''
# LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def difference_of_sum(nums)
  elem = 0
  digit = 0
  nums.each do |num|
    elem += num
    x = num
    while x > 0
      digit += x % 10
      x /= 10
    end
  end
  (elem - digit).abs
end
''')

add("2536_increment_submatrices_by_one", r'''
# LeetCode 2536 - Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[][]}
def range_add_queries(n, queries)
  diff = Array.new(n + 1) { Array.new(n + 1, 0) }
  queries.each do |q|
    r1, c1, r2, c2 = q
    diff[r1][c1] += 1
    diff[r1][c2 + 1] -= 1
    diff[r2 + 1][c1] -= 1
    diff[r2 + 1][c2 + 1] += 1
  end
  mat = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    n.times do |j|
      v = diff[i][j]
      v += mat[i - 1][j] if i > 0
      v += mat[i][j - 1] if j > 0
      v -= mat[i - 1][j - 1] if i > 0 && j > 0
      mat[i][j] = v
    end
  end
  mat
end
''')

add("2537_count_the_number_of_good_subarrays", r'''
# LeetCode 2537 - Count the Number of Good Subarrays
# https://leetcode.com/problems/count-the-number-of-good-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_good(nums, k)
  freq = Hash.new(0)
  pairs = 0
  ans = 0
  left = 0
  nums.each_with_index do |x, right|
    pairs += freq[x]
    freq[x] += 1
    while pairs >= k
      ans += nums.length - right
      freq[nums[left]] -= 1
      pairs -= freq[nums[left]]
      left += 1
    end
  end
  ans
end
''')

add("2538_difference_between_maximum_and_minimum_price_sum", r'''
# LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @return {Integer}
def max_output(n, edges, price)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0

  dfs = lambda do |u, p|
    max_child = 0
    g[u].each do |v|
      next if v == p

      child = dfs.call(v, u)
      max_child = child if child > max_child
      ans = child if child > ans
    end
    price[u] + max_child
  end

  dfs.call(0, -1)
  ans
end
''')

add("2539_count_the_number_of_good_subsequences", r'''
# LeetCode 2539 - Count the Number of Good Subsequences
# https://leetcode.com/problems/count-the-number-of-good-subsequences/

# @param {String} s
# @return {Integer}
def count_good_subsequences(s)
  mod = 1_000_000_007
  cnt = Array.new(26, 0)
  maxf = 0
  s.each_byte do |b|
    idx = b - 97
    cnt[idx] += 1
    maxf = cnt[idx] if cnt[idx] > maxf
  end

  mod_pow = lambda do |a, e|
    res = 1
    while e > 0
      res = res * a % mod if e.odd?
      a = a * a % mod
      e >>= 1
    end
    res
  end

  fact = Array.new(maxf + 1, 0)
  inv_fact = Array.new(maxf + 1, 0)
  fact[0] = 1
  (1..maxf).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact[maxf] = mod_pow.call(fact[maxf], mod - 2)
  maxf.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }

  comb = lambda do |n, k|
    return 0 if k < 0 || k > n

    fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod
  end

  ans = 0
  (1..maxf).each do |k|
    ways = 1
    26.times do |i|
      ways = ways * (1 + comb.call(cnt[i], k)) % mod if cnt[i] >= k
    end
    ans = (ans + ways - 1 + mod) % mod
  end
  ans
end
''')

add("2540_minimum_common_value", r'''
# LeetCode 2540 - Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def get_common(nums1, nums2)
  i = j = 0
  while i < nums1.length && j < nums2.length
    return nums1[i] if nums1[i] == nums2[j]

    if nums1[i] < nums2[j]
      i += 1
    else
      j += 1
    end
  end
  -1
end
''')

add("2541_minimum_operations_to_make_array_equal_ii", r'''
# LeetCode 2541 - Minimum Operations to Make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def min_operations(nums1, nums2, k)
  if k == 0
    nums1.each_with_index { |x, i| return -1 if x != nums2[i] }
    return 0
  end
  pos = 0
  neg = 0
  nums1.each_with_index do |x, i|
    d = x - nums2[i]
    return -1 if d % k != 0

    if d > 0
      pos += d / k
    else
      neg += (-d) / k
    end
  end
  pos != neg ? -1 : pos
end
''')

add("2542_maximum_subsequence_score", HEAP + r'''
# LeetCode 2542 - Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def max_score(nums1, nums2, k)
  n = nums1.length
  idx = (0...n).to_a.sort_by { |i| -nums2[i] }
  pq = MinHeap.new
  s = 0
  ans = 0
  idx.each do |i|
    pq.push(nums1[i])
    s += nums1[i]
    if pq.length > k
      s -= pq.pop
    end
    if pq.length == k
      cand = s * nums2[i]
      ans = cand if cand > ans
    end
  end
  ans
end
''')

add("2543_check_if_point_is_reachable", r'''
# LeetCode 2543 - Check if Point Is Reachable
# https://leetcode.com/problems/check-if-point-is-reachable/

# @param {Integer} target_x
# @param {Integer} target_y
# @return {Boolean}
def is_reachable(target_x, target_y)
  g = target_x.gcd(target_y)
  g /= 2 while g.even?
  g == 1
end
''')

add("2544_alternating_digit_sum", r'''
# LeetCode 2544 - Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/

# @param {Integer} n
# @return {Integer}
def alternate_digit_sum(n)
  digits = []
  x = n
  while x > 0
    digits << (x % 10)
    x /= 10
  end
  ans = 0
  sign = 1
  (digits.length - 1).downto(0) do |i|
    ans += sign * digits[i]
    sign = -sign
  end
  ans
end
''')

written = 0
for folder, body in S.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
