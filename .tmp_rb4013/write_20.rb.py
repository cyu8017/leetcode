#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2327_number_of_people_aware_of_a_secret"] = r'''# LeetCode 2327 - Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

# @param {Integer} n
# @param {Integer} delay
# @param {Integer} forget
# @return {Integer}
def people_aware_of_secret(n, delay, forget)
  mod = 1_000_000_007
  dp = Array.new(n + 1, 0)
  dp[1] = 1
  share = 0
  (2..n).each do |day|
    share = (share + dp[day - delay]) % mod if day - delay >= 1
    share = (share - dp[day - forget] + mod) % mod if day - forget >= 1
    dp[day] = share
  end
  ans = 0
  ((n - forget + 1)..n).each do |day|
    ans = (ans + dp[day]) % mod if day >= 1
  end
  ans
end
'''

FILES["2328_number_of_increasing_paths_in_a_grid"] = r'''# LeetCode 2328 - Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def count_paths(grid)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n, 0) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  dfs = lambda do |r, c|
    return dp[r][c] if dp[r][c] != 0
    res = 1
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c]
        res = (res + dfs.call(nr, nc)) % mod
      end
    end
    dp[r][c] = res
    res
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each { |j| ans = (ans + dfs.call(i, j)) % mod }
  end
  ans
end
'''

FILES["2330_valid_palindrome_iv"] = r'''# LeetCode 2330 - Valid Palindrome IV
# https://leetcode.com/problems/valid-palindrome-iv/

# @param {String} s
# @return {Boolean}
def make_palindrome(s)
  diff = 0
  i = 0
  j = s.length - 1
  while i < j
    if s[i] != s[j]
      diff += 1
      return false if diff > 2
    end
    i += 1
    j -= 1
  end
  true
end
'''

FILES["2331_evaluate_boolean_binary_tree"] = r'''# LeetCode 2331 - Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Boolean}
def evaluate_tree(root)
  return root.val == 1 if root.left.nil? && root.right.nil?
  l = evaluate_tree(root.left)
  r = evaluate_tree(root.right)
  return l || r if root.val == 2
  l && r
end
'''

FILES["2332_the_latest_time_to_catch_a_bus"] = r'''# LeetCode 2332 - The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

# @param {Integer[]} buses
# @param {Integer[]} passengers
# @param {Integer} capacity
# @return {Integer}
def latest_time_catch_the_bus(buses, passengers, capacity)
  buses = buses.sort
  passengers = passengers.sort
  pos = 0
  buses.each_with_index do |bus, bi|
    cap = capacity
    while cap > 0 && pos < passengers.length && passengers[pos] <= bus
      pos += 1
      cap -= 1
    end
    if bi == buses.length - 1
      cand = bus
      cand = passengers[pos - 1] if cap == 0
      taken = {}
      passengers.each { |p| taken[p] = true }
      cand -= 1 while taken[cand]
      return cand
    end
  end
  -1
end
'''

FILES["2333_minimum_sum_of_squared_difference"] = r'''# LeetCode 2333 - Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k1
# @param {Integer} k2
# @return {Integer}
def min_sum_square_diff(nums1, nums2, k1, k2)
  n = nums1.length
  diff = Array.new(n, 0)
  max_d = 0
  (0...n).each do |i|
    d = (nums1[i] - nums2[i]).abs
    diff[i] = d
    max_d = d if d > max_d
  end
  k = k1 + k2
  freq = Array.new(max_d + 1, 0)
  diff.each { |d| freq[d] += 1 }
  max_d.downto(1) do |d|
    break if k <= 0
    next if freq[d] == 0
    take = freq[d]
    take = k if take > k
    freq[d] -= take
    freq[d - 1] += take
    k -= take
  end
  ans = 0
  (0..max_d).each { |d| ans += d * d * freq[d] }
  ans
end
'''

FILES["2334_subarray_with_elements_greater_than_varying_threshold"] = r'''# LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def valid_subarray_size(nums, threshold)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  stack = []
  (0...n).each do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= nums[i]
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end
  stack.clear
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= nums[i]
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end
  (0...n).each do |i|
    k = right[i] - left[i] - 1
    return k if nums[i] > threshold / k
  end
  -1
