#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2416_sum_of_prefix_scores_of_strings", r'''
# LeetCode 2416 - Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

# @param {String[]} words
# @return {Integer[]}
def sum_prefix_scores(words)
  root = { "child" => Array.new(26), "cnt" => 0 }
  words.each do |w|
    cur = root
    w.each_byte do |b|
      c = b - 97
      cur["child"][c] = { "child" => Array.new(26), "cnt" => 0 } if cur["child"][c].nil?
      cur = cur["child"][c]
      cur["cnt"] += 1
    end
  end
  ans = Array.new(words.length, 0)
  words.each_with_index do |w, i|
    cur = root
    s = 0
    w.each_byte do |b|
      cur = cur["child"][b - 97]
      s += cur["cnt"]
    end
    ans[i] = s
  end
  ans
end
''')

add("2417_closest_fair_integer", r'''
# LeetCode 2417 - Closest Fair Integer
# https://leetcode.com/problems/closest-fair-integer/

# @param {Integer} n
# @return {Integer}
def closest_fair(n)
  x = n
  loop do
    s = x.to_s
    if s.length.odd?
      p = 1
      s.length.times { p *= 10 }
      return closest_fair(p)
    end
    even = odd = 0
    s.each_byte do |b|
      if (b - 48).even?
        even += 1
      else
        odd += 1
      end
    end
    return x if even == odd

    x += 1
  end
end
''')

add("2418_sort_the_people", r'''
# LeetCode 2418 - Sort the People
# https://leetcode.com/problems/sort-the-people/

# @param {String[]} names
# @param {Integer[]} heights
# @return {String[]}
def sort_people(names, heights)
  n = names.length
  idx = (0...n).to_a
  idx.sort_by! { |i| -heights[i] }
  idx.map { |i| names[i] }
end
''')

add("2419_longest_subarray_with_maximum_bitwise_and", r'''
# LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  ans = cur = 0
  nums.each do |x|
    if x == mx
      cur += 1
      ans = cur if cur > ans
    else
      cur = 0
    end
  end
  ans
end
''')

add("2420_find_all_good_indices", r'''
# LeetCode 2420 - Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def good_indices(nums, k)
  n = nums.length
  dec = Array.new(n, 0)
  inc = Array.new(n, 0)
  dec[0] = 1
  (1...n).each do |i|
    dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1
  end
  inc[n - 1] = 1
  (n - 2).downto(0) do |i|
    inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1
  end
  ans = []
  k.upto(n - k - 1) do |i|
    ans << i if dec[i - 1] >= k && inc[i + 1] >= k
  end
  ans
end
''')

add("2421_number_of_good_paths", r'''
# LeetCode 2421 - Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/

# @param {Integer[]} vals
# @param {Integer[][]} edges
# @return {Integer}
def number_of_good_paths(vals, edges)
  n = vals.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  parent = (0...n).to_a

  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end

  nodes = (0...n).to_a
  nodes.sort_by! { |i| vals[i] }
  ans = n
  i = 0
  while i < n
    j = i
    j += 1 while j < n && vals[nodes[j]] == vals[nodes[i]]
    (i...j).each do |k|
      u = nodes[k]
      g[u].each do |v|
        next if vals[v] > vals[u]

        ru = find.call(u)
        rv = find.call(v)
        parent[ru] = rv if ru != rv
      end
    end
    freq = Hash.new(0)
    (i...j).each { |k| freq[find.call(nodes[k])] += 1 }
    freq.each_value { |c| ans += c * (c - 1) / 2 }
    i = j
  end
  ans
end
''')

add("2422_merge_operations_to_turn_array_into_a_palindrome", r'''
# LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  l = 0
  r = nums.length - 1
  left = nums[l]
  right = nums[r]
  ans = 0
  while l < r
    if left == right
      l += 1
      r -= 1
      if l < r
        left = nums[l]
        right = nums[r]
      end
    elsif left < right
      l += 1
      left += nums[l]
      ans += 1
    else
      r -= 1
      right += nums[r]
      ans += 1
    end
  end
  ans
end
''')

add("2423_remove_letter_to_equalize_frequency", r'''
# LeetCode 2423 - Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

# @param {String} word
# @return {Boolean}
def equal_frequency(word)
  (0...word.length).each do |skip|
    cnt = Array.new(26, 0)
    word.each_char.with_index do |ch, i|
      next if i == skip

      cnt[ch.ord - 97] += 1
    end
    freq = Hash.new(0)
    cnt.each { |c| freq[c] += 1 if c > 0 }
    return true if freq.length == 1
  end
  false
end
''')

add("2424_longest_uploaded_prefix", r'''
# LeetCode 2424 - Longest Uploaded Prefix
# https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix
  def initialize(n)
    @uploaded = Array.new(n + 2, false)
    @prefix_len = 0
  end

  def upload(video)
    @uploaded[video] = true
    @prefix_len += 1 while @uploaded[@prefix_len + 1]
    nil
  end

  def longest
    @prefix_len
  end
