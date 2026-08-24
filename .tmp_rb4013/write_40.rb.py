#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2350_shortest_impossible_sequence_of_rolls"] = r'''# LeetCode 2350 - Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

# @param {Integer[]} rolls
# @param {Integer} k
# @return {Integer}
def shortest_sequence(rolls, k)
  seen = {}
  ans = 1
  rolls.each do |r|
    seen[r] = true
    if seen.length == k
      ans += 1
      seen.clear
    end
  end
  ans
end
'''

FILES["2351_first_letter_to_appear_twice"] = r'''# LeetCode 2351 - First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/

# @param {String} s
# @return {String}
def repeated_character(s)
  seen = Array.new(26, false)
  s.each_char do |c|
    i = c.ord - 97
    return c if seen[i]
    seen[i] = true
  end
  0.chr
end
'''

FILES["2352_equal_row_and_column_pairs"] = r'''# LeetCode 2352 - Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

# @param {Integer[][]} grid
# @return {Integer}
def equal_pairs(grid)
  n = grid.length
  freq = Hash.new(0)
  (0...n).each { |i| freq[grid[i].dup] += 1 }
  ans = 0
  (0...n).each do |j|
    col = (0...n).map { |i| grid[i][j] }
    ans += freq[col]
  end
  ans
end
'''

FILES["2353_design_a_food_rating_system"] = r'''# LeetCode 2353 - Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings
  def initialize(foods, cuisines, ratings)
    @cuisine_of = {}
    @rating_of = {}
    @heaps = {}
    foods.each_index do |i|
      @cuisine_of[foods[i]] = cuisines[i]
      @rating_of[foods[i]] = ratings[i]
      @heaps[cuisines[i]] ||= []
      @heaps[cuisines[i]] << foods[i]
    end
  end

  def change_rating(food, new_rating)
    @rating_of[food] = new_rating
  end

  def highest_rated(cuisine)
    foods = @heaps[cuisine]
    foods.sort_by! { |x| [-@rating_of[x], x] }
    foods[0]
  end
end
'''

FILES["2354_number_of_excellent_pairs"] = r'''# LeetCode 2354 - Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_excellent_pairs(nums, k)
  uniq = {}
  nums.each { |x| uniq[x] = true }
  cnt = Array.new(32, 0)
  bit_count = lambda do |x|
    c = 0
    while x != 0
      x &= x - 1
      c += 1
    end
    c
  end
  uniq.each_key { |x| cnt[bit_count.call(x)] += 1 }
  ans = 0
  (0...32).each do |i|
    (0...32).each { |j| ans += cnt[i] * cnt[j] if i + j >= k }
  end
  ans
end
'''

FILES["2355_maximum_number_of_books_you_can_take"] = r'''# LeetCode 2355 - Maximum Number of Books You Can Take
# https://leetcode.com/problems/maximum-number-of-books-you-can-take/

# @param {Integer[]} books
# @return {Integer}
def maximum_books(books)
  n = books.length
  dp = Array.new(n, 0)
  stack = []
  interval_sum = lambda do |l, r, h|
    width = r - l + 1
    return width * (2 * h - width + 1) / 2 if h >= width
    h * (h + 1) / 2
  end
  ans = 0
  (0...n).each do |i|
    stack.pop while !stack.empty? && books[stack[-1]] >= books[i] - (i - stack[-1])
    if stack.empty?
      dp[i] = interval_sum.call(0, i, books[i])
    else
      j = stack[-1]
      dp[i] = dp[j] + interval_sum.call(j + 1, i, books[i])
    end
    ans = dp[i] if dp[i] > ans
    stack << i
  end
  ans
end
'''

FILES["2357_make_array_zero_by_subtracting_equal_amounts"] = r'''# LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  seen = {}
  nums.each { |x| seen[x] = true if x > 0 }
  seen.length
end
'''

FILES["2358_maximum_number_of_groups_entering_a_competition"] = r'''# LeetCode 2358 - Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

# @param {Integer[]} grades
# @return {Integer}
def maximum_groups(grades)
  n = grades.length
  k = 0
  k += 1 while (k + 1) * (k + 2) / 2 <= n
  k
end
'''

FILES["2359_find_closest_node_to_given_two_nodes"] = r'''# LeetCode 2359 - Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

# @param {Integer[]} edges
# @param {Integer} node1
# @param {Integer} node2
# @return {Integer}
def closest_meeting_node(edges, node1, node2)
  n = edges.length
  dist = lambda do |start|
    d = Array.new(n, -1)
    cur = start
    step = 0
    while cur != -1 && d[cur] == -1
      d[cur] = step
      cur = edges[cur]
      step += 1
    end
    d
  end
  d1 = dist.call(node1)
  d2 = dist.call(node2)
  ans = -1
  best = Float::INFINITY
  (0...n).each do |i|
    next if d1[i] == -1 || d2[i] == -1
    mx = [d1[i], d2[i]].max
    if mx < best
      best = mx
      ans = i
    end
  end
  ans
end
'''

FILES["2360_longest_cycle_in_a_graph"] = r'''# LeetCode 2360 - Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/

# @param {Integer[]} edges
# @return {Integer}
def longest_cycle(edges)
  n = edges.length
  vis = Array.new(n, false)
  ans = -1
  (0...n).each do |i|
    next if vis[i]
    dist = {}
    cur = i
    step = 0
    while cur != -1 && !vis[cur]
      vis[cur] = true
      dist[cur] = step
      cur = edges[cur]
      step += 1
    end
    if cur != -1 && dist.key?(cur)
      cand = step - dist[cur]
      ans = cand if cand > ans
    end
  end
  ans
