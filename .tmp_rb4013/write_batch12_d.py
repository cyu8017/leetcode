#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2910_minimum_number_of_groups_to_create_a_valid_assignment", r'''
# LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

# @param {Integer[]} balls
# @return {Integer}
def min_groups_for_valid_assignment(balls)
  freq = {}
  balls.each { |b| freq[b] = freq.fetch(b, 0) + 1 }
  counts = freq.values
  min_f = counts.min
  min_f.downto(1) do |size|
    ok = true
    groups = 0
    counts.each do |c|
      rem = c % (size + 1)
      g2 = c / (size + 1)
      if rem == 0
        groups += g2
      elsif size - rem <= g2
        groups += g2 + 1
      else
        ok = false
        break
      end
    end
    return groups if ok
  end
  balls.length
end
''')

add("2911_minimum_changes_to_make_k_semi_palindromes", r'''
# LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_changes(s, k)
  n = s.length
  inf = 1 << 20
  cost = Array.new(n) { Array.new(n, inf) }

  semi_cost = lambda do |l, r|
    length = r - l + 1
    best = inf
    (1...length).each do |d|
      next unless length % d == 0

      chg = 0
      (0...d).each do |start|
        chars = []
        i = l + start
        while i <= r
          chars << s[i]
          i += d
        end
        i = 0
        j = chars.length - 1
        while i < j
          chg += 1 if chars[i] != chars[j]
          i += 1
          j -= 1
        end
      end
      best = chg if chg < best
    end
    best
  end

  (0...n).each do |i|
    (i + 1...n).each { |j| cost[i][j] = semi_cost.call(i, j) }
  end
  dp = Array.new(k + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0
  (1..k).each do |p|
    (1..n).each do |i|
      (0...i - 1).each do |t|
        cand = dp[p - 1][t] + cost[t][i - 1]
        dp[p][i] = cand if cand < dp[p][i]
      end
    end
  end
  dp[k][n]
end
''')

add("2912_number_of_ways_to_reach_destination_in_the_grid", r'''
# LeetCode 2912 - Number of Ways to Reach Destination in the Grid
# https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @param {Integer[]} source
# @param {Integer[]} dest
# @return {Integer}
def number_of_ways(n, m, k, source, dest)
  mod = 1_000_000_007
  sx, sy = source[0], source[1]
  tx, ty = dest[0], dest[1]
  same = row = col = other = 0
  if sx == tx && sy == ty
    same = 1
  elsif sx == tx
    row = 1
  elsif sy == ty
    col = 1
  else
    other = 1
  end
  k.times do
    ns = (row + col) % mod
    nr = (same * (m - 1) + row * (m - 2) + other) % mod
    nc = (same * (n - 1) + col * (n - 2) + other) % mod
    no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4)) % mod
    same, row, col, other = ns, nr, nc, no
  end
  same
end
''')

add("2913_subarrays_distinct_element_sum_of_squares_i", r'''
# LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    seen = {}
    (i...n).each do |j|
      seen[nums[j]] = true
      d = seen.length
      ans += d * d
    end
  end
  ans
end
''')

add("2914_minimum_number_of_changes_to_make_binary_string_beautiful", r'''
# LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

# @param {String} s
# @return {Integer}
def min_changes(s)
  ans = 0
  0.step(s.length - 1, 2) { |i| ans += 1 if s[i] != s[i + 1] }
  ans
end
''')

add("2915_length_of_the_longest_subsequence_that_sums_to_target", r'''
# LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def length_of_longest_subsequence(nums, target)
  dp = Array.new(target + 1, -1)
  dp[0] = 0
  nums.each do |v|
    target.downto(v) do |s|
      dp[s] = dp[s - v] + 1 if dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]
    end
  end
  dp[target]
