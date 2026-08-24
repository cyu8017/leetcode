#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2962_count_subarrays_where_max_element_appears_at_least_k_times", r'''
# LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  mx = nums.max
  ans = 0
  cnt = 0
  left = 0
  nums.each_with_index do |v, right|
    cnt += 1 if v == mx
    while cnt >= k
      cnt -= 1 if nums[left] == mx
      left += 1
    end
    ans += left
  end
  ans
end
''')

add("2963_count_the_number_of_good_partitions", r'''
# LeetCode 2963 - Count the Number of Good Partitions
# https://leetcode.com/problems/count-the-number-of-good-partitions/

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_partitions(nums)
  mod = 1_000_000_007
  last = {}
  nums.each_with_index { |v, i| last[v] = i }
  ans = 1
  finish = 0
  nums.each_with_index do |v, i|
    finish = last[v] if last[v] > finish
    ans = ans * 2 % mod if i == finish && i != nums.length - 1
  end
  ans
end
''')

add("2964_number_of_divisible_triplet_sums", r'''
# LeetCode 2964 - Number of Divisible Triplet Sums
# https://leetcode.com/problems/number-of-divisible-triplet-sums/

# @param {Integer[]} nums
# @param {Integer} d
# @return {Integer}
def divisible_triplet_count(nums, d)
  n = nums.length
  ans = 0
  n.times do |i|
    freq = Hash.new(0)
    (i + 1...n).each do |j|
      need = (d - (nums[i] + nums[j]) % d) % d
      ans += freq[need]
      freq[nums[j] % d] += 1
    end
  end
  ans
end
''')

add("2965_find_missing_and_repeated_values", r'''
# LeetCode 2965 - Find Missing and Repeated Values
# https://leetcode.com/problems/find-missing-and-repeated-values/

# @param {Integer[][]} grid
# @return {Integer[]}
def find_missing_and_repeated_values(grid)
  n = grid.length
  freq = Array.new(n * n + 1, 0)
  n.times { |i| n.times { |j| freq[grid[i][j]] += 1 } }
  rep = 0
  miss = 0
  (1..n * n).each do |i|
    rep = i if freq[i] == 2
    miss = i if freq[i] == 0
  end
  [rep, miss]
end
''')

add("2966_divide_array_into_arrays_with_max_difference", r'''
# LeetCode 2966 - Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[][]}
def divide_array(nums, k)
  nums.sort!
  ans = []
  i = 0
  while i < nums.length
    return [] if nums[i + 2] - nums[i] > k

    ans << [nums[i], nums[i + 1], nums[i + 2]]
    i += 3
  end
  ans
end
''')

add("2967_minimum_cost_to_make_array_equalindromic", r'''
# LeetCode 2967 - Minimum Cost to Make Array Equalindromic
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  nums.sort!
  n = nums.length
  median = nums[n / 2]
  candidates = [make_pal(median)]
  s = median.to_s
  half = s[0, (s.length + 1) / 2].to_i
  (-2..2).each do |d|
    h = half + d
    next if h <= 0

    hs = h.to_s
    pal = if s.length.even?
            hs + hs.reverse
          else
            hs + hs[0...-1].reverse
          end
    candidates << pal.to_i
  end
  [1, 9, 11, 99, 101].each { |v| candidates << v }
  ans = 1 << 60
  candidates.each do |p|
    next if p <= 0

    c = cost_of(nums, p)
    ans = c if c < ans
  end
  ans
end

def make_pal(x)
  ch = x.to_s.chars
  i = 0
  j = ch.length - 1
  while i < j
    ch[j] = ch[i]
    i += 1
    j -= 1
  end
  ch.join.to_i
end

def cost_of(nums, p)
  c = 0
  nums.each { |v| c += (v - p).abs }
  c
end
''')

add("2968_apply_operations_to_maximize_frequency_score", r'''
# LeetCode 2968 - Apply Operations to Maximize Frequency Score
# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency_score(nums, k)
  nums.sort!
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 1
  left = 0
  n.times do |right|
    left += 1 while cost_range(nums, pref, left, right) > k
    ans = right - left + 1 if right - left + 1 > ans
  end
  ans
end

def cost_range(nums, pref, l, r)
  mid = (l + r) >> 1
  left = nums[mid] * (mid - l) - (pref[mid] - pref[l])
  right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid)
  left + right
end
''')

add("2969_minimum_number_of_coins_for_fruits_ii", r'''
# LeetCode 2969 - Minimum Number of Coins for Fruits II
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

# @param {Integer[]} prices
# @return {Integer}
def minimum_coins(prices)
  n = prices.length
  dp = Array.new(n + 1, 1 << 30)
  dp[0] = 0
  (1..n).each do |i|
    j = i
    while j <= n && j <= 2 * i
      cand = dp[i - 1] + prices[i - 1]
      dp[j] = cand if cand < dp[j]
      j += 1
    end
  end
  dp[n]
