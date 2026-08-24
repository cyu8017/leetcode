#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2806_account_balance_after_rounded_purchase"] = r'''# LeetCode 2806 - Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase/

# @param {Integer} purchase_amount
# @return {Integer}
def account_balance_after_purchase(purchase_amount)
  r = ((purchase_amount + 5) / 10) * 10
  100 - r
end
'''

FILES["2807_insert_greatest_common_divisors_in_linked_list"] = r'''# LeetCode 2807 - Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def insert_greatest_common_divisors(head)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  cur = head
  while cur && cur.next
    g = gcd.call(cur.val, cur.next.val)
    node = ListNode.new(g, cur.next)
    cur.next = node
    cur = node.next
  end
  head
end
'''

FILES["2808_minimum_seconds_to_equalize_a_circular_array"] = r'''# LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_seconds(nums)
  n = nums.length
  pos = {}
  nums.each_with_index { |v, i| (pos[v] ||= []) << i }
  ans = n
  pos.each_value do |p|
    max_gap = 0
    p.each_index do |i|
      gap = i + 1 < p.length ? p[i + 1] - p[i] : p[0] + n - p[i]
      max_gap = [max_gap, gap / 2].max
    end
    ans = [ans, max_gap].min
  end
  ans
end
'''

FILES["2809_minimum_time_to_make_array_sum_at_most_x"] = r'''# LeetCode 2809 - Minimum Time to Make Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} x
# @return {Integer}
def minimum_time(nums1, nums2, x)
  n = nums1.length
  arr = (0...n).map { |i| [nums1[i], nums2[i]] }
  sum1 = nums1.sum
  sum2 = nums2.sum
  arr.sort_by! { |p| p[1] }
  dp = Array.new(n + 1, 0)
  (0...n).each do |i|
    (i + 1).downto(1) do |j|
      dp[j] = [dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1]].max
    end
  end
  (0..n).each { |t| return t if sum1 + sum2 * t - dp[t] <= x }
  -1
end
'''

FILES["2810_faulty_keyboard"] = r'''# LeetCode 2810 - Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/

# @param {String} s
# @return {String}
def final_string(s)
  b = +""
  s.each_char do |c|
    if c == "i"
      b.reverse!
    else
      b << c
    end
  end
  b
end
'''

FILES["2811_check_if_it_is_possible_to_split_array"] = r'''# LeetCode 2811 - Check if it is Possible to Split Array
# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Boolean}
def can_split_array(nums, m)
  n = nums.length
  return true if n <= 2
  (0...(n - 1)).each { |i| return true if nums[i] + nums[i + 1] >= m }
  false
end
'''

FILES["2812_find_the_safest_path_in_a_grid"] = r'''# LeetCode 2812 - Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_safeness_factor(grid)
  n = grid.length
  dist = Array.new(n) { Array.new(n, -1) }
  q = []
  (0...n).each do |i|
    (0...n).each do |j|
      if grid[i][j] == 1
        dist[i][j] = 0
        q << [i, j]
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  h = 0
  while h < q.length
    x, y = q[h]
    h += 1
    dirs.each do |dx, dy|
      ni = x + dx
      nj = y + dy
      if ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1
        dist[ni][nj] = dist[x][y] + 1
        q << [ni, nj]
      end
    end
  end

  ok = lambda do |sf|
    return false if dist[0][0] < sf
    seen = Array.new(n) { Array.new(n, false) }
    st = [[0, 0]]
    seen[0][0] = true
    until st.empty?
      x, y = st.pop
      return true if x == n - 1 && y == n - 1
      dirs.each do |dx, dy|
        ni = x + dx
        nj = y + dy
        if ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf
          seen[ni][nj] = true
          st << [ni, nj]
        end
      end
    end
    false
  end

  lo = 0
  hi = n * n
  ans = 0
  while lo <= hi
    mid = (lo + hi) >> 1
    if ok.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
'''

FILES["2813_maximum_elegance_of_a_k_length_subsequence"] = r'''# LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

