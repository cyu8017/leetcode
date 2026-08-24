#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


HEAP = r'''
class MinHeap
  def initialize(arr = [])
    @a = arr.dup
    ((@a.length / 2) - 1).downto(0) { |i| down(i) }
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def peek
    @a[0]
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] >= @a[p]

      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && @a[l] < @a[s]
      s = r if r < n && @a[r] < @a[s]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end
'''

add("2570_merge_two_2d_arrays_by_summing_values", r'''
# LeetCode 2570 - Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

# @param {Integer[][]} nums1
# @param {Integer[][]} nums2
# @return {Integer[][]}
def merge_arrays(nums1, nums2)
  ans = []
  i = j = 0
  while i < nums1.length && j < nums2.length
    if nums1[i][0] == nums2[j][0]
      ans << [nums1[i][0], nums1[i][1] + nums2[j][1]]
      i += 1
      j += 1
    elsif nums1[i][0] < nums2[j][0]
      ans << [nums1[i][0], nums1[i][1]]
      i += 1
    else
      ans << [nums2[j][0], nums2[j][1]]
      j += 1
    end
  end
  while i < nums1.length
    ans << [nums1[i][0], nums1[i][1]]
    i += 1
  end
  while j < nums2.length
    ans << [nums2[j][0], nums2[j][1]]
    j += 1
  end
  ans
end
''')

add("2571_minimum_operations_to_reduce_an_integer_to_0", r'''
# LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

# @param {Integer} n
# @return {Integer}
def min_operations(n)
  ans = 0
  while n > 0
    if (n & 3) == 3
      n += 1
      ans += 1
    elsif (n & 1) != 0
      n -= 1
      ans += 1
    else
      n >>= 1
    end
  end
  ans
end
''')

add("2572_count_the_number_of_square_free_subsets", r'''
# LeetCode 2572 - Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

# @param {Integer[]} nums
# @return {Integer}
def square_free_subsets(nums)
  mod = 1_000_000_007
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }

  mask_of = lambda do |x|
    mask = 0
    primes.each_with_index do |p, i|
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
        return -1 if cnt > 1
      end
      mask |= 1 << i if cnt == 1
    end
    mask
  end

  dp = Array.new(1 << 10, 0)
  dp[0] = 1
  freq.each do |x, c|
    next if x == 1

    m = mask_of.call(x)
    next if m < 0

    ((1 << 10) - 1).downto(0) do |state|
      dp[state | m] = (dp[state | m] + dp[state] * c) % mod if (state & m) == 0
    end
  end
  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ones = freq[1]
  mul = 1
  ones.times { mul = mul * 2 % mod }
  ans = ans * mul % mod
  (ans - 1 + mod) % mod
end
''')

add("2573_find_the_string_with_lcp", r'''
# LeetCode 2573 - Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/

# @param {Integer[][]} lcp
# @return {String}
def find_the_string(lcp)
  n = lcp.length
  s = Array.new(n, 0)
  c = 97
  n.times do |i|
    next if s[i] != 0
    return "" if c > 122

    s[i] = c
    (i + 1...n).each { |j| s[j] = c if lcp[i][j] > 0 }
    c += 1
  end
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      v = 0
      if s[i] == s[j]
        v = 1
        v += lcp[i + 1][j + 1] if i + 1 < n && j + 1 < n
      end
      return "" if lcp[i][j] != v
    end
  end
  s.map(&:chr).join
end
''')

add("2574_left_and_right_sum_differences", r'''
# LeetCode 2574 - Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

# @param {Integer[]} nums
# @return {Integer[]}
def left_right_difference(nums)
  total = nums.sum
  ans = Array.new(nums.length, 0)
  left = 0
  nums.each_with_index do |x, i|
    right = total - left - x
    ans[i] = (left - right).abs
    left += x
  end
  ans
end
''')

