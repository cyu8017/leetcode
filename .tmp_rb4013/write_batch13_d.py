#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3025_find_the_number_of_ways_to_place_people_i", r'''
# LeetCode 3025 - Find the Number of Ways to Place People I
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

# @param {Integer[][]} points
# @return {Integer}
def number_of_pairs(points)
  points.sort_by! { |a| [a[0], -a[1]] }
  ans = 0
  points.length.times do |i|
    y1 = points[i][1]
    max_y = -1 << 60
    (i + 1...points.length).each do |j|
      y2 = points[j][1]
      if max_y < y2 && y2 <= y1
        max_y = y2
        ans += 1
      end
    end
  end
  ans
end
''')

add("3026_maximum_good_subarray_sum", r'''
# LeetCode 3026 - Maximum Good Subarray Sum
# https://leetcode.com/problems/maximum-good-subarray-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_subarray_sum(nums, k)
  p = {}
  p[nums[0]] = 0
  s = 0
  n = nums.length
  ans = -1 << 60
  n.times do |i|
    s += nums[i]
    ans = [ans, s - p[nums[i] - k]].max if p.key?(nums[i] - k)
    ans = [ans, s - p[nums[i] + k]].max if p.key?(nums[i] + k)
    break if i + 1 == n

    old = p[nums[i + 1]]
    p[nums[i + 1]] = s if old.nil? || s < old
  end
  ans == -1 << 60 ? 0 : ans
end
''')

add("3027_find_the_number_of_ways_to_place_people_ii", r'''
# LeetCode 3027 - Find the Number of Ways to Place People II
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

# @param {Integer[][]} points
# @return {Integer}
def number_of_pairs(points)
  points.sort_by! { |a| [a[0], -a[1]] }
  ans = 0
  points.length.times do |i|
    y1 = points[i][1]
    max_y = -1 << 60
    (i + 1...points.length).each do |j|
      y2 = points[j][1]
      if max_y < y2 && y2 <= y1
        max_y = y2
        ans += 1
      end
    end
  end
  ans
end
''')

add("3028_ant_on_the_boundary", r'''
# LeetCode 3028 - Ant on the Boundary
# https://leetcode.com/problems/ant-on-the-boundary/

# @param {Integer[]} nums
# @return {Integer}
def return_to_boundary_count(nums)
  s = 0
  ans = 0
  nums.each do |x|
    s += x
    ans += 1 if s == 0
  end
  ans
end
''')

add("3029_minimum_time_to_revert_word_to_initial_state_i", r'''
# LeetCode 3029 - Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_time_to_initial_state(word, k)
  n = word.length
  i = k
  while i < n
    return i / k if word[i..-1] == word[0, n - i]

    i += k
  end
  (n + k - 1) / k
end
''')

add("3030_find_the_grid_of_region_average", r'''
# LeetCode 3030 - Find the Grid of Region Average
# https://leetcode.com/problems/find-the-grid-of-region-average/

# @param {Integer[][]} image
# @param {Integer} threshold
# @return {Integer[][]}
def result_grid(image, threshold)
  n = image.length
  m = image[0].length
  ans = Array.new(n) { Array.new(m, 0) }
  ct = Array.new(n) { Array.new(m, 0) }
  (0...n - 2).each do |i|
    (0...m - 2).each do |j|
      region = true
      3.times do |k|
        2.times do |l|
          region &&= (image[i + k][j + l] - image[i + k][j + l + 1]).abs <= threshold
        end
      end
      2.times do |k|
        3.times do |l|
          region &&= (image[i + k][j + l] - image[i + k + 1][j + l]).abs <= threshold
        end
      end
      next unless region

      tot = 0
      3.times { |k| 3.times { |l| tot += image[i + k][j + l] } }
      3.times do |k|
        3.times do |l|
          ct[i + k][j + l] += 1
          ans[i + k][j + l] += tot / 9
        end
      end
    end
  end
  n.times do |i|
    m.times do |j|
      ans[i][j] = if ct[i][j] == 0
                    image[i][j]
                  else
                    ans[i][j] / ct[i][j]
                  end
    end
  end
  ans
