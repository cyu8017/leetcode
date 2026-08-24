#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3423_maximum_difference_between_adjacent_elements_in_a_circular_array", r'''
# LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

# @param {Integer[]} nums
# @return {Integer}
def max_adjacent_distance(nums)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    d = (nums[i] - nums[(i + 1) % n]).abs
    ans = d if d > ans
  end
  ans
end
''')

add("3424_minimum_cost_to_make_arrays_identical", r'''
# LeetCode 3424 - Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

# @param {Integer[]} arr
# @param {Integer[]} brr
# @param {Integer} k
# @return {Integer}
def min_cost(arr, brr, k)
  no_swap = 0
  (0...arr.length).each { |i| no_swap += (arr[i] - brr[i]).abs }
  a2 = arr.sort
  b2 = brr.sort
  with_swap = k
  (0...a2.length).each { |i| with_swap += (a2[i] - b2[i]).abs }
  no_swap < with_swap ? no_swap : with_swap
end
''')

add("3425_longest_special_path", r'''
# LeetCode 3425 - Longest Special Path
# https://leetcode.com/problems/longest-special-path/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @return {Integer[]}
def longest_special_path(edges, nums)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  best_len = 0
  best_nodes = 1
  last = {}
  path = []
  dfs = nil
  dfs = lambda do |u, p, dist, left|
    seen = last.key?(nums[u])
    prev_pos = seen ? last[nums[u]] : -1
    last[nums[u]] = path.length
    new_left = left
    new_left = prev_pos + 1 if seen && prev_pos >= left
    path << dist
    length = dist - path[new_left]
    nodes = path.length - new_left
    if length > best_len || (length == best_len && nodes < best_nodes)
      best_len = length
      best_nodes = nodes
    end
    g[u].each do |v, w|
      next if v == p

      dfs.call(v, u, dist + w, new_left)
    end
    path.pop
    if seen
      last[nums[u]] = prev_pos
    else
      last.delete(nums[u])
    end
  end
  dfs.call(0, -1, 0, 0)
  [best_len, best_nodes]
end
''')

add("3426_manhattan_distances_of_all_arrangements_of_pieces", r'''
# LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def distance_sum(m, n, k)
  mod = 1_000_000_007
  return 0 if k < 2

  total_cells = m * n
  pair_choose = comb_3426(total_cells - 2, k - 2, mod)
  sum_dist = 0
  (1...m).each { |d| sum_dist += d * (m - d) * n * n }
  (1...n).each { |d| sum_dist += d * (n - d) * m * m }
  sum_dist % mod * pair_choose % mod
end

def mod_pow_3426(a, e, mod)
  r = 1
  base = a % mod
  while e > 0
    r = (r * base) % mod if (e & 1) != 0
    base = (base * base) % mod
    e >>= 1
  end
  r
end

def comb_3426(nn, kk, mod)
  return 0 if kk < 0 || kk > nn

  num = 1
  den = 1
  (0...kk).each do |i|
    num = num * (nn - i) % mod
    den = den * (i + 1) % mod
  end
  num * mod_pow_3426(den, mod - 2, mod) % mod
end
''')

add("3427_sum_of_variable_length_subarrays", r'''
# LeetCode 3427 - Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def subarray_sum(nums)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 0
  (0...n).each do |i|
    start = i - nums[i]
    start = 0 if start < 0
    ans += pref[i + 1] - pref[start]
  end
  ans
end
''')

add("3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences", r'''
# LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_max_sums(nums, k)
  mod = 1_000_000_007
  nums = nums.sort
  n = nums.length
  c = Array.new(n + 1) { Array.new(k, 0) }
  (0..n).each do |i|
    c[i][0] = 1
    j = 1
    while j < k && j <= i
      c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
      j += 1
    end
  end
  ans = 0
  (0...n).each do |i|
    ways_max = 0
    j = 0
    while j < k && j <= i
      ways_max = (ways_max + c[i][j]) % mod
      j += 1
    end
    ways_min = 0
    right = n - i - 1
    j = 0
    while j < k && j <= right
      ways_min = (ways_min + c[right][j]) % mod
      j += 1
    end
    ans = (ans + nums[i] * ways_max % mod + nums[i] * ways_min % mod) % mod
  end
  ans
end
''')

add("3429_paint_house_iv", r'''
# LeetCode 3429 - Paint House IV
# https://leetcode.com/problems/paint-house-iv/