add("2575_find_the_divisibility_array_of_a_string", r'''
# LeetCode 2575 - Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

# @param {String} word
# @param {Integer} m
# @return {Integer[]}
def divisibility_array(word, m)
  ans = Array.new(word.length, 0)
  cur = 0
  word.each_char.with_index do |ch, i|
    cur = (cur * 10 + (ch.ord - 48)) % m
    ans[i] = 1 if cur == 0
  end
  ans
end
''')

add("2576_find_the_maximum_number_of_marked_indices", r'''
# LeetCode 2576 - Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

# @param {Integer[]} nums
# @return {Integer}
def max_num_of_marked_indices(nums)
  nums = nums.sort
  n = nums.length
  i = 0
  ans = 0
  ((n + 1) / 2...n).each do |j|
    if 2 * nums[i] <= nums[j]
      ans += 2
      i += 1
    end
  end
  ans
end
''')

add("2577_minimum_time_to_visit_a_cell_in_a_grid", '''
# LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
''' + HEAP + r'''
# @param {Integer[][]} grid
# @return {Integer}
def minimum_time(grid)
  return -1 if grid[0][1] > 1 && grid[1][0] > 1

  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, 1 << 30) }
  h = MinHeap.new
  h.push([0, 0, 0])
  dist[0][0] = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until h.empty?
    t, r, c = h.pop
    return t if r == m - 1 && c == n - 1
    next if t > dist[r][c]

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n

      nt = t + 1
      if nt < grid[nr][nc]
        wait = grid[nr][nc] - nt
        wait += 1 if wait.odd?
        nt += wait
      end
      if nt < dist[nr][nc]
        dist[nr][nc] = nt
        h.push([nt, nr, nc])
      end
    end
  end
  -1
end
''')

add("2578_split_with_minimum_sum", r'''
# LeetCode 2578 - Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/

# @param {Integer} num
# @return {Integer}
def split_num(num)
  digits = []
  while num > 0
    digits << (num % 10)
    num /= 10
  end
  digits.sort!
  a = b = 0
  digits.each_with_index do |d, i|
    if i.even?
      a = a * 10 + d
    else
      b = b * 10 + d
    end
  end
  a + b
end
''')

add("2579_count_total_number_of_colored_cells", r'''
# LeetCode 2579 - Count Total Number of Colored Cells
# https://leetcode.com/problems/count-total-number-of-colored-cells/

# @param {Integer} n
# @return {Integer}
def colored_cells(n)
  1 + 2 * n * (n - 1)
end
''')

add("2580_count_ways_to_group_overlapping_ranges", r'''
# LeetCode 2580 - Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

# @param {Integer[][]} ranges
# @return {Integer}
def count_ways(ranges)
  mod = 1_000_000_007
  ranges = ranges.sort_by { |r| r[0] }
  groups = 0
  endi = -1
  ranges.each do |r|
    if r[0] > endi
      groups += 1
      endi = r[1]
    elsif r[1] > endi
      endi = r[1]
    end
  end
  ans = 1
  groups.times { ans = ans * 2 % mod }
  ans
end
''')

add("2581_count_number_of_possible_root_nodes", r'''
# LeetCode 2581 - Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

# @param {Integer[][]} edges
# @param {Integer[][]} guesses
# @param {Integer} k
# @return {Integer}
def root_count(edges, guesses, k)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  guess_set = {}
  guesses.each { |a, b| guess_set["#{a},#{b}"] = true }

  dfs1 = nil
  dfs1 = lambda do |u, p|
    cnt = 0
    g[u].each do |v|
      next if v == p

      cnt += 1 if guess_set["#{u},#{v}"]
      cnt += dfs1.call(v, u)
    end
    cnt
  end

  ans = 0
  dfs2 = nil
  dfs2 = lambda do |u, p, cur|
    ans += 1 if cur >= k
    g[u].each do |v|
      next if v == p

      nxt = cur
      nxt -= 1 if guess_set["#{u},#{v}"]
      nxt += 1 if guess_set["#{v},#{u}"]
      dfs2.call(v, u, nxt)
    end
  end

  dfs2.call(0, -1, dfs1.call(0, -1))
  ans
end
''')

