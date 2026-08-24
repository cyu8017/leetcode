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

add("2545_sort_the_students_by_their_kth_score", r'''
# LeetCode 2545 - Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

# @param {Integer[][]} score
# @param {Integer} k
# @return {Integer[][]}
def sort_the_students(score, k)
  score.sort_by { |row| -row[k] }
end
''')

add("2546_apply_bitwise_operations_to_make_strings_equal", r'''
# LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

# @param {String} s
# @param {String} target
# @return {Boolean}
def make_strings_equal(s, target)
  has1s = false
  has1t = false
  s.length.times do |i|
    has1s = true if s[i] == "1"
    has1t = true if target[i] == "1"
  end
  has1s == has1t
end
''')

add("2547_minimum_cost_to_split_an_array", r'''
# LeetCode 2547 - Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_cost(nums, k)
  n = nums.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  n.times do |i|
    freq = Hash.new(0)
    trimmed = 0
    (i...n).each do |j|
      c = freq[nums[j]] + 1
      freq[nums[j]] = c
      if c == 2
        trimmed += 2
      elsif c > 2
        trimmed += 1
      end
      cost = dp[i] + k + trimmed
      dp[j + 1] = cost if cost < dp[j + 1]
    end
  end
  dp[n]
end
''')

add("2548_maximum_price_to_fill_a_bag", r'''
# LeetCode 2548 - Maximum Price to Fill a Bag
# https://leetcode.com/problems/maximum-price-to-fill-a-bag/

# @param {Integer[][]} items
# @param {Integer} capacity
# @return {Float}
def max_price(items, capacity)
  items = items.sort_by { |it| -(it[0].to_f / it[1]) }
  ans = 0.0
  remain = capacity
  items.each do |price, weight|
    if remain >= weight
      ans += price
      remain -= weight
    else
      ans += price.to_f * remain / weight
      remain = 0
      break
    end
  end
  return -1 if remain > 0

  ans
end
''')

add("2549_count_distinct_numbers_on_board", r'''
# LeetCode 2549 - Count Distinct Numbers on Board
# https://leetcode.com/problems/count-distinct-numbers-on-board/

# @param {Integer} n
# @return {Integer}
def distinct_integers(n)
  return 1 if n == 1

  n - 1
end
''')

add("2550_count_collisions_of_monkeys_on_a_polygon", r'''
# LeetCode 2550 - Count Collisions of Monkeys on a Polygon
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

# @param {Integer} n
# @return {Integer}
def monkey_move(n)
  mod = 1_000_000_007
  ((2.pow(n, mod) - 2) + mod) % mod
end
''')

add("2551_put_marbles_in_bags", r'''
# LeetCode 2551 - Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

# @param {Integer[]} weights
# @param {Integer} k
# @return {Integer}
def put_marbles(weights, k)
  n = weights.length
  return 0 if k == 1 || k == n

  pair = (0...n - 1).map { |i| weights[i] + weights[i + 1] }
  pair.sort!
  mn = 0
  mx = 0
  (k - 1).times do |i|
    mn += pair[i]
    mx += pair[n - 2 - i]
  end
  mx - mn
end
''')

add("2552_count_increasing_quadruplets", r'''
# LeetCode 2552 - Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/

# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
  n = nums.length
  ans = 0
  great = Array.new(n, 0)
  n.times do |j|
    j.times do |i|
      if nums[i] < nums[j]
        ans += great[i]
      elsif nums[i] > nums[j]
        great[i] += 1
      end
    end
  end
  ans
end
''')

add("2553_separate_the_digits_in_an_array", r'''
# LeetCode 2553 - Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
  ans = []
  nums.each do |num|
    digits = []
    while num > 0
      digits << (num % 10)
      num /= 10
    end
    (digits.length - 1).downto(0) { |i| ans << digits[i] }
  end
  ans
end
''')

add("2554_maximum_number_of_integers_to_choose_from_a_range_i", r'''
# LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
  ban = {}
  banned.each { |x| ban[x] = true }
  ans = 0
  s = 0
  (1..n).each do |i|
    next if ban[i]
    break if s + i > max_sum

    s += i
    ans += 1
  end
  ans
end
''')

add("2555_maximize_win_from_two_segments", r'''
# LeetCode 2555 - Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/

# @param {Integer[]} prize_positions
# @param {Integer} k
# @return {Integer}
def maximize_win(prize_positions, k)
  n = prize_positions.length
  dp = Array.new(n + 1, 0)
  ans = 0
  left = 0
  n.times do |right|
    left += 1 while prize_positions[right] - prize_positions[left] > k
    cur = right - left + 1
    ans = dp[left] + cur if dp[left] + cur > ans
    best = cur
    best = dp[right] if dp[right] > best
    dp[right + 1] = best
  end
  ans
end
''')