# @param {Integer[][]} items
# @param {Integer} k
# @return {Integer}
def find_maximum_elegance(items, k)
  items = items.sort_by { |it| -it[0] }
  seen = {}
  total = 0
  dup = []
  (0...k).each do |i|
    total += items[i][0]
    c = items[i][1]
    if seen[c]
      dup << items[i][0]
    else
      seen[c] = true
    end
  end
  ans = total + seen.length * seen.length
  (k...items.length).each do |i|
    c = items[i][1]
    next if seen[c] || dup.empty?
    total += items[i][0] - dup.pop
    seen[c] = true
    ans = [ans, total + seen.length * seen.length].max
  end
  ans
end
'''

FILES["2814_minimum_time_takes_to_reach_destination_without_drowning"] = r'''# LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
# https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

# @param {String[][]} land
# @return {Integer}
def minimum_seconds(land)
  m = land.length
  n = land[0].length
  inf = 10**9
  water = Array.new(m) { Array.new(n, inf) }
  wq = []
  sx = sy = dx = dy = 0
  (0...m).each do |i|
    (0...n).each do |j|
      cell = land[i][j]
      if cell == "*"
        water[i][j] = 0
        wq << [i, j]
      elsif cell == "S"
        sx = i
        sy = j
      elsif cell == "D"
        dx = i
        dy = j
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  h = 0
  while h < wq.length
    x, y = wq[h]
    h += 1
    dirs.each do |ddx, ddy|
      ni = x + ddx
      nj = y + ddy
      next if ni < 0 || nj < 0 || ni >= m || nj >= n
      cell = land[ni][nj]
      next if cell == "X" || cell == "D"
      if water[ni][nj] > water[x][y] + 1
        water[ni][nj] = water[x][y] + 1
        wq << [ni, nj]
      end
    end
  end
  dist = Array.new(m) { Array.new(n, -1) }
  q = [[sx, sy]]
  dist[sx][sy] = 0
  h = 0
  while h < q.length
    x, y = q[h]
    h += 1
    return dist[x][y] if x == dx && y == dy
    dirs.each do |ddx, ddy|
      ni = x + ddx
      nj = y + ddy
      next if ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1
      next if land[ni][nj] == "X"
      nd = dist[x][y] + 1
      next if land[ni][nj] != "D" && nd >= water[ni][nj]
      dist[ni][nj] = nd
      q << [ni, nj]
    end
  end
  -1
end
'''

FILES["2815_max_pair_sum_in_an_array"] = r'''# LeetCode 2815 - Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
  best = {}
  ans = -1
  nums.each do |v|
    x = v
    md = 0
    while x > 0
      md = [md, x % 10].max
      x /= 10
    end
    if best.key?(md)
      ans = [ans, best[md] + v].max
      best[md] = [best[md], v].max
    else
      best[md] = v
    end
  end
  ans
end
'''

FILES["2816_double_a_number_represented_as_a_linked_list"] = r'''# LeetCode 2816 - Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def double_it(head)
  rev = lambda do |node|
    prev = nil
    while node
      nxt = node.next
      node.next = prev
      prev = node
      node = nxt
    end
    prev
  end
  head = rev.call(head)
  carry = 0
  cur = head
  prev = nil
  while cur
    val = cur.val * 2 + carry
    cur.val = val % 10
    carry = val / 10
    prev = cur
    cur = cur.next
  end
  prev.next = ListNode.new(carry) if carry > 0 && !prev.nil?
  rev.call(head)
end
'''

FILES["2817_minimum_absolute_difference_between_elements_with_constraint"] = r'''# LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_absolute_difference(nums, x)
  if x == 0
    ans0 = 10**18
    (1...nums.length).each { |i| ans0 = [ans0, (nums[i] - nums[i - 1]).abs].min }
    return ans0
  end
  ans = 10**18
  arr = []
  insert = lambda do |v|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.insert(lo, v)
  end
  lower_bound = lambda do |v|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  (x...nums.length).each do |i|
    insert.call(nums[i - x])
    cur = nums[i]
    idx = lower_bound.call(cur)
    ans = [ans, arr[idx] - cur].min if idx < arr.length
    ans = [ans, cur - arr[idx - 1]].min if idx > 0
  end
  ans