add("2582_pass_the_pillow", r'''
# LeetCode 2582 - Pass the Pillow
# https://leetcode.com/problems/pass-the-pillow/

# @param {Integer} n
# @param {Integer} time
# @return {Integer}
def pass_the_pillow(n, time)
  cycle = 2 * (n - 1)
  t = time % cycle
  return 1 + t if t < n

  n - (t - (n - 1))
end
''')

add("2583_kth_largest_sum_in_a_binary_tree", r'''
# LeetCode 2583 - Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_largest_level_sum(root, k)
  return -1 if root.nil?

  sums = []
  q = [root]
  until q.empty?
    sz = q.length
    s = 0
    sz.times do
      node = q.shift
      s += node.val
      q << node.left if node.left
      q << node.right if node.right
    end
    sums << s
  end
  sums.sort!.reverse!
  return -1 if k > sums.length

  sums[k - 1]
end
''')

add("2584_split_the_array_to_make_coprime_products", r'''
# LeetCode 2584 - Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

# @param {Integer[]} nums
# @return {Integer}
def find_valid_split(nums)
  first = {}
  last = {}

  factorize = lambda do |x, idx|
    p = 2
    while p * p <= x
      if x % p == 0
        first[p] = idx unless first.key?(p)
        last[p] = idx
        x /= p while x % p == 0
      end
      p += 1
    end
    if x > 1
      first[x] = idx unless first.key?(x)
      last[x] = idx
    end
  end

  n = nums.length
  nums.each_with_index { |num, i| factorize.call(num, i) }
  far = 0
  (0...n - 1).each do |i|
    x = nums[i]
    p = 2
    while p * p <= x
      if x % p == 0
        far = last[p] if last[p] > far
        x /= p while x % p == 0
      end
      p += 1
    end
    far = last[x] if x > 1 && last[x] > far
    return i if far == i
  end
  -1
end
''')

add("2585_number_of_ways_to_earn_points", r'''
# LeetCode 2585 - Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

# @param {Integer} target
# @param {Integer[][]} types
# @return {Integer}
def ways_to_reach_target(target, types)
  mod = 1_000_000_007
  dp = Array.new(target + 1, 0)
  dp[0] = 1
  types.each do |count, marks|
    target.downto(0) do |s|
      k = 1
      while k <= count && s - k * marks >= 0
        dp[s] = (dp[s] + dp[s - k * marks]) % mod
        k += 1
      end
    end
  end
  dp[target]
end
''')

add("2586_count_the_number_of_vowel_strings_in_range", r'''
# LeetCode 2586 - Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

# @param {String[]} words
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def vowel_strings(words, left, right)
  is_v = lambda { |c| c == "a" || c == "e" || c == "i" || c == "o" || c == "u" }
  ans = 0
  (left..right).each do |i|
    w = words[i]
    ans += 1 if is_v.call(w[0]) && is_v.call(w[-1])
  end
  ans
end
''')

add("2587_rearrange_array_to_maximize_prefix_score", r'''
# LeetCode 2587 - Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  nums = nums.sort
  s = 0
  ans = 0
  (nums.length - 1).downto(0) do |i|
    s += nums[i]
    break unless s > 0

    ans += 1
  end
  ans
end
''')

add("2588_count_the_number_of_beautiful_subarrays", r'''
# LeetCode 2588 - Count the Number of Beautiful Subarrays
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def beautiful_subarrays(nums)
  freq = Hash.new(0)
  freq[0] = 1
  xorv = 0
  ans = 0
  nums.each do |x|
    xorv ^= x
    ans += freq[xorv]
    freq[xorv] += 1
  end
  ans
end
''')

