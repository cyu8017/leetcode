#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3285_find_indices_of_stable_mountains", r'''
# LeetCode 3285 - Find Indices of Stable Mountains
# https://leetcode.com/problems/find-indices-of-stable-mountains/

# @param {Integer[]} height
# @param {Integer} threshold
# @return {Integer[]}
def stable_mountains(height, threshold)
  ans = []
  (1...height.length).each do |i|
    ans << i if height[i - 1] > threshold
  end
  ans
end
''')

add("3286_find_a_safe_walk_through_a_grid", r'''
# LeetCode 3286 - Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

# @param {Integer[][]} grid
# @param {Integer} health
# @return {Boolean}
def find_safe_walk(grid, health)
  m = grid.length
  n = grid[0].length
  vis = Array.new(m) { Array.new(n, -1) }
  qh = health - grid[0][0]
  return false if qh <= 0

  q = [[0, 0, qh]]
  vis[0][0] = qh
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until q.empty?
    cur = q.shift
    return true if cur[0] == m - 1 && cur[1] == n - 1

    dirs.each do |d|
      nr = cur[0] + d[0]
      nc = cur[1] + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      nh = cur[2] - grid[nr][nc]
      next if nh <= 0

      if nh > vis[nr][nc]
        vis[nr][nc] = nh
        q << [nr, nc, nh]
      end
    end
  end
  false
end
''')

add("3287_find_the_maximum_sequence_value_of_array", r'''
# LeetCode 3287 - Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_value(nums, k)
  n = nums.length
  maxv = 128
  left = Array.new(n + 1) { Array.new(k + 1) { Array.new(maxv, false) } }
  left[0][0][0] = true
  n.times do |i|
    (0..k).each do |j|
      maxv.times do |v|
        next unless left[i][j][v]

        left[i + 1][j][v] = true
        left[i + 1][j + 1][v | nums[i]] = true if j < k
      end
    end
  end
  right = Array.new(n + 1) { Array.new(k + 1) { Array.new(maxv, false) } }
  right[n][0][0] = true
  (n - 1).downto(0) do |i|
    (0..k).each do |j|
      maxv.times do |v|
        next unless right[i + 1][j][v]

        right[i][j][v] = true
        right[i][j + 1][v | nums[i]] = true if j < k
      end
    end
  end
  ans = 0
  (k..(n - k)).each do |mid|
    maxv.times do |a|
      next unless left[mid][k][a]

      maxv.times do |b|
        ans = a ^ b if right[mid][k][b] && (a ^ b) > ans
      end
    end
  end
  ans
end
''')

add("3288_length_of_the_longest_increasing_path", r'''
# LeetCode 3288 - Length of the Longest Increasing Path
# https://leetcode.com/problems/length-of-the-longest-increasing-path/

