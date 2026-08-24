#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}


def add(folder, body):
    FILES[folder] = body if body.endswith("\n") else body + "\n"


add("2702_minimum_operations_to_make_numbers_non_positive", r'''# LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

# @param {Integer[]} nums
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def min_operations(nums, x, y)
  lo = 0
  hi = 0
  nums.each do |v|
    a = (v + y - 1) / y
    b = (v + x - 1) / x
    hi = [hi, a, b].max
  end
  hi += nums.length
  ok = lambda do |ops|
    extra = 0
    nums.each do |v|
      remain = v - ops * y
      extra += (remain + (x - y) - 1) / (x - y) if remain > 0
    end
    extra <= ops
  end
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("2703_return_length_of_arguments_passed", r'''# LeetCode 2703 - Return Length of Arguments Passed
# https://leetcode.com/problems/return-length-of-arguments-passed/

# @return {Integer}
def arguments_length(*args)
  args.length
end
''')

add("2704_to_be_or_not_to_be", r'''# LeetCode 2704 - To Be Or Not To Be
# https://leetcode.com/problems/to-be-or-not-to-be/

# @param {Object} val
# @return {Hash}
def expect(val)
  {
    "toBe" => lambda do |other|
      return true if val == other

      raise "Not Equal"
    end,
    "notToBe" => lambda do |other|
      return true if val != other

      raise "Equal"
    end
  }
end
''')

add("2705_compact_object", r'''# LeetCode 2705 - Compact Object
# https://leetcode.com/problems/compact-object/

# @param {Object} obj
# @return {Object}
def compact_object(obj)
  if obj.is_a?(Array)
    out = []
    obj.each do |x|
      v = compact_object(x)
      out << v if v
    end
    return out
  end
  if obj.is_a?(Hash)
    out = {}
    obj.each do |k, val|
      v = compact_object(val)
      out[k] = v if v
    end
    return out
  end
  obj
end
''')

add("2706_buy_two_chocolates", r'''# LeetCode 2706 - Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/

# @param {Integer[]} prices
# @param {Integer} money
# @return {Integer}
def buy_choco(prices, money)
  prices = prices.sort
  cost = prices[0] + prices[1]
  cost <= money ? money - cost : money
end
''')

add("2707_extra_characters_in_a_string", r'''# LeetCode 2707 - Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/

# @param {String} s
# @param {String[]} dictionary
# @return {Integer}
def min_extra_char(s, dictionary)
  dct = {}
  dictionary.each { |w| dct[w] = true }
  n = s.length
  dp = Array.new(n + 1, n)
  dp[0] = 0
  n.times do |i|
    dp[i + 1] = [dp[i + 1], dp[i] + 1].min
    ((i + 1)..n).each do |j|
      dp[j] = [dp[j], dp[i]].min if dct[s[i...j]]
    end
  end
  dp[n]
end
''')

add("2708_maximum_strength_of_a_group", r'''# LeetCode 2708 - Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/

# @param {Integer[]} nums
# @return {Integer}
def max_strength(nums)
  nums = nums.sort
  n = nums.length
  return nums[0] if n == 1

  prod = 1
  used = false
  i = 0
  while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0
    prod *= nums[i] * nums[i + 1]
    used = true
    i += 2
  end
  neg_left = i < n && nums[i] < 0
  while i < n
    if nums[i] > 0
      prod *= nums[i]
      used = true
    end
    i += 1
  end
  unless used
    if neg_left
      nums.each { |x| return 0 if x == 0 }
      return nums[n - 1]
    end
    return 0
  end
  prod
end
''')

add("2709_greatest_common_divisor_traversal", r'''# LeetCode 2709 - Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/

# @param {Integer[]} nums
# @return {Boolean}
def can_traverse_all_pairs(nums)
  n = nums.length
  return true if n == 1

  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  parent = (0..mx).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  has = Array.new(mx + 1, false)
  nums.each do |x|
    return false if x == 1

    has[x] = true
  end
  sieve = Array.new(mx + 1, 0)
  (2..mx).each do |i|
    next unless sieve[i] == 0

    i.step(mx, i) do |j|
      sieve[j] = i if sieve[j] == 0
      unite.call(i, j) if has[j]
    end
  end
  root = find.call(nums[0])
  nums.each { |x| return false if find.call(x) != root }
  true
end
''')

add("2710_remove_trailing_zeros_from_a_string", r'''# LeetCode 2710 - Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

# @param {String} num
# @return {String}
def remove_trailing_zeros(num)
  last = num.length - 1
  last -= 1 while last >= 0 && num[last] == "0"
  num[0..last]
end
''')

add("2711_difference_of_number_of_distinct_values_on_diagonals", r'''# LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

# @param {Integer[][]} grid
# @return {Integer[][]}
def difference_of_distinct_values(grid)
  m = grid.length
  n = grid[0].length
  ans = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      top = {}
      bot = {}
      r = i - 1
      c = j - 1
      while r >= 0 && c >= 0
        top[grid[r][c]] = true
        r -= 1
        c -= 1
      end
      r = i + 1
      c = j + 1
      while r < m && c < n
        bot[grid[r][c]] = true
        r += 1
        c += 1
      end
      ans[i][j] = (top.length - bot.length).abs
    end
  end
  ans
end
''')

add("2712_minimum_cost_to_make_all_characters_equal", r'''# LeetCode 2712 - Minimum Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

# @param {String} s
# @return {Integer}
def minimum_cost(s)
  n = s.length
  ans = 0
  (1...n).each { |i| ans += [i, n - i].min if s[i] != s[i - 1] }
  ans
end
''')

add("2713_maximum_strictly_increasing_cells_in_a_matrix", r'''# LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

# @param {Integer[][]} mat
# @return {Integer}
def max_increasing_cells(mat)
  m = mat.length
  n = mat[0].length
  cells = []
  m.times { |i| n.times { |j| cells << [mat[i][j], i, j] } }
  cells.sort_by! { |x| x[0] }
  row_max = Array.new(m, 0)
  col_max = Array.new(n, 0)
  dp = Array.new(m) { Array.new(n, 0) }
  ans = 0
  i = 0
  while i < cells.length
    j = i
    j += 1 while j < cells.length && cells[j][0] == cells[i][0]
    buf = []
    (i...j).each do |k|
      r = cells[k][1]
      c = cells[k][2]
      best = [row_max[r], col_max[c]].max
      dp[r][c] = best + 1
      ans = [ans, dp[r][c]].max
      buf << [r, c, dp[r][c]]
    end
    buf.each do |r, c, v|
      row_max[r] = [row_max[r], v].max
      col_max[c] = [col_max[c], v].max
    end
    i = j
  end
  ans
end
''')

add("2714_find_shortest_path_with_k_hops", r'''# LeetCode 2714 - Find Shortest Path With K Hops
# https://leetcode.com/problems/find-shortest-path-with-k-hops/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} s
# @param {Integer} d
# @param {Integer} k
# @return {Integer}
def shortest_path_with_hops(n, edges, s, d, k)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  inf = 10**18
  dist = Array.new(n) { Array.new(k + 1, inf) }
  dist[s][0] = 0
  pq = [[0, s, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    cd, u, hops = pq.shift
    return cd if u == d
    next if cd > dist[u][hops]

    g[u].each do |to, w|
      if cd + w < dist[to][hops]
        dist[to][hops] = cd + w
        pq << [dist[to][hops], to, hops]
      end
      if hops < k && cd < dist[to][hops + 1]
        dist[to][hops + 1] = cd
        pq << [cd, to, hops + 1]
      end
    end
  end
  -1
end
''')

add("2715_timeout_cancellation", r'''# LeetCode 2715 - Timeout Cancellation
# https://leetcode.com/problems/timeout-cancellation/

# @param {Proc} fn
# @param {Object[]} args
# @param {Integer} t
# @return {Proc}
def cancellable(fn, args, t)
  cancelled = false
  Thread.new do
    sleep(t / 1000.0)
    fn.call(*args) unless cancelled
  end
  lambda { cancelled = true }
end
''')

add("2716_minimize_string_length", r'''# LeetCode 2716 - Minimize String Length
# https://leetcode.com/problems/minimize-string-length/

# @param {String} s
# @return {Integer}
def minimized_string_length(s)
  s.chars.uniq.length
end
''')

add("2717_semi_ordered_permutation", r'''# LeetCode 2717 - Semi-Ordered Permutation
# https://leetcode.com/problems/semi-ordered-permutation/

# @param {Integer[]} nums
# @return {Integer}
def semi_ordered_permutation(nums)
  n = nums.length
  p1 = 0
  pn = 0
  nums.each_with_index do |x, i|
    p1 = i if x == 1
    pn = i if x == n
  end
  ans = p1 + (n - 1 - pn)
  ans -= 1 if p1 > pn
  ans
end
''')

add("2718_sum_of_matrix_after_queries", r'''# LeetCode 2718 - Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer}
def matrix_sum_queries(n, queries)
  row_done = Array.new(n, false)
  col_done = Array.new(n, false)
  rows_left = n
  cols_left = n
  ans = 0
  (queries.length - 1).downto(0) do |i|
    typ, idx, val = queries[i]
    if typ == 0
      unless row_done[idx]
        ans += val * cols_left
        row_done[idx] = true
        rows_left -= 1
      end
    else
      unless col_done[idx]
        ans += val * rows_left
        col_done[idx] = true
        cols_left -= 1
      end
    end
  end
  ans
end
''')

add("2719_count_of_integers", r'''# LeetCode 2719 - Count of Integers
# https://leetcode.com/problems/count-of-integers/

# @param {String} num1
# @param {String} num2
# @param {Integer} min_sum
# @param {Integer} max_sum
# @return {Integer}
def count(num1, num2, min_sum, max_sum)
  mod = 1_000_000_007
  dec = lambda do |s|
    arr = s.chars
    i = arr.length - 1
    while i >= 0 && arr[i] == "0"
      arr[i] = "9"
      i -= 1
    end
    arr[i] = (arr[i].ord - 1).chr if i >= 0
    j = 0
    j += 1 while j < arr.length - 1 && arr[j] == "0"
    arr[j..].join
  end
  dp = lambda do |s|
    memo = {}
    dfs = nil
    dfs = lambda do |pos, sm, tight|
      return 0 if sm > max_sum
      return sm >= min_sum ? 1 : 0 if pos == s.length

      key = [pos, sm, tight]
      return memo[key] if memo.key?(key)

      up = tight ? s[pos].ord - 48 : 9
      res = 0
      (0..up).each do |d|
        res = (res + dfs.call(pos + 1, sm + d, tight && d == up)) % mod
      end
      memo[key] = res
      res
    end
    dfs.call(0, 0, true)
  end
  (dp.call(num2) - dp.call(dec.call(num1)) + mod) % mod
end
''')

add("2721_execute_asynchronous_functions_in_parallel", r'''# LeetCode 2721 - Execute Asynchronous Functions in Parallel
# https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

# @param {Proc[]} functions
# @return {Array}
def promise_all(functions)
  n = functions.length
  return [] if n == 0

  ans = Array.new(n)
  n.times do |i|
    result = functions[i].call
    ans[i] = result.respond_to?(:call) ? result.call : result
  end
  ans
end
''')

add("2722_join_two_arrays_by_id", r'''# LeetCode 2722 - Join Two Arrays by ID
# https://leetcode.com/problems/join-two-arrays-by-id/

# @param {Hash[]} arr1
# @param {Hash[]} arr2
# @return {Hash[]}
def join(arr1, arr2)
  by_id = {}
  arr1.each { |obj| by_id[obj["id"]] = obj.dup }
  arr2.each do |obj|
    if by_id.key?(obj["id"])
      by_id[obj["id"]].merge!(obj)
    else
      by_id[obj["id"]] = obj.dup
    end
  end
  by_id.values.sort_by { |o| o["id"] }
end
''')

add("2723_add_two_promises", r'''# LeetCode 2723 - Add Two Promises
# https://leetcode.com/problems/add-two-promises/

# @param {Object} promise1
# @param {Object} promise2
# @return {Object}
def add_two_promises(promise1, promise2)
  resolve = lambda do |p|
    p.respond_to?(:call) ? p.call : p
  end
  resolve.call(promise1) + resolve.call(promise2)
end
''')

add("2724_sort_by", r'''# LeetCode 2724 - Sort By
# https://leetcode.com/problems/sort-by/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def sort_by(arr, fn)
  arr.sort_by { |x| fn.call(x) }
end
''')

add("2725_interval_cancellation", r'''# LeetCode 2725 - Interval Cancellation
# https://leetcode.com/problems/interval-cancellation/

# @param {Proc} fn
# @param {Object[]} args
# @param {Integer} t
# @return {Proc}
def cancellable(fn, args, t)
  cancelled = false
  fn.call(*args)
  Thread.new do
    until cancelled
      sleep(t / 1000.0)
      fn.call(*args) unless cancelled
    end
  end
  lambda { cancelled = true }
end
''')

add("2726_calculator_with_method_chaining", r'''# LeetCode 2726 - Calculator with Method Chaining
# https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator
  def initialize(value)
    @val = value.to_f
  end

  def add(value)
    @val += value
    self
  end

  def subtract(value)
    @val -= value
    self
  end

  def multiply(value)
    @val *= value
    self
  end

  def divide(value)
    raise "Division by zero is not allowed" if value == 0

    @val /= value
    self
  end

  def power(value)
    @val **= value
    self
  end

  def get_result
    @val
  end
end

# @param {Float} value
# @return {Calculator}
def calculator(value)
  Calculator.new(value)
end
''')

for folder, body in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print("wrote", folder)

print("batch D", len(FILES))
