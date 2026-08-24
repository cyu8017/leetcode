#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3848_check_digitorial_permutation", r'''
# LeetCode 3848 - Check Digitorial Permutation
# https://leetcode.com/problems/check-digitorial-permutation/

# @param {Integer} n
# @return {Boolean}
def is_digitorial_permutation(n)
  f = Array.new(10, 0)
  f[0] = 1
  (1...10).each { |i| f[i] = f[i - 1] * i }
  x = 0
  y = n
  while y > 0
    x += f[y % 10]
    y /= 10
  end
  a = x.to_s.chars.sort.join
  b = n.to_s.chars.sort.join
  a == b
end
''')

add("3849_maximum_bitwise_xor_after_rearrangement", r'''
# LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

# @param {String} s
# @param {String} t
# @return {String}
def maximum_xor(s, t)
  cnt = [0, 0]
  t.each_byte { |c| cnt[c - 48] += 1 }
  ans = Array.new(s.length, "")
  s.length.times do |i|
    x = s[i].ord - 48
    if cnt[x ^ 1] > 0
      cnt[x ^ 1] -= 1
      ans[i] = "1"
    else
      cnt[x] -= 1
      ans[i] = "0"
    end
  end
  ans.join
end
''')

add("3850_count_sequences_to_k", r'''
# LeetCode 3850 - Count Sequences to K
# https://leetcode.com/problems/count-sequences-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_sequences(nums, k)
  f = {}
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  dfs = nil
  dfs = lambda do |i, p, q|
    return (p == k && q == 1) ? 1 : 0 if i == nums.length
    key = "#{i},#{p},#{q}"
    return f[key] if f.key?(key)
    res = dfs.call(i + 1, p, q)
    x = nums[i]
    g1 = gcd.call(p * x, q)
    res += dfs.call(i + 1, (p * x) / g1, q / g1)
    g2 = gcd.call(p, q * x)
    res += dfs.call(i + 1, p / g2, (q * x) / g2)
    f[key] = res
    res
  end
  dfs.call(0, 1, 1)
end
''')

add("3851_maximum_requests_without_violating_the_limit", r'''
# LeetCode 3851 - Maximum Requests Without Violating the Limit
# https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

# @param {Integer[][]} requests
# @param {Integer} k
# @param {Integer} window
# @return {Integer}
def max_requests(requests, k, window)
  g = {}
  requests.each do |r|
    g[r[0]] ||= []
    g[r[0]] << r[1]
  end
  ans = requests.length
  g.each_value do |ts|
    ts.sort!
    kept = []
    ts.each do |t|
      kept.shift while !kept.empty? && t - kept[0] > window
      if kept.length < k
        kept << t
      else
        ans -= 1
      end
    end
  end
  ans
end
''')

add("3852_smallest_pair_with_different_frequencies", r'''
# LeetCode 3852 - Smallest Pair With Different Frequencies
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/

# @param {Integer[]} nums
# @return {Integer[]}
def min_distinct_freq_pair(nums)
  cnt = Hash.new(0)
  nums.each { |v| cnt[v] += 1 }
  x = nums.min
  min_y = Float::INFINITY
  cnt.each_key do |y|
    min_y = y if y < min_y && cnt[x] != cnt[y]
  end
  return [-1, -1] if min_y == Float::INFINITY
  [x, min_y.to_i]
end
''')

add("3853_merge_close_characters", r'''
# LeetCode 3853 - Merge Close Characters
# https://leetcode.com/problems/merge-close-characters/

# @param {String} s
# @param {Integer} k
# @return {String}
def merge_characters(s, k)
  last = {}
  ans = ""
  s.each_char do |c|
    cur = ans.length
    next if last.key?(c) && cur - last[c] <= k
    ans += c
    last[c] = cur
  end
  ans
end
''')

add("3854_minimum_operations_to_make_array_parity_alternating", r'''
# LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
# https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