# @param {Integer} n
# @param {Integer[][]} cost
# @return {Integer}
def min_cost(n, cost)
  inf = 10**18
  m = n / 2
  dp = Array.new(3) { Array.new(3, 0) }
  (0...3).each do |a|
    (0...3).each do |b|
      dp[a][b] = a == b ? inf : cost[0][a] + cost[n - 1][b]
    end
  end
  (1...m).each do |i|
    ndp = Array.new(3) { Array.new(3, inf) }
    (0...3).each do |pa|
      (0...3).each do |pb|
        next if dp[pa][pb] >= inf

        (0...3).each do |a|
          next if a == pa

          (0...3).each do |b|
            next if b == pb || a == b

            v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
            ndp[a][b] = v if v < ndp[a][b]
          end
        end
      end
    end
    dp = ndp
  end
  ans = inf
  (0...3).each do |a|
    (0...3).each do |b|
      ans = dp[a][b] if dp[a][b] < ans
    end
  end
  ans
end
''')

add("3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays", r'''
# LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_max_subarray_sum(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    mn = mx = nums[i]
    j = i
    while j < n && j - i + 1 <= k
      mn = nums[j] if nums[j] < mn
      mx = nums[j] if nums[j] > mx
      ans += mn + mx
      j += 1
    end
  end
  ans
end
''')

add("3431_minimum_unlocked_indices_to_sort_nums", r'''
# LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
# https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

# @param {Integer[]} nums
# @param {Integer[]} locked
# @return {Integer}
def min_unlocked_indices(nums, locked)
  n = nums.length
  need = false
  (1...n).each do |i|
    if nums[i] < nums[i - 1]
      need = true
      break
    end
  end
  return 0 unless need

  left = n
  right = -1
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      next unless nums[i] > nums[j]

      left = i if i < left
      right = j if j > right
    end
  end
  return 0 if right < left

  ans = 0
  (left..right).each { |i| ans += 1 if locked[i] == 1 }
  tmp = nums.dup
  lock = locked.dup
  (left..right).each { |i| lock[i] = 0 }
  changed = true
  while changed
    changed = false
    (0...(n - 1)).each do |i|
      next unless lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1]

      tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
      changed = true
    end
  end
  (1...n).each { |i| return -1 if tmp[i] < tmp[i - 1] }
  ans
end
''')

add("3432_count_partitions_with_even_sum_difference", r'''
# LeetCode 3432 - Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

# @param {Integer[]} nums
# @return {Integer}
def count_partitions(nums)
  total = 0
  nums.each { |x| total += x }
  ans = 0
  left = 0
  (0...(nums.length - 1)).each do |i|
    left += nums[i]
    ans += 1 if (left - (total - left)) % 2 == 0
  end
  ans
end
''')

add("3433_count_mentions_per_user", r'''
# LeetCode 3433 - Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/

# @param {Integer} number_of_users
# @param {String[][]} events
# @return {Integer[]}
def count_mentions(number_of_users, events)
  events = events.sort_by { |e| [e[1].to_i, e[0] == "OFFLINE" ? 0 : 1] }
  online = Array.new(number_of_users, true)
  offline_until = Array.new(number_of_users, 0)
  ans = Array.new(number_of_users, 0)
  events.each do |e|
    t = e[1].to_i
    (0...number_of_users).each do |i|
      online[i] = true if !online[i] && offline_until[i] <= t
    end
    if e[0] == "OFFLINE"
      uid = e[2].to_i
      online[uid] = false
      offline_until[uid] = t + 60
    else
      msg = e[2]
      if msg == "ALL"
        (0...number_of_users).each { |i| ans[i] += 1 }
      elsif msg == "HERE"
        (0...number_of_users).each { |i| ans[i] += 1 if online[i] }
      else
        msg.split(" ").each do |part|
          uid = part[2..].to_i
          ans[uid] += 1
        end
      end
    end
  end
  ans
end
''')

add("3434_maximum_frequency_after_subarray_operation", r'''
# LeetCode 3434 - Maximum Frequency After Subarray Operation
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency(nums, k)
  base = 0
  nums.each { |x| base += 1 if x == k }
  ans = base
  uniq = {}
  nums.each { |x| uniq[x] = true }
  uniq.each_key do |v|
    next if v == k

    best = 0
    cur = 0
    nums.each do |x|
      delta = 0
      if x == v
        delta = 1
      elsif x == k
        delta = -1
      end
      cur += delta
      cur = 0 if cur < 0
      best = cur if cur > best
    end
    ans = base + best if base + best > ans
  end
  ans
end
''')

add("3435_frequencies_of_shortest_supersequences", r'''
# LeetCode 3435 - Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/

# @param {String[]} words
# @return {Integer[][]}
def supersequences(words)
  used = Array.new(26, false)
  words.each do |w|
    used[w[0].ord - 97] = true
    used[w[1].ord - 97] = true
  end
  letters = (0...26).select { |i| used[i] }
  m = letters.length
  freq = Array.new(26, 0)
  best = 10**9
  best_freqs = []
  dfs = nil
  dfs = lambda do |i|
    if i == m
      words.each do |w|
        a = w[0].ord - 97
        b = w[1].ord - 97
        if a == b
          return if freq[a] < 2
        elsif freq[a] < 1 || freq[b] < 1
          return
        end
      end
      s = freq.sum
      f = freq.dup
      if s < best
        best = s
        best_freqs = [f]
      elsif s == best
        best_freqs << f
      end
      return
    end
    l = letters[i]
    (1..2).each do |c|
      freq[l] = c
      dfs.call(i + 1)
    end
    freq[l] = 0
  end
  dfs.call(0)
  best_freqs