end
''')

add("2970_count_the_number_of_incremovable_subarrays_i", r'''
# LeetCode 2970 - Count the Number of Incremovable Subarrays I
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    i.upto(n - 1) do |j|
      prev = -1
      ok = true
      n.times do |t|
        next if t >= i && t <= j
        if nums[t] <= prev
          ok = false
          break
        end
        prev = nums[t]
      end
      ans += 1 if ok
    end
  end
  ans
end
''')

add("2971_find_polygon_with_the_largest_perimeter", r'''
# LeetCode 2971 - Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
  nums.sort!
  total = nums.sum
  (nums.length - 1).downto(2) do |i|
    total -= nums[i]
    return total + nums[i] if total > nums[i]
  end
  -1
end
''')

add("2972_count_the_number_of_incremovable_subarrays_ii", r'''
# LeetCode 2972 - Count the Number of Incremovable Subarrays II
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
  n = nums.length
  left = 0
  left += 1 while left + 1 < n && nums[left] < nums[left + 1]
  return n * (n + 1) / 2 if left == n - 1

  ans = left + 2
  right = n - 1
  while right > 0 && (right == n - 1 || nums[right] < nums[right + 1])
    left -= 1 while left >= 0 && nums[left] >= nums[right]
    ans += left + 2
    right -= 1
    break if right > 0 && nums[right] >= nums[right + 1]
  end
  ans
end
''')

add("2973_find_number_of_coins_to_place_in_tree_nodes", r'''
# LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

# @param {Integer[][]} edges
# @param {Integer[]} cost
# @return {Integer[]}
def placed_coins(edges, cost)
  n = cost.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = Array.new(n, 0)
  dfs = lambda do |u, p|
    vals = [cost[u]]
    g[u].each do |v|
      next if v == p

      vals += dfs.call(v, u)
    end
    vals.sort!
    if vals.length < 3
      ans[u] = 1
    else
      m = vals.length
      cand1 = vals[m - 1] * vals[m - 2] * vals[m - 3]
      cand2 = vals[0] * vals[1] * vals[m - 1]
      best = [cand1, cand2].max
      best = 0 if best < 0
      ans[u] = best
    end
    return vals if vals.length <= 5

    [vals[0], vals[1], vals[-3], vals[-2], vals[-1]]
  end
  dfs.call(0, -1)
  ans
end
''')

add("2974_minimum_number_game", r'''
# LeetCode 2974 - Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/

# @param {Integer[]} nums
# @return {Integer[]}
def number_game(nums)
  nums.sort!
  i = 0
  while i + 1 < nums.length
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    i += 2
  end
  nums
end
''')

add("2975_maximum_square_area_by_removing_fences_from_a_field", r'''
# LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} h_fences
# @param {Integer[]} v_fences
# @return {Integer}
def maximize_square_area(m, n, h_fences, v_fences)
  mod = 1_000_000_007
  hg = fence_gaps(h_fences, m)
  vg = fence_gaps(v_fences, n)
  best = -1
  hg.each_key do |g|
    best = g if vg[g] && g > best
  end
  return -1 if best < 0

  best * best % mod
end

def fence_gaps(fences, bound)
  lst = [1] + fences + [bound]
  lst.sort!
  g = {}
  lst.length.times do |i|
    (i + 1...lst.length).each { |j| g[lst[j] - lst[i]] = true }
  end
  g
end
''')

add("2976_minimum_cost_to_convert_string_i", r'''
# LeetCode 2976 - Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

# @param {String} source
# @param {String} target
# @param {Character[]} original
# @param {Character[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
  inf = 1 << 60
  dist = Array.new(26) { Array.new(26, inf) }
  26.times { |i| dist[i][i] = 0 }
  original.length.times do |i|
    u = original[i][0].ord - 97
    v = changed[i][0].ord - 97
    ww = cost[i]
    dist[u][v] = ww if ww < dist[u][v]
  end
  26.times do |k|
    26.times do |i|
      26.times do |j|
        dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
      end
    end
  end
  ans = 0
  source.length.times do |i|
    a = source[i].ord - 97
    b = target[i].ord - 97
    return -1 if dist[a][b] >= inf / 2

    ans += dist[a][b]
  end
  ans
end
''')

add("2977_minimum_cost_to_convert_string_ii", r'''
# LeetCode 2977 - Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

