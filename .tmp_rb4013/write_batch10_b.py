#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}


def add(folder, body):
    FILES[folder] = body if body.endswith("\n") else body + "\n"


add("2645_minimum_additions_to_make_valid_string", r'''# LeetCode 2645 - Minimum Additions to Make Valid String
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

# @param {String} word
# @return {Integer}
def add_minimum(word)
  ans = 0
  expect = 0
  i = 0
  n = word.length
  while i < n
    need = (97 + expect).chr
    if word[i] == need
      i += 1
    else
      ans += 1
    end
    expect = (expect + 1) % 3
  end
  ans += (3 - expect) % 3
  ans
end
''')

add("2646_minimize_the_total_price_of_the_trips", r'''# LeetCode 2646 - Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @param {Integer[][]} trips
# @return {Integer}
def minimum_total_price(n, edges, price, trips)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  cnt = Array.new(n, 0)
  path = nil
  path = lambda do |u, p, target|
    if u == target
      cnt[u] += 1
      return true
    end
    g[u].each do |v|
      next if v == p
      if path.call(v, u, target)
        cnt[u] += 1
        return true
      end
    end
    false
  end
  trips.each { |a, b| path.call(a, -1, b) }
  dfs = nil
  dfs = lambda do |u, p|
    full = price[u] * cnt[u]
    half = full / 2
    g[u].each do |v|
      next if v == p

      child = dfs.call(v, u)
      full += [child[0], child[1]].min
      half += child[0]
    end
    [full, half]
  end
  res = dfs.call(0, -1)
  [res[0], res[1]].min
end
''')

add("2647_color_the_triangle_red", r'''# LeetCode 2647 - Color the Triangle Red
# https://leetcode.com/problems/color-the-triangle-red/

# @param {Integer} n
# @return {Integer[][]}
def color_red(n)
  ans = []
  (1..n).each { |i| ans << [i, 1] }
  ((n % 2) + 2).step(n, 2) do |i|
    (2...(2 * (n - i) + 3)).each { |j| ans << [i, j] }
  end
  ans
end
''')

add("2648_generate_fibonacci_sequence", r'''# LeetCode 2648 - Generate Fibonacci Sequence
# https://leetcode.com/problems/generate-fibonacci-sequence/

# @return {Enumerator}
def fib_generator
  Enumerator.new do |y|
    a = 0
    b = 1
    loop do
      y << a
      a, b = b, a + b
    end
  end
end
''')

add("2649_nested_array_generator", r'''# LeetCode 2649 - Nested Array Generator
# https://leetcode.com/problems/nested-array-generator/

# @param {Object[]} arr
# @return {Enumerator}
def inorder_traversal(arr)
  Enumerator.new do |y|
    walk = lambda do |a|
      a.each do |x|
        if x.is_a?(Array)
          walk.call(x)
        else
          y << x
        end
      end
    end
    walk.call(arr)
  end
end
''')

add("2650_design_cancellable_function", r'''# LeetCode 2650 - Design Cancellable Function
# https://leetcode.com/problems/design-cancellable-function/

# @param {Enumerator} generator
# @return {Array}
def cancellable(generator)
  cancelled = false
  cancel = lambda { cancelled = true }
  run = lambda do
    enum = generator
    nxt = enum.next
    loop do
      begin
        value = nxt.respond_to?(:call) ? nxt.call : nxt
        nxt = if cancelled
                enum.raise(RuntimeError, "Cancelled")
              else
                enum.feed(value)
                enum.next
              end
      rescue StopIteration => e
        return e.result
      rescue StandardError => e
        begin
          nxt = enum.raise(e)
        rescue StopIteration => se
          return se.result
        end
      end
    end
  end
  [cancel, run]
end
''')