end
''')

add("3437_permutations_iii", r'''
# LeetCode 3437 - Permutations III
# https://leetcode.com/problems/permutations-iii/

# @param {Integer} n
# @return {Integer[][]}
def permute(n)
  ans = []
  used = Array.new(n + 1, false)
  cur = []
  dfs = nil
  dfs = lambda do
    if cur.length == n
      ans << cur.dup
      return
    end
    (1..n).each do |i|
      next if used[i]
      next if !cur.empty? && (cur[-1] % 2 == i % 2)

      used[i] = true
      cur << i
      dfs.call
      cur.pop
      used[i] = false
    end
  end
  dfs.call
  ans
end
''')

add("3438_find_valid_pair_of_adjacent_digits_in_string", r'''
# LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

# @param {String} s
# @return {String}
def find_valid_pair(s)
  freq = Array.new(10, 0)
  s.each_char { |c| freq[c.ord - 48] += 1 }
  (0...(s.length - 1)).each do |i|
    a = s[i].ord - 48
    b = s[i + 1].ord - 48
    return s[i, 2] if a != b && freq[a] == a && freq[b] == b
  end
  ""
end
''')

add("3439_reschedule_meetings_for_maximum_free_time_i", r'''
# LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

# @param {Integer} event_time
# @param {Integer} k
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def max_free_time(event_time, k, start_time, end_time)
  n = start_time.length
  gaps = Array.new(n + 1, 0)
  gaps[0] = start_time[0]
  (1...n).each { |i| gaps[i] = start_time[i] - end_time[i - 1] }
  gaps[n] = event_time - end_time[n - 1]
  window = k + 1
  s = 0
  (0...[window, gaps.length].min).each { |i| s += gaps[i] }
  ans = s
  (window...gaps.length).each do |i|
    s += gaps[i] - gaps[i - window]
    ans = s if s > ans
  end
  ans
end
''')

add("3440_reschedule_meetings_for_maximum_free_time_ii", r'''
# LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

# @param {Integer} event_time
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def max_free_time(event_time, start_time, end_time)
  n = start_time.length
  gaps = Array.new(n + 1, 0)
  gaps[0] = start_time[0]
  (1...n).each { |i| gaps[i] = start_time[i] - end_time[i - 1] }
  gaps[n] = event_time - end_time[n - 1]
  ans = 0
  gaps.each { |g| ans = g if g > ans }
  left_max = Array.new(n + 1, 0)
  right_max = Array.new(n + 1, 0)
  (0..(n)).each do |i|
    left_max[i] = gaps[i]
    left_max[i] = left_max[i - 1] if i > 0 && left_max[i - 1] > left_max[i]
  end
  n.downto(0) do |i|
    right_max[i] = gaps[i]
    right_max[i] = right_max[i + 1] if i < n && right_max[i + 1] > right_max[i]
  end
  (0...n).each do |i|
    dur = end_time[i] - start_time[i]
    merged = gaps[i] + gaps[i + 1]
    best_other = 0
    best_other = left_max[i - 1] if i > 0 && left_max[i - 1] > best_other
    best_other = right_max[i + 2] if i + 2 <= n && right_max[i + 2] > best_other
    cand = merged
    cand = merged + dur if best_other >= dur
    ans = cand if cand > ans
  end
  ans
end
''')

add("3441_minimum_cost_good_caption", r'''
# LeetCode 3441 - Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/

# @param {String} caption
# @return {String}
def min_cost_good_caption(caption)
  n = caption.length
  return "" if n < 3

  ans = caption.chars
  i = 0
  while i < n
    j = i
    j += 1 while j < n && ans[j] == ans[i]
    if j - i >= 3
      i = j
      next
    end
    need = 3 - (j - i)
    if j + need <= n
      (0...need).each { |t| ans[j + t] = ans[i] }
      i = j + need
    else
      ch = "a"
      if i > 0
        ch = ans[i - 1]
      elsif j < n
        ch = caption[j]
      end
      (i...n).each { |t| ans[t] = ch }
      break
    end
  end
  i = 0
  while i < n
    j = i
    j += 1 while j < n && ans[j] == ans[i]
    return "" if j - i < 3

    i = j
  end
  ans.join
end
''')

add("3442_maximum_difference_between_even_and_odd_frequency_i", r'''
# LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