end
''')

add("3031_minimum_time_to_revert_word_to_initial_state_ii", r'''
# LeetCode 3031 - Minimum Time to Revert Word to Initial State II
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Hashing
  def initialize(word, bas, mod)
    @mod = mod
    n = word.length
    @p = Array.new(n + 1, 0)
    @h = Array.new(n + 1, 0)
    @p[0] = 1
    @h[0] = 0
    (1..n).each do |i|
      @p[i] = @p[i - 1] * bas % mod
      @h[i] = (@h[i - 1] * bas + (word[i - 1].ord - 97)) % mod
    end
  end

  def query(l, r)
    (@h[r] - @h[l - 1] * @p[r - l + 1] % @mod + @mod) % @mod
  end
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_time_to_initial_state(word, k)
  hashing = Hashing.new(word, 13331, 998_244_353)
  n = word.length
  i = k
  while i < n
    return i / k if hashing.query(1, n - i) == hashing.query(i + 1, n)

    i += k
  end
  (n + k - 1) / k
end
''')

add("3032_count_numbers_with_unique_digits_ii", r'''
# LeetCode 3032 - Count Numbers With Unique Digits II
# https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def number_count(a, b)
  count_unique(b) - count_unique(a - 1)
end

def count_unique(n)
  return 0 if n < 0

  num = n.to_s
  f = Array.new(num.length) { Array.new(1 << 10, -1) }
  dfs = lambda do |pos, mask, limit|
    return mask != 0 ? 1 : 0 if pos >= num.length
    return f[pos][mask] if !limit && f[pos][mask] != -1

    up = limit ? (num[pos].ord - 48) : 9
    ans = 0
    (0..up).each do |i|
      next if ((mask >> i) & 1) != 0

      nxt = mask | (1 << i)
      nxt = 0 if mask == 0 && i == 0
      ans += dfs.call(pos + 1, nxt, limit && i == up)
    end
    f[pos][mask] = ans unless limit
    ans
  end
  dfs.call(0, 0, true)
end
''')

add("3033_modify_the_matrix", r'''
# LeetCode 3033 - Modify the Matrix
# https://leetcode.com/problems/modify-the-matrix/

# @param {Integer[][]} matrix
# @return {Integer[][]}
def modified_matrix(matrix)
  m = matrix.length
  n = matrix[0].length
  n.times do |j|
    mx = -1
    m.times { |i| mx = matrix[i][j] if matrix[i][j] > mx }
    m.times { |i| matrix[i][j] = mx if matrix[i][j] == -1 }
  end
  matrix
end
''')

add("3034_number_of_subarrays_that_match_a_pattern_i", r'''
# LeetCode 3034 - Number of Subarrays That Match a Pattern I
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

# @param {Integer[]} nums
# @param {Integer[]} pattern
# @return {Integer}
def count_matching_subarrays(nums, pattern)
  n = nums.length
  m = pattern.length
  ans = 0
  (0...n - m).each do |i|
    ok = 1
    k = 0
    while k < m && ok != 0
      ok = 0 if f_rel(nums[i + k], nums[i + k + 1]) != pattern[k]
      k += 1
    end
    ans += ok
  end
  ans
end

def f_rel(a, b)
  return 0 if a == b

  a < b ? 1 : -1
end
''')

add("3035_maximum_palindromes_after_operations", r'''
# LeetCode 3035 - Maximum Palindromes After Operations
# https://leetcode.com/problems/maximum-palindromes-after-operations/

# @param {String[]} words
# @return {Integer}
def max_palindromes_after_operations(words)
  s = 0
  mask = 0
  words.each do |w|
    s += w.length
    w.each_char { |ch| mask ^= 1 << (ch.ord - 97) }
  end
  s -= popcount(mask)
  words.sort_by!(&:length)
  ans = 0
  words.each do |w|
    s -= (w.length / 2) * 2
    break if s < 0

    ans += 1
  end
  ans
end

def popcount(x)
  c = 0
  while x != 0
    c += x & 1
    x >>= 1
  end
  c
end
''')

add("3036_number_of_subarrays_that_match_a_pattern_ii", r'''
# LeetCode 3036 - Number of Subarrays That Match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

# @param {Integer[]} nums
# @param {Integer[]} pattern
# @return {Integer}
def count_matching_subarrays(nums, pattern)
  n = pattern.length
  ps = Array.new(n + 1, 0)
  ps[0] = -1
  ps[1] = 0
  p = 0
  (2..n).each do |i|
    x = pattern[i - 1]
    while p >= 0 && pattern[p] != x
      p = ps[p]
    end
    p += 1
    ps[i] = p
  end
  res = 0
  m = nums.length
  p = 0
  (1...m).each do |i|
    t = nums[i] - nums[i - 1]
    t = if t > 0
          1
        elsif t < 0
          -1
        else
          0
        end
    while p >= 0 && pattern[p] != t
      p = ps[p]
    end
    p += 1
    if p == n
      res += 1
      p = ps[p]
    end
  end
  res
