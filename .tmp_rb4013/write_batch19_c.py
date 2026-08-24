#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3666_minimum_operations_to_equalize_binary_string", r'''
# LeetCode 3666 - Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

require "set"

# @param {String} s
# @param {Integer} k
# @return {Integer}
def min_operations(s, k)
  n = s.length
  ts = [Set.new, Set.new]
  (0..n).each { |i| ts[i % 2] << i }
  cnt0 = s.count("0")
  ts[cnt0 % 2].delete(cnt0)
  q = [cnt0]
  ans = 0
  until q.empty?
    nq = []
    q.each do |cur|
      return ans if cur == 0

      l = cur + k - 2 * [cur, k].min
      r = cur + k - 2 * [k - n + cur, 0].max
      t = ts[l % 2]
      t.to_a.sort.each do |it|
        next if it < l
        break if it > r

        nq << it
        t.delete(it)
      end
    end
    q = nq
    ans += 1
  end
  -1
end
''')

add("3667_sort_array_by_absolute_value", r'''
# LeetCode 3667 - Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_by_absolute_value(nums)
  nums.sort_by(&:abs)
end
''')

add("3668_restore_finishing_order", r'''
# LeetCode 3668 - Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/

# @param {Integer[]} order
# @param {Integer[]} friends
# @return {Integer[]}
def recover_order(order, friends)
  n = order.length
  d = Array.new(n + 1, 0)
  order.each_with_index { |x, i| d[x] = i }
  friends.sort_by { |a| d[a] }
end
''')

add("3669_balanced_k_factor_decomposition", r'''
# LeetCode 3669 - Balanced K-Factor Decomposition
# https://leetcode.com/problems/balanced-k-factor-decomposition/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def min_difference(n, k)
  mx = 100_001
  unless defined?($g3669) && $g3669
    g = Array.new(mx) { [] }
    (1...mx).each do |i|
      i.step(mx - 1, i) { |j| g[j] << i }
    end
    $g3669 = g
  end
  g = $g3669
  cur = Float::INFINITY
  ans = []
  path = Array.new(k, 0)
  dfs = nil
  dfs = lambda do |i, x, mi, mxv|
    if i == 0
      d = [mxv, x].max - [mi, x].min
      if d < cur
        cur = d
        path[i] = x
        ans = path.dup
      end
      return
    end
    g[x].each do |y|
      path[i] = y
      dfs.call(i - 1, x / y, [mi, y].min, [mxv, y].max)
    end
  end
  dfs.call(k - 1, n, 10**18, 0)
  ans
end
''')

add("3670_maximum_product_of_two_integers_with_no_common_bits", r'''
# LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
# https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  max_v = nums.empty? ? 0 : nums.max
  bits_n = 0
  x = max_v
  while x > 0
    bits_n += 1
    x >>= 1
  end
  bits_n = 1 if bits_n == 0
  size = 1 << bits_n
  best = Array.new(size, 0)
  nums.each { |v| best[v] = v if v > best[v] }
  (0...size).each do |mask|
    (0...bits_n).each do |b|
      next if (mask & (1 << b)) == 0

      sub = mask ^ (1 << b)
      best[mask] = best[sub] if best[sub] > best[mask]
    end
  end
  ans = 0
  nums.each do |v|
    comp = (size - 1) ^ v
    if best[comp] > 0
      p = v * best[comp]
      ans = p if p > ans
    end
  end
  ans
end
''')

add("3671_sum_of_beautiful_subsequences", r'''
# LeetCode 3671 - Sum of Beautiful Subsequences
# https://leetcode.com/problems/sum-of-beautiful-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def total_beauty(nums)
  mod = 1_000_000_007
  mx = nums.max
  pos = Array.new(mx + 1) { [] }
  nums.each_with_index { |v, i| pos[v] << i }
  cnt = Array.new(mx + 1, 0)
  (1..mx).each do |g|
    seq = []
    g.step(mx, g) { |m| seq.concat(pos[m]) }
    next if seq.empty?

    seq.sort!
    ways = 1
    seq.length.times { ways = (ways * 2) % mod }
    cnt[g] = (ways - 1 + mod) % mod
  end
  ans = 0
  mx.downto(1) do |g|
    (2 * g).step(mx, g) { |m| cnt[g] = (cnt[g] - cnt[m] + mod) % mod }
    ans = (ans + cnt[g] * g) % mod
  end
  ans
end
''')

add("3672_sum_of_weighted_modes_in_subarrays", r'''
# LeetCode 3672 - Sum of Weighted Modes in Subarrays
# https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def mode_weight(nums, k)
  cnt = Hash.new(0)
  pq = []
  push = lambda do |freq, val|
    pq << [-freq, val]
  end
  get_mode = lambda do
    loop do
      freq = -pq[0][0]
      val = pq[0][1]
      return freq * val if cnt[val] == freq

      pq.shift
    end
  end
  (0...k).each do |i|
    x = nums[i]
    cnt[x] += 1
    push.call(cnt[x], x)
  end
  pq.sort_by! { |a| [a[0], a[1]] }
  ans = get_mode.call
  (k...nums.length).each do |i|
    x = nums[i]
    y = nums[i - k]
    cnt[x] += 1
    cnt[y] -= 1
    push.call(cnt[x], x)
    push.call(cnt[y], y)
    pq.sort_by! { |a| [a[0], a[1]] }
    ans += get_mode.call
  end
  ans