end
'''

FILES["2335_minimum_amount_of_time_to_fill_cups"] = r'''# LeetCode 2335 - Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

# @param {Integer[]} amount
# @return {Integer}
def fill_cups(amount)
  a, b, c = amount[0], amount[1], amount[2]
  a, b = b, a if a < b
  a, c = c, a if a < c
  b, c = c, b if b < c
  return a if a >= b + c
  (a + b + c + 1) / 2
end
'''

FILES["2336_smallest_number_in_infinite_set"] = r'''# LeetCode 2336 - Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet
  def initialize
    @nxt = 1
    @added = {}
    @heap = []
  end

  def pop_smallest
    unless @heap.empty?
      x = _pop
      @added.delete(x)
      return x
    end
    val = @nxt
    @nxt += 1
    val
  end

  def add_back(num)
    if num < @nxt && !@added.key?(num)
      @added[num] = true
      _push(num)
    end
  end

  private

  def _bubble_up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @heap[p] <= @heap[i]
      @heap[p], @heap[i] = @heap[i], @heap[p]
      i = p
    end
  end

  def _bubble_down(i)
    n = @heap.length
    loop do
      smallest = i
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = l if l < n && @heap[l] < @heap[smallest]
      smallest = r if r < n && @heap[r] < @heap[smallest]
      break if smallest == i
      @heap[smallest], @heap[i] = @heap[i], @heap[smallest]
      i = smallest
    end
  end

  def _push(x)
    @heap << x
    _bubble_up(@heap.length - 1)
  end

  def _pop
    top = @heap[0]
    last = @heap.pop
    unless @heap.empty?
      @heap[0] = last
      _bubble_down(0)
    end
    top
  end
end
'''

FILES["2337_move_pieces_to_obtain_a_string"] = r'''# LeetCode 2337 - Move Pieces to Obtain a String
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

# @param {String} start
# @param {String} target
# @return {Boolean}
def can_change(start, target)
  n = start.length
  i = 0
  j = 0
  while i < n || j < n
    i += 1 while i < n && start[i] == "_"
    j += 1 while j < n && target[j] == "_"
    return i == n && j == n if i == n || j == n
    return false if start[i] != target[j]
    return false if start[i] == "L" && i < j
    return false if start[i] == "R" && i > j
    i += 1
    j += 1
  end
  true
end
'''

FILES["2338_count_the_number_of_ideal_arrays"] = r'''# LeetCode 2338 - Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

# @param {Integer} n
# @param {Integer} max_value
# @return {Integer}
def ideal_arrays(n, max_value)
  mod = 1_000_000_007
  max_len = 14
  comb = Array.new(n + 1) { Array.new(max_len + 1, 0) }
  (0..n).each do |i|
    comb[i][0] = 1
    (1..[max_len, i].min).each do |j|
      comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
    end
  end
  dp = Array.new(max_value + 1) { Array.new(max_len + 1, 0) }
  (1..max_value).each { |i| dp[i][1] = 1 }
  (2..max_len).each do |length|
    (1..max_value).each do |v|
      m = 2 * v
      while m <= max_value
        dp[m][length] = (dp[m][length] + dp[v][length - 1]) % mod
        m += v
      end
    end
  end
  ans = 0
  (1..max_value).each do |v|
    (1..[max_len, n].min).each do |length|
      ans = (ans + (dp[v][length] * comb[n - 1][length - 1]) % mod) % mod
    end
  end
  ans
end
'''

FILES["2340_minimum_adjacent_swaps_to_make_a_valid_array"] = r'''# LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_swaps(nums)
  n = nums.length
  min_i = 0
  max_i = 0
  (1...n).each do |i|
    min_i = i if nums[i] < nums[min_i]
    max_i = i if nums[i] >= nums[max_i]
  end
  ans = min_i + (n - 1 - max_i)
  ans -= 1 if min_i > max_i
  ans
end
'''

FILES["2341_maximum_number_of_pairs_in_array"] = r'''# LeetCode 2341 - Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

