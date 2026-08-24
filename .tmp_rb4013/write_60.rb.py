#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2373_largest_local_values_in_a_matrix"] = r'''# LeetCode 2373 - Largest Local Values in a Matrix
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

# @param {Integer[][]} grid
# @return {Integer[][]}
def largest_local(grid)
  n = grid.length
  ans = Array.new(n - 2) { Array.new(n - 2, 0) }
  (0...n - 2).each do |i|
    (0...n - 2).each do |j|
      mx = 0
      (i...i + 3).each do |r|
        (j...j + 3).each { |c| mx = grid[r][c] if grid[r][c] > mx }
      end
      ans[i][j] = mx
    end
  end
  ans
end
'''

FILES["2374_node_with_highest_edge_score"] = r'''# LeetCode 2374 - Node With Highest Edge Score
# https://leetcode.com/problems/node-with-highest-edge-score/

# @param {Integer[]} edges
# @return {Integer}
def edge_score(edges)
  n = edges.length
  score = Array.new(n, 0)
  (0...n).each { |i| score[edges[i]] += i }
  ans = 0
  (1...n).each { |i| ans = i if score[i] > score[ans] }
  ans
end
'''

FILES["2375_construct_smallest_number_from_di_string"] = r'''# LeetCode 2375 - Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

# @param {String} pattern
# @return {String}
def smallest_number(pattern)
  n = pattern.length
  ans = (0..n).map { |i| (49 + i).chr }
  i = 0
  while i < n
    if pattern[i] == "I"
      i += 1
      next
    end
    j = i
    j += 1 while j < n && pattern[j] == "D"
    l = i
    r = j
    while l < r
      ans[l], ans[r] = ans[r], ans[l]
      l += 1
      r -= 1
    end
    i = j
  end
  ans.join
end
'''

FILES["2376_count_special_integers"] = r'''# LeetCode 2376 - Count Special Integers
# https://leetcode.com/problems/count-special-integers/

# @param {Integer} n
# @return {Integer}
def count_special_numbers(n)
  s = n.to_s
  m = s.length
  ans = 0
  perm = 9
  (1...m).each do |i|
    ans += perm
    perm *= 10 - i
  end
  used = Array.new(10, false)
  (0...m).each do |i|
    start = i == 0 ? 1 : 0
    digit = s[i].ord - 48
    (start...digit).each do |d|
      next if used[d]
      rem = 10 - (i + 1)
      ways = 1
      (i + 1...m).each do
        ways *= rem
        rem -= 1
      end
      ans += ways
    end
    return ans if used[digit]
    used[digit] = true
  end
  ans + 1
end
'''

FILES["2378_choose_edges_to_maximize_score_in_a_tree"] = r'''# LeetCode 2378 - Choose Edges to Maximize Score in a Tree
# https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

# @param {Integer[][]} edges
# @return {Integer}
def max_score(edges)
  n = edges.length
  g = Array.new(n) { [] }
  (1...n).each do |i|
    p = edges[i][0]
    w = edges[i][1]
    g[p] << [i, w]
  end
  dfs = lambda do |u|
    base = 0
    best_gain = 0
    g[u].each do |to, w|
      child = dfs.call(to)
      base += child[0]
      gain = child[1] + w - child[0]
      best_gain = gain if gain > best_gain
    end
    [base + best_gain, base]
  end
  dfs.call(0)[0]
end
'''

FILES["2379_minimum_recolors_to_get_k_consecutive_black_blocks"] = r'''# LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

# @param {String} blocks
# @param {Integer} k
# @return {Integer}
def minimum_recolors(blocks, k)
  white = 0
  (0...k).each { |i| white += 1 if blocks[i] == "W" }
  ans = white
  (k...blocks.length).each do |i|
    white += 1 if blocks[i] == "W"
    white -= 1 if blocks[i - k] == "W"
    ans = white if white < ans
  end
  ans
end
'''

FILES["2380_time_needed_to_rearrange_a_binary_string"] = r'''# LeetCode 2380 - Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

# @param {String} s
# @return {Integer}
def seconds_to_remove_occurrences(s)
  ans = 0
  zeros = 0
  s.each_char do |c|
    if c == "0"
      zeros += 1
    elsif zeros > 0
      ans = [ans + 1, zeros].max
    end
  end
  ans
end
'''

FILES["2381_shifting_letters_ii"] = r'''# LeetCode 2381 - Shifting Letters II
# https://leetcode.com/problems/shifting-letters-ii/

