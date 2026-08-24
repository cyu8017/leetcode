#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3312_sorted_gcd_pair_queries", r'''
# LeetCode 3312 - Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def gcd_values(nums, queries)
  max_v = nums.max
  cnt = Array.new(max_v + 1, 0)
  nums.each { |x| cnt[x] += 1 }
  div_cnt = Array.new(max_v + 1, 0)
  (1..max_v).each do |g|
    c = 0
    m = g
    while m <= max_v
      c += cnt[m]
      m += g
    end
    div_cnt[g] = c * (c - 1) / 2
  end
  exact = Array.new(max_v + 1, 0)
  max_v.downto(1) do |g|
    exact[g] = div_cnt[g]
    m = 2 * g
    while m <= max_v
      exact[g] -= exact[m]
      m += g
    end
  end
  pref = Array.new(max_v + 1, 0)
  (1..max_v).each { |g| pref[g] = pref[g - 1] + exact[g] }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 1
    hi = max_v
    while lo < hi
      mid = (lo + hi) >> 1
      if pref[mid] > q
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans[i] = lo
  end
  ans
end
''')

add("3313_find_the_last_marked_nodes_in_tree", r'''
# LeetCode 3313 - Find the Last Marked Nodes in Tree
# https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

# @param {Integer[][]} g
# @param {Integer} start
# @return {Array}
def last_marked_bfs(g, start)
  n = g.length
  dist = Array.new(n, -1)
  q = [start]
  dist[start] = 0
  far = start
  qi = 0
  while qi < q.length
    u = q[qi]
    qi += 1
    far = u if dist[u] > dist[far]
    g[u].each do |v|
      if dist[v] == -1
        dist[v] = dist[u] + 1
        q << v
      end
    end
  end
  [far, dist]
end

# @param {Integer[][]} edges
# @return {Integer[]}
def last_marked_nodes(edges)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  u = last_marked_bfs(g, 0)[0]
  v, du = last_marked_bfs(g, u)
  dv = last_marked_bfs(g, v)[1]
  n.times.map { |i| du[i] >= dv[i] ? u : v }
end
''')

add("3314_construct_the_minimum_bitwise_array_i", r'''
# LeetCode 3314 - Construct the Minimum Bitwise Array I
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
  ans = Array.new(nums.length, -1)
  nums.each_with_index do |n, i|
    n.times do |x|
      if (x | (x + 1)) == n
        ans[i] = x
        break
      end
    end
  end
  ans
end
''')

add("3315_construct_the_minimum_bitwise_array_ii", r'''
# LeetCode 3315 - Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
  ans = Array.new(nums.length, -1)
  nums.each_with_index do |n, i|
    next if n == 2

    31.times do |b|
      next if ((n >> b) & 1) == 0

      x = n ^ (1 << b)
      if (x | (x + 1)) == n
        ans[i] = x
        break
      end
    end
  end
  ans
end
''')

add("3316_find_maximum_removals_from_source_string", r'''
# LeetCode 3316 - Find Maximum Removals From Source String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/

# @param {Integer} remove_first
# @param {String} source
# @param {String} pattern
# @param {Integer[]} target_indices
# @param {Integer} n
# @return {Boolean}
def removals_ok(remove_first, source, pattern, target_indices, n)
  mark = Array.new(n, false)
  remove_first.times { |i| mark[target_indices[i]] = true }
  j = 0
  i = 0
  while i < n && j < pattern.length
    j += 1 if !mark[i] && source[i] == pattern[j]
    i += 1
  end
  j == pattern.length
end