# @param {Integer[]} a
# @return {Integer}
def lis(a)
  tails = []
  a.each do |x|
    lo = 0
    hi = tails.length
    while lo < hi
      mid = (lo + hi) >> 1
      if tails[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == tails.length
      tails << x
    else
      tails[lo] = x
    end
  end
  tails.length
end

# @param {Integer[][]} coordinates
# @param {Integer} k
# @return {Integer}
def max_path_length(coordinates, k)
  n = coordinates.length
  arr = n.times.map { |i| [coordinates[i][0], coordinates[i][1], i] }
  arr.sort_by! { |a| [a[0], -a[1]] }
  kx = coordinates[k][0]
  ky = coordinates[k][1]
  left = []
  right = []
  arr.each do |p|
    left << p[1] if p[0] < kx && p[1] < ky
    right << p[1] if p[0] > kx && p[1] > ky
  end
  lis(left) + 1 + lis(right)
end
''')

add("3289_the_two_sneaky_numbers_of_digitville", r'''
# LeetCode 3289 - The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

# @param {Integer[]} nums
# @return {Integer[]}
def get_sneaky_numbers(nums)
  seen = {}
  ans = []
  nums.each do |x|
    if seen[x]
      ans << x
    else
      seen[x] = true
    end
  end
  ans
end
''')

add("3290_maximum_multiplication_score", r'''
# LeetCode 3290 - Maximum Multiplication Score
# https://leetcode.com/problems/maximum-multiplication-score/

# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def max_score(a, b)
  neg = -(1 << 62)
  dp = [0, neg, neg, neg, neg]
  b.each do |x|
    4.downto(1) do |k|
      next if dp[k - 1] == neg

      v = dp[k - 1] + a[k - 1] * x
      dp[k] = v if v > dp[k]
    end
  end
  dp[4]
end
''')

add("3291_minimum_number_of_valid_strings_to_form_target_i", r'''
# LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

# @param {String[]} words
# @param {String} target
# @return {Integer}
def min_valid_strings(words, target)
  n = target.length
  inf = 1_000_000_000
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  root = { next: Array.new(26) }
  words.each do |w|
    cur = root
    w.each_char do |c|
      ci = c.ord - 97
      cur[:next][ci] ||= { next: Array.new(26) }
      cur = cur[:next][ci]
    end
  end
  n.times do |i|
    next if dp[i] == inf

    cur = root
    (i...n).each do |j|
      ci = target[j].ord - 97
      break unless cur[:next][ci]

      cur = cur[:next][ci]
      dp[j + 1] = dp[i] + 1 if dp[i] + 1 < dp[j + 1]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
''')

add("3292_minimum_number_of_valid_strings_to_form_target_ii", r'''
# LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

# @param {String[]} words
# @param {String} target
# @return {Integer}
def min_valid_strings(words, target)
  n = target.length
  inf = 1_000_000_000
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  root = { next: Array.new(26) }
  words.each do |w|
    cur = root
    w.each_char do |c|
      ci = c.ord - 97
      cur[:next][ci] ||= { next: Array.new(26) }
      cur = cur[:next][ci]
    end
  end
  n.times do |i|
    next if dp[i] == inf

    cur = root
    (i...n).each do |j|
      ci = target[j].ord - 97
      break unless cur[:next][ci]

      cur = cur[:next][ci]
      dp[j + 1] = dp[i] + 1 if dp[i] + 1 < dp[j + 1]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
''')

add("3294_convert_doubly_linked_list_to_array_ii", r'''
# LeetCode 3294 - Convert Doubly Linked List to Array II
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node
  attr_accessor :val, :prev, :next

  def initialize(val = 0, prev = nil, nxt = nil)
    @val = val
    @prev = prev
    @next = nxt
  end
end

# @param {Node} node
# @return {Integer[]}
def to_array(node)
  node = node.prev while !node.nil? && !node.prev.nil?
  ans = []
  until node.nil?
    ans << node.val
    node = node.next
  end
  ans
end
''')

add("3295_report_spam_message", r'''
# LeetCode 3295 - Report Spam Message
# https://leetcode.com/problems/report-spam-message/

# @param {String[]} message
# @param {String[]} banned_words
# @return {Boolean}
def report_spam(message, banned_words)
  ban = {}
  banned_words.each { |w| ban[w] = true }
  cnt = 0
  message.each do |w|
    if ban[w]
      cnt += 1
      return true if cnt >= 2
    end
  end
  false
end
''')

add("3296_minimum_number_of_seconds_to_make_mountain_height_zero", r'''
# LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

# @param {Integer} t
# @param {Integer} mountain_height
# @param {Integer[]} worker_times
# @return {Boolean}
def mountain_seconds_ok(t, mountain_height, worker_times)
  total = 0
  worker_times.each do |w|
    l = 0
    h = mountain_height
    while l < h
      mid = (l + h + 1) / 2
      if w * mid * (mid + 1) / 2 <= t
        l = mid
      else
        h = mid - 1
      end
    end
    total += l
    return true if total >= mountain_height
  end
  total >= mountain_height
end

# @param {Integer} mountain_height
# @param {Integer[]} worker_times
# @return {Integer}
def min_number_of_seconds(mountain_height, worker_times)
  lo = 0
  hi = 10**18
  while lo < hi
    mid = (lo + hi) / 2
    if mountain_seconds_ok(mid, mountain_height, worker_times)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3297_count_substrings_that_can_be_rearranged_to_contain_a_string_i", r'''
# LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def valid_substring_count(word1, word2)
  need = Array.new(26, 0)
  required = 0
  word2.each_char do |c|
    i = c.ord - 97
    required += 1 if need[i] == 0
    need[i] += 1
  end
  have = Array.new(26, 0)
  formed = 0
  ans = 0
  l = 0
  word1.length.times do |r|
    c = word1[r].ord - 97
    have[c] += 1
    formed += 1 if have[c] == need[c] && need[c] > 0
    while formed == required && l <= r
      ans += word1.length - r
      c2 = word1[l].ord - 97
      formed -= 1 if have[c2] == need[c2] && need[c2] > 0
      have[c2] -= 1
      l += 1
    end
  end
  ans
end
''')

add("3298_count_substrings_that_can_be_rearranged_to_contain_a_string_ii", r'''
# LeetCode 3298 - Count Substrings That Can Be Rearranged to Contain a String II
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def valid_substring_count(word1, word2)
  need = Array.new(26, 0)
  required = 0
  word2.each_char do |c|
    i = c.ord - 97
    required += 1 if need[i] == 0
    need[i] += 1
  end
  have = Array.new(26, 0)
  formed = 0
  ans = 0
  l = 0
  word1.length.times do |r|
    c = word1[r].ord - 97
    have[c] += 1
    formed += 1 if have[c] == need[c] && need[c] > 0
    while formed == required && l <= r
      ans += word1.length - r
      c2 = word1[l].ord - 97
      formed -= 1 if have[c2] == need[c2] && need[c2] > 0
      have[c2] -= 1
      l += 1
    end
  end
  ans
end
''')

add("3299_sum_of_consecutive_subsequences", r'''
# LeetCode 3299 - Sum of Consecutive Subsequences
# https://leetcode.com/problems/sum-of-consecutive-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def range_sum(nums)
  mod = 1_000_000_007
  cnt = {}
  sm = {}
  ans = 0
  nums.each do |x|
    cl = cnt[x - 1] || 0
    sl = sm[x - 1] || 0
    cr = cnt[x + 1] || 0
    sr = sm[x + 1] || 0
    c = (1 + cl + cr) % mod
    s = (x + sl + (cl * x % mod) + sr + (cr * x % mod)) % mod
    if cl > 0 && cr > 0
      c = (c + (cl * cr % mod)) % mod
      s = (s + (sl * cr % mod) + (sr * cl % mod) + (cl * cr % mod * x % mod)) % mod
    end
    cnt[x] = ((cnt[x] || 0) + c) % mod
    sm[x] = ((sm[x] || 0) + s) % mod
    ans = (ans + s) % mod
  end
  ans
end
''')

add("3300_minimum_element_after_replacement_with_digit_sum", r'''
# LeetCode 3300 - Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

# @param {Integer[]} nums
# @return {Integer}
def min_element(nums)
  ans = 1_000_000_000
  nums.each do |num|
    x = num
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    ans = s if s < ans
  end
  ans
end
''')

add("3301_maximize_the_total_height_of_unique_towers", r'''
# LeetCode 3301 - Maximize the Total Height of Unique Towers
# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

# @param {Integer[]} maximum_height
# @return {Integer}
def maximum_total_sum(maximum_height)
  maximum_height.sort!.reverse!
  ans = 0
  prev = 10**18
  maximum_height.each do |h|
    cur = h
    cur = prev - 1 if cur >= prev
    return -1 if cur <= 0

    ans += cur
    prev = cur
  end
  ans
end
''')

add("3302_find_the_lexicographically_smallest_valid_sequence", r'''
# LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

# @param {String} w1
# @param {String} w2
# @param {Integer} i
# @param {Integer} j
# @param {Boolean} used_skip
# @param {Integer[]} right
# @return {Boolean}
def can_finish_valid_sequence(w1, w2, i, j, used_skip, right)
  m = w2.length
  return true if j >= m
  unless used_skip
    return true if right[j] >= i
    return true if j + 1 <= m && right[j + 1] > i
    return true if right[j] > i

    return false
  end
  right[j] >= i
end

# @param {String} word1
# @param {String} word2
# @return {Integer[]}
def valid_sequence(word1, word2)
  n = word1.length
  m = word2.length
  right = Array.new(m + 1, 0)
  right[m] = n
  j = m - 1
  i = n - 1
  while i >= 0 && j >= 0
    if word1[i] == word2[j]
      right[j] = i
      j -= 1
    end
    i -= 1
  end
  while j >= 0
    right[j] = -1
    j -= 1
  end
  ans = Array.new(m, 0)
  used_skip = false
  i = 0
  m.times do |jj|
    found = false
    while i < n
      if word1[i] == word2[jj]
        if can_finish_valid_sequence(word1, word2, i + 1, jj + 1, used_skip, right)
          ans[jj] = i
          i += 1
          found = true
          break
        end
      elsif !used_skip
        if can_finish_valid_sequence(word1, word2, i + 1, jj + 1, true, right)
          ans[jj] = i
          i += 1
          used_skip = true
          found = true
          break
        end
      end
      i += 1
    end
    return [] unless found
  end
  ans
end
''')

add("3303_find_the_occurrence_of_first_almost_equal_substring", r'''
# LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

# @param {String} s
# @param {String} pattern
# @return {Integer}
def min_starting_index(s, pattern)
  n = s.length
  m = pattern.length
  (0..(n - m)).each do |i|
    diff = 0
    m.times do |j|
      if s[i + j] != pattern[j]
        diff += 1
        break if diff > 1
      end
    end
    return i if diff <= 1
  end
  -1
end
''')

add("3304_find_the_k_th_character_in_string_game_i", r'''
# LeetCode 3304 - Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

# @param {Integer} k
# @return {Character}
def kth_character(k)
  s = "a"
  while s.length < k
    n = s.length
    add = ""
    n.times do |i|
      add << (97 + ((s[i].ord - 97 + 1) % 26)).chr
    end
    s += add
  end
  s[k - 1]
end
''')

add("3305_count_of_substrings_containing_every_vowel_and_k_consonants_i", r'''
# LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

# @param {String} c
# @return {Boolean}
def vowel_char?(c)
  c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def at_least_vowel_consonant(word, k)
  cnt = {}
  cons = 0
  l = 0
  ans = 0
  word.length.times do |r|
    c = word[r]
    if vowel_char?(c)
      cnt[c] = (cnt[c] || 0) + 1
    else
      cons += 1
    end
    while cnt.length == 5 && cons >= k
      ans += word.length - r
      c2 = word[l]
      if vowel_char?(c2)
        nv = cnt[c2] - 1
        if nv == 0
          cnt.delete(c2)
        else
          cnt[c2] = nv
        end
      else
        cons -= 1
      end
      l += 1
    end
  end
  ans
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_of_substrings(word, k)
  at_least_vowel_consonant(word, k) - at_least_vowel_consonant(word, k + 1)
end
''')

add("3306_count_of_substrings_containing_every_vowel_and_k_consonants_ii", r'''
# LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

# @param {String} c
# @return {Boolean}
def vowel_char?(c)
  c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def at_least_vowel_consonant(word, k)
  cnt = {}
  cons = 0
  l = 0
  ans = 0
  word.length.times do |r|
    c = word[r]
    if vowel_char?(c)
      cnt[c] = (cnt[c] || 0) + 1
    else
      cons += 1
    end
    while cnt.length == 5 && cons >= k
      ans += word.length - r
      c2 = word[l]
      if vowel_char?(c2)
        nv = cnt[c2] - 1
        if nv == 0
          cnt.delete(c2)
        else
          cnt[c2] = nv
        end
      else
        cons -= 1
      end
      l += 1
    end
  end
  ans
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_of_substrings(word, k)
  at_least_vowel_consonant(word, k) - at_least_vowel_consonant(word, k + 1)
end
''')

add("3307_find_the_k_th_character_in_string_game_ii", r'''
# LeetCode 3307 - Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

# @param {Integer} k
# @param {Integer[]} operations
# @return {Character}
def kth_character(k, operations)
  shift = 0
  ops = operations.dup
  until ops.empty?
    op = ops.pop
    half = 1 << ops.length
    if k > half
      k -= half
      shift += 1 if op == 1
    end
  end
  (97 + (shift % 26)).chr
end
''')

add("3309_maximum_possible_number_by_binary_concatenation", r'''
# LeetCode 3309 - Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

# @param {Integer} x
# @return {String}
def to_bin_str(x)
  return "0" if x == 0

  s = ""
  while x > 0
    s = (x & 1).to_s + s
    x >>= 1
  end
  s
end

# @param {Integer} i
# @param {Integer[]} idx
# @param {String[]} bs
# @param {Integer[]} ans
# @return {void}
def perm_bin_concat(i, idx, bs, ans)
  if i == 3
    s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
    v = 0
    s.each_char { |c| v = v * 2 + (c.ord - 48) }
    ans[0] = v if v > ans[0]
    return
  end
  (i...3).each do |j|
    idx[i], idx[j] = idx[j], idx[i]
    perm_bin_concat(i + 1, idx, bs, ans)
    idx[i], idx[j] = idx[j], idx[i]
  end
end

# @param {Integer[]} nums
# @return {Integer}
def max_good_number(nums)
  bs = [to_bin_str(nums[0]), to_bin_str(nums[1]), to_bin_str(nums[2])]
  idx = [0, 1, 2]
  ans = [0]
  perm_bin_concat(0, idx, bs, ans)
  ans[0]
end
''')

add("3310_remove_methods_from_project", r'''
# LeetCode 3310 - Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} invocations
# @return {Integer[]}
def remaining_methods(n, k, invocations)
  g = Array.new(n) { [] }
  invocations.each { |e| g[e[0]] << e[1] }
  sus = Array.new(n, false)
  stack = [k]
  until stack.empty?
    u = stack.pop
    next if sus[u]

    sus[u] = true
    g[u].each { |v| stack << v }
  end
  invocations.each do |e|
    return (0...n).to_a if !sus[e[0]] && sus[e[1]]
  end
  (0...n).select { |i| !sus[i] }
end
''')

add("3311_construct_2d_grid_matching_graph_layout", r'''
# LeetCode 3311 - Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def construct_grid_layout(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  deg = n.times.map { |i| g[i].length }
  start = 0
  n.times do |i|
    if deg[i] == 1
      start = i
      break
    end
    start = i if deg[i] == 2
  end
  vis = Array.new(n, false)
  row = []
  cur = start
  prev = -1
  loop do
    row << cur
    vis[cur] = true
    nxt = -1
    g[cur].each do |v|
      next unless v != prev && !vis[v] && deg[v] <= 3

      nxt = v
      break if deg[v] < 4
    end
    break if nxt == -1

    prev = cur
    cur = nxt
  end
  width = row.length
  height = width != 0 ? n / width : n
  if width == 0 || width * height != n
    (1..n).each do |w|
      next unless n % w == 0

      width = w
      height = n / w
      break
    end
  end
  grid = Array.new(height) { Array.new(width, 0) }
  n.times { |i| grid[i / width][i % width] = i }
  grid
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
print(f"batch16_a written={written} failed={failed}")
print("keys", len(S))