end
''')

add("3037_find_pattern_in_infinite_stream_ii", r'''
# LeetCode 3037 - Find Pattern in Infinite Stream II
# https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

# @param {Object} stream
# @param {Integer[]} pattern
# @return {Integer}
def find_pattern(stream, pattern)
  lps = get_lps(pattern)
  i = 0
  j = 0
  bit = 0
  read_next = false
  loop do
    unless read_next
      bit = stream.next
      read_next = true
    end
    if bit == pattern[j]
      i += 1
      read_next = false
      j += 1
      return i - j if j == pattern.length
    elsif j > 0
      j = lps[j - 1]
    else
      i += 1
      read_next = false
    end
  end
end

def get_lps(pattern)
  n = pattern.length
  lps = Array.new(n, 0)
  j = 0
  (1...n).each do |i|
    j = lps[j - 1] while j > 0 && pattern[j] != pattern[i]
    if pattern[i] == pattern[j]
      j += 1
      lps[i] = j
    end
  end
  lps
end
''')

add("3038_maximum_number_of_operations_with_the_same_score_i", r'''
# LeetCode 3038 - Maximum Number of Operations With the Same Score I
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

# @param {Integer[]} nums
# @return {Integer}
def max_operations(nums)
  s = nums[0] + nums[1]
  n = nums.length
  ans = 0
  i = 0
  while i + 1 < n && nums[i] + nums[i + 1] == s
    ans += 1
    i += 2
  end
  ans
end
''')

add("3039_apply_operations_to_make_string_empty", r'''
# LeetCode 3039 - Apply Operations to Make String Empty
# https://leetcode.com/problems/apply-operations-to-make-string-empty/

# @param {String} s
# @return {String}
def last_non_empty_string(s)
  cnt = Array.new(26, 0)
  last = Array.new(26, 0)
  mx = 0
  s.length.times do |i|
    c = s[i].ord - 97
    cnt[c] += 1
    last[c] = i
    mx = cnt[c] if cnt[c] > mx
  end
  ans = ""
  s.length.times do |i|
    c = s[i].ord - 97
    ans += s[i] if cnt[c] == mx && last[c] == i
  end
  ans
end
''')

add("3040_maximum_number_of_operations_with_the_same_score_ii", r'''
# LeetCode 3040 - Maximum Number of Operations With the Same Score II
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_operations(nums)
  n = nums.length
  1 + [
    ops_g(nums, n, 2, n - 1, nums[0] + nums[1]),
    ops_g(nums, n, 0, n - 3, nums[n - 1] + nums[n - 2]),
    ops_g(nums, n, 1, n - 2, nums[0] + nums[n - 1])
  ].max
end

def ops_g(nums, n, i0, j0, score)
  f = Array.new(n) { Array.new(n, -1) }
  dfs = lambda do |i, j|
    return 0 if j - i < 1
    return f[i][j] if f[i][j] != -1

    ans = 0
    ans = [ans, 1 + dfs.call(i + 2, j)].max if nums[i] + nums[i + 1] == score
    ans = [ans, 1 + dfs.call(i + 1, j - 1)].max if nums[i] + nums[j] == score
    ans = [ans, 1 + dfs.call(i, j - 2)].max if nums[j - 1] + nums[j] == score
    f[i][j] = ans
    ans
  end
  dfs.call(i0, j0)
end
''')

add("3041_maximize_consecutive_elements_in_an_array_after_modification", r'''
# LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

# @param {Integer[]} nums
# @return {Integer}
def max_selected_elements(nums)
  nums.sort!
  dp = Hash.new(0)
  ans = 0
  nums.each do |num|
    dn = dp[num]
    dnm1 = dp[num - 1]
    dp[num + 1] = dn + 1
    dp[num] = dnm1 + 1
    ans = [ans, dp[num], dp[num + 1]].max
  end
  ans
end
''')

add("3042_count_prefix_and_suffix_pairs_i", r'''
# LeetCode 3042 - Count Prefix and Suffix Pairs I
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

# @param {String[]} words
# @return {Integer}
def count_prefix_suffix_pairs(words)
  ans = 0
  words.length.times do |i|
    s = words[i]
    (i + 1...words.length).each do |j|
      t = words[j]
      ans += 1 if t.length >= s.length && t.start_with?(s) && t.end_with?(s)
    end
  end
  ans
