#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3395_subsequences_with_a_unique_middle_mode_i", r'''
# LeetCode 3395 - Subsequences with a Unique Middle Mode I
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

# @param {Integer[]} nums
# @return {Integer}
def subsequences_with_middle_mode(nums)
  mod = 1_000_000_007
  n = nums.length
  ans = 0
  (2...(n - 2)).each do |mid|
    (0...mid).each do |a|
      ((a + 1)...mid).each do |b|
        ((mid + 1)...n).each do |c|
          ((c + 1)...n).each do |d|
            ans += 1 if unique_mode_3395([nums[a], nums[b], nums[mid], nums[c], nums[d]])
          end
        end
      end
    end
  end
  ans % mod
end

def unique_mode_3395(a)
  freq = Hash.new(0)
  a.each { |x| freq[x] += 1 }
  best = 0
  cnt = 0
  freq.each_value do |f|
    if f > best
      best = f
      cnt = 1
    elsif f == best
      cnt += 1
    end
  end
  cnt == 1
end
''')

add("3396_minimum_number_of_operations_to_make_elements_in_array_distinct", r'''
# LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  lst = nums.dup
  ops = 0
  loop do
    seen = {}
    dup = false
    lst.each do |x|
      if seen[x]
        dup = true
        break
      end
      seen[x] = true
    end
    return ops unless dup
    return ops + 1 if lst.length <= 3

    lst = lst[3..]
    ops += 1
  end
end
''')

add("3397_maximum_number_of_distinct_elements_after_operations", r'''
# LeetCode 3397 - Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_distinct_elements(nums, k)
  nums = nums.sort
  ans = 0
  prev = -4_503_599_627_370_496
  nums.each do |x|
    cur = x - k
    cur = prev + 1 if cur <= prev
    next if cur > x + k

    ans += 1
    prev = cur
  end
  ans
end
''')

add("3398_smallest_substring_with_identical_characters_i", r'''
# LeetCode 3398 - Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

# @param {String} s
# @param {Integer} num_ops
# @return {Integer}
def min_length(s, num_ops)
  n = s.length
  ok = lambda do |len|
    return false if len == 0

    ops = 0
    i = 0
    while i < n
      j = i
      j += 1 while j < n && s[j] == s[i]
      ops += (j - i) / (len + 1)
      i = j
    end
    ops <= num_ops
  end
  lo = 1
  hi = n
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