end
''')

add("2916_subarrays_distinct_element_sum_of_squares_ii", r'''
# LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  mod = 1_000_000_007
  n = nums.length
  tree = Array.new(4 * (n + 2)) { { "sum" => 0, "sumSq" => 0, "lazy" => 0 } }

  apply = lambda do |idx, l, r, val|
    length = r - l + 1
    tree[idx]["sumSq"] = (
      tree[idx]["sumSq"] +
      2 * val % mod * tree[idx]["sum"] % mod +
      val % mod * val % mod * length % mod
    ) % mod
    tree[idx]["sum"] = (tree[idx]["sum"] + val % mod * length % mod) % mod
    tree[idx]["lazy"] = (tree[idx]["lazy"] + val) % mod
  end

  update = nil
  update = lambda do |idx, l, r, ql, qr, val|
    return if ql > r || qr < l
    if ql <= l && r <= qr
      apply.call(idx, l, r, val)
      return
    end
    if tree[idx]["lazy"] != 0 && l != r
      mid = (l + r) / 2
      apply.call(idx * 2, l, mid, tree[idx]["lazy"])
      apply.call(idx * 2 + 1, mid + 1, r, tree[idx]["lazy"])
      tree[idx]["lazy"] = 0
    end
    mid = (l + r) / 2
    update.call(idx * 2, l, mid, ql, qr, val)
    update.call(idx * 2 + 1, mid + 1, r, ql, qr, val)
    tree[idx]["sum"] = (tree[idx * 2]["sum"] + tree[idx * 2 + 1]["sum"]) % mod
    tree[idx]["sumSq"] = (tree[idx * 2]["sumSq"] + tree[idx * 2 + 1]["sumSq"]) % mod
  end

  last = {}
  ans = 0
  (1..n).each do |i|
    v = nums[i - 1]
    prev = last.fetch(v, 0)
    update.call(1, 1, n, prev + 1, i, 1)
    ans = (ans + tree[1]["sumSq"]) % mod
    last[v] = i
  end
  ans
end
''')

add("2917_find_the_k_or_of_an_array", r'''
# LeetCode 2917 - Find the K-or of an Array
# https://leetcode.com/problems/find-the-k-or-of-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_k_or(nums, k)
  ans = 0
  (0...31).each do |b|
    cnt = 0
    nums.each { |v| cnt += 1 if (v & (1 << b)) != 0 }
    ans |= 1 << b if cnt >= k
  end
  ans
end
''')

add("2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros", r'''
# LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_sum(nums1, nums2)
  s1 = s2 = z1 = z2 = 0
  nums1.each do |v|
    if v == 0
      z1 += 1
      s1 += 1
    else
      s1 += v
    end
  end
  nums2.each do |v|
    if v == 0
      z2 += 1
      s2 += 1
    else
      s2 += v
    end
  end
  return -1 if z1 == 0 && s1 < s2
  return -1 if z2 == 0 && s2 < s1

  s1 > s2 ? s1 : s2
end
''')

add("2919_minimum_increment_operations_to_make_array_beautiful", r'''
# LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_increment_operations(nums, k)
  dp0 = dp1 = dp2 = 0
  nums.each do |v|
    cost = v < k ? k - v : 0
    nd0 = cost + [dp0, dp1, dp2].min
    dp0, dp1, dp2 = dp1, dp2, nd0
  end
  [dp0, dp1, dp2].min
end
''')

add("2920_maximum_points_after_collecting_coins_from_all_nodes", r'''
# LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

# @param {Integer[][]} edges
# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def maximum_points(edges, coins, k)
  n = coins.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  memo = {}

  dfs = nil
  dfs = lambda do |u, p, shifts|
    shifts = 14 if shifts > 14
    key = (u << 5) | shifts
    return memo[key] if memo.key?(key)

    c = coins[u] >> shifts
    opt1 = c - k
    opt2 = c / 2
    g[u].each do |v|
      next if v == p

      opt1 += dfs.call(v, u, shifts)
      opt2 += dfs.call(v, u, shifts + 1)
    end
    best = [opt1, opt2].max
    memo[key] = best
    best
  end

  dfs.call(0, -1, 0)
end
''')

add("2921_maximum_profitable_triplets_with_increasing_prices_ii", r'''
# LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

# @param {Integer[]} prices
# @param {Integer[]} profits
# @return {Integer}
def max_profit(prices, profits)
  n = prices.length
  ans = -1
  bit = Array.new(5002, 0)

  update = lambda do |i, val|
    while i < bit.length
      bit[i] = val if val > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = -1
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  max_left = Array.new(n, 0)
  (0...n).each do |j|
    max_left[j] = query.call(prices[j] - 1)
    update.call(prices[j], profits[j])
  end
  (0...n).each do |j|
    best_r = -1
    (j + 1...n).each do |k|
      best_r = profits[k] if prices[k] > prices[j] && profits[k] > best_r
    end
    if max_left[j] >= 0 && best_r >= 0
      cand = max_left[j] + profits[j] + best_r
      ans = cand if cand > ans
    end
  end
  ans