# @param {Integer[]} nums
# @return {Integer[]}
def number_of_pairs(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  pairs = 0
  left = 0
  cnt.each_value do |c|
    pairs += c / 2
    left += c % 2
  end
  [pairs, left]
end
'''

FILES["2342_max_sum_of_a_pair_with_equal_sum_of_digits"] = r'''# LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  digit_sum = lambda do |x|
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    s
  end
  best = {}
  ans = -1
  nums.each do |x|
    ds = digit_sum.call(x)
    if best.key?(ds)
      cand = best[ds] + x
      ans = cand if cand > ans
      best[ds] = x if x > best[ds]
    else
      best[ds] = x
    end
  end
  ans
end
'''

FILES["2343_query_kth_smallest_trimmed_number"] = r'''# LeetCode 2343 - Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

# @param {String[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def smallest_trimmed_numbers(nums, queries)
  n = nums.length
  m = queries.length
  ans = Array.new(m, 0)
  (0...m).each do |qi|
    k = queries[qi][0]
    trim = queries[qi][1]
    arr = []
    (0...n).each do |i|
      s = nums[i]
      arr << [s[s.length - trim..], i]
    end
    arr.sort_by! { |x| [x[0], x[1]] }
    ans[qi] = arr[k - 1][1]
  end
  ans
end
'''

FILES["2344_minimum_deletions_to_make_array_divisible"] = r'''# LeetCode 2344 - Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

# @param {Integer[]} nums
# @param {Integer[]} nums_divide
# @return {Integer}
def min_operations(nums, nums_divide)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  g = nums_divide[0]
  (1...nums_divide.length).each { |i| g = gcd.call(g, nums_divide[i]) }
  nums = nums.sort
  nums.each_with_index { |x, i| return i if g % x == 0 }
  -1
end
'''

FILES["2345_finding_the_number_of_visible_mountains"] = r'''# LeetCode 2345 - Finding the Number of Visible Mountains
# https://leetcode.com/problems/finding-the-number-of-visible-mountains/

# @param {Integer[][]} peaks
# @return {Integer}
def visible_mountains(peaks)
  arr = peaks.map { |p| [p[0] - p[1], p[0] + p[1]] }
  arr.sort_by! { |a| [a[0], -a[1]] }
  ans = 0
  max_r = -Float::INFINITY
  i = 0
  while i < arr.length
    j = i
    j += 1 while j < arr.length && arr[j][0] == arr[i][0] && arr[j][1] == arr[i][1]
    if arr[i][1] > max_r
      ans += 1 if j - i == 1
      max_r = arr[i][1]
    end
    i = j
  end
  ans
end
'''

FILES["2347_best_poker_hand"] = r'''# LeetCode 2347 - Best Poker Hand
# https://leetcode.com/problems/best-poker-hand/

# @param {Integer[]} ranks
# @param {String[]} suits
# @return {String}
def best_hand(ranks, suits)
  return "Flush" if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]
  cnt = Hash.new(0)
  best = 0
  ranks.each do |r|
    cnt[r] += 1
    best = cnt[r] if cnt[r] > best
  end
  return "Three of a Kind" if best >= 3
  return "Pair" if best == 2
  "High Card"
end
'''

FILES["2348_number_of_zero_filled_subarrays"] = r'''# LeetCode 2348 - Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def zero_filled_subarray(nums)
  ans = 0
  streak = 0
  nums.each do |x|
    if x == 0
      streak += 1
      ans += streak
    else
      streak = 0
    end
  end
  ans
end
'''

FILES["2349_design_a_number_container_system"] = r'''# LeetCode 2349 - Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers
  def initialize
    @idx = {}
    @heap = {}
  end

  def change(index, number)
    @idx[index] = number
    @heap[number] ||= []
    @heap[number] << index
  end

  def find(number)
    h = @heap[number]
    return -1 if h.nil? || h.empty?
    h.sort!
    until h.empty?
      i = h[0]
      return i if @idx[i] == number
      h.shift
    end
    -1
  end
end
'''

for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {folder}")
print(f"done {len(FILES)}")