# @param {Integer[]} nums
# @return {Integer[]}
def make_parity_alternating(nums)
  return [0, 0] if nums.length == 1
  mn = nums.min
  mx = nums.max
  f = lambda do |k, mn_v, mx_v|
    cnt = 0
    a = Float::INFINITY
    b = -Float::INFINITY
    nums.each_with_index do |x, i|
      if ((x - i) & 1) != k
        cnt += 1
        if x == mn_v
          x += 1
        elsif x == mx_v
          x -= 1
        end
      end
      a = [a, x].min
      b = [b, x].max
    end
    [cnt, [1, (b - a).to_i].max]
  end
  r0 = f.call(0, mn, mx)
  r1 = f.call(1, mn, mx)
  return r0[0] < r1[0] ? r0 : r1 if r0[0] != r1[0]
  r0[1] <= r1[1] ? r0 : r1
end
''')

add("3855_sum_of_k_digit_numbers_in_a_range", r'''
# LeetCode 3855 - Sum of K-Digit Numbers in a Range
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def sum_of_numbers(l, r, k)
  qpow = lambda do |a, n, mod|
    a %= mod
    res = 1
    while n > 0
      res = res * a % mod if n.odd?
      a = a * a % mod
      n >>= 1
    end
    res
  end
  mod = 1_000_000_007
  n = r - l + 1
  s = ((l + r) * n / 2) % mod
  part1 = qpow.call(n % mod, k - 1, mod)
  part2 = (qpow.call(10, k, mod) - 1 + mod) % mod
  inv9 = qpow.call(9, mod - 2, mod)
  ans = s
  ans = ans * part1 % mod
  ans = ans * part2 % mod
  ans * inv9 % mod
end
''')

add("3856_trim_trailing_vowels", r'''
# LeetCode 3856 - Trim Trailing Vowels
# https://leetcode.com/problems/trim-trailing-vowels/

# @param {String} s
# @return {String}
def trim_trailing_vowels(s)
  i = s.length - 1
  i -= 1 while i >= 0 && "aeiou".include?(s[i])
  s[0, i + 1]
end
''')

add("3857_minimum_cost_to_split_into_ones", r'''
# LeetCode 3857 - Minimum Cost to Split into Ones
# https://leetcode.com/problems/minimum-cost-to-split-into-ones/

# @param {Integer} n
# @return {Integer}
def min_cost(n)
  n * (n - 1) / 2
end
''')

add("3858_minimum_bitwise_or_from_grid", r'''
# LeetCode 3858 - Minimum Bitwise OR From Grid
# https://leetcode.com/problems/minimum-bitwise-or-from-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_or(grid)
  mx = 0
  grid.each { |row| row.each { |x| mx = [mx, x].max } }
  m = bit_len_3858(mx)
  ans = 0
  (m - 1).downto(0) do |i|
    mask = ans | ((1 << i) - 1)
    grid.each do |row|
      found = row.any? { |x| (x | mask) == mask }
      unless found
        ans |= 1 << i
        break
      end
    end
  end
  ans
end

def bit_len_3858(x)
  return 0 if x == 0
  n = 0
  while x > 0
    n += 1
    x >>= 1
  end
  n
end
''')

add("3859_count_subarrays_with_k_distinct_integers", r'''
# LeetCode 3859 - Count Subarrays With K Distinct Integers
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def count_subarrays(nums, k, m)
  f = lambda do |lim|
    cnt = Hash.new(0)
    ans = 0
    l = 0
    t = 0
    nums.each do |x|
      c = cnt[x] + 1
      cnt[x] = c
      t += 1 if c == m
      while cnt.length >= lim && t >= k
        y = nums[l]
        l += 1
        cy = cnt[y] - 1
        t -= 1 if cy == m - 1
        if cy == 0
          cnt.delete(y)
        else
          cnt[y] = cy
        end
      end
      ans += l
    end
    ans
  end
  f.call(k) - f.call(k + 1)
end
''')

add("3860_unique_email_groups", r'''
# LeetCode 3860 - Unique Email Groups
# https://leetcode.com/problems/unique-email-groups/

# @param {String[]} emails
# @return {Integer}
def unique_email_groups(emails)
  st = {}
  emails.each do |email|
    at = email.index("@")
    local = email[0, at]
    domain = email[(at + 1)..].downcase
    plus = local.index("+")
    local = local[0, plus] if plus
    cleaned = local.delete(".").downcase
    st[cleaned + domain] = true
  end
  st.length