end
''')

add("2425_bitwise_xor_of_all_pairings", r'''
# LeetCode 2425 - Bitwise XOR of All Pairings
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def xor_all_nums(nums1, nums2)
  ans = 0
  nums1.each { |x| ans ^= x } if nums2.length.odd?
  nums2.each { |x| ans ^= x } if nums1.length.odd?
  ans
end
''')

add("2426_number_of_pairs_satisfying_inequality", r'''
# LeetCode 2426 - Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} diff
# @return {Integer}
def number_of_pairs(nums1, nums2, diff)
  n = nums1.length
  arr = Array.new(n) { |i| nums1[i] - nums2[i] }
  tmp = Array.new(n, 0)

  merge_count = lambda do |l, r|
    return 0 if r - l <= 1

    m = (l + r) >> 1
    ans = merge_count.call(l, m) + merge_count.call(m, r)
    j = m
    (l...m).each do |i|
      j += 1 while j < r && arr[j] < arr[i] - diff
      ans += r - j
    end
    p = l
    q = m
    i2 = l
    while p < m && q < r
      if arr[p] <= arr[q]
        tmp[i2] = arr[p]
        p += 1
      else
        tmp[i2] = arr[q]
        q += 1
      end
      i2 += 1
    end
    while p < m
      tmp[i2] = arr[p]
      p += 1
      i2 += 1
    end
    while q < r
      tmp[i2] = arr[q]
      q += 1
      i2 += 1
    end
    (l...r).each { |t| arr[t] = tmp[t] }
    ans
  end

  merge_count.call(0, n)
end
''')

add("2427_number_of_common_factors", r'''
# LeetCode 2427 - Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def common_factors(a, b)
  gcd = lambda do |x, y|
    while y != 0
      x, y = y, x % y
    end
    x
  end

  g = gcd.call(a, b)
  ans = 0
  i = 1
  while i * i <= g
    if g % i == 0
      ans += 1
      ans += 1 if i * i != g
    end
    i += 1
  end
  ans
end
''')

add("2428_maximum_sum_of_an_hourglass", r'''
# LeetCode 2428 - Maximum Sum of an Hourglass
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

# @param {Integer[][]} grid
# @return {Integer}
def max_sum(grid)
  m = grid.length
  n = grid[0].length
  ans = -1 << 60
  (0...(m - 2)).each do |i|
    (0...(n - 2)).each do |j|
      s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
          grid[i + 1][j + 1] +
          grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
      ans = s if s > ans
    end
  end
  ans
end
''')

add("2429_minimize_xor", r'''
# LeetCode 2429 - Minimize XOR
# https://leetcode.com/problems/minimize-xor/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def minimize_xor(num1, num2)
  bits = 0
  x = num2
  while x != 0
    x &= x - 1
    bits += 1
  end
  ans = 0
  31.downto(0) do |i|
    break if bits <= 0
    next if ((num1 >> i) & 1) == 0

    ans |= 1 << i
    bits -= 1
  end
  (0...32).each do |i|
    break if bits <= 0
    next if ((ans >> i) & 1) != 0

    ans |= 1 << i
    bits -= 1
  end
  ans
end
''')

add("2430_maximum_deletions_on_a_string", r'''
# LeetCode 2430 - Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/

# @param {String} s
# @return {Integer}
def delete_string(s)
  n = s.length
  lcp = Array.new(n + 1) { Array.new(n + 1, 0) }
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      lcp[i][j] = lcp[i + 1][j + 1] + 1 if s[i] == s[j]
    end
  end
  dp = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    dp[i] = 1
    length = 1
    while i + 2 * length <= n
      dp[i] = [dp[i], 1 + dp[i + length]].max if lcp[i][i + length] >= length
      length += 1
    end
  end
  dp[0]
end
''')

add("2431_maximize_total_tastiness_of_purchased_fruits", r'''
# LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
# https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

# @param {Integer[]} price
# @param {Integer[]} tastiness
# @param {Integer} max_amount
# @param {Integer} max_coupons
# @return {Integer}
def max_tastiness(price, tastiness, max_amount, max_coupons)
  n = price.length
  neg = -(2_147_483_647 / 2)
  dp = Array.new(max_amount + 1) { Array.new(max_coupons + 1, neg) }
  dp[0][0] = 0
  (0...n).each do |i|
    p = price[i]
    t = tastiness[i]
    max_amount.downto(0) do |a|
      max_coupons.downto(0) do |c|
        next if dp[a][c] < 0

        dp[a + p][c] = [dp[a + p][c], dp[a][c] + t].max if a + p <= max_amount
        if c + 1 <= max_coupons && a + p / 2 <= max_amount
          half = a + p / 2
          dp[half][c + 1] = [dp[half][c + 1], dp[a][c] + t].max
        end
      end
    end
  end
  ans = 0
  (0..max_amount).each do |a|
    (0..max_coupons).each { |c| ans = dp[a][c] if dp[a][c] > ans }
  end
  ans