end
''')

add("3674_minimum_operations_to_equalize_array", r'''
# LeetCode 3674 - Minimum Operations to Equalize Array
# https://leetcode.com/problems/minimum-operations-to-equalize-array/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  nums.each { |x| return 1 if x != nums[0] }
  0
end
''')

add("3675_minimum_operations_to_transform_string", r'''
# LeetCode 3675 - Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/

# @param {String} s
# @return {Integer}
def min_operations(s)
  ans = 0
  s.each_char do |c|
    next if c == "a"

    v = 26 - (c.ord - 97)
    ans = v if v > ans
  end
  ans
end
''')

add("3676_count_bowl_subarrays", r'''
# LeetCode 3676 - Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def bowl_subarrays(nums)
  n = nums.length
  ans = 0
  ngr = Array.new(n, -1)
  ngl = Array.new(n, -1)
  stack = []
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] < nums[i]
    ngr[i] = stack[-1] unless stack.empty?
    stack << i
  end
  stack.clear
  (0...n).each do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] < nums[i]
    ngl[i] = stack[-1] unless stack.empty?
    stack << i
  end
  (0...n).each do |i|
    ans += 1 if ngr[i] != -1 && ngr[i] - i >= 2
    ans += 1 if ngl[i] != -1 && i - ngl[i] >= 2
  end
  ans
end
''')

add("3677_count_binary_palindromic_numbers", r'''
# LeetCode 3677 - Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/

# @param {Integer} n
# @return {Integer}
def count_binary_palindromes(n)
  return 1 if n == 0

  ans = 1
  s = ""
  x = n
  while x > 0
    s += (x & 1).to_s
    x /= 2
  end
  s = s.reverse
  l = s.length
  (1...l).each do |length|
    half = (length + 1) / 2
    ans += 1 << (half - 1)
  end
  half = (l + 1) / 2
  prefix = s[0, half]
  start = 1 << (half - 1)
  pref_val = 0
  prefix.each_char { |c| pref_val = (pref_val << 1) | (c.ord - 48) }
  ans += pref_val - start
  pal = prefix.dup
  (half - 1 - (l % 2)).downto(0) { |i| pal += prefix[i] }
  pval = 0
  pal.each_char { |c| pval = (pval << 1) | (c.ord - 48) }
  ans += 1 if pval <= n
  ans
end
''')

add("3678_smallest_absent_positive_greater_than_average", r'''
# LeetCode 3678 - Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

# @param {Integer[]} nums
# @return {Integer}
def smallest_absent(nums)
  s = {}
  total = 0
  nums.each do |x|
    s[x] = true
    total += x
  end
  ans = [1, total / nums.length + 1].max
  ans += 1 while s[ans]
  ans
end
''')

add("3679_minimum_discards_to_balance_inventory", r'''
# LeetCode 3679 - Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/

# @param {Integer[]} arrivals
# @param {Integer} w
# @param {Integer} m
# @return {Integer}
def min_arrivals_to_discard(arrivals, w, m)
  cnt = Hash.new(0)
  n = arrivals.length
  marked = Array.new(n, 0)
  ans = 0
  (0...n).each do |i|
    x = arrivals[i]
    cnt[arrivals[i - w]] -= marked[i - w] if i >= w
    if cnt[x] >= m
      ans += 1
    else
      marked[i] = 1
      cnt[x] += 1
    end
  end
  ans
end
''')

add("3680_generate_schedule", r'''
# LeetCode 3680 - Generate Schedule
# https://leetcode.com/problems/generate-schedule/

# @param {Integer} n
# @return {Integer[][]}
def generate_schedule(n)
  return [] if n < 5

  matches = []
  (0...n).each do |i|
    (0...n).each { |j| matches << [i, j] if i != j }
  end
  used = Array.new(matches.length, false)
  sched = []
  last = [-1, -1]
  dfs = nil
  dfs = lambda do
    return true if sched.length == matches.length

    matches.each_with_index do |m, i|
      next if used[i]
      next if m[0] == last[0] || m[0] == last[1] || m[1] == last[0] || m[1] == last[1]

      used[i] = true
      sched << m
      p0 = last[0]
      p1 = last[1]
      last[0] = m[0]
      last[1] = m[1]
      return true if dfs.call

      last[0] = p0
      last[1] = p1
      sched.pop
      used[i] = false
    end
    false
  end
  return sched if dfs.call

  []
end
''')

add("3681_maximum_xor_of_subsequences", r'''
# LeetCode 3681 - Maximum XOR of Subsequences
# https://leetcode.com/problems/maximum-xor-of-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def max_xor_subsequences(nums)
  basis = Array.new(32, 0)
  nums.each do |x|
    cur = x
    31.downto(0) do |b|
      next if (cur & (1 << b)) == 0

      if basis[b] == 0
        basis[b] = cur
        break
      end
      cur ^= basis[b]
    end
  end
  ans = 0
  31.downto(0) { |b| ans ^= basis[b] if (ans ^ basis[b]) > ans }
  ans
