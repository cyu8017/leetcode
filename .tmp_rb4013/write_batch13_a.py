#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2937_make_three_strings_equal", r'''
# LeetCode 2937 - Make Three Strings Equal
# https://leetcode.com/problems/make-three-strings-equal/

# @param {String} s1
# @param {String} s2
# @param {String} s3
# @return {Integer}
def find_minimum_operations(s1, s2, s3)
  n = [s1.length, s2.length, s3.length].min
  i = 0
  while i < n && s1[i] == s2[i] && s2[i] == s3[i]
    i += 1
  end
  return -1 if i == 0

  s1.length + s2.length + s3.length - 3 * i
end
''')

add("2938_separate_black_and_white_balls", r'''
# LeetCode 2938 - Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/

# @param {String} s
# @return {Integer}
def minimum_steps(s)
  ans = 0
  zeros = 0
  (s.length - 1).downto(0) do |i|
    if s[i] == "0"
      zeros += 1
    else
      ans += zeros
    end
  end
  ans
end
''')

add("2939_maximum_xor_product", r'''
# LeetCode 2939 - Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} n
# @return {Integer}
def maximum_xor_product(a, b, n)
  mod = 1_000_000_007
  aa = a
  bb = b
  (n - 1).downto(0) do |i|
    bit = 1 << i
    abit = aa & bit
    bbit = bb & bit
    if abit == bbit
      aa |= bit
      bb |= bit
    elsif aa > bb
      bb |= bit
      aa &= ~bit
    else
      aa |= bit
      bb &= ~bit
    end
  end
  ((aa % mod) * (bb % mod)) % mod
end
''')

add("2940_find_building_where_alice_and_bob_can_meet", r'''
# LeetCode 2940 - Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

# @param {Integer[]} heights
# @param {Integer[][]} queries
# @return {Integer[]}
def leftmost_building_queries(heights, queries)
  qn = queries.length
  ans = Array.new(qn, -1)
  buckets = Array.new(heights.length) { [] }
  qn.times do |qi|
    a = queries[qi][0]
    b = queries[qi][1]
    a, b = b, a if a > b
    if a == b || heights[a] < heights[b]
      ans[qi] = b
      next
    end
    buckets[b] << [heights[a], qi]
  end
  st = []
  (heights.length - 1).downto(0) do |i|
    buckets[i].each do |h, qi|
      lo = 0
      hi = st.length - 1
      pos = -1
      while lo <= hi
        mid = (lo + hi) / 2
        if st[mid][0] > h
          pos = st[mid][1]
          lo = mid + 1
        else
          hi = mid - 1
        end
      end
      ans[qi] = pos
    end
    st.pop while !st.empty? && st[-1][0] <= heights[i]
    st << [heights[i], i]
  end
  ans
end
''')

add("2941_maximum_gcd_sum_of_a_subarray", r'''
# LeetCode 2941 - Maximum GCD-Sum of a Subarray
# https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_gcd_sum(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 0
  st = []
  n.times do |i|
    nst = [[nums[i], i]]
    st.each do |p|
      g = nums[i].gcd(p[0])
      if nst[-1][0] == g
        nst[-1][1] = p[1] if p[1] < nst[-1][1]
        next
      end
      nst << [g, p[1]]
    end
    st = nst
    st.each do |g, idx|
      if i - idx + 1 >= k
        cand = (pref[i + 1] - pref[idx]) * g
        ans = cand if cand > ans
      end
    end
  end
  ans
end
''')

add("2942_find_words_containing_character", r'''
# LeetCode 2942 - Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/

# @param {String[]} words
# @param {Character} x
# @return {Integer[]}
def find_words_containing(words, x)
  ans = []
  words.each_with_index { |w, i| ans << i if w.include?(x) }
  ans