end
'''

FILES["2818_apply_operations_to_maximize_score"] = r'''# LeetCode 2818 - Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  mod = 1_000_000_007
  n = nums.length
  max_v = nums.max || 0
  spf = Array.new(max_v + 1, 0)
  (2..max_v).each do |i|
    next unless spf[i] == 0
    i.step(max_v, i) { |j| spf[j] = i if spf[j] == 0 }
  end
  prime_score = lambda do |x|
    seen = {}
    while x > 1
      p = spf[x]
      seen[p] = true
      x /= p while x % p == 0
    end
    seen.length
  end
  score = nums.map { |v| prime_score.call(v) }
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  st = []
  (0...n).each do |i|
    st.pop while !st.empty? && score[st[-1]] < score[i]
    left[i] = st.empty? ? -1 : st[-1]
    st << i
  end
  st.clear
  (n - 1).downto(0) do |i|
    st.pop while !st.empty? && score[st[-1]] <= score[i]
    right[i] = st.empty? ? n : st[-1]
    st << i
  end
  arr = (0...n).map { |i| [nums[i], (i - left[i]) * (right[i] - i)] }
  arr.sort_by! { |p| -p[0] }
  mod_pow = lambda do |a, b|
    res = 1
    base = a % mod
    exp = b
    while exp > 0
      res = res * base % mod if exp.odd?
      base = base * base % mod
      exp >>= 1
    end
    res
  end
  ans = 1
  remain = k
  arr.each do |val, cnt|
    break if remain <= 0
    use = cnt < remain ? cnt : remain
    ans = ans * mod_pow.call(val, use) % mod
    remain -= use
  end
  ans
end
'''

FILES["2819_minimum_relative_loss_after_buying_chocolates"] = r'''# LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
# https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

# @param {Integer[]} prices
# @param {Integer[][]} queries
# @return {Integer[]}
def minimum_relative_losses(prices, queries)
  prices = prices.sort
  n = prices.length
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(kk, m), qi|
    losses = Array.new(n, 0)
    (0...n).each do |i|
      losses[i] = prices[i] <= kk ? prices[i] : 2 * kk - prices[i]
    end
    losses.sort!
    total = 0
    (0...m).each { |i| total += losses[i] }
    ans[qi] = total
  end
  ans
end
'''

FILES["2821_delay_the_resolution_of_each_promise"] = r'''# LeetCode 2821 - Delay the Resolution of Each Promise
# https://leetcode.com/problems/delay-the-resolution-of-each-promise/

# @param {Proc[]} functions
# @param {Integer} ms
# @return {Proc[]}
def delay_all(functions, ms)
  functions.map do |fn|
    lambda do
      fn.respond_to?(:call) ? fn.call : fn
    end
  end
end
'''

FILES["2822_inversion_of_object"] = r'''# LeetCode 2822 - Inversion of Object
# https://leetcode.com/problems/inversion-of-object/

# @param {Object} obj
# @return {Hash}
def invert_object(obj)
  inverted = {}
  keys = obj.is_a?(Hash) ? obj.keys : (0...obj.length)
  keys.each do |key|
    val = obj[key]
    key_s = key.to_s
    if inverted.key?(val)
      inverted[val] = [inverted[val]] unless inverted[val].is_a?(Array)
      inverted[val] << key_s
    else
      inverted[val] = key_s
    end
  end
  inverted
end
'''

FILES["2823_deep_object_filter"] = r'''# LeetCode 2823 - Deep Object Filter
# https://leetcode.com/problems/deep-object-filter/

# @param {Object} obj
# @param {Proc} fn
# @return {Object}
def deep_filter(obj, fn)
  unless obj.is_a?(Hash) || obj.is_a?(Array)
    return fn.call(obj) ? obj : nil
  end
  if obj.is_a?(Array)
    res = []
    obj.each do |v|
      f = deep_filter(v, fn)
      res << f unless f.nil?
    end
    return res.empty? ? nil : res
  end
  res = {}
  obj.each do |k, v|
    f = deep_filter(v, fn)
    res[k] = f unless f.nil?
  end
  res.empty? ? nil : res
end
'''

FILES["2824_count_pairs_whose_sum_is_less_than_target"] = r'''# LeetCode 2824 - Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_pairs(nums, target)
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if nums[i] + nums[j] < target }
  end
  ans
end
'''

FILES["2825_make_string_a_subsequence_using_cyclic_increments"] = r'''# LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

# @param {String} str1
# @param {String} str2
# @return {Boolean}
def can_make_subsequence(str1, str2)
  j = 0
  i = 0
  while i < str1.length && j < str2.length
    a = str1[i].ord - 97
    b = str2[j].ord - 97
    j += 1 if a == b || (a + 1) % 26 == b
    i += 1
  end
  j == str2.length