end
''')

add("3682_minimum_index_sum_of_common_elements", r'''
# LeetCode 3682 - Minimum Index Sum of Common Elements
# https://leetcode.com/problems/minimum-index-sum-of-common-elements/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_sum(nums1, nums2)
  inf = 1 << 30
  d = {}
  nums2.each_with_index { |x, i| d[x] = i unless d.key?(x) }
  ans = inf
  nums1.each_with_index do |x, i|
    ans = [ans, i + d[x]].min if d.key?(x)
  end
  ans == inf ? -1 : ans
end
''')

add("3683_earliest_time_to_finish_one_task", r'''
# LeetCode 3683 - Earliest Time to Finish One Task
# https://leetcode.com/problems/earliest-time-to-finish-one-task/

# @param {Integer[][]} tasks
# @return {Integer}
def earliest_time(tasks)
  ans = 200
  tasks.each { |task| ans = [ans, task[0] + task[1]].min }
  ans
end
''')

add("3684_maximize_sum_of_at_most_k_distinct_elements", r'''
# LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_k_distinct(nums, k)
  nums = nums.sort
  n = nums.length
  ans = []
  (n - 1).downto(0) do |i|
    next if i + 1 < n && nums[i] == nums[i + 1]

    ans << nums[i]
    k -= 1
    break if k == 0
  end
  ans
end
''')

add("3685_subsequence_sum_after_capping_elements", r'''
# LeetCode 3685 - Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean[]}
def subsequence_sum_after_capping(nums, k)
  n = nums.length
  sorted_nums = nums.sort
  ans = Array.new(n, false)
  reach = Array.new(k + 1, false)
  reach[0] = true
  idx = 0
  (1..n).each do |x|
    while idx < n && sorted_nums[idx] <= x
      v = sorted_nums[idx]
      k.downto(v) { |s| reach[s] = true if reach[s - v] }
      idx += 1
    end
    tmp = reach.dup
    rem = n - idx
    (0..k).each do |s|
      next unless reach[s]

      t = 1
      while t <= rem && s + t * x <= k
        tmp[s + t * x] = true
        t += 1
      end
    end
    ans[x - 1] = tmp[k]
  end
  ans
end
''')

add("3686_number_of_stable_subsequences", r'''
# LeetCode 3686 - Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def count_stable_subsequences(nums)
  mod = 1_000_000_007
  a1 = a2 = b1 = b2 = 0
  nums.each do |x|
    if x.odd?
      na1 = (1 + b1 + b2) % mod
      na2 = a1
      a1 = (a1 + na1) % mod
      a2 = (a2 + na2) % mod
    else
      nb1 = (1 + a1 + a2) % mod
      nb2 = b1
      b1 = (b1 + nb1) % mod
      b2 = (b2 + nb2) % mod
    end
  end
  (((a1 + a2) % mod + b1) % mod + b2) % mod
end
''')

add("3687_library_late_fee_calculator", r'''
# LeetCode 3687 - Library Late Fee Calculator
# https://leetcode.com/problems/library-late-fee-calculator/

# @param {Integer[]} days_late
# @return {Integer}
def late_fee(days_late)
  fee = lambda do |x|
    return 1 if x == 1
    return 3 * x if x > 5

    2 * x
  end
  days_late.sum { |x| fee.call(x) }
end
''')

add("3688_bitwise_or_of_even_numbers_in_an_array", r'''
# LeetCode 3688 - Bitwise OR of Even Numbers in an Array
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def even_number_bitwise_o_rs(nums)
  ans = 0
  nums.each { |x| ans |= x if x.even? }
  ans
end
''')

add("3689_maximum_total_subarray_value_i", r'''
# LeetCode 3689 - Maximum Total Subarray Value I
# https://leetcode.com/problems/maximum-total-subarray-value-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_total_value(nums, k)
  k * (nums.max - nums.min)
end
''')

add("3690_split_and_merge_array_transformation", r'''
# LeetCode 3690 - Split and Merge Array Transformation
# https://leetcode.com/problems/split-and-merge-array-transformation/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_split_merge(nums1, nums2)
  n = nums1.length
  to_arr = lambda do |nums|
    t = Array.new(6, 0)
    (0...n).each { |i| t[i] = nums[i] }
    t
  end
  start = to_arr.call(nums1)
  target = to_arr.call(nums2)
  vis = { start => true }
  q = [start]
  ans = 0
  loop do
    nq = []
    q.each do |cur|
      return ans if cur == target

      (0...n).each do |l|
        (l...n).each do |r|
          remain = cur[0...l] + cur[(r + 1)...n]
          sub = cur[l..r]
          (0..remain.length).each do |pos|
            nxt_slice = remain[0...pos] + sub + remain[pos..-1]
            nxt = to_arr.call(nxt_slice)
            unless vis[nxt]
              vis[nxt] = true
              nq << nxt
            end
          end
        end
      end
    end
    q = nq
    ans += 1
  end
end
''')

if __name__ == "__main__":
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch C written={written}")