# @param {String} s
# @return {Integer}
def max_difference(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  max_odd = 0
  min_even = 10**9
  freq.each do |f|
    next if f == 0

    if f.odd?
      max_odd = f if f > max_odd
    elsif f < min_even
      min_even = f
    end
  end
  max_odd - min_even
end
''')

add("3443_maximum_manhattan_distance_after_k_changes", r'''
# LeetCode 3443 - Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_distance(s, k)
  ans = 0
  lat = 0
  lon = 0
  s.each_char.with_index do |c, i|
    case c
    when "N" then lat += 1
    when "S" then lat -= 1
    when "E" then lon += 1
    else lon -= 1
    end
    md = lat.abs + lon.abs
    steps = i + 1
    cur = md + 2 * k
    cur = steps if cur > steps
    ans = cur if cur > ans
  end
  ans
end
''')

add("3444_minimum_increments_for_target_multiples_in_an_array", r'''
# LeetCode 3444 - Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def minimum_increments(nums, target)
  m = target.length
  nmask = 1 << m
  inf = 10**18
  dp = Array.new(nmask, inf)
  dp[0] = 0
  nums.each do |x|
    ndp = dp.dup
    (0...nmask).each do |mask|
      (1...nmask).each do |sub|
        l = 1
        ok = true
        (0...m).each do |i|
          next if (sub & (1 << i)) == 0

          l = lcm_3444(l, target[i])
          if l > 1_000_000_000
            ok = false
            break
          end
        end
        next unless ok

        cost = (l - x % l) % l
        nm = mask | sub
        ndp[nm] = dp[mask] + cost if dp[mask] + cost < ndp[nm]
      end
    end
    dp = ndp
  end
  dp[nmask - 1]
end

def gcd_3444(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

def lcm_3444(a, b)
  a / gcd_3444(a, b) * b
end
''')

add("3445_maximum_difference_between_even_and_odd_frequency_ii", r'''
# LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_difference(s, k)
  n = s.length
  ans = -10**9
  (0...5).each do |a|
    (0...5).each do |b|
      next if a == b

      pref_a = Array.new(n + 1, 0)
      pref_b = Array.new(n + 1, 0)
      (0...n).each do |i|
        pref_a[i + 1] = pref_a[i]
        pref_b[i + 1] = pref_b[i]
        pref_a[i + 1] += 1 if s[i].ord - 48 == a
        pref_b[i + 1] += 1 if s[i].ord - 48 == b
      end
      (0...n).each do |i|
        ((i + k - 1)...n).each do |j|
          fa = pref_a[j + 1] - pref_a[i]
          fb = pref_b[j + 1] - pref_b[i]
          ans = fa - fb if fa.odd? && fb.even? && fb > 0 && fa - fb > ans
        end
      end
    end
  end
  ans
end
''')

add("3446_sort_matrix_by_diagonals", r'''
# LeetCode 3446 - Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/

# @param {Integer[][]} grid
# @return {Integer[][]}
def sort_matrix(grid)
  n = grid.length
  diags = {}
  (0...n).each do |i|
    (0...n).each do |j|
      key = i - j
      diags[key] ||= []
      diags[key] << grid[i][j]
    end
  end
  diags.each do |key, lst|
    if key >= 0
      lst.sort! { |a, b| b <=> a }
    else
      lst.sort!
    end
  end
  idx = {}
  (0...n).each do |i|
    (0...n).each do |j|
      k = i - j
      pos = idx[k] || 0
      grid[i][j] = diags[k][pos]
      idx[k] = pos + 1
    end
  end
  grid
end
''')

add("3447_assign_elements_to_groups_with_constraints", r'''
# LeetCode 3447 - Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

# @param {Integer[]} groups
# @param {Integer[]} elements
# @return {Integer[]}
def assign_elements(groups, elements)
  max_v = 100_001
  first = Array.new(max_v, -1)
  elements.each_with_index do |e, i|
    first[e] = i if e < max_v && first[e] == -1
  end
  ans = Array.new(groups.length, 0)
  groups.each_with_index do |g, gi|
    best = -1
    d = 1
    while d * d <= g
      if g % d == 0
        best = first[d] if first[d] != -1 && (best == -1 || first[d] < best)
        other = g / d
        best = first[other] if first[other] != -1 && (best == -1 || first[other] < best)
      end
      d += 1
    end
    ans[gi] = best
  end
  ans
end
''')

add("3448_count_substrings_divisible_by_last_digit", r'''
# LeetCode 3448 - Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

# @param {String} s
# @return {Integer}
def count_substrings(s)
  ans = 0
  n = s.length
  (0...n).each do |r|
    last = s[r].ord - 48
    next if last == 0

    mod = 0
    p = 1 % last
    r.downto(0) do |l|
      mod = (mod + (s[l].ord - 48) * p) % last
      p = (p * 10) % last
      ans += 1 if mod == 0
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