add("2651_calculate_delayed_arrival_time", r'''# LeetCode 2651 - Calculate Delayed Arrival Time
# https://leetcode.com/problems/calculate-delayed-arrival-time/

# @param {Integer} arrival_time
# @param {Integer} delayed_time
# @return {Integer}
def find_delayed_arrival_time(arrival_time, delayed_time)
  (arrival_time + delayed_time) % 24
end
''')

add("2652_sum_multiples", r'''# LeetCode 2652 - Sum Multiples
# https://leetcode.com/problems/sum-multiples/

# @param {Integer} n
# @return {Integer}
def sum_of_multiples(n)
  ans = 0
  (1..n).each { |i| ans += i if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 }
  ans
end
''')

add("2653_sliding_subarray_beauty", r'''# LeetCode 2653 - Sliding Subarray Beauty
# https://leetcode.com/problems/sliding-subarray-beauty/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def get_subarray_beauty(nums, k, x)
  freq = Array.new(101, 0)
  ans = Array.new(nums.length - k + 1, 0)
  nums.each_with_index do |num, i|
    freq[num + 50] += 1
    freq[nums[i - k] + 50] -= 1 if i >= k
    next if i < k - 1

    need = x
    val = 0
    50.times do |j|
      need -= freq[j]
      if need <= 0
        val = j - 50
        break
      end
    end
    ans[i - k + 1] = val
  end
  ans
end
''')

add("2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1", r'''# LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  ones = nums.count(1)
  return n - ones if ones > 0

  best = n + 1
  n.times do |i|
    g = 0
    (i...n).each do |j|
      g = gcd.call(g, nums[j])
      if g == 1
        best = [best, j - i].min
        break
      end
    end
  end
  return -1 if best == n + 1

  best + n - 1
end
''')

add("2655_find_maximal_uncovered_ranges", r'''# LeetCode 2655 - Find Maximal Uncovered Ranges
# https://leetcode.com/problems/find-maximal-uncovered-ranges/

# @param {Integer} n
# @param {Integer[][]} ranges
# @return {Integer[][]}
def find_maximal_uncovered_ranges(n, ranges)
  ranges = ranges.sort_by { |r| r[0] }
  ans = []
  cur = 0
  ranges.each do |r|
    ans << [cur, r[0] - 1] if r[0] > cur
    cur = r[1] + 1 if r[1] + 1 > cur
  end
  ans << [cur, n - 1] if cur < n
  ans
end
''')

add("2656_maximum_sum_with_exactly_k_elements", r'''# LeetCode 2656 - Maximum Sum With Exactly K Elements
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximize_sum(nums, k)
  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  k * mx + k * (k - 1) / 2
end
''')

add("2657_find_the_prefix_common_array_of_two_arrays", r'''# LeetCode 2657 - Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def find_the_prefix_common_array(a, b)
  n = a.length
  seen_a = Array.new(n + 1, false)
  seen_b = Array.new(n + 1, false)
  ans = Array.new(n, 0)
  common = 0
  n.times do |i|
    if seen_b[a[i]]
      common += 1
    end
    seen_a[a[i]] = true
    if seen_a[b[i]]
      common += 1
    end
    seen_b[b[i]] = true
    ans[i] = common
  end
  ans
end
''')

add("2658_maximum_number_of_fish_in_a_grid", r'''# LeetCode 2658 - Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def find_max_fish(grid)
  m = grid.length
  n = grid[0].length
  dfs = nil
  dfs = lambda do |r, c|
    return 0 if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0

    fish = grid[r][c]
    grid[r][c] = 0
    fish + dfs.call(r + 1, c) + dfs.call(r - 1, c) + dfs.call(r, c + 1) + dfs.call(r, c - 1)
  end
  best = 0
  m.times do |i|
    n.times do |j|
      best = [best, dfs.call(i, j)].max if grid[i][j] > 0
    end
  end
  best
end
''')

add("2659_make_array_empty", r'''# LeetCode 2659 - Make Array Empty
# https://leetcode.com/problems/make-array-empty/

# @param {Integer[]} nums
# @return {Integer}
def count_operations_to_empty_array(nums)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  ans = n
  (1...n).each { |i| ans += n - i if idx[i] < idx[i - 1] }
  ans
end
''')