end
''')

add("3043_find_the_length_of_the_longest_common_prefix", r'''
# LeetCode 3043 - Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def longest_common_prefix(arr1, arr2)
  s = {}
  arr1.each do |x0|
    x = x0
    while x > 0
      s[x] = true
      x /= 10
    end
  end
  mx = 0
  arr2.each do |x0|
    x = x0
    while x > 0
      if s[x]
        mx = x if x > mx
        break
      end
      x /= 10
    end
  end
  mx > 0 ? mx.to_s.length : 0
end
''')

add("3044_most_frequent_prime", r'''
# LeetCode 3044 - Most Frequent Prime
# https://leetcode.com/problems/most-frequent-prime/

# @param {Integer[][]} mat
# @return {Integer}
def most_frequent_prime(mat)
  m = mat.length
  n = mat[0].length
  cnt = Hash.new(0)
  m.times do |i|
    n.times do |j|
      (-1..1).each do |a|
        (-1..1).each do |b|
          next if a == 0 && b == 0

          x = i + a
          y = j + b
          v = mat[i][j]
          while x >= 0 && x < m && y >= 0 && y < n
            v = v * 10 + mat[x][y]
            cnt[v] += 1 if prime?(v)
            x += a
            y += b
          end
        end
      end
    end
  end
  ans = -1
  mx = 0
  cnt.each do |key, value|
    if mx < value || (mx == value && ans < key)
      mx = value
      ans = key
    end
  end
  ans
end

def prime?(n)
  return false if n < 2

  i = 2
  while i <= n / i
    return false if n % i == 0

    i += 1
  end
  true
end
''')

add("3045_count_prefix_and_suffix_pairs_ii", r'''
# LeetCode 3045 - Count Prefix and Suffix Pairs II
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

class Node
  attr_accessor :children, :cnt

  def initialize
    @children = {}
    @cnt = 0
  end
end

# @param {String[]} words
# @return {Integer}
def count_prefix_suffix_pairs(words)
  trie = Node.new
  ans = 0
  words.each do |s|
    node = trie
    m = s.length
    m.times do |i|
      p = s[i].ord * 32 + s[m - i - 1].ord
      nxt = node.children[p]
      unless nxt
        nxt = Node.new
        node.children[p] = nxt
      end
      node = nxt
      ans += node.cnt
    end
    node.cnt += 1
  end
  ans
end
''')

add("3046_split_the_array", r'''
# LeetCode 3046 - Split the Array
# https://leetcode.com/problems/split-the-array/

# @param {Integer[]} nums
# @return {Boolean}
def is_possible_to_split(nums)
  cnt = Array.new(101, 0)
  nums.each do |x|
    cnt[x] += 1
    return false if cnt[x] >= 3
  end
  true
end
''')

add("3047_find_the_largest_area_of_square_inside_two_rectangles", r'''
# LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

# @param {Integer[][]} bottom_left
# @param {Integer[][]} top_right
# @return {Integer}
def largest_square_area(bottom_left, top_right)
  ans = 0
  n = bottom_left.length
  n.times do |i|
    x1 = bottom_left[i][0]
    y1 = bottom_left[i][1]
    x2 = top_right[i][0]
    y2 = top_right[i][1]
    (i + 1...n).each do |j|
      x3 = bottom_left[j][0]
      y3 = bottom_left[j][1]
      x4 = top_right[j][0]
      y4 = top_right[j][1]
      ww = [x2, x4].min - [x1, x3].max
      h = [y2, y4].min - [y1, y3].max
      e = [ww, h].min
      ans = e * e if e > 0 && e * e > ans
    end
  end
  ans
end
''')

add("3048_earliest_second_to_mark_indices_i", r'''
# LeetCode 3048 - Earliest Second to Mark Indices I
# https://leetcode.com/problems/earliest-second-to-mark-indices-i/

# @param {Integer[]} nums
# @param {Integer[]} change_indices
# @return {Integer}
def earliest_second_to_mark_indices(nums, change_indices)
  n = nums.length
  m = change_indices.length
  ok = lambda do |t|
    last = Array.new(n + 1, 0)
    t.times { |s| last[change_indices[s]] = s }
    decrement = 0
    marked = 0
    t.times do |s|
      i = change_indices[s]
      if last[i] == s
        return false if decrement < nums[i - 1]

        decrement -= nums[i - 1]
        marked += 1
      else
        decrement += 1
      end
    end
    marked == n
  end
  l = 0
  r = m + 1
  while l < r
    mid = (l + r) >> 1
    if ok.call(mid)
      r = mid
    else
      l = mid + 1
    end
  end
  l > m ? -1 : l
end
''')

written = 0
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body)
    written += 1
    print(f"wrote {name}")

print(f"written={written}")