# @param {String} s
# @param {Integer[][]} shifts
# @return {String}
def shifting_letters(s, shifts)
  n = s.length
  diff = Array.new(n + 1, 0)
  shifts.each do |sh|
    d = sh[2] == 0 ? -1 : 1
    diff[sh[0]] += d
    diff[sh[1] + 1] -= d
  end
  arr = s.chars
  cur = 0
  (0...n).each do |i|
    cur = (cur + diff[i]) % 26
    cur += 26 if cur < 0
    arr[i] = (97 + (arr[i].ord - 97 + cur) % 26).chr
  end
  arr.join
end
'''

FILES["2382_maximum_segment_sum_after_removals"] = r'''# LeetCode 2382 - Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

# @param {Integer[]} nums
# @param {Integer[]} remove_queries
# @return {Integer[]}
def maximum_segment_sum(nums, remove_queries)
  n = nums.length
  parent = (0...n).to_a
  ssum = Array.new(n, 0)
  active = Array.new(n, false)
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    parent[rb] = ra
    ssum[ra] += ssum[rb]
  end
  ans = Array.new(n, 0)
  best = 0
  (n - 1).downto(0) do |i|
    ans[i] = best
    idx = remove_queries[i]
    active[idx] = true
    ssum[idx] = nums[idx]
    unite.call(idx, idx - 1) if idx > 0 && active[idx - 1]
    unite.call(idx, idx + 1) if idx + 1 < n && active[idx + 1]
    cand = ssum[find.call(idx)]
    best = cand if cand > best
  end
  ans
end
'''

FILES["2383_minimum_hours_of_training_to_win_a_competition"] = r'''# LeetCode 2383 - Minimum Hours of Training to Win a Competition
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

# @param {Integer} initial_energy
# @param {Integer} initial_experience
# @param {Integer[]} energy
# @param {Integer[]} experience
# @return {Integer}
def min_number_of_hours(initial_energy, initial_experience, energy, experience)
  ans = 0
  en = initial_energy
  ex = initial_experience
  energy.each_index do |i|
    if en <= energy[i]
      need = energy[i] - en + 1
      ans += need
      en += need
    end
    if ex <= experience[i]
      need = experience[i] - ex + 1
      ans += need
      ex += need
    end
    en -= energy[i]
    ex += experience[i]
  end
  ans
end
'''

FILES["2384_largest_palindromic_number"] = r'''# LeetCode 2384 - Largest Palindromic Number
# https://leetcode.com/problems/largest-palindromic-number/

# @param {String} num
# @return {String}
def largest_palindromic(num)
  freq = Array.new(10, 0)
  num.each_char { |ch| freq[ch.ord - 48] += 1 }
  left = ""
  9.downto(0) do |d|
    pairs = freq[d] / 2
    left += d.to_s * pairs
    freq[d] %= 2
  end
  mid = ""
  9.downto(0) do |d|
    if freq[d] > 0
      mid = d.to_s
      break
    end
  end
  return mid.empty? ? "0" : mid if left.empty?
  return mid.empty? ? "0" : mid if left[0] == "0"
  left + mid + left.reverse
end
'''

FILES["2385_amount_of_time_for_binary_tree_to_be_infected"] = r'''# LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} start
# @return {Integer}
def amount_of_time(root, start)
  g = {}
  build = lambda do |node, parent|
    return if node.nil?
    if parent
      (g[node.val] ||= []) << parent.val
      (g[parent.val] ||= []) << node.val
    end
    build.call(node.left, node)
    build.call(node.right, node)
  end
  build.call(root, nil)
  ans = 0
  vis = { start => true }
  q = [[start, 0]]
  until q.empty?
    cur, d = q.shift
    ans = d if d > ans
    (g[cur] || []).each do |nxt|
      unless vis[nxt]
        vis[nxt] = true
        q << [nxt, d + 1]
      end
    end
  end
  ans
end
'''

FILES["2386_find_the_k_sum_of_an_array"] = r'''# LeetCode 2386 - Find the K-Sum of an Array
# https://leetcode.com/problems/find-the-k-sum-of-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_sum(nums, k)
  total = 0
  n = nums.length
  abs_nums = Array.new(n, 0)
  (0...n).each do |i|
    if nums[i] >= 0
      total += nums[i]
      abs_nums[i] = nums[i]
    else
      abs_nums[i] = -nums[i]
    end
  end
  abs_nums.sort!
  h = []
  push = lambda do |item|
    h << item
    i = h.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if h[p][0] >= h[i][0]
      h[p], h[i] = h[i], h[p]
      i = p
    end
  end
  pop = lambda do
    top = h[0]
    last = h.pop
    unless h.empty?
      h[0] = last
      i = 0
      loop do
        largest = i
        l = i * 2 + 1
        r = i * 2 + 2
        largest = l if l < h.length && h[l][0] > h[largest][0]
        largest = r if r < h.length && h[r][0] > h[largest][0]
        break if largest == i
        h[largest], h[i] = h[i], h[largest]
        i = largest
      end
    end
    top
  end
  push.call([total, 0])
  (k - 1).times do
    cur = pop.call
    s = cur[0]
    i = cur[1]
    next if i >= abs_nums.length
    push.call([s - abs_nums[i], i + 1])
    push.call([s - abs_nums[i] + abs_nums[i - 1], i + 1]) if i > 0
  end
  h[0][0]