add("3399_smallest_substring_with_identical_characters_ii", r'''
# LeetCode 3399 - Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

# @param {String} s
# @param {Integer} num_ops
# @return {Integer}
def min_length(s, num_ops)
  n = s.length
  ok = lambda do |len|
    ops = 0
    i = 0
    while i < n
      j = i
      j += 1 while j < n && s[j] == s[i]
      ops += (j - i) / (len + 1)
      i = j
    end
    ops <= num_ops
  end
  lo = 1
  hi = n
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

add("3400_maximum_number_of_matching_indices_after_right_shifts", r'''
# LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
# https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximum_matching_indices(nums1, nums2)
  n = nums1.length
  ans = 0
  (0...n).each do |shift|
    cnt = 0
    (0...n).each do |i|
      cnt += 1 if nums1[(i - shift + n) % n] == nums2[i]
    end
    ans = cnt if cnt > ans
  end
  ans
end
''')

add("3402_minimum_operations_to_make_columns_strictly_increasing", r'''
# LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  ans = 0
  (0...n).each do |j|
    (1...m).each do |i|
      if grid[i][j] <= grid[i - 1][j]
        need = grid[i - 1][j] + 1
        ans += need - grid[i][j]
        grid[i][j] = need
      end
    end
  end
  ans
end
''')

add("3403_find_the_lexicographically_largest_string_from_the_box_i", r'''
# LeetCode 3403 - Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

# @param {String} word
# @param {Integer} num_friends
# @return {String}
def answer_string(word, num_friends)
  return word if num_friends == 1

  n = word.length
  max_len = n - (num_friends - 1)
  ans = ""
  (0...n).each do |i|
    last = i + max_len
    last = n if last > n
    cand = word[i...last]
    ans = cand if cand > ans
  end
  ans
end
''')

add("3404_count_special_subsequences", r'''
# LeetCode 3404 - Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def number_of_subsequences(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    ((i + 2)...n).each do |j|
      ((j + 2)...n).each do |k|
        ((k + 2)...n).each do |l|
          ans += 1 if nums[i] * nums[k] == nums[j] * nums[l]
        end
      end
    end
  end
  ans
end
''')

add("3405_count_the_number_of_arrays_with_k_matching_adjacent_elements", r'''
# LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def count_good_arrays(n, m, k)
  mod = 1_000_000_007
  (comb_3405(n - 1, k, mod) * m % mod * mod_pow_3405(m - 1, n - 1 - k, mod)) % mod
end

def mod_pow_3405(a, e, mod)
  r = 1
  base = ((a % mod) + mod) % mod
  exp = e
  while exp > 0
    r = (r * base) % mod if (exp & 1) != 0
    base = (base * base) % mod
    exp >>= 1
  end
  r
end

def comb_3405(nn, kk, mod)
  return 0 if kk < 0 || kk > nn

  num = 1
  den = 1
  (0...kk).each do |i|
    num = (num * (nn - i)) % mod
    den = (den * (i + 1)) % mod
  end
  (num * mod_pow_3405(den, mod - 2, mod)) % mod
end
''')

add("3406_find_the_lexicographically_largest_string_from_the_box_ii", r'''
# LeetCode 3406 - Find the Lexicographically Largest String From the Box II
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

# @param {String} word
# @param {Integer} num_friends
# @return {String}
def answer_string(word, num_friends)
  return word if num_friends == 1

  n = word.length
  max_len = n - (num_friends - 1)
  ans = ""
  (0...n).each do |i|
    last = i + max_len
    last = n if last > n
    cand = word[i...last]
    ans = cand if cand > ans
  end
  ans
end
''')

add("3407_substring_matching_pattern", r'''
# LeetCode 3407 - Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/

# @param {String} s
# @param {String} p
# @return {Boolean}
def has_match(s, p)
  i = p.index("*")
  left = p[0...i]
  right = p[(i + 1)..]
  li = s.index(left)
  return false if li.nil?

  !s.index(right, li + left.length).nil?
end
''')

add("3408_design_task_manager", r'''
# LeetCode 3408 - Design Task Manager
# https://leetcode.com/problems/design-task-manager/

class TaskManager
  def initialize(tasks)
    @pri = {}
    @user = {}
    @h = []
    tasks.each { |t| add(t[0], t[1], t[2]) }
  end

  def add(user_id, task_id, priority)
    @pri[task_id] = priority
    @user[task_id] = user_id
    @h << [priority, task_id, user_id]
  end

  def edit(task_id, new_priority)
    @pri[task_id] = new_priority
    @h << [new_priority, task_id, @user[task_id]]
  end

  def rmv(task_id)
    @pri.delete(task_id)
    @user.delete(task_id)
  end

  def exec_top
    @h.sort_by! { |a| [a[0], a[1]] }
    until @h.empty?
      top = @h.pop
      p = @pri[top[1]]
      if !p.nil? && p == top[0] && @user[top[1]] == top[2]
        @pri.delete(top[1])
        uid = @user[top[1]]
        @user.delete(top[1])
        return uid
      end
    end
    -1
  end
end
''')

add("3409_longest_subsequence_with_decreasing_adjacent_difference", r'''
# LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  n = nums.length
  ans = 1
  dp = Array.new(n) { Array.new(301, 0) }
  (0...n).each do |i|
    (0...i).each do |j|
      d = (nums[i] - nums[j]).abs
      best = 1
      (d..300).each do |pd|
        best = dp[j][pd] if dp[j][pd] > best
      end
      dp[i][d] = best + 1 if best + 1 > dp[i][d]
      ans = dp[i][d] if dp[i][d] > ans
    end
    dp[i][0] = 1 if dp[i][0] < 1
  end
  ans
end
''')

add("3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element", r'''
# LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

# @param {Integer[]} nums
# @return {Integer}
def max_subarray_sum(nums)
  ans = kadane_3410(nums)
  uniq = {}
  nums.each { |x| uniq[x] = true if x < 0 }
  uniq.each_key do |v|
    b = nums.select { |x| x != v }
    next if b.empty?

    cand = kadane_3410(b)
    ans = cand if cand > ans
  end
  ans
end

def kadane_3410(a)
  best = -9_007_199_254_740_991
  cur = 0
  a.each do |x|
    cur += x
    best = cur if cur > best
    cur = 0 if cur < 0
  end
  all_neg = true
  mx = a[0]
  a.each do |x|
    mx = x if x > mx
    all_neg = false if x >= 0
  end
  return mx if all_neg

  best
end
''')

add("3411_maximum_subarray_with_equal_products", r'''
# LeetCode 3411 - Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/

# @param {Integer[]} nums
# @return {Integer}
def max_length(nums)
  n = nums.length
  ans = 1
  (0...n).each do |i|
    prod = 1
    g = 0
    l = 1
    (i...n).each do |j|
      break if prod > 1_000_000_000 / nums[j]

      prod *= nums[j]
      if g == 0
        g = nums[j]
        l = nums[j]
      else
        g = gcd_3411(g, nums[j])
        l = l / gcd_3411(l, nums[j]) * nums[j]
      end
      ans = j - i + 1 if prod == l * g && j - i + 1 > ans
    end
  end
  ans
end

def gcd_3411(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end
''')

add("3412_find_mirror_score_of_a_string", r'''
# LeetCode 3412 - Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/

# @param {String} s
# @return {Integer}
def calculate_score(s)
  stacks = Array.new(26) { [] }
  ans = 0
  s.each_char.with_index do |ch, i|
    ci = ch.ord - 97
    mir = 25 - ci
    if !stacks[mir].empty?
      j = stacks[mir].pop
      ans += i - j
    else
      stacks[ci] << i
    end
  end
  ans
end
''')

add("3413_maximum_coins_from_k_consecutive_bags", r'''
# LeetCode 3413 - Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

# @param {Integer[][]} coins
# @param {Integer} k
# @return {Integer}
def maximum_coins(coins, k)
  coins = coins.sort_by { |a| a[0] }
  ans = 0
  n = coins.length
  (0...n).each do |i|
    s = 0
    start = coins[i][0]
    last = start + k - 1
    j = i
    while j < n && coins[j][0] <= last
      l = coins[j][0]
      r = coins[j][1]
      r = last if r > last
      l = start if l < start
      s += (r - l + 1) * coins[j][2] if l <= r
      j += 1
    end
    ans = s if s > ans
  end
  (0...n).each do |i|
    s = 0
    last = coins[i][1]
    start = last - k + 1
    (0..i).each do |j|
      l = coins[j][0]
      r = coins[j][1]
      l = start if l < start
      r = last if r > last
      s += (r - l + 1) * coins[j][2] if l <= r
    end
    ans = s if s > ans
  end
  ans
end
''')

add("3414_maximum_score_of_non_overlapping_intervals", r'''
# LeetCode 3414 - Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

# @param {Integer[][]} intervals
# @return {Integer[]}
def maximum_weight(intervals)
  n = intervals.length
  arr = intervals.each_with_index.map { |it, i| { l: it[0], r: it[1], w: it[2], i: i } }
  arr.sort_by! { |a| a[:r] }
  dp = Array.new(n + 1) { Array.new(5) { { score: 0, idx: [] } } }
  (1..n).each do |i|
    cur = arr[i - 1]
    (0...5).each { |t| dp[i][t] = copy_state_3414(dp[i - 1][t]) }
    lo = 0
    hi = i - 1
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid][:r] < cur[:l]
        lo = mid + 1
      else
        hi = mid
      end
    end
    prev = lo
    (1...5).each do |t|
      prev_state = dp[prev][t - 1]
      cand = copy_state_3414(prev_state)
      cand[:score] = prev_state[:score] + cur[:w]
      cand[:idx] << cur[:i]
      cand[:idx].sort!
      dp[i][t] = better_3414(dp[i][t], cand)
    end
  end
  best = dp[n][0]
  (1...5).each { |t| best = better_3414(best, dp[n][t]) }
  best[:idx]
end

def copy_state_3414(s)
  { score: s[:score], idx: s[:idx].dup }
end

def better_3414(a, b)
  return a[:score] > b[:score] ? a : b if a[:score] != b[:score]

  m = [a[:idx].length, b[:idx].length].min
  (0...m).each do |i|
    return a[:idx][i] < b[:idx][i] ? a : b if a[:idx][i] != b[:idx][i]
  end
  a[:idx].length <= b[:idx].length ? a : b
end
''')

add("3416_subsequences_with_a_unique_middle_mode_ii", r'''
# LeetCode 3416 - Subsequences with a Unique Middle Mode II
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

# @param {Integer[]} nums
# @return {Integer}
def subsequences_with_middle_mode(nums)
  mod = 1_000_000_007
  n = nums.length
  ans = 0
  (2...(n - 2)).each do |mid|
    (0...mid).each do |a|
      ((a + 1)...mid).each do |b|
        ((mid + 1)...n).each do |c|
          ((c + 1)...n).each do |d|
            ans = (ans + 1) % mod if unique_mode_3416([nums[a], nums[b], nums[mid], nums[c], nums[d]])
          end
        end
      end
    end
  end
  ans
end

def unique_mode_3416(a)
  freq = Hash.new(0)
  a.each { |x| freq[x] += 1 }
  best = 0
  cnt = 0
  freq.each_value do |f|
    if f > best
      best = f
      cnt = 1
    elsif f == best
      cnt += 1
    end
  end
  cnt == 1
end
''')

add("3417_zigzag_grid_traversal_with_skip", r'''
# LeetCode 3417 - Zigzag Grid Traversal With Skip
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

# @param {Integer[][]} grid
# @return {Integer[]}
def zigzag_traversal(grid)
  ans = []
  skip = false
  grid.each_with_index do |row, i|
    if i.even?
      row.each do |v|
        ans << v unless skip
        skip = !skip
      end
    else
      (row.length - 1).downto(0) do |j|
        ans << row[j] unless skip
        skip = !skip
      end
    end
  end
  ans
end
''')

add("3418_maximum_amount_of_money_robot_can_earn", r'''
# LeetCode 3418 - Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

# @param {Integer[][]} coins
# @return {Integer}
def maximum_amount(coins)
  m = coins.length
  n = coins[0].length
  neg = -(1 << 30)
  dp = Array.new(m) { Array.new(n) { Array.new(3, neg) } }
  if coins[0][0] < 0
    dp[0][0][0] = coins[0][0]
    dp[0][0][1] = 0
    dp[0][0][2] = 0
  else
    dp[0][0][0] = coins[0][0]
    dp[0][0][1] = coins[0][0]
    dp[0][0][2] = coins[0][0]
  end
  (0...m).each do |i|
    (0...n).each do |j|
      next if i == 0 && j == 0

      (0...3).each do |k|
        best = neg
        best = [best, dp[i - 1][j][k]].max if i > 0
        best = [best, dp[i][j - 1][k]].max if j > 0
        next if best == neg

        if coins[i][j] >= 0
          dp[i][j][k] = best + coins[i][j]
        else
          dp[i][j][k] = [dp[i][j][k], best + coins[i][j]].max
        end
      end
      (1...3).each do |k|
        best = neg
        best = [best, dp[i - 1][j][k - 1]].max if i > 0
        best = [best, dp[i][j - 1][k - 1]].max if j > 0
        dp[i][j][k] = [dp[i][j][k], best].max if best != neg && coins[i][j] < 0
      end
    end
  end
  [dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]].max