add("2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip", r'''
# LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

# @param {Integer[][]} grid
# @return {Boolean}
def is_possible_to_cut_path(grid)
  m = grid.length
  n = grid[0].length

  dfs = lambda do |r, c|
    return true if r == m - 1 && c == n - 1
    return false if r >= m || c >= n || grid[r][c] == 0

    grid[r][c] = 0 unless r == 0 && c == 0
    dfs.call(r + 1, c) || dfs.call(r, c + 1)
  end

  return true unless dfs.call(0, 0)

  grid[0][0] = 1
  !dfs.call(0, 0)
end
''')

add("2557_maximum_number_of_integers_to_choose_from_a_range_ii", r'''
# LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
  banned = banned.sort
  uniq = []
  banned.each do |x|
    uniq << x if x >= 1 && x <= n && (uniq.empty? || uniq[-1] != x)
  end
  ans = 0
  remain = max_sum
  prev = 0

  check = lambda do |l, r|
    return if l > r || remain <= 0

    lo = l
    hi = r
    best = l - 1
    while lo <= hi
      mid = (lo + hi) / 2
      cnt = mid - l + 1
      s = (l + mid) * cnt / 2
      if s <= remain
        best = mid
        lo = mid + 1
      else
        hi = mid - 1
      end
    end
    if best >= l
      cnt = best - l + 1
      ans += cnt
      remain -= (l + best) * cnt / 2
    end
  end

  uniq.each do |b|
    check.call(prev + 1, b - 1)
    prev = b
  end
  check.call(prev + 1, n)
  ans
end
''')

add("2558_take_gifts_from_the_richest_pile", HEAP + r'''
# LeetCode 2558 - Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

# @param {Integer[]} gifts
# @param {Integer} k
# @return {Integer}
def pick_gifts(gifts, k)
  h = MinHeap.new(gifts.map { |g| -g })
  k.times do
    x = -h.pop
    h.push(-Integer.sqrt(x))
  end
  -h.sum
end
''')

add("2559_count_vowel_strings_in_ranges", r'''
# LeetCode 2559 - Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

# @param {String[]} words
# @param {Integer[][]} queries
# @return {Integer[]}
def vowel_strings(words, queries)
  is_v = lambda { |c| c == "a" || c == "e" || c == "i" || c == "o" || c == "u" }
  n = words.length
  pref = Array.new(n + 1, 0)
  n.times do |i|
    pref[i + 1] = pref[i]
    w = words[i]
    pref[i + 1] += 1 if !w.empty? && is_v.call(w[0]) && is_v.call(w[-1])
  end
  queries.map { |l, r| pref[r + 1] - pref[l] }
end
''')