end
'''

FILES["2387_median_of_a_row_wise_sorted_matrix"] = r'''# LeetCode 2387 - Median of a Row Wise Sorted Matrix
# https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def matrix_median(grid)
  m = grid.length
  n = grid[0].length
  lo = 1
  hi = 1_000_000
  need = (m * n) / 2 + 1
  count_le = lambda do |x|
    cnt = 0
    grid.each do |row|
      l = 0
      r = n
      while l < r
        mid = (l + r) >> 1
        if row[mid] <= x
          l = mid + 1
        else
          r = mid
        end
      end
      cnt += l
    end
    cnt
  end
  while lo < hi
    mid = (lo + hi) >> 1
    if count_le.call(mid) >= need
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
'''

FILES["2389_longest_subsequence_with_limited_sum"] = r'''# LeetCode 2389 - Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def answer_queries(nums, queries)
  nums = nums.sort
  (1...nums.length).each { |i| nums[i] += nums[i - 1] }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 0
    hi = nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if nums[mid] <= q
        lo = mid + 1
      else
        hi = mid
      end
    end
    ans[i] = lo
  end
  ans
end
'''

FILES["2390_removing_stars_from_a_string"] = r'''# LeetCode 2390 - Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/

# @param {String} s
# @return {String}
def remove_stars(s)
  stack = []
  s.each_char do |c|
    if c == "*"
      stack.pop
    else
      stack << c
    end
  end
  stack.join
end
'''

FILES["2391_minimum_amount_of_time_to_collect_garbage"] = r'''# LeetCode 2391 - Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

# @param {String[]} garbage
# @param {Integer[]} travel
# @return {Integer}
def garbage_collection(garbage, travel)
  ans = 0
  last_m = 0
  last_p = 0
  last_g = 0
  garbage.each_with_index do |g, i|
    ans += g.length
    g.each_char do |c|
      if c == "M"
        last_m = i
      elsif c == "P"
        last_p = i
      else
        last_g = i
      end
    end
  end
  pref = Array.new(travel.length + 1, 0)
  travel.each_index { |i| pref[i + 1] = pref[i] + travel[i] }
  ans + pref[last_m] + pref[last_p] + pref[last_g]
end
'''

FILES["2392_build_a_matrix_with_conditions"] = r'''# LeetCode 2392 - Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/

# @param {Integer} k
# @param {Integer[][]} row_conditions
# @param {Integer[][]} col_conditions
# @return {Integer[][]}
def build_matrix(k, row_conditions, col_conditions)
  topo = lambda do |conds|
    g = Array.new(k + 1) { [] }
    indeg = Array.new(k + 1, 0)
    conds.each do |c|
      g[c[0]] << c[1]
      indeg[c[1]] += 1
    end
    q = (1..k).select { |i| indeg[i] == 0 }
    order = []
    until q.empty?
      u = q.shift
      order << u
      g[u].each do |v|
        indeg[v] -= 1
        q << v if indeg[v] == 0
      end
    end
    return nil if order.length != k
    order
  end
  row_order = topo.call(row_conditions)
  col_order = topo.call(col_conditions)
  return [] if row_order.nil? || col_order.nil?
  row_pos = Array.new(k + 1, 0)
  col_pos = Array.new(k + 1, 0)
  (0...k).each do |i|
    row_pos[row_order[i]] = i
    col_pos[col_order[i]] = i
  end
  ans = Array.new(k) { Array.new(k, 0) }
  (1..k).each { |v| ans[row_pos[v]][col_pos[v]] = v }
  ans
end
'''

FILES["2393_count_strictly_increasing_subarrays"] = r'''# LeetCode 2393 - Count Strictly Increasing Subarrays
# https://leetcode.com/problems/count-strictly-increasing-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_subarrays(nums)
  ans = 0
  length = 0
  nums.each_index do |i|
    if i > 0 && nums[i] > nums[i - 1]
      length += 1
    else
      length = 1
    end
    ans += length
  end
  ans
end
'''

FILES["2395_find_subarrays_with_equal_sum"] = r'''# LeetCode 2395 - Find Subarrays With Equal Sum
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

# @param {Integer[]} nums
# @return {Boolean}
def find_subarrays(nums)
  seen = {}
  (0...nums.length - 1).each do |i|
    s = nums[i] + nums[i + 1]
    return true if seen[s]
    seen[s] = true
  end
  false
end
'''

for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {folder}")
print(f"done {len(FILES)}")