# @param {String} source
# @param {String} pattern
# @param {Integer[]} target_indices
# @return {Integer}
def max_removals(source, pattern, target_indices)
  n = source.length
  lo = 0
  hi = target_indices.length
  while lo < hi
    mid = (lo + hi + 1) >> 1
    if removals_ok(mid, source, pattern, target_indices, n)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("3317_find_the_number_of_possible_ways_for_an_event", r'''
# LeetCode 3317 - Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

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

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def number_of_ways(n, x, y)
  mod = 1_000_000_007
  dp = Array.new(n + 1) { Array.new(x + 1, 0) }
  dp[0][0] = 1
  (1..n).each do |i|
    (1..[x, i].min).each do |j|
      dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
    end
  end
  fact = Array.new(x + 1, 0)
  fact[0] = 1
  (1..x).each { |i| fact[i] = fact[i - 1] * i % mod }
  ans = 0
  ypow = 1
  (1..[x, n].min).each do |k|
    ypow = ypow * y % mod
    perm = fact[x] * mod_pow(fact[x - k], mod - 2, mod) % mod
    ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
  end
  ans
end
''')

add("3318_find_x_sum_of_all_k_long_subarrays_i", r'''
# LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  (0..(n - k)).each do |i|
    freq = {}
    (i...(i + k)).each { |j| freq[nums[j]] = (freq[nums[j]] || 0) + 1 }
    arr = freq.map { |key, val| [key, val] }
    arr.sort_by! { |a| [-a[1], -a[0]] }
    lim = [x, arr.length].min
    keep = {}
    lim.times { |t| keep[arr[t][0]] = true }
    s = 0
    (i...(i + k)).each { |j| s += nums[j] if keep[nums[j]] }
    ans[i] = s
  end
  ans
end
''')

add("3319_k_th_largest_perfect_subtree_size_in_binary_tree", r'''
# LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_largest_perfect_subtree(root, k)
  sizes = []
  dfs = lambda do |node|
    return [0, 0, 1] if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    sz = left[1] + right[1] + 1
    perf = left[2] == 1 && right[2] == 1 && left[0] == right[0]
    sizes << sz if perf
    [[left[0], right[0]].max + 1, sz, perf ? 1 : 0]
  end
  dfs.call(root)
  sizes.sort!.reverse!
  return -1 if k > sizes.length

  sizes[k - 1]
end
''')

add("3320_count_the_number_of_winning_sequences", r'''
# LeetCode 3320 - Count the Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/

# @param {String} s
# @return {Integer}
def count_winning_sequences(s)
  mod = 1_000_000_007
  n = s.length
  mp = { "F" => 0, "W" => 1, "E" => 2 }
  beat = [2, 0, 1]
  score = Array.new(3) { Array.new(3, 0) }
  3.times do |a|
    3.times do |b|
      score[a][b] = if a == b
                      0
                    elsif beat[a] == b
                      1
                    else
                      -1
                    end
    end
  end
  offset = n
  dp = Array.new(3) { Array.new(2 * n + 1, 0) }
  b0 = mp[s[0]]
  3.times { |a| dp[a][score[a][b0] + offset] = 1 }
  (1...n).each do |i|
    ndp = Array.new(3) { Array.new(2 * n + 1, 0) }
    b = mp[s[i]]
    3.times do |last|
      (0..(2 * n)).each do |d|
        next if dp[last][d] == 0

        3.times do |a|
          next if a == last

          nd = d + score[a][b]
          next if nd < 0 || nd > 2 * n

          ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
        end
      end
    end
    dp = ndp
  end
  ans = 0
  3.times do |a|
    ((offset + 1)..(2 * n)).each { |d| ans = (ans + dp[a][d]) % mod }
  end
  ans
end
''')

add("3321_find_x_sum_of_all_k_long_subarrays_ii", r'''
# LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  (0..(n - k)).each do |i|
    freq = {}
    (i...(i + k)).each { |j| freq[nums[j]] = (freq[nums[j]] || 0) + 1 }
    arr = freq.map { |key, val| [key, val] }
    arr.sort_by! { |a| [-a[1], -a[0]] }
    lim = [x, arr.length].min
    keep = {}
    lim.times { |t| keep[arr[t][0]] = true }
    s = 0
    (i...(i + k)).each { |j| s += nums[j] if keep[nums[j]] }
    ans[i] = s
  end
  ans
end
''')