end
'''

FILES["2826_sorting_three_groups"] = r'''# LeetCode 2826 - Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  n = nums.length
  inf = 10**9
  dp = Array.new(n + 1) { Array.new(4, inf) }
  dp[0][1] = dp[0][2] = dp[0][3] = 0
  (1..n).each do |i|
    v = nums[i - 1]
    (1..3).each do |g|
      cost = v == g ? 0 : 1
      (1..g).each { |prev| dp[i][g] = [dp[i][g], dp[i - 1][prev] + cost].min }
    end
  end
  [dp[n][1], dp[n][2], dp[n][3]].min
end
'''

FILES["2827_number_of_beautiful_integers_in_the_range"] = r'''# LeetCode 2827 - Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

# @param {Integer} low
# @param {Integer} high
# @param {Integer} k
# @return {Integer}
def number_of_beautiful_integers(low, high, k)
  count = lambda do |n|
    return 0 if n < 0
    s = n.to_s
    memo = Array.new(12) { Array.new(45) { Array.new(22) { Array.new(2) { Array.new(2, -1) } } } }
    dfs = lambda do |pos, diff, mod, tight, started|
      if pos == s.length
        return started == 1 && diff == 0 && mod == 0 ? 1 : 0
      end
      cached = memo[pos][diff + 20][mod][tight][started]
      return cached if cached != -1
      up = tight == 1 ? s[pos].ord - 48 : 9
      ans = 0
      (0..up).each do |digit|
        nt = tight == 1 && digit == up ? 1 : 0
        if started == 0
          if digit == 0
            ans += dfs.call(pos + 1, diff, mod, nt, 0)
          else
            nd = diff + (digit.even? ? 1 : -1)
            ans += dfs.call(pos + 1, nd, digit % k, nt, 1)
          end
        else
          nd = diff + (digit.even? ? 1 : -1)
          ans += dfs.call(pos + 1, nd, (mod * 10 + digit) % k, nt, 1)
        end
      end
      memo[pos][diff + 20][mod][tight][started] = ans
      ans
    end
    dfs.call(0, 0, 0, 1, 0)
  end
  count.call(high) - count.call(low - 1)
end
'''

FILES["2828_check_if_a_string_is_an_acronym_of_words"] = r'''# LeetCode 2828 - Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

# @param {String[]} words
# @param {String} s
# @return {Boolean}
def is_acronym(words, s)
  return false if words.length != s.length
  words.each_with_index do |w, i|
    return false if w.nil? || w.empty? || w[0] != s[i]
  end
  true
end
'''

FILES["2829_determine_the_minimum_sum_of_a_k_avoiding_array"] = r'''# LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def minimum_sum(n, k)
  used = {}
  total = 0
  x = 1
  while used.length < n
    unless used[k - x]
      used[x] = true
      total += x
    end
    x += 1
  end
  total
end
'''

FILES["2830_maximize_the_profit_as_the_salesman"] = r'''# LeetCode 2830 - Maximize the Profit as the Salesman
# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

# @param {Integer} n
# @param {Integer[][]} offers
# @return {Integer}
def maximize_the_profit(n, offers)
  by_end = Array.new(n) { [] }
  offers.each { |o| by_end[o[1]] << o }
  dp = Array.new(n + 1, 0)
  (0...n).each do |en|
    dp[en + 1] = dp[en]
    by_end[en].each { |o| dp[en + 1] = [dp[en + 1], dp[o[0]] + o[2]].max }
  end
  dp[n]
end
'''

FILES["2831_find_the_longest_equal_subarray"] = r'''# LeetCode 2831 - Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_equal_subarray(nums, k)
  pos = {}
  nums.each_with_index { |v, i| (pos[v] ||= []) << i }
  ans = 0
  pos.each_value do |p|
    left = 0
    p.each_index do |right|
      left += 1 while p[right] - p[left] - (right - left) > k
      ans = [ans, right - left + 1].max
    end
  end
  ans
end
'''

written = 0
failed = []
for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    if path.parent.exists():
        path.write_text(content, encoding="utf-8")
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            path.write_bytes(data[3:])
        written += 1
    else:
        failed.append(folder)
print(f"batch_d wrote {written} files, failed {failed}")