add("2560_house_robber_iv", r'''
# LeetCode 2560 - House Robber IV
# https://leetcode.com/problems/house-robber-iv/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_capability(nums, k)
  lo = nums.min
  hi = nums.max

  ok = lambda do |cap|
    cnt = 0
    i = 0
    while i < nums.length
      if nums[i] <= cap
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    cnt >= k
  end

  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("2561_rearranging_fruits", r'''
# LeetCode 2561 - Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/

# @param {Integer[]} basket1
# @param {Integer[]} basket2
# @return {Integer}
def min_cost(basket1, basket2)
  freq = Hash.new(0)
  mn = Float::INFINITY
  basket1.each do |x|
    freq[x] += 1
    mn = x if x < mn
  end
  basket2.each do |x|
    freq[x] -= 1
    mn = x if x < mn
  end
  extra = []
  freq.each do |key, v|
    return -1 if v.odd?

    (v.abs / 2).times { extra << key }
  end
  extra.sort!
  ans = 0
  (extra.length / 2).times do |i|
    cand = extra[i]
    twice = 2 * mn
    ans += cand < twice ? cand : twice
  end
  ans
end
''')

add("2562_find_the_array_concatenation_value", r'''
# LeetCode 2562 - Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/

# @param {Integer[]} nums
# @return {Integer}
def find_the_array_conc_val(nums)
  ans = 0
  l = 0
  r = nums.length - 1
  while l <= r
    if l == r
      ans += nums[l]
      break
    end
    left = nums[l]
    right = nums[r]
    p = 1
    t = right
    while t > 0
      p *= 10
      t /= 10
    end
    ans += left * p + right
    l += 1
    r -= 1
  end
  ans
end
''')

add("2563_count_the_number_of_fair_pairs", r'''
# LeetCode 2563 - Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def count_fair_pairs(nums, lower, upper)
  nums = nums.sort

  count = lambda do |x|
    ans = 0
    l = 0
    r = nums.length - 1
    while l < r
      if nums[l] + nums[r] <= x
        ans += r - l
        l += 1
      else
        r -= 1
      end
    end
    ans
  end

  count.call(upper) - count.call(lower - 1)
end
''')

add("2564_substring_xor_queries", r'''
# LeetCode 2564 - Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[][]}
def substring_xor_queries(s, queries)
  pos = {}
  n = s.length
  n.times do |i|
    if s[i] == "0"
      pos[0] = [i, i] unless pos.key?(0)
      next
    end
    val = 0
    i.upto([n, i + 30].min - 1) do |j|
      val = val * 2 + (s[j].ord - 48)
      pos[val] = [i, j] unless pos.key?(val)
    end
  end
  queries.map do |a, b|
    need = a ^ b
    pos.key?(need) ? pos[need].dup : [-1, -1]
  end
end
''')

add("2565_subsequence_with_the_minimum_score", r'''
# LeetCode 2565 - Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

# @param {String} s
# @param {String} t
# @return {Integer}
def minimum_score(s, t)
  n = s.length
  m = t.length
  left = Array.new(m, -1)
  right = Array.new(m, -1)
  j = 0
  i = 0
  while i < n && j < m
    if s[i] == t[j]
      left[j] = i
      j += 1
    end
    i += 1
  end
  j = m - 1
  i = n - 1
  while i >= 0 && j >= 0
    if s[i] == t[j]
      right[j] = i
      j -= 1
    end
    i -= 1
  end
  return 0 if m > 0 && left[m - 1] != -1

  ans = m
  m.times do |i|
    next unless right[i] != -1

    ans = i if i < ans
    break
  end
  (m - 1).downto(0) do |i|
    next unless left[i] != -1

    rem = m - 1 - i
    ans = rem if rem < ans
    break
  end
  j = 0
  m.times do |i|
    break if left[i] == -1

    j += 1 while j < m && (right[j] == -1 || right[j] <= left[i])
    if j < m
      rem = j - i - 1
      ans = rem if rem < ans
    end
  end
  ans
end
''')

add("2566_maximum_difference_by_remapping_a_digit", r'''
# LeetCode 2566 - Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

# @param {Integer} num
# @return {Integer}
def min_max_difference(num)
  s = num.to_s

  remap = lambda do |frm, to|
    v = 0
    s.each_char do |c|
      d = c == frm ? to : c
      v = v * 10 + (d.ord - 48)
    end
    v
  end

  max_v = num
  s.each_char do |c|
    if c != "9"
      max_v = remap.call(c, "9")
      break
    end
  end
  min_v = remap.call(s[0], "0")
  max_v - min_v
end
''')

add("2567_minimum_score_by_changing_two_elements", r'''
# LeetCode 2567 - Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

# @param {Integer[]} nums
# @return {Integer}
def minimize_sum(nums)
  nums = nums.sort
  n = nums.length
  [nums[n - 1] - nums[2], nums[n - 3] - nums[0], nums[n - 2] - nums[1]].min
end
''')

add("2568_minimum_impossible_or", r'''
# LeetCode 2568 - Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/

# @param {Integer[]} nums
# @return {Integer}
def min_impossible_or(nums)
  s = {}
  nums.each { |x| s[x] = true }
  x = 1
  while s[x]
    x <<= 1
  end
  x
end
''')

add("2569_handling_sum_queries_after_update", r'''
# LeetCode 2569 - Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def handle_query(nums1, nums2, queries)
  n = nums1.length
  ones = Array.new(4 * n, 0)
  lazy = Array.new(4 * n, false)

  build = nil
  build = lambda do |idx, l, r|
    if l == r
      ones[idx] = nums1[l]
      return
    end
    m = (l + r) >> 1
    build.call(idx * 2, l, m)
    build.call(idx * 2 + 1, m + 1, r)
    ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
  end

  apply = lambda do |idx, l, r|
    ones[idx] = (r - l + 1) - ones[idx]
    lazy[idx] = !lazy[idx]
  end

  push = lambda do |idx, l, r|
    if lazy[idx] && l != r
      m = (l + r) >> 1
      apply.call(idx * 2, l, m)
      apply.call(idx * 2 + 1, m + 1, r)
      lazy[idx] = false
    end
  end

  update = nil
  update = lambda do |idx, l, r, ql, qr|
    if ql <= l && r <= qr
      apply.call(idx, l, r)
      return
    end
    push.call(idx, l, r)
    m = (l + r) >> 1
    update.call(idx * 2, l, m, ql, qr) if ql <= m
    update.call(idx * 2 + 1, m + 1, r, ql, qr) if qr > m
    ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
  end

  build.call(1, 0, n - 1)
  sum2 = nums2.sum
  ans = []
  queries.each do |q|
    if q[0] == 1
      update.call(1, 0, n - 1, q[1], q[2])
    elsif q[0] == 2
      sum2 += q[1] * ones[1]
    else
      ans << sum2
    end
  end
  ans
end
''')

written = 0
for folder, body in S.items():
    path = ROOT / folder / "solution.rb"
    # For heap files, put header first
    if body.lstrip().startswith("class MinHeap"):
        # extract first leetcode header from after heap - already has header after HEAP
        pass
    path.write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