add("3323_minimize_connected_groups_by_inserting_interval", r'''
# LeetCode 3323 - Minimize Connected Groups by Inserting Interval
# https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

# @param {Integer[][]} intervals
# @param {Integer} k
# @return {Integer}
def min_connected_groups(intervals, k)
  intervals.sort_by! { |a| a[0] }
  merged = []
  intervals.each do |it|
    if merged.empty? || it[0] > merged[-1][1]
      merged << [it[0], it[1]]
    elsif it[1] > merged[-1][1]
      merged[-1][1] = it[1]
    end
  end
  m = merged.length
  ans = m
  m.times do |i|
    endv = merged[i][1] + k
    j = i
    j += 1 while j < m && merged[j][0] <= endv
    groups = i + 1 + (m - j)
    ans = groups if groups < ans
  end
  ans
end
''')

add("3324_find_the_sequence_of_strings_appeared_on_the_screen", r'''
# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

# @param {String} target
# @return {String[]}
def string_sequence(target)
  ans = []
  cur = ""
  target.each_char do |ch|
    cur += "a"
    ans << cur
    while cur[-1] != ch
      last = (cur[-1].ord + 1).chr
      cur = cur[0...-1] + last
      ans << cur
    end
  end
  ans
end
''')

add("3325_count_substrings_with_k_frequency_characters_i", r'''
# LeetCode 3325 - Count Substrings With K-Frequency Characters I
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def number_of_substrings(s, k)
  n = s.length
  ans = 0
  n.times do |i|
    freq = Array.new(26, 0)
    (i...n).each do |j|
      freq[s[j].ord - 97] += 1
      if freq.any? { |f| f >= k }
        ans += n - j
        break
      end
    end
  end
  ans
end
''')

add("3326_minimum_division_operations_to_make_array_non_decreasing", r'''
# LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

# @param {Integer} x
# @return {Integer}
def smallest_proper_divisor(x)
  d = 2
  while d * d <= x
    return d if x % d == 0

    d += 1
  end
  x
end

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ops = 0
  (nums.length - 2).downto(0) do |i|
    next if nums[i] <= nums[i + 1]

    while nums[i] > nums[i + 1]
      d = smallest_proper_divisor(nums[i])
      return -1 if d == nums[i]

      nums[i] = nums[i] / d
      ops += 1
      return -1 if nums[i] > nums[i + 1] && smallest_proper_divisor(nums[i]) == nums[i]
    end
  end
  ops
end
''')

add("3327_check_if_dfs_strings_are_palindromes", r'''
# LeetCode 3327 - Check DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

# @param {String} t
# @return {Boolean}
def palindrome_str?(t)
  i = 0
  j = t.length - 1
  while i < j
    return false if t[i] != t[j]

    i += 1
    j -= 1
  end
  true
end

# @param {Integer[]} parent
# @param {String} s
# @return {Boolean[]}
def find_answer(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  ans = Array.new(n, false)
  dfs_str = lambda do |u|
    out = ""
    g[u].each { |v| out += dfs_str.call(v) }
    out += s[u]
    ans[u] = palindrome_str?(out)
    out
  end
  dfs_str.call(0)
  ans
end
''')

add("3329_count_substrings_with_k_frequency_characters_ii", r'''
# LeetCode 3329 - Count Substrings With K-Frequency Characters II
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def number_of_substrings(s, k)
  n = s.length
  ans = 0
  n.times do |i|
    freq = Array.new(26, 0)
    (i...n).each do |j|
      freq[s[j].ord - 97] += 1
      if freq.any? { |f| f >= k }
        ans += n - j
        break
      end
    end
  end
  ans
end
''')