end
''')

add("2943_maximize_area_of_square_hole_in_grid", r'''
# LeetCode 2943 - Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} h_bars
# @param {Integer[]} v_bars
# @return {Integer}
def maximize_square_hole_area(n, m, h_bars, v_bars)
  side = max_gap(h_bars.dup)
  vs = max_gap(v_bars.dup)
  side = vs if vs < side
  side * side
end

def max_gap(bars)
  return 1 if bars.empty?

  bars.sort!
  best = 1
  cur = 1
  (1...bars.length).each do |i|
    if bars[i] == bars[i - 1] + 1
      cur += 1
    else
      cur = 1
    end
    best = cur if cur > best
  end
  best + 1
end
''')

add("2944_minimum_number_of_coins_for_fruits", r'''
# LeetCode 2944 - Minimum Number of Coins for Fruits
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

# @param {Integer[]} prices
# @return {Integer}
def minimum_coins(prices)
  n = prices.length
  dp = Array.new(n + 1, 1 << 30)
  dp[0] = 0
  (1..n).each do |i|
    j = i
    while j <= n && j <= i + i
      cand = dp[i - 1] + prices[i - 1]
      dp[j] = cand if cand < dp[j]
      j += 1
    end
  end
  dp[n]
end
''')

add("2945_find_maximum_non_decreasing_array_length", r'''
# LeetCode 2945 - Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

# @param {Integer[]} nums
# @return {Integer}
def find_maximum_length(nums)
  n = nums.length
  pref = Array.new(n + 1, 0)
  last = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  dp = Array.new(n + 1, 0)
  dq = [[0, 0]]
  (1..n).each do |i|
    dq.shift while dq.length > 1 && dq[1][1] <= pref[i]
    j = dq[0][0]
    dp[i] = dp[j] + 1
    last[i] = pref[i] - pref[j]
    val = pref[i] + last[i]
    dq.pop while !dq.empty? && dq[-1][1] >= val
    dq << [i, val]
  end
  dp[n]
end
''')

add("2946_matrix_similarity_after_cyclic_shifts", r'''
# LeetCode 2946 - Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

# @param {Integer[][]} mat
# @param {Integer} k
# @return {Boolean}
def are_similar(mat, k)
  m = mat.length
  n = mat[0].length
  m.times do |i|
    if i.even?
      shift = n - (k % n)
      shift = 0 if shift == n
    else
      shift = k % n
    end
    n.times do |j|
      return false if mat[i][j] != mat[i][(j + shift) % n]
    end
  end
  true
end
''')

add("2947_count_beautiful_substrings_i", r'''
# LeetCode 2947 - Count Beautiful Substrings I
# https://leetcode.com/problems/count-beautiful-substrings-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def beautiful_substrings(s, k)
  ans = 0
  n = s.length
  n.times do |i|
    v = 0
    c = 0
    i.upto(n - 1) do |j|
      if vowel?(s[j])
        v += 1
      else
        c += 1
      end
      ans += 1 if v == c && (v * c) % k == 0
    end
  end
  ans
end

def vowel?(ch)
  ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
end
''')

add("2948_make_lexicographically_smallest_array_by_swapping_elements", r'''
# LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer[]}
def lexicographically_smallest_array(nums, limit)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  ans = Array.new(n, 0)
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit
    group_idx = idx[i...j].sort
    (j - i).times { |t| ans[group_idx[t]] = nums[idx[i + t]] }
    i = j
  end
  ans
end
''')

add("2949_count_beautiful_substrings_ii", r'''
# LeetCode 2949 - Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def beautiful_substrings(s, k)
  x = 1
  x += 1 while (x * x) % k != 0
  freq = { [0, 0] => 1 }
  bal = 0
  vowels = 0
  ans = 0
  s.each_char do |ch|
    if vowel?(ch)
      bal += 1
      vowels += 1
    else
      bal -= 1
    end
    key = [bal, vowels % x]
    f = freq[key] || 0
    ans += f
    freq[key] = f + 1
  end
  ans
end

def vowel?(ch)
  ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