end
''')

add("3861_minimum_capacity_box", r'''
# LeetCode 3861 - Minimum Capacity Box
# https://leetcode.com/problems/minimum-capacity-box/

# @param {Integer[]} capacity
# @param {Integer} item_size
# @return {Integer}
def minimum_index(capacity, item_size)
  ans = -1
  capacity.each_with_index do |c, i|
    ans = i if c >= item_size && (ans == -1 || c < capacity[ans])
  end
  ans
end
''')

add("3862_find_the_smallest_balanced_index", r'''
# LeetCode 3862 - Find the Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/

# @param {Integer[]} nums
# @return {Integer}
def smallest_balanced_index(nums)
  s = nums.sum
  p = 1
  (nums.length - 1).downto(0) do |i|
    s -= nums[i]
    return i if s == p
    p *= nums[i]
    break if p >= s
  end
  -1
end
''')

add("3863_minimum_operations_to_sort_a_string", r'''
# LeetCode 3863 - Minimum Operations to Sort a String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/

# @param {String} s
# @return {Integer}
def min_operations(s)
  n = s.length
  sorted_ok = true
  (1...n).each do |i|
    if s[i] < s[i - 1]
      sorted_ok = false
      break
    end
  end
  return 0 if sorted_ok
  return -1 if n == 2
  mn = s.chars.min
  mx = s.chars.max
  return 1 if s[0] == mn || s[n - 1] == mx
  (1...(n - 1)).each { |i| return 2 if s[i] == mn || s[i] == mx }
  3
end
''')

add("3864_minimum_cost_to_partition_a_binary_string", r'''
# LeetCode 3864 - Minimum Cost to Partition a Binary String
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

# @param {String} s
# @param {Integer} enc_cost
# @param {Integer} flat_cost
# @return {Integer}
def min_cost(s, enc_cost, flat_cost)
  n = s.length
  pre = Array.new(n + 1, 0)
  (1..n).each { |i| pre[i] = pre[i - 1] + (s[i - 1].ord - 48) }
  dfs = nil
  dfs = lambda do |l, r|
    x = pre[r] - pre[l]
    res = x != 0 ? (r - l) * x * enc_cost : flat_cost
    if (r - l).even?
      m = (l + r) / 2
      res = [res, dfs.call(l, m) + dfs.call(m, r)].min
    end
    res
  end
  dfs.call(0, n)
end
''')

add("3865_reverse_k_subarrays", r'''
# LeetCode 3865 - Reverse K Subarrays
# https://leetcode.com/problems/reverse-k-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def reverse_subarrays(nums, k)
  n = nums.length
  m = n / k
  i = 0
  while i < n
    lo = i
    hi = i + m - 1
    while lo < hi
      nums[lo], nums[hi] = nums[hi], nums[lo]
      lo += 1
      hi -= 1
    end
    i += m
  end
  nums
end
''')

add("3866_first_unique_even_element", r'''
# LeetCode 3866 - First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/

# @param {Integer[]} nums
# @return {Integer}
def first_unique_even(nums)
  cnt = Array.new(101, 0)
  nums.each { |x| cnt[x] += 1 }
  nums.each { |x| return x if x.even? && cnt[x] == 1 }
  -1
end
''')

add("3867_sum_of_gcd_of_formed_pairs", r'''
# LeetCode 3867 - Sum of GCD of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