add("3330_find_the_original_typed_string_i", r'''
# LeetCode 3330 - Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/

# @param {String} word
# @return {Integer}
def possible_string_count(word)
  ans = 1
  (1...word.length).each { |i| ans += 1 if word[i] == word[i - 1] }
  ans
end
''')

add("3331_find_subtree_sizes_after_changes", r'''
# LeetCode 3331 - Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/

# @param {Integer[]} parent
# @param {String} s
# @return {Integer[]}
def find_subtree_sizes(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  new_parent = parent.dup
  last = Array.new(26, -1)
  dfs1 = lambda do |u|
    c = s[u].ord - 97
    prev = last[c]
    new_parent[u] = prev if prev != -1
    last[c] = u
    g[u].each { |v| dfs1.call(v) }
    last[c] = prev
  end
  dfs1.call(0)
  ng = Array.new(n) { [] }
  (1...n).each { |i| ng[new_parent[i]] << i }
  ans = Array.new(n, 0)
  dfs2 = lambda do |u|
    sz = 1
    ng[u].each { |v| sz += dfs2.call(v) }
    ans[u] = sz
    sz
  end
  dfs2.call(0)
  ans
end
''')

add("3332_maximum_points_tourist_can_earn", r'''
# LeetCode 3332 - Maximum Points Tourist Can Earn
# https://leetcode.com/problems/maximum-points-tourist-can-earn/

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} stay_score
# @param {Integer[][]} travel_score
# @return {Integer}
def max_score(n, k, stay_score, travel_score)
  dp = Array.new(n, 0)
  k.times do |day|
    ndp = Array.new(n, -(1 << 30))
    n.times do |dest|
      best = -(1 << 30)
      n.times do |src|
        val = dp[src]
        val += src == dest ? stay_score[day][dest] : travel_score[src][dest]
        best = val if val > best
      end
      ndp[dest] = best
    end
    dp = ndp
  end
  ans = dp[0]
  (1...n).each { |i| ans = dp[i] if dp[i] > ans }
  ans
end
''')

add("3333_find_the_original_typed_string_ii", r'''
# LeetCode 3333 - Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def possible_string_count(word, k)
  mod = 1_000_000_007
  groups = []
  i = 0
  while i < word.length
    j = i
    j += 1 while j < word.length && word[j] == word[i]
    groups << (j - i)
    i = j
  end
  total = 1
  groups.each { |g| total = total * g % mod }
  return total if k <= groups.length

  need = k - 1
  dp = Array.new(need, 0)
  dp[0] = 1
  groups.each do |g|
    ndp = Array.new(need, 0)
    pref = Array.new(need + 1, 0)
    need.times { |ii| pref[ii + 1] = (pref[ii] + dp[ii]) % mod }
    need.times do |s|
      lo = s - g
      lo = 0 if lo < 0
      hi = s - 1
      ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod if hi >= 0
    end
    dp = ndp
  end
  bad = 0
  dp.each { |v| bad = (bad + v) % mod }
  (total - bad + mod) % mod
end
''')

add("3334_find_the_maximum_factor_score_of_array", r'''
# LeetCode 3334 - Find the Maximum Factor Score of Array
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def lcm_int(a, b)
  a / gcd_int(a, b) * b
end

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  n = nums.length
  gcd_all = nums[0]
  lcm_all = nums[0]
  (1...n).each do |i|
    gcd_all = gcd_int(gcd_all, nums[i])
    lcm_all = lcm_int(lcm_all, nums[i])
  end
  ans = gcd_all * lcm_all
  n.times do |skip|
    g = 0
    l = 1
    first = true
    n.times do |i|
      next if i == skip

      if first
        g = l = nums[i]
        first = false
      else
        g = gcd_int(g, nums[i])
        l = lcm_int(l, nums[i])
      end
    end
    next if first

    v = g * l
    ans = v if v > ans
  end
  ans
end
''')