end
''')

add("2950_number_of_divisible_substrings", r'''
# LeetCode 2950 - Number of Divisible Substrings
# https://leetcode.com/problems/number-of-divisible-substrings/

# @param {String} word
# @return {Integer}
def count_divisible_substrings(word)
  vals = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
  ans = 0
  n = word.length
  n.times do |i|
    s = 0
    i.upto(n - 1) do |j|
      s += vals[word[j].ord - 97]
      ans += 1 if s % (j - i + 1) == 0
    end
  end
  ans
end
''')

add("2951_find_the_peaks", r'''
# LeetCode 2951 - Find the Peaks
# https://leetcode.com/problems/find-the-peaks/

# @param {Integer[]} mountain
# @return {Integer[]}
def find_peaks(mountain)
  ans = []
  (1...mountain.length - 1).each do |i|
    ans << i if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]
  end
  ans
end
''')

add("2952_minimum_number_of_coins_to_be_added", r'''
# LeetCode 2952 - Minimum Number of Coins to be Added
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

# @param {Integer[]} coins
# @param {Integer} target
# @return {Integer}
def minimum_added_coins(coins, target)
  coins.sort!
  ans = 0
  reach = 0
  i = 0
  while reach < target
    if i < coins.length && coins[i] <= reach + 1
      reach += coins[i]
      i += 1
    else
      reach += reach + 1
      ans += 1
    end
  end
  ans
end
''')

add("2953_count_complete_substrings", r'''
# LeetCode 2953 - Count Complete Substrings
# https://leetcode.com/problems/count-complete-substrings/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_complete_substrings(word, k)
  n = word.length
  ans = 0
  i = 0
  while i < n
    j = i
    j += 1 while j + 1 < n && (word[j + 1].ord - word[j].ord).abs <= 2
    seg = word[i..j]
    m = seg.length
    (1..26).each do |chars|
      length = chars * k
      break if length > m

      freq = Array.new(26, 0)
      unique = 0
      m.times do |r|
        c = seg[r].ord - 97
        freq[c] += 1
        unique += 1 if freq[c] == 1
        if r >= length
          c2 = seg[r - length].ord - 97
          freq[c2] -= 1
          unique -= 1 if freq[c2] == 0
        end
        if r >= length - 1 && unique == chars
          ok = true
          freq.each do |f|
            if f != 0 && f != k
              ok = false
              break
            end
          end
          ans += 1 if ok
        end
      end
    end
    i = j + 1
  end
  ans
end
''')

add("2954_count_the_number_of_infection_sequences", r'''
# LeetCode 2954 - Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/

MOD = 1_000_000_007

# @param {Integer} n
# @param {Integer[]} sick
# @return {Integer}
def number_of_sequence(n, sick)
  fact = Array.new(n + 1, 0)
  inv_fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }
  m = sick.length
  total_empty = n - m
  ans = fact[total_empty]
  prev = -1
  sick.each do |s|
    gap = s - prev - 1
    if prev == -1
      ans = ans * inv_fact[gap] % MOD
    elsif gap > 0
      ans = ans * inv_fact[gap] % MOD * mod_pow(2, gap - 1) % MOD
    end
    prev = s
  end
  gap2 = n - prev - 1
  ans * inv_fact[gap2] % MOD
end

def mod_pow(a, b)
  res = 1
  a %= MOD
  while b > 0
    res = res * a % MOD if b.odd?
    a = a * a % MOD
    b >>= 1
  end
  res
end
''')

add("2955_number_of_same_end_substrings", r'''
# LeetCode 2955 - Number of Same-End Substrings
# https://leetcode.com/problems/number-of-same-end-substrings/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def same_end_substring_count(s, queries)
  n = s.length
  pref = Array.new(n + 1) { Array.new(26, 0) }
  n.times do |i|
    26.times { |c| pref[i + 1][c] = pref[i][c] }
    pref[i + 1][s[i].ord - 97] += 1
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r), qi|
    total = 0
    26.times do |c|
      cnt = pref[r + 1][c] - pref[l][c]
      total += cnt * (cnt + 1) / 2
    end
    ans[qi] = total
  end
  ans