# @param {String} source
# @param {String} target
# @param {String[]} original
# @param {String[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
  inf = 1 << 60
  ids = {}
  original.length.times do |i|
    ids[original[i]] = ids.length unless ids.key?(original[i])
    ids[changed[i]] = ids.length unless ids.key?(changed[i])
  end
  m = ids.length
  dist = Array.new(m) { Array.new(m, inf) }
  m.times { |i| dist[i][i] = 0 }
  original.length.times do |i|
    u = ids[original[i]]
    v = ids[changed[i]]
    ww = cost[i]
    dist[u][v] = ww if ww < dist[u][v]
  end
  m.times do |k|
    m.times do |i|
      m.times do |j|
        dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
      end
    end
  end
  n = source.length
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  lens = {}
  ids.each_key { |key| lens[key.length] = true }
  n.times do |i|
    next if dp[i] >= inf / 2

    dp[i + 1] = dp[i] if source[i] == target[i] && dp[i] < dp[i + 1]
    lens.each_key do |len|
      next if i + len > n

      ss = source[i, len]
      tt = target[i, len]
      next unless ids.key?(ss) && ids.key?(tt)

      iu = ids[ss]
      iv = ids[tt]
      if dist[iu][iv] < inf / 2
        cand = dp[i] + dist[iu][iv]
        dp[i + len] = cand if cand < dp[i + len]
      end
    end
  end
  return -1 if dp[n] >= inf / 2

  dp[n]
end
''')

add("2979_most_expensive_item_that_can_not_be_bought", r'''
# LeetCode 2979 - Most Expensive Item That Can Not Be Bought
# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

# @param {Integer} prime_one
# @param {Integer} prime_two
# @return {Integer}
def most_expensive_item(prime_one, prime_two)
  prime_one * prime_two - prime_one - prime_two
end
''')

add("2980_check_if_bitwise_or_has_trailing_zeros", r'''
# LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

# @param {Integer[]} nums
# @return {Boolean}
def has_trailing_zeros(nums)
  even = 0
  nums.each do |v|
    if v.even?
      even += 1
      return true if even >= 2
    end
  end
  false
end
''')

add("2981_find_longest_special_substring_that_occurs_thrice_i", r'''
# LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

# @param {String} s
# @return {Integer}
def maximum_length(s)
  n = s.length
  ans = -1
  n.times do |i|
    i.upto(n - 1) do |j|
      break if s[j] != s[i]

      length = j - i + 1
      cnt = 0
      (0..n - length).each do |k|
        ok = true
        length.times do |t|
          if s[k + t] != s[i + t]
            ok = false
            break
          end
        end
        cnt += 1 if ok
      end
      ans = length if cnt >= 3 && length > ans
    end
  end
  ans
end
''')

add("2982_find_longest_special_substring_that_occurs_thrice_ii", r'''
# LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

# @param {String} s
# @return {Integer}
def maximum_length(s)
  groups = Array.new(26) { [] }
  n = s.length
  i = 0
  while i < n
    j = i
    j += 1 while j < n && s[j] == s[i]
    groups[s[i].ord - 97] << (j - i)
    i = j
  end
  ans = -1
  26.times do |c|
    arr = groups[c]
    next if arr.empty?

    arr.sort!.reverse!
    arr[0].downto(1) do |len|
      cnt = 0
      arr.each { |g| cnt += g - len + 1 if g >= len }
      if cnt >= 3
        ans = len if len > ans
        break
      end
    end
  end
  ans
end
''')

add("2983_palindrome_rearrangement_queries", r'''
# LeetCode 2983 - Palindrome Rearrangement Queries
# https://leetcode.com/problems/palindrome-rearrangement-queries/

# @param {String} s
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_make_palindrome_queries(s, queries)
  n = s.length
  m = n / 2
  t = s[m..-1].reverse
  s = s[0...m]
  pre1 = Array.new(m + 1) { Array.new(26, 0) }
  pre2 = Array.new(m + 1) { Array.new(26, 0) }
  diff = Array.new(m + 1, 0)
  (1..m).each do |i|
    26.times do |k|
      pre1[i][k] = pre1[i - 1][k]
      pre2[i][k] = pre2[i - 1][k]
    end
    pre1[i][s[i - 1].ord - 97] += 1
    pre2[i][t[i - 1].ord - 97] += 1
    diff[i] = diff[i - 1] + (s[i - 1] == t[i - 1] ? 0 : 1)
  end
  ans = []
  queries.each do |q|
    a = q[0]
    b = q[1]
    c = n - 1 - q[3]
    d = n - 1 - q[2]
    ans << if a <= c
             pal_check(pre1, pre2, diff, a, b, c, d)
           else
             pal_check(pre2, pre1, diff, c, d, a, b)
           end
  end
  ans
end

def pal_count_pref(pre, i, j)
  cnt = Array.new(26, 0)
  26.times { |k| cnt[k] = pre[j + 1][k] - pre[i][k] }
  cnt
end