add("2589_minimum_time_to_complete_all_tasks", r'''
# LeetCode 2589 - Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

# @param {Integer[][]} tasks
# @return {Integer}
def find_minimum_time(tasks)
  tasks = tasks.sort_by { |t| t[1] }
  on = Array.new(2001, false)
  ans = 0
  tasks.each do |start, endi, dur|
    have = 0
    (start..endi).each { |i| have += 1 if on[i] }
    need = dur - have
    i = endi
    while i >= start && need > 0
      unless on[i]
        on[i] = true
        need -= 1
        ans += 1
      end
      i -= 1
    end
  end
  ans
end
''')

add("2590_design_a_todo_list", r'''
# LeetCode 2590 - Design a Todo List
# https://leetcode.com/problems/design-a-todo-list/

class TodoList
  def initialize
    @next_id = 1
    @tasks = {}
    @users = {}
  end

  def add_task(user_id, task_description, due_date, tags)
    tid = @next_id
    @next_id += 1
    @tasks[tid] = {
      id: tid,
      description: task_description,
      due_date: due_date,
      user_id: user_id,
      tags: tags.to_h { |t| [t, true] },
      done: false
    }
    @users[user_id] ||= []
    @users[user_id] << tid
    tid
  end

  def get_all_tasks(user_id)
    return [] unless @users.key?(user_id)

    ids = @users[user_id].dup
    ids.sort_by! { |i| @tasks[i][:due_date] }
    ans = []
    ids.each do |tid|
      ans << @tasks[tid][:description] unless @tasks[tid][:done]
    end
    ans
  end

  def get_tasks_for_tag(user_id, tag)
    return [] unless @users.key?(user_id)

    ids = @users[user_id].dup
    ids.sort_by! { |i| @tasks[i][:due_date] }
    ans = []
    ids.each do |tid|
      tk = @tasks[tid]
      ans << tk[:description] if !tk[:done] && tk[:tags][tag]
    end
    ans
  end

  def complete_task(user_id, task_id)
    tk = @tasks[task_id]
    return if tk.nil? || tk[:user_id] != user_id || tk[:done]

    tk[:done] = true
    nil
  end
end
''')

add("2591_distribute_money_to_maximum_children", r'''
# LeetCode 2591 - Distribute Money to Maximum Children
# https://leetcode.com/problems/distribute-money-to-maximum-children/

# @param {Integer} money
# @param {Integer} children
# @return {Integer}
def dist_money(money, children)
  return -1 if money < children

  money -= children
  ans = money / 7
  ans = children if ans > children
  remain_money = money - ans * 7
  remain_child = children - ans
  if remain_child == 0 && remain_money > 0
    ans -= 1
  elsif remain_child == 1 && remain_money == 3
    ans -= 1
  end
  return 0 if ans < 0

  ans
end
''')

add("2592_maximize_greatness_of_an_array", r'''
# LeetCode 2592 - Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def maximize_greatness(nums)
  nums = nums.sort
  i = 0
  nums.each { |x| i += 1 if x > nums[i] }
  i
end
''')

add("2593_find_score_of_an_array_after_marking_all_elements", r'''
# LeetCode 2593 - Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

# @param {Integer[]} nums
# @return {Integer}
def find_score(nums)
  n = nums.length
  idx = (0...n).to_a.sort_by { |i| [nums[i], i] }
  marked = Array.new(n, false)
  ans = 0
  idx.each do |i|
    next if marked[i]

    ans += nums[i]
    marked[i] = true
    marked[i - 1] = true if i - 1 >= 0
    marked[i + 1] = true if i + 1 < n
  end
  ans
end
''')

add("2594_minimum_time_to_repair_cars", r'''
# LeetCode 2594 - Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars/

# @param {Integer[]} ranks
# @param {Integer} cars
# @return {Integer}
def repair_cars(ranks, cars)
  mn = ranks.min
  lo = 1
  hi = mn * cars * cars

  ok = lambda do |t|
    done = 0
    ranks.each do |r|
      l = 0
      h = cars
      while l < h
        mid = (l + h + 1) / 2
        if r * mid * mid <= t
          l = mid
        else
          h = mid - 1
        end
      end
      done += l
      return true if done >= cars
    end
    done >= cars
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

written = 0
for folder, body in S.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