add("2660_determine_the_winner_of_a_bowling_game", r'''# LeetCode 2660 - Determine the Winner of a Bowling Game
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

# @param {Integer[]} player1
# @param {Integer[]} player2
# @return {Integer}
def is_winner(player1, player2)
  score = lambda do |p|
    s = 0
    p.each_with_index do |pins, i|
      mul = 1
      mul = 2 if (i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)
      s += mul * pins
    end
    s
  end
  a = score.call(player1)
  b = score.call(player2)
  return 1 if a > b
  return 2 if b > a

  0
end
''')

add("2661_first_completely_painted_row_or_column", r'''# LeetCode 2661 - First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/

# @param {Integer[]} arr
# @param {Integer[][]} mat
# @return {Integer}
def first_complete_index(arr, mat)
  m = mat.length
  n = mat[0].length
  pos_r = Array.new(m * n + 1, 0)
  pos_c = Array.new(m * n + 1, 0)
  m.times do |i|
    n.times do |j|
      pos_r[mat[i][j]] = i
      pos_c[mat[i][j]] = j
    end
  end
  row_cnt = Array.new(m, 0)
  col_cnt = Array.new(n, 0)
  arr.each_with_index do |val, i|
    r = pos_r[val]
    c = pos_c[val]
    row_cnt[r] += 1
    col_cnt[c] += 1
    return i if row_cnt[r] == n || col_cnt[c] == m
  end
  -1
end
''')

add("2662_minimum_cost_of_a_path_with_special_roads", r'''# LeetCode 2662 - Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

# @param {Integer[]} start
# @param {Integer[]} target
# @param {Integer[][]} special_roads
# @return {Integer}
def minimum_cost(start, target, special_roads)
  points = [start, target]
  special_roads.each do |r|
    points << [r[0], r[1]]
    points << [r[2], r[3]]
  end
  n = points.length
  man = lambda { |a, b| (a[0] - b[0]).abs + (a[1] - b[1]).abs }
  g = Array.new(n) { [] }
  n.times do |i|
    n.times do |j|
      g[i] << [j, man.call(points[i], points[j])] if i != j
    end
  end
  special_roads.each do |r|
    u = v = -1
    points.each_with_index do |p, i|
      u = i if p[0] == r[0] && p[1] == r[1]
      v = i if p[0] == r[2] && p[1] == r[3]
    end
    g[u] << [v, r[4]] if u >= 0 && v >= 0
  end
  dist = Array.new(n, 10**18)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    cost, idx = pq.shift
    next if cost > dist[idx]

    g[idx].each do |to, w|
      if cost + w < dist[to]
        dist[to] = cost + w
        pq << [dist[to], to]
      end
    end
  end
  dist[1]
end
''')

add("2663_lexicographically_smallest_beautiful_string", r'''# LeetCode 2663 - Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_beautiful_string(s, k)
  n = s.length
  b = s.chars
  (n - 1).downto(0) do |i|
    ((b[i].ord + 1)...(97 + k)).each do |code|
      c = code.chr
      next if (i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2])

      b[i] = c
      ((i + 1)...n).each do |j|
        (97...(97 + k)).each do |nc|
          ch = nc.chr
          next if (j > 0 && ch == b[j - 1]) || (j > 1 && ch == b[j - 2])

          b[j] = ch
          break
        end
      end
      return b.join
    end
  end
  ""
end
''')

add("2664_the_knights_tour", r'''# LeetCode 2664 - The Knight's Tour
# https://leetcode.com/problems/the-knights-tour/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
def tour_of_knight(m, n, r, c)
  dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  ans = Array.new(m) { Array.new(n, -1) }
  dfs = nil
  dfs = lambda do |x, y, step|
    ans[x][y] = step
    return true if step == m * n - 1

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      if nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1
        return true if dfs.call(nx, ny, step + 1)
      end
    end
    ans[x][y] = -1
    false
  end
  dfs.call(r, c, 0)
  ans
end
''')