end
''')

add("3419_minimize_the_maximum_edge_weight_of_graph", r'''
# LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} threshold
# @return {Integer}
def min_max_weight(n, edges, _threshold)
  ok = lambda do |mid|
    g = Array.new(n) { [] }
    edges.each { |e| g[e[1]] << e[0] if e[2] <= mid }
    vis = Array.new(n, false)
    q = [0]
    vis[0] = true
    cnt = 1
    until q.empty?
      u = q.shift
      g[u].each do |v|
        next if vis[v]

        vis[v] = true
        cnt += 1
        q << v
      end
    end
    cnt == n
  end
  lo = 1
  hi = 1_000_001
  ans = -1
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      ans = mid
      hi = mid
    else
      lo = mid + 1
    end
  end
  ans
end
''')

add("3420_count_non_decreasing_subarrays_after_k_operations", r'''
# LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_non_decreasing_subarrays(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    cost = 0
    max_v = nums[i]
    (i...n).each do |j|
      if nums[j] >= max_v
        max_v = nums[j]
      else
        cost += max_v - nums[j]
      end
      break if cost > k

      ans += 1
    end
  end
  ans
end
''')

add("3422_minimum_operations_to_make_subarray_elements_equal", r'''
# LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  n = nums.length
  ans = 10**18
  (0..(n - k)).each do |i|
    sub = nums[i, k].sort
    med = sub[k / 2]
    cost = 0
    sub.each { |x| cost += (x - med).abs }
    ans = cost if cost < ans
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
        if body.startswith("\ufeff"):
            raise RuntimeError("BOM")
        written += 1
        print("OK", name)
    except Exception as e:
        failed.append((name, str(e)))
        print("FAIL", name, e)
print(f"written={written} failed={len(failed)}")