# @param {Integer[]} nums
# @return {Integer}
def gcd_sum(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  prefix_gcd = Array.new(n, 0)
  mx = 0
  n.times do |i|
    mx = [mx, nums[i]].max
    prefix_gcd[i] = gcd.call(nums[i], mx)
  end
  prefix_gcd.sort!
  ans = 0
  (n / 2).times { |i| ans += gcd.call(prefix_gcd[i], prefix_gcd[n - i - 1]) }
  ans
end
''')

add("3868_minimum_cost_to_equalize_arrays_using_swaps", r'''
# LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_cost(nums1, nums2)
  cnt2 = Hash.new(0)
  nums2.each { |x| cnt2[x] += 1 }
  cnt1 = Hash.new(0)
  nums1.each do |x|
    c = cnt2[x]
    if c > 0
      cnt2[x] = c - 1
    else
      cnt1[x] += 1
    end
  end
  ans = 0
  cnt1.each_value do |v|
    return -1 if v.odd?
    ans += v / 2
  end
  cnt2.each_value { |v| return -1 if v.odd? }
  ans
end
''')

add("3869_count_fancy_numbers_in_a_range", r'''
# LeetCode 3869 - Count Fancy Numbers in a Range
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_fancy(l, r)
  check = lambda do |s|
    return s % 11 != 0 if s < 100
    mid = (s / 10) % 10
    last = s % 10
    mid > 1 && mid < last
  end
  num = ""
  n = 0
  f = []
  dfs = nil
  dfs = lambda do |pos, s, prev, st, lim|
    if pos >= n
      return st != 3 ? 1 : (check.call(s) ? 1 : 0)
    end
    return f[pos][s][prev][st] if !lim && f[pos][s][prev][st] != -1
    up = lim ? num[pos].ord - 48 : 9
    res = 0
    (0..up).each do |i|
      nxt_st = st
      if st == 0
        nxt_st = if prev == 0
                   0
                 elsif i > prev
                   1
                 elsif i < prev
                   2
                 else
                   3
                 end
      elsif st == 1
        nxt_st = i > prev ? 1 : 3
      elsif st == 2
        nxt_st = i < prev ? 2 : 3
      else
        nxt_st = 3
      end
      res += dfs.call(pos + 1, s + i, i, nxt_st, lim && i == up)
    end
    f[pos][s][prev][st] = res unless lim
    res
  end
  calc = lambda do |x|
    return 0 if x < 0
    num = x.to_s
    n = num.length
    f = Array.new(n) { Array.new(9 * n + 1) { Array.new(10) { Array.new(4, -1) } } }
    dfs.call(0, 0, 0, 0, true)
  end
  calc.call(r) - calc.call(l - 1)
end
''')

add("3870_count_commas_in_range", r'''
# LeetCode 3870 - Count Commas in Range
# https://leetcode.com/problems/count-commas-in-range/

# @param {Integer} n
# @return {Integer}
def count_commas(n)
  [0, n - 999].max
end
''')

add("3871_count_commas_in_range_ii", r'''
# LeetCode 3871 - Count Commas in Range II
# https://leetcode.com/problems/count-commas-in-range-ii/

# @param {Integer} n
# @return {Integer}
def count_commas(n)
  ans = 0
  x = 1000
  while x <= n
    ans += n - x + 1
    x *= 1000
  end
  ans
end
''')

add("3872_longest_arithmetic_sequence_after_changing_at_most_one_element", r'''
# LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
# https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_arithmetic(nums)
  n = nums.length
  d = Array.new(n, 0)
  (1...n).each { |i| d[i] = nums[i] - nums[i - 1] }
  f = Array.new(n, 2)
  g = Array.new(n, 2)
  f[0] = 1
  g[n - 1] = 1
  (2...n).each { |i| f[i] = f[i - 1] + 1 if d[i] == d[i - 1] }
  (n - 3).downto(0) { |i| g[i] = g[i + 1] + 1 if d[i + 1] == d[i + 2] }
  ans = 3
  n.times do |i|
    ans = [ans, [f[i], g[i]].max].max
    ans = [ans, f[i - 1] + 1].max if i > 0
    ans = [ans, g[i + 1] + 1].max if i + 1 < n
    if i > 0 && i < n - 1
      diff = nums[i + 1] - nums[i - 1]
      if diff.even?
        diff /= 2
        k = 3
        k += f[i - 1] - 1 if i > 1 && diff == d[i - 1]
        k += g[i + 1] - 1 if i < n - 2 && diff == d[i + 2]
        ans = [ans, k].max
      end
    end
  end
  ans
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch21_b written={written}")


if __name__ == "__main__":
    main()