end
''')

add("2923_find_champion_i", r'''
# LeetCode 2923 - Find Champion I
# https://leetcode.com/problems/find-champion-i/

# @param {Integer[][]} grid
# @return {Integer}
def find_champion(grid)
  n = grid.length
  (0...n).each do |i|
    win = true
    (0...n).each do |j|
      if i != j && grid[i][j] == 0
        win = false
        break
      end
    end
    return i if win
  end
  -1
end
''')

add("2924_find_champion_ii", r'''
# LeetCode 2924 - Find Champion II
# https://leetcode.com/problems/find-champion-ii/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_champion(n, edges)
  indeg = Array.new(n, 0)
  edges.each { |e| indeg[e[1]] += 1 }
  ans = -1
  (0...n).each do |i|
    next unless indeg[i] == 0
    return -1 if ans != -1

    ans = i
  end
  ans
end
''')

add("2925_maximum_score_after_applying_operations_on_a_tree", r'''
# LeetCode 2925 - Maximum Score After Applying Operations on a Tree
# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

# @param {Integer[][]} edges
# @param {Integer[]} values
# @return {Integer}
def maximum_score_after_operations(edges, values)
  n = values.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  total = values.sum

  dfs = lambda do |u, p|
    sum_kids = 0
    is_leaf = true
    g[u].each do |v|
      next if v == p

      is_leaf = false
      sum_kids += dfs.call(v, u)
    end
    return values[u] if is_leaf

    values[u] < sum_kids ? values[u] : sum_kids
  end

  total - dfs.call(0, -1)