end
''')

add("2432_the_employee_that_worked_on_the_longest_task", r'''
# LeetCode 2432 - The Employee That Worked on the Longest Task
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

# @param {Integer} n
# @param {Integer[][]} logs
# @return {Integer}
def hardest_worker(n, logs)
  ans = logs[0][0]
  best = logs[0][1]
  prev = 0
  logs.each do |emp, t|
    dur = t - prev
    if dur > best || (dur == best && emp < ans)
      best = dur
      ans = emp
    end
    prev = t
  end
  ans
end
''')

add("2433_find_the_original_array_of_prefix_xor", r'''
# LeetCode 2433 - Find The Original Array of Prefix Xor
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

# @param {Integer[]} pref
# @return {Integer[]}
def find_array(pref)
  ans = Array.new(pref.length, 0)
  ans[0] = pref[0]
  (1...pref.length).each { |i| ans[i] = pref[i] ^ pref[i - 1] }
  ans
end
''')

add("2434_using_a_robot_to_print_the_lexicographically_smallest_string", r'''
# LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

# @param {String} s
# @return {String}
def robot_with_string(s)
  n = s.length
  min_suf = Array.new(n + 1, "")
  min_suf[n] = ("z".ord + 1).chr
  (n - 1).downto(0) do |i|
    min_suf[i] = s[i] < min_suf[i + 1] ? s[i] : min_suf[i + 1]
  end
  stack = []
  ans = []
  (0...n).each do |i|
    stack << s[i]
    ans << stack.pop while !stack.empty? && stack[-1] <= min_suf[i + 1]
  end
  ans << stack.pop until stack.empty?
  ans.join
end
''')

add("2435_paths_in_matrix_whose_sum_is_divisible_by_k", r'''
# LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def number_of_paths(grid, k)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n) { Array.new(k, 0) } }
  dp[0][0][grid[0][0] % k] = 1
  (0...m).each do |i|
    (0...n).each do |j|
      (0...k).each do |r|
        next if dp[i][j][r] == 0

        if i + 1 < m
          nr = (r + grid[i + 1][j]) % k
          dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod
        end
        if j + 1 < n
          nr = (r + grid[i][j + 1]) % k
          dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod
        end
      end
    end
  end
  dp[m - 1][n - 1][0]
end
''')

add("2436_minimum_split_into_subarrays_with_gcd_greater_than_one", r'''
# LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
# https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

# @param {Integer[]} nums
# @return {Integer}
def minimum_splits(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 1
  g = nums[0]
  (1...nums.length).each do |i|
    ng = gcd.call(g, nums[i])
    if ng == 1
      ans += 1
      g = nums[i]
    else
      g = ng
    end
  end
  ans
end
''')

add("2437_number_of_valid_clock_times", r'''
# LeetCode 2437 - Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/

# @param {String} time
# @return {Integer}
def count_time(time)
  ans = 0
  (0...24).each do |h|
    (0...60).each do |m|
      h0 = (h / 10).to_s
      h1 = (h % 10).to_s
      m0 = (m / 10).to_s
      m1 = (m % 10).to_s
      next if time[0] != "?" && time[0] != h0
      next if time[1] != "?" && time[1] != h1
      next if time[3] != "?" && time[3] != m0
      next if time[4] != "?" && time[4] != m1

      ans += 1
    end
  end
  ans
end
''')

add("2438_range_product_queries_of_powers", r'''
# LeetCode 2438 - Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def product_queries(n, queries)
  mod = 1_000_000_007
  powers = []
  (0...31).each { |bit| powers << (1 << bit) if ((n >> bit) & 1) != 0 }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    prod = 1
    q[0].upto(q[1]) { |j| prod = (prod * powers[j]) % mod }
    ans[i] = prod
  end
  ans
end
''')

add("2439_minimize_maximum_of_array", r'''
# LeetCode 2439 - Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/

# @param {Integer[]} nums
# @return {Integer}
def minimize_array_value(nums)
  total = 0
  ans = 0
  nums.each_with_index do |x, i|
    total += x
    avg = (total + i) / (i + 1)
    ans = avg if avg > ans
  end
  ans
end
''')

add("2440_create_components_with_same_value", r'''
# LeetCode 2440 - Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def component_value(nums, edges)
  n = nums.length
  total = nums.sum
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  dfs = lambda do |u, p, target|
    s = nums[u]
    g[u].each do |v|
      next if v == p

      sub = dfs.call(v, u, target)
      return -1 if sub < 0

      s += sub
    end
    return -1 if s > target
    return 0 if s == target

    s
  end

  n.downto(1) do |parts|
    next if total % parts != 0

    return parts - 1 if dfs.call(0, -1, total / parts) == 0
  end
  0
end
''')


def write_all() -> None:
    written = 0
    for folder, content in S.items():
        path = ROOT / folder / "solution.rb"
        path.write_bytes(content.encode("utf-8"))
        written += 1
        print(folder)
    print(f"wrote {written}")


if __name__ == "__main__":
    write_all()