def pal_sub_cnt(cnt1, cnt2)
  cnt = Array.new(26, 0)
  26.times do |i|
    cnt[i] = cnt1[i] - cnt2[i]
    return nil if cnt[i] < 0
  end
  cnt
end

def pal_eq_cnt(a, b)
  26.times { |i| return false if a[i] != b[i] }
  true
end

def pal_check(pre1, pre2, diff, a, b, c, d)
  return false if diff[a] > 0 || diff[diff.length - 1] - diff[[b, d].max + 1] > 0
  return pal_eq_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, b)) if d <= b
  if b < c
    return diff[c] - diff[b + 1] == 0 &&
           pal_eq_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, b)) &&
           pal_eq_cnt(pal_count_pref(pre1, c, d), pal_count_pref(pre2, c, d))
  end
  cnt1 = pal_sub_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, c - 1))
  cnt2 = pal_sub_cnt(pal_count_pref(pre2, c, d), pal_count_pref(pre1, b + 1, d))
  !cnt1.nil? && !cnt2.nil? && pal_eq_cnt(cnt1, cnt2)
end
''')

add("2992_number_of_self_divisible_permutations", r'''
# LeetCode 2992 - Number of Self-Divisible Permutations
# https://leetcode.com/problems/number-of-self-divisible-permutations/

# @param {Integer} n
# @return {Integer}
def self_divisible_permutation_count(n)
  ans = 0
  used = Array.new(n + 1, false)
  dfs = lambda do |pos|
    if pos > n
      ans += 1
      return
    end
    (1..n).each do |v|
      next if used[v]
      next if v.gcd(pos) != 1

      used[v] = true
      dfs.call(pos + 1)
      used[v] = false
    end
  end
  dfs.call(1)
  ans
end
''')

add("2996_smallest_missing_integer_greater_than_sequential_prefix_sum", r'''
# LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

# @param {Integer[]} nums
# @return {Integer}
def missing_integer(nums)
  total = nums[0]
  i = 1
  while i < nums.length && nums[i] == nums[i - 1] + 1
    total += nums[i]
    i += 1
  end
  seen = {}
  nums.each { |v| seen[v] = true }
  total += 1 while seen[total]
  total
end
''')

add("2997_minimum_number_of_operations_to_make_array_xor_equal_to_k", r'''
# LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  xorr = 0
  nums.each { |v| xorr ^= v }
  diff = xorr ^ k
  ans = 0
  while diff > 0
    ans += diff & 1
    diff >>= 1
  end
  ans
end
''')

add("2998_minimum_number_of_operations_to_make_x_and_y_equal", r'''
# LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def minimum_operations_to_make_equal(x, y)
  return y - x if x <= y

  q = [[x, 0]]
  seen = { x => true }
  qi = 0
  while qi < q.length
    v, d = q[qi]
    qi += 1
    return d if v == y

    cands = [v + 1, v - 1]
    cands << (v / 11) if v % 11 == 0
    cands << (v / 5) if v % 5 == 0
    cands.each do |nxt|
      if nxt > 0 && nxt < 2 * x + 20 && !seen[nxt]
        seen[nxt] = true
        q << [nxt, d + 1]
      end
    end
  end
  -1
end
''')

add("2999_count_the_number_of_powerful_integers", r'''
# LeetCode 2999 - Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/

# @param {Integer} start
# @param {Integer} finish
# @param {Integer} limit
# @param {String} s
# @return {Integer}
def number_of_powerful_int(start, finish, limit, s)
  count_powerful(finish, limit, s) - count_powerful(start - 1, limit, s)
end

def count_powerful(num, limit, s)
  return 0 if num < 0

  s.length.times { |i| return 0 if s[i].ord - 48 > limit }
  t = num.to_s
  n = t.length
  sn = s.length
  return 0 if n < sn

  ans = 0
  (sn...n).each do |length|
    pre_len = length - sn
    if pre_len == 0
      ans += 1
    else
      ways = limit
      (1...pre_len).each { |_| ways *= limit + 1 }
      ans += ways
    end
  end
  pref = n - sn
  memo = {}
  dfs = lambda do |i, tight|
    if i == pref
      return tight ? (t[pref..-1] >= s ? 1 : 0) : 1
    end

    key = (i << 1) | (tight ? 1 : 0)
    return memo[key] if memo.key?(key)

    up = tight ? (t[i].ord - 48) : limit
    up = limit if up > limit
    res = 0
    (0..up).each do |d|
      next if i == 0 && d == 0

      res += dfs.call(i + 1, tight && d == t[i].ord - 48)
    end
    memo[key] = res
    res
  end
  ans + dfs.call(0, true)
end
''')

written = 0
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body)
    written += 1
    print(f"wrote {name}")

print(f"written={written}")