add("3335_total_characters_in_string_after_transformations_i", r'''
# LeetCode 3335 - Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

# @param {String} s
# @param {Integer} t
# @return {Integer}
def length_after_transformations(s, t)
  mod = 1_000_000_007
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  t.times do
    ncnt = Array.new(26, 0)
    25.times { |i| ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod }
    ncnt[0] = (ncnt[0] + cnt[25]) % mod
    ncnt[1] = (ncnt[1] + cnt[25]) % mod
    cnt = ncnt
  end
  ans = 0
  cnt.each { |v| ans = (ans + v) % mod }
  ans
end
''')

add("3336_find_the_number_of_subsequences_with_equal_gcd", r'''
# LeetCode 3336 - Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  return b if a == 0

  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[]} nums
# @return {Integer}
def subsequence_pair_count(nums)
  mod = 1_000_000_007
  max_v = nums.max
  dp = Array.new(max_v + 1) { Array.new(max_v + 1, 0) }
  dp[0][0] = 1
  nums.each do |x|
    ndp = Array.new(max_v + 1) { Array.new(max_v + 1, 0) }
    (0..max_v).each do |a|
      (0..max_v).each { |b| ndp[a][b] = dp[a][b] }
    end
    (0..max_v).each do |a|
      (0..max_v).each do |b|
        next if dp[a][b] == 0

        na = a == 0 ? x : gcd_int(a, x)
        nb = b == 0 ? x : gcd_int(b, x)
        ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
        ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
      end
    end
    dp = ndp
  end
  ans = 0
  (1..max_v).each { |g| ans = (ans + dp[g][g]) % mod }
  ans
end
''')

add("3337_total_characters_in_string_after_transformations_ii", r'''
# LeetCode 3337 - Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

# @param {Integer[][]} a
# @param {Integer[][]} b
# @param {Integer} mod
# @return {Integer[][]}
def mat_mul(a, b, mod)
  n = a.length
  c = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    n.times do |k|
      next if a[i][k] == 0

      n.times { |j| c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod }
    end
  end
  c
end

# @param {Integer[][]} a
# @param {Integer} e
# @param {Integer} mod
# @return {Integer[][]}
def mat_pow(a, e, mod)
  n = a.length
  r = Array.new(n) { Array.new(n, 0) }
  n.times { |i| r[i][i] = 1 }
  while e > 0
    r = mat_mul(r, a, mod) if (e & 1) != 0
    a = mat_mul(a, a, mod)
    e >>= 1
  end
  r
end

# @param {String} s
# @param {Integer} t
# @param {Integer[]} nums
# @return {Integer}
def length_after_transformations(s, t, nums)
  mod = 1_000_000_007
  mat = Array.new(26) { Array.new(26, 0) }
  26.times do |i|
    (1..nums[i]).each { |j| mat[i][(i + j) % 26] = 1 }
  end
  mat = mat_pow(mat, t, mod)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  ans = 0
  26.times do |i|
    26.times { |j| ans = (ans + cnt[i] * mat[i][j] % mod) % mod }
  end
  ans
end
''')

add("3339_find_the_number_of_k_even_arrays", r'''
# LeetCode 3339 - Find the Number of K-Even Arrays
# https://leetcode.com/problems/find-the-number-of-k-even-arrays/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def count_of_arrays(n, m, k)
  mod = 1_000_000_007
  even = m / 2
  odd = m - even
  dp = Array.new(n + 1) { Array.new(k + 1) { [0, 0] } }
  dp[1][0][0] = odd
  dp[1][0][1] = even
  (1...n).each do |i|
    (0..k).each do |j|
      dp[i + 1][j][0] = (dp[i + 1][j][0] + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod) % mod
      dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
      if j < k
        dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod) % mod
      end
    end
  end
  (dp[n][k][0] + dp[n][k][1]) % mod
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
print(f"batch16_b written={written} failed={failed}")
print("keys", len(S))