end
''')

add("2926_maximum_balanced_subsequence_sum", r'''
# LeetCode 2926 - Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_balanced_subsequence_sum(nums)
  neg_inf = -(2**53) / 4
  n = nums.length
  keys = nums.each_with_index.map { |v, i| v - i }
  uniq = keys.uniq.sort
  bit = Array.new(uniq.length + 2, neg_inf)

  idx_of = lambda do |v|
    lo = 0
    hi = uniq.length
    while lo < hi
      mid = (lo + hi) / 2
      if uniq[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  update = lambda do |i, val|
    while i < bit.length
      bit[i] = val if val > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = neg_inf
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  ans = neg_inf
  (0...n).each do |i|
    id_ = idx_of.call(keys[i])
    best = query.call(id_)
    cur = nums[i]
    if best > neg_inf / 2
      cand = best + nums[i]
      cur = cand if cand > cur
    end
    update.call(id_, cur)
    ans = cur if cur > ans
  end
  ans
end
''')

add("2927_distribute_candies_among_children_iii", r'''
# LeetCode 2927 - Distribute Candies Among Children III
# https://leetcode.com/problems/distribute-candies-among-children-iii/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  comb = lambda do |x|
    return 0 if x < 2

    x * (x - 1) / 2
  end

  ans = comb.call(n + 2)
  ans -= 3 * comb.call(n - limit + 1)
  ans += 3 * comb.call(n - 2 * (limit + 1) + 2)
  ans -= comb.call(n - 3 * (limit + 1) + 2)
  ans = 0 if ans < 0
  ans
end
''')

add("2928_distribute_candies_among_children_i", r'''
# LeetCode 2928 - Distribute Candies Among Children I
# https://leetcode.com/problems/distribute-candies-among-children-i/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  ans = 0
  (0..limit).each do |i|
    (0..limit).each do |j|
      k = n - i - j
      ans += 1 if k >= 0 && k <= limit
    end
  end
  ans
end
''')

add("2929_distribute_candies_among_children_ii", r'''
# LeetCode 2929 - Distribute Candies Among Children II
# https://leetcode.com/problems/distribute-candies-among-children-ii/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  comb2 = lambda do |x|
    return 0 if x < 0

    (x + 1) * (x + 2) / 2
  end

  ans = comb2.call(n)
  ans -= 3 * comb2.call(n - (limit + 1))
  ans += 3 * comb2.call(n - 2 * (limit + 1))
  ans -= comb2.call(n - 3 * (limit + 1))
  ans
end
''')

add("2930_number_of_strings_which_can_be_rearranged_to_contain_substring", r'''
# LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

# @param {Integer} n
# @return {Integer}
def string_count(n)
  return 0 if n < 4

  mod = 1_000_000_007
  mod_pow = lambda do |a, b|
    res = 1
    a %= mod
    while b > 0
      res = (res * a) % mod if (b & 1) != 0
      a = (a * a) % mod
      b >>= 1
    end
    res
  end

  (
    mod_pow.call(26, n) -
    (mod_pow.call(25, n - 1) * (75 + n)) +
    (mod_pow.call(24, n - 1) * (72 + 2 * n)) -
    (mod_pow.call(23, n - 1) * (23 + n))
  ) % mod
end
''')

add("2931_maximum_spending_after_buying_items", r'''
# LeetCode 2931 - Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/

# @param {Integer[][]} values
# @return {Integer}
def max_spending(values)
  m = values.length
  n = values[0].length
  idx = Array.new(m, n - 1)
  ans = 0
  day = 1
  total = m * n
  total.times do
    best_i = -1
    best_v = 10**18
    (0...m).each do |i|
      if idx[i] >= 0 && values[i][idx[i]] < best_v
        best_v = values[i][idx[i]]
        best_i = i
      end
    end
    ans += best_v * day
    idx[best_i] -= 1
    day += 1
  end
  ans
end
''')

add("2932_maximum_strong_pair_xor_i", r'''
# LeetCode 2932 - Maximum Strong Pair XOR I
# https://leetcode.com/problems/maximum-strong-pair-xor-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_strong_pair_xor(nums)
  ans = 0
  (0...nums.length).each do |i|
    (i...nums.length).each do |j|
      x = nums[i]
      y = nums[j]
      if (x - y).abs <= [x, y].min
        xorr = x ^ y
        ans = xorr if xorr > ans
      end
    end
  end
  ans
end
''')

add("2933_high_access_employees", r'''
# LeetCode 2933 - High-Access Employees
# https://leetcode.com/problems/high-access-employees/

# @param {String[][]} access_times
# @return {String[]}
def find_high_access_employees(access_times)
  m = {}
  access_times.each do |name, t|
    hh = (t[0].ord - 48) * 10 + (t[1].ord - 48)
    mm = (t[2].ord - 48) * 10 + (t[3].ord - 48)
    m[name] ||= []
    m[name] << hh * 60 + mm
  end
  ans = []
  m.each do |name, times|
    times.sort!
    (0...times.length - 2).each do |i|
      if times[i + 2] - times[i] < 60
        ans << name
        break
      end
    end
  end
  ans.sort
end
''')

add("2934_minimum_operations_to_maximize_last_elements_in_arrays", r'''
# LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
# https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
  calc = lambda do |a1, a2|
    n = a1.length
    ops = 0
    last1 = a1[n - 1]
    last2 = a2[n - 1]
    (0...n - 1).each do |i|
      x = a1[i]
      y = a2[i]
      next if x <= last1 && y <= last2
      if y <= last1 && x <= last2
        ops += 1
        next
      end
      return 1 << 30
    end
    ops
  end

  n = nums1.length
  ans = calc.call(nums1, nums2)
  t = nums1[n - 1]
  nums1[n - 1] = nums2[n - 1]
  nums2[n - 1] = t
  cand = calc.call(nums1, nums2) + 1
  ans = cand if cand < ans
  nums2[n - 1] = nums1[n - 1]
  nums1[n - 1] = t
  ans >= (1 << 30) ? -1 : ans
end
''')

add("2935_maximum_strong_pair_xor_ii", r'''
# LeetCode 2935 - Maximum Strong Pair XOR II
# https://leetcode.com/problems/maximum-strong-pair-xor-ii/

# @param {Integer[]} nums
# @return {Integer}
def maximum_strong_pair_xor(nums)
  nums = nums.sort
  ans = 0
  nums.each_with_index do |x, i|
    j = i
    while j < nums.length && nums[j] <= 2 * x
      xorr = x ^ nums[j]
      ans = xorr if xorr > ans
      j += 1
    end
  end
  ans
end
''')

add("2936_number_of_equal_numbers_blocks", r'''
# LeetCode 2936 - Number of Equal Numbers Blocks
# https://leetcode.com/problems/number-of-equal-numbers-blocks/

# @param {Integer[]} nums
# @return {Integer}
def block_count(nums)
  return 0 if nums.empty?

  ans = 1
  (1...nums.length).each { |i| ans += 1 if nums[i] != nums[i - 1] }
  ans
end
''')


def main() -> None:
    written = 0
    missing = []
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        if not path.parent.exists():
            missing.append(name)
            continue
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
    print(f"wrote={written} missing={missing}")


if __name__ == "__main__":
    main()