end
'''

FILES["2361_minimum_costs_using_the_train_line"] = r'''# LeetCode 2361 - Minimum Costs Using the Train Line
# https://leetcode.com/problems/minimum-costs-using-the-train-line/

# @param {Integer[]} regular
# @param {Integer[]} express
# @param {Integer} express_cost
# @return {Integer[]}
def minimum_costs(regular, express, express_cost)
  n = regular.length
  ans = Array.new(n, 0)
  reg = 0
  exp = express_cost
  (0...n).each do |i|
    next_reg = [reg + regular[i], exp + express[i]].min
    next_exp = [reg + regular[i] + express_cost, exp + express[i]].min
    reg = next_reg
    exp = next_exp
    ans[i] = [reg, exp].min
  end
  ans
end
'''

FILES["2363_merge_similar_items"] = r'''# LeetCode 2363 - Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/

# @param {Integer[][]} items1
# @param {Integer[][]} items2
# @return {Integer[][]}
def merge_similar_items(items1, items2)
  mp = Hash.new(0)
  items1.each { |it| mp[it[0]] += it[1] }
  items2.each { |it| mp[it[0]] += it[1] }
  mp.keys.sort.map { |k| [k, mp[k]] }
end
'''

FILES["2364_count_number_of_bad_pairs"] = r'''# LeetCode 2364 - Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

# @param {Integer[]} nums
# @return {Integer}
def count_bad_pairs(nums)
  n = nums.length
  total = n * (n - 1) / 2
  freq = Hash.new(0)
  good = 0
  nums.each_with_index do |x, i|
    key = x - i
    good += freq[key]
    freq[key] += 1
  end
  total - good
end
'''

FILES["2365_task_scheduler_ii"] = r'''# LeetCode 2365 - Task Scheduler II
# https://leetcode.com/problems/task-scheduler-ii/

# @param {Integer[]} tasks
# @param {Integer} space
# @return {Integer}
def task_scheduler_ii(tasks, space)
  nxt = {}
  day = 0
  tasks.each do |t|
    day = nxt[t] if nxt.key?(t) && nxt[t] > day
    day += 1
    nxt[t] = day + space
  end
  day
end
'''

FILES["2366_minimum_replacements_to_sort_the_array"] = r'''# LeetCode 2366 - Minimum Replacements to Sort the Array
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_replacement(nums)
  ans = 0
  n = nums.length
  prev = nums[n - 1]
  (n - 2).downto(0) do |i|
    if nums[i] <= prev
      prev = nums[i]
      next
    end
    parts = (nums[i] + prev - 1) / prev
    ans += parts - 1
    prev = nums[i] / parts
  end
  ans
end
'''

FILES["2367_number_of_arithmetic_triplets"] = r'''# LeetCode 2367 - Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

# @param {Integer[]} nums
# @param {Integer} diff
# @return {Integer}
def arithmetic_triplets(nums, diff)
  seen = {}
  nums.each { |x| seen[x] = true }
  ans = 0
  nums.each { |x| ans += 1 if seen[x + diff] && seen[x + 2 * diff] }
  ans
end
'''

FILES["2368_reachable_nodes_with_restrictions"] = r'''# LeetCode 2368 - Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} restricted
# @return {Integer}
def reachable_nodes(n, edges, restricted)
  ban = {}
  restricted.each { |x| ban[x] = true }
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0
  vis = Array.new(n, false)
  q = [0]
  vis[0] = true
  until q.empty?
    u = q.shift
    ans += 1
    g[u].each do |v|
      if !vis[v] && !ban.key?(v)
        vis[v] = true
        q << v
      end
    end
  end
  ans
end
'''

FILES["2369_check_if_there_is_a_valid_partition_for_the_array"] = r'''# LeetCode 2369 - Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

# @param {Integer[]} nums
# @return {Boolean}
def valid_partition(nums)
  n = nums.length
  dp = Array.new(n + 1, false)
  dp[0] = true
  (1..n).each do |i|
    dp[i] = true if i >= 2 && nums[i - 1] == nums[i - 2] && dp[i - 2]
    dp[i] = true if i >= 3 && nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3]
    dp[i] = true if i >= 3 && nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3]
  end
  dp[n]
end
'''

FILES["2370_longest_ideal_subsequence"] = r'''# LeetCode 2370 - Longest Ideal Subsequence
# https://leetcode.com/problems/longest-ideal-subsequence/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_ideal_string(s, k)
  dp = Array.new(26, 0)
  ans = 0
  s.each_char do |ch|
    c = ch.ord - 97
    best = 0
    (0...26).each { |p| best = dp[p] if (c - p).abs <= k && dp[p] > best }
    dp[c] = best + 1
    ans = dp[c] if dp[c] > ans
  end
  ans
end
'''

FILES["2371_minimize_maximum_value_in_a_grid"] = r'''# LeetCode 2371 - Minimize Maximum Value in a Grid
# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer[][]}
def min_score(grid)
  m = grid.length
  n = grid[0].length
  arr = []
  (0...m).each do |i|
    (0...n).each { |j| arr << [grid[i][j], i, j] }
  end
  arr.sort_by! { |x| x[0] }
  row_max = Array.new(m, 0)
  col_max = Array.new(n, 0)
  ans = Array.new(m) { Array.new(n, 0) }
  arr.each do |_, i, j|
    val = [row_max[i], col_max[j]].max + 1
    ans[i][j] = val
    row_max[i] = val
    col_max[j] = val
  end
  ans
end
'''

for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {folder}")
print(f"done {len(FILES)}")