add("2665_counter_ii", r'''# LeetCode 2665 - Counter II
# https://leetcode.com/problems/counter-ii/

# @param {Integer} init
# @return {Hash}
def create_counter(init)
  cur = init
  {
    "increment" => lambda {
      cur += 1
      cur
    },
    "decrement" => lambda {
      cur -= 1
      cur
    },
    "reset" => lambda {
      cur = init
      cur
    }
  }
end
''')

add("2666_allow_one_function_call", r'''# LeetCode 2666 - Allow One Function Call
# https://leetcode.com/problems/allow-one-function-call/

# @param {Proc} fn
# @return {Proc}
def once(fn)
  called = false
  res = nil
  lambda do |*args|
    return nil if called

    called = true
    res = fn.call(*args)
    res
  end
end
''')

add("2667_create_hello_world_function", r'''# LeetCode 2667 - Create Hello World Function
# https://leetcode.com/problems/create-hello-world-function/

# @return {Proc}
def create_hello_world
  lambda { |*_args| "Hello World" }
end
''')

add("2670_find_the_distinct_difference_array", r'''# LeetCode 2670 - Find the Distinct Difference Array
# https://leetcode.com/problems/find-the-distinct-difference-array/

# @param {Integer[]} nums
# @return {Integer[]}
def distinct_difference_array(nums)
  n = nums.length
  suf = Array.new(n + 1, 0)
  seen = {}
  (n - 1).downto(0) do |i|
    seen[nums[i]] = true
    suf[i] = seen.length
  end
  seen = {}
  ans = Array.new(n, 0)
  n.times do |i|
    seen[nums[i]] = true
    ans[i] = seen.length - suf[i + 1]
  end
  ans
end
''')

add("2671_frequency_tracker", r'''# LeetCode 2671 - Frequency Tracker
# https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker
  def initialize
    @freq = Hash.new(0)
    @count = Hash.new(0)
  end

  def add(number)
    old = @freq[number]
    @count[old] -= 1 if old > 0
    @freq[number] = old + 1
    @count[old + 1] += 1
    nil
  end

  def delete_one(number)
    old = @freq[number]
    return if old == 0

    @count[old] -= 1
    @freq[number] = old - 1
    @count[old - 1] += 1 if old - 1 > 0
    nil
  end

  def has_frequency(frequency)
    @count[frequency] > 0
  end
end
''')

add("2672_number_of_adjacent_elements_with_the_same_color", r'''# LeetCode 2672 - Number of Adjacent Elements With the Same Color
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def color_the_array(n, queries)
  colors = Array.new(n, 0)
  ans = Array.new(queries.length, 0)
  same = 0
  queries.each_with_index do |(idx, color), i|
    if colors[idx] != 0
      same -= 1 if idx > 0 && colors[idx] == colors[idx - 1]
      same -= 1 if idx + 1 < n && colors[idx] == colors[idx + 1]
    end
    colors[idx] = color
    same += 1 if idx > 0 && colors[idx] == colors[idx - 1]
    same += 1 if idx + 1 < n && colors[idx] == colors[idx + 1]
    ans[i] = same
  end
  ans
end
''')

add("2673_make_costs_of_paths_equal_in_a_binary_tree", r'''# LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

# @param {Integer} n
# @param {Integer[]} cost
# @return {Integer}
def min_increments(n, cost)
  ans = 0
  (n / 2 - 1).downto(0) do |i|
    l = 2 * i + 1
    r = 2 * i + 2
    ans += (cost[l] - cost[r]).abs
    cost[i] += [cost[l], cost[r]].max
  end
  ans
end
''')

for folder, body in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print("wrote", folder)

print("batch B", len(FILES))