end
''')

add("2956_find_common_elements_between_two_arrays", r'''
# LeetCode 2956 - Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def find_intersection_values(nums1, nums2)
  s1 = nums1.to_h { |v| [v, true] }
  s2 = nums2.to_h { |v| [v, true] }
  a = nums1.count { |v| s2[v] }
  b = nums2.count { |v| s1[v] }
  [a, b]
end
''')

add("2957_remove_adjacent_almost_equal_characters", r'''
# LeetCode 2957 - Remove Adjacent Almost-Equal Characters
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

# @param {String} word
# @return {Integer}
def remove_almost_equal_characters(word)
  ans = 0
  i = 1
  n = word.length
  while i < n
    if (word[i].ord - word[i - 1].ord).abs <= 1
      ans += 1
      i += 2
    else
      i += 1
    end
  end
  ans
end
''')

add("2958_length_of_longest_subarray_with_at_most_k_frequency", r'''
# LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_length(nums, k)
  freq = Hash.new(0)
  ans = 0
  left = 0
  nums.each_with_index do |v, right|
    freq[v] += 1
    while freq[v] > k
      freq[nums[left]] -= 1
      left += 1
    end
    ans = right - left + 1 if right - left + 1 > ans
  end
  ans
end
''')

add("2959_number_of_possible_sets_of_closing_branches", r'''
# LeetCode 2959 - Number of Possible Sets of Closing Branches
# https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

# @param {Integer} n
# @param {Integer} max_distance
# @param {Integer[][]} roads
# @return {Integer}
def number_of_sets(n, max_distance, roads)
  ans = 0
  (1 << n).times do |mask|
    dist = Array.new(n) { Array.new(n, 1 << 29) }
    n.times { |i| dist[i][i] = 0 }
    roads.each do |u, v, w|
      if (mask & (1 << u)) != 0 && (mask & (1 << v)) != 0 && w < dist[u][v]
        dist[u][v] = w
        dist[v][u] = w
      end
    end
    n.times do |k|
      next if (mask & (1 << k)) == 0

      n.times do |i|
        next if (mask & (1 << i)) == 0

        n.times do |j|
          next if (mask & (1 << j)) == 0

          dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
        end
      end
    end
    ok = true
    i = 0
    while i < n && ok
      if (mask & (1 << i)) == 0
        i += 1
        next
      end
      n.times do |j|
        next if (mask & (1 << j)) == 0

        if dist[i][j] > max_distance
          ok = false
          break
        end
      end
      i += 1
    end
    ans += 1 if ok
  end
  ans
end
''')

add("2960_count_tested_devices_after_test_operations", r'''
# LeetCode 2960 - Count Tested Devices After Test Operations
# https://leetcode.com/problems/count-tested-devices-after-test-operations/

# @param {Integer[]} battery_percentages
# @return {Integer}
def count_tested_devices(battery_percentages)
  ans = 0
  battery_percentages.each { |b| ans += 1 if b > ans }
  ans
end
''')

add("2961_double_modular_exponentiation", r'''
# LeetCode 2961 - Double Modular Exponentiation
# https://leetcode.com/problems/double-modular-exponentiation/

# @param {Integer[][]} variables
# @param {Integer} target
# @return {Integer[]}
def get_good_indices(variables, target)
  ans = []
  variables.each_with_index do |v, i|
    a, b, c, m = v
    ans << i if mod_pow(mod_pow(a, b, 10), c, m) == target
  end
  ans
end

def mod_pow(a, b, mod)
  res = 1 % mod
  a %= mod
  while b > 0
    res = res * a % mod if (b & 1) != 0
    a = a * a % mod
    b >>= 1
  end
  res
end
''')

written = 0
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body)
    written += 1
    print(f"wrote {name}")

print(f"written={written}")
