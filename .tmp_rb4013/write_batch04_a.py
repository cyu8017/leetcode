#!/usr/bin/env python3
from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end
"""

LIST = """class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end
"""


def hdr(num, title, slug):
    return f"# LeetCode {num} - {title}\n# https://leetcode.com/problems/{slug}/\n\n"


files = {}

files["0980_unique_paths_iii"] = hdr("0980", "Unique Paths III", "unique-paths-iii") + """# @param {Integer[][]} grid
# @return {Integer}
def unique_paths_iii(grid)
  m = grid.length
  n = grid[0].length
  empty = 0
  sr = sc = 0
  m.times do |i|
    n.times do |j|
      empty += 1 if grid[i][j] != -1
      if grid[i][j] == 1
        sr = i
        sc = j
      end
    end
  end
  ans = 0

  dfs = lambda do |r, c, remain|
    if grid[r][c] == 2
      ans += 1 if remain == 1
      return
    end
    temp = grid[r][c]
    grid[r][c] = -1
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      dfs.call(nr, nc, remain - 1) if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1
    end
    grid[r][c] = temp
  end

  dfs.call(sr, sc, empty)
  ans
end
"""

files["0981_time_based_key_value_store"] = hdr("0981", "Time Based Key-Value Store", "time-based-key-value-store") + """class TimeMap
  def initialize
    @store = Hash.new { |h, k| h[k] = [] }
  end

  def set(key, value, timestamp)
    @store[key] << [timestamp, value]
  end

  def get(key, timestamp)
    arr = @store[key]
    return "" if arr.empty?

    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid][0] <= timestamp
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo.positive? ? arr[lo - 1][1] : ""
  end
end
"""

files["0982_triples_with_bitwise_and_equal_to_zero"] = hdr("0982", "Triples with Bitwise AND Equal To Zero", "triples-with-bitwise-and-equal-to-zero") + """# @param {Integer[]} nums
# @return {Integer}
def count_triplets(nums)
  cnt = Hash.new(0)
  nums.each do |a|
    nums.each { |b| cnt[a & b] += 1 }
  end
  ans = 0
  nums.each do |c|
    cnt.each { |ab, times| ans += times if (ab & c).zero? }
  end
  ans
end
"""

files["0983_minimum_cost_for_tickets"] = hdr("0983", "Minimum Cost For Tickets", "minimum-cost-for-tickets") + """# @param {Integer[]} days
# @param {Integer[]} costs
# @return {Integer}
def mincost_tickets(days, costs)
  dayset = days.to_h { |d| [d, true] }
  last = days[-1]
  dp = Array.new(last + 1, 0)
  (1..last).each do |d|
    if dayset[d]
      dp[d] = [
        dp[d - 1] + costs[0],
        dp[[0, d - 7].max] + costs[1],
        dp[[0, d - 30].max] + costs[2]
      ].min
    else
      dp[d] = dp[d - 1]
    end
  end
  dp[last]
end
"""

files["0984_string_without_aaa_or_bbb"] = hdr("0984", "String Without AAA or BBB", "string-without-aaa-or-bbb") + """# @param {Integer} a
# @param {Integer} b
# @return {String}
def str_without3a3b(a, b)
  ans = []
  while a > 0 || b > 0
    write_a = if ans.length >= 2 && ans[-1] == ans[-2]
                ans[-1] == "b"
              else
                a >= b
              end
    if write_a
      ans << "a"
      a -= 1
    else
      ans << "b"
      b -= 1
    end
  end
  ans.join
end
"""

files["0985_sum_of_even_numbers_after_queries"] = hdr("0985", "Sum of Even Numbers After Queries", "sum-of-even-numbers-after-queries") + """# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(nums, queries)
  even = nums.select { |x| x.even? }.sum
  ans = []
  queries.each do |val, i|
    even -= nums[i] if nums[i].even?
    nums[i] += val
    even += nums[i] if nums[i].even?
    ans << even
  end
  ans
end
"""

files["0986_interval_list_intersections"] = hdr("0986", "Interval List Intersections", "interval-list-intersections") + """# @param {Integer[][]} first_list
# @param {Integer[][]} second_list
# @return {Integer[][]}
def interval_intersection(first_list, second_list)
  i = j = 0
  ans = []
  while i < first_list.length && j < second_list.length
    lo = [first_list[i][0], second_list[j][0]].max
    hi = [first_list[i][1], second_list[j][1]].min
    ans << [lo, hi] if lo <= hi
    if first_list[i][1] < second_list[j][1]
      i += 1
    else
      j += 1
    end
  end
  ans
end
"""

files["0987_vertical_order_traversal_of_a_binary_tree"] = hdr("0987", "Vertical Order Traversal of a Binary Tree", "vertical-order-traversal-of-a-binary-tree") + TREE + """
# @param {TreeNode} root
# @return {Integer[][]}
def vertical_traversal(root)
  nodes = []
  dfs = lambda do |node, row, col|
    return if node.nil?

    nodes << [col, row, node.val]
    dfs.call(node.left, row + 1, col - 1)
    dfs.call(node.right, row + 1, col + 1)
  end
  dfs.call(root, 0, 0)
  nodes.sort!
  ans = Hash.new { |h, k| h[k] = [] }
  nodes.each { |col, _, val| ans[col] << val }
  ans.keys.sort.map { |c| ans[c] }
end
"""

files["0988_smallest_string_starting_from_leaf"] = hdr("0988", "Smallest String Starting From Leaf", "smallest-string-starting-from-leaf") + TREE + """
# @param {TreeNode} root
# @return {String}
def smallest_from_leaf(root)
  best = "~"
  dfs = lambda do |node, path|
    return if node.nil?

    path = (97 + node.val).chr + path
    if node.left.nil? && node.right.nil?
      best = path if path < best
      return
    end
    dfs.call(node.left, path)
    dfs.call(node.right, path)
  end
  dfs.call(root, "")
  best
end
"""

files["0989_add_to_array_form_of_integer"] = hdr("0989", "Add to Array-Form of Integer", "add-to-array-form-of-integer") + """# @param {Integer[]} num
# @param {Integer} k
# @return {Integer[]}
def add_to_array_form(num, k)
  i = num.length - 1
  while k > 0 || i >= 0
    if i >= 0
      k += num[i]
      num[i] = k % 10
      i -= 1
    else
      num.unshift(k % 10)
    end
    k /= 10
  end
  num
end
"""

files["0990_satisfiability_of_equality_equations"] = hdr("0990", "Satisfiability of Equality Equations", "satisfiability-of-equality-equations") + """# @param {String[]} equations
# @return {Boolean}
def equations_possible(equations)
  parent = (0...26).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  equations.each do |eq|
    parent[find.call(eq[0].ord - 97)] = find.call(eq[3].ord - 97) if eq[1] == "="
  end
  equations.each do |eq|
    return false if eq[1] == "!" && find.call(eq[0].ord - 97) == find.call(eq[3].ord - 97)
  end
  true
end
"""

files["0991_broken_calculator"] = hdr("0991", "Broken Calculator", "broken-calculator") + """# @param {Integer} start_value
# @param {Integer} target
# @return {Integer}
def broken_calc(start_value, target)
  ans = 0
  while target > start_value
    if target.odd?
      target += 1
    else
      target /= 2
    end
    ans += 1
  end
  ans + start_value - target
end
"""

files["0992_subarrays_with_k_different_integers"] = hdr("0992", "Subarrays with K Different Integers", "subarrays-with-k-different-integers") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_with_k_distinct(nums, k)
  at_most = lambda do |m|
    count = Hash.new(0)
    left = ans = 0
    nums.each_with_index do |x, right|
      count[x] += 1
      while count.length > m
        count[nums[left]] -= 1
        count.delete(nums[left]) if count[nums[left]].zero?
        left += 1
      end
      ans += right - left + 1
    end
    ans
  end
  at_most.call(k) - at_most.call(k - 1)
end
"""

files["0993_cousins_in_binary_tree"] = hdr("0993", "Cousins in Binary Tree", "cousins-in-binary-tree") + TREE + """
# @param {TreeNode} root
# @param {Integer} x
# @param {Integer} y
# @return {Boolean}
def is_cousins(root, x, y)
  info = {}
  dfs = lambda do |node, parent, depth|
    return if node.nil?

    info[node.val] = [depth, parent] if node.val == x || node.val == y
    dfs.call(node.left, node, depth + 1)
    dfs.call(node.right, node, depth + 1)
  end
  dfs.call(root, nil, 0)
  info[x][0] == info[y][0] && !info[x][1].equal?(info[y][1])
end
"""

files["0994_rotting_oranges"] = hdr("0994", "Rotting Oranges", "rotting-oranges") + """# @param {Integer[][]} grid
# @return {Integer}
def oranges_rotting(grid)
  m = grid.length
  n = grid[0].length
  queue = []
  fresh = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 2
        queue << [i, j]
      elsif grid[i][j] == 1
        fresh += 1
      end
    end
  end
  minutes = 0
  while !queue.empty? && fresh.positive?
    queue.length.times do
      r, c = queue.shift
      [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
        next unless nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1

        grid[nr][nc] = 2
        fresh -= 1
        queue << [nr, nc]
      end
    end
    minutes += 1
  end
  fresh.zero? ? minutes : -1
end
"""

files["0995_minimum_number_of_k_consecutive_bit_flips"] = hdr("0995", "Minimum Number of K Consecutive Bit Flips", "minimum-number-of-k-consecutive-bit-flips") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_k_bit_flips(nums, k)
  n = nums.length
  flip = Array.new(n, 0)
  ans = flipped = 0
  nums.each_with_index do |bit, i|
    flipped ^= flip[i - k] if i >= k
    next unless bit == flipped
    return -1 if i + k > n

    ans += 1
    flipped ^= 1
    flip[i] = 1
  end
  ans
end
"""

files["0996_number_of_squareful_arrays"] = hdr("0996", "Number of Squareful Arrays", "number-of-squareful-arrays") + """# @param {Integer[]} nums
# @return {Integer}
def num_squareful_perms(nums)
  count = Hash.new(0)
  nums.each { |x| count[x] += 1 }
  graph = {}
  count.each_key { |x| graph[x] = [] }
  count.each_key do |a|
    count.each_key do |b|
      s = a + b
      r = Integer.sqrt(s)
      graph[a] << b if r * r == s
    end
  end
  ans = 0
  dfs = lambda do |x, remain|
    if remain.zero?
      ans += 1
      return
    end
    graph[x].each do |y|
      next unless count[y].positive?

      count[y] -= 1
      dfs.call(y, remain - 1)
      count[y] += 1
    end
  end
  count.each_key do |x|
    count[x] -= 1
    dfs.call(x, nums.length - 1)
    count[x] += 1
  end
  ans
end
"""

files["0997_find_the_town_judge"] = hdr("0997", "Find the Town Judge", "find-the-town-judge") + """# @param {Integer} n
# @param {Integer[][]} trust
# @return {Integer}
def find_judge(n, trust)
  score = Array.new(n + 1, 0)
  trust.each do |a, b|
    score[a] -= 1
    score[b] += 1
  end
  (1..n).each { |i| return i if score[i] == n - 1 }
  -1
end
"""

files["0998_maximum_binary_tree_ii"] = hdr("0998", "Maximum Binary Tree II", "maximum-binary-tree-ii") + TREE + """
# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_max_tree(root, val)
  if root.nil? || val > root.val
    node = TreeNode.new(val)
    node.left = root
    return node
  end
  root.right = insert_into_max_tree(root.right, val)
  root
end
"""

files["0999_available_captures_for_rook"] = hdr("0999", "Available Captures for Rook", "available-captures-for-rook") + """# @param {Character[][]} board
# @return {Integer}
def num_rook_captures(board)
  m = board.length
  n = board[0].length
  r = c = -1
  m.times do |i|
    board[i].length.times do |j|
      if board[i][j] == "R"
        r = i
        c = j
      end
    end
  end
  return 0 if r < 0

  ans = 0
  [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
    i = r + dr
    j = c + dc
    while i >= 0 && i < m && j >= 0 && j < board[i].length
      break if board[i][j] == "B"

      if board[i][j] == "p"
        ans += 1
        break
      end
      i += dr
      j += dc
    end
  end
  ans
end
"""

files["2000_reverse_prefix_of_word"] = hdr("2000", "Reverse Prefix of Word", "reverse-prefix-of-word") + """# @param {String} word
# @param {Character} ch
# @return {String}
def reverse_prefix(word, ch)
  i = word.index(ch)
  return word if i.nil?

  word[0..i].reverse + word[i + 1..]
end
"""

files["2001_number_of_pairs_of_interchangeable_rectangles"] = hdr("2001", "Number of Pairs of Interchangeable Rectangles", "number-of-pairs-of-interchangeable-rectangles") + """# @param {Integer[][]} rectangles
# @return {Integer}
def interchangeable_rectangles(rectangles)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  freq = {}
  ans = 0
  rectangles.each do |w, h|
    g = gcd.call(w, h)
    key = [w / g, h / g]
    f = freq[key] || 0
    ans += f
    freq[key] = f + 1
  end
  ans
end
"""

files["2002_maximum_product_of_the_length_of_two_palindromic_subsequences"] = hdr("2002", "Maximum Product of the Length of Two Palindromic Subsequences", "maximum-product-of-the-length-of-two-palindromic-subsequences") + """# @param {String} s
# @return {Integer}
def max_product(s)
  pal_len = lambda do |mask|
    chars = []
    s.each_char.with_index { |ch, i| chars << ch if (mask & (1 << i)) != 0 }
    l = 0
    r = chars.length - 1
    while l < r
      return 0 if chars[l] != chars[r]

      l += 1
      r -= 1
    end
    chars.length
  end
  n = s.length
  best = 0
  total = 1 << n
  (1...total).each do |mask1|
    len1 = pal_len.call(mask1)
    next if len1.zero?

    remain = (total - 1) ^ mask1
    mask2 = remain
    while mask2 > 0
      len2 = pal_len.call(mask2)
      best = len1 * len2 if len2.positive? && len1 * len2 > best
      mask2 = (mask2 - 1) & remain
    end
  end
  best
end
"""

files["2003_smallest_missing_genetic_value_in_each_subtree"] = hdr("2003", "Smallest Missing Genetic Value in Each Subtree", "smallest-missing-genetic-value-in-each-subtree") + """# @param {Integer[]} parents
# @param {Integer[]} nums
# @return {Integer[]}
def smallest_missing_value_subtree(parents, nums)
  n = parents.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parents[i]] << i }
  ans = Array.new(n, 1)
  one = nums.index(1)
  return ans if one.nil?

  seen = {}
  collect = lambda do |u|
    return if seen[nums[u]]

    seen[nums[u]] = true
    children[u].each { |v| collect.call(v) }
  end
  miss = 1
  node = one
  prev = -1
  while node != -1
    children[node].each { |v| collect.call(v) if v != prev }
    seen[nums[node]] = true
    miss += 1 while seen[miss]
    ans[node] = miss
    prev = node
    node = parents[node]
  end
  ans
end
"""

files["2005_subtree_removal_game_with_fibonacci_tree"] = hdr("2005", "Subtree Removal Game with Fibonacci Tree", "subtree-removal-game-with-fibonacci-tree") + """# @param {Integer} n
# @return {Boolean}
def find_game_winner(n)
  n % 6 != 1
end
"""


def write_all(mapping):
    written = 0
    for folder, content in mapping.items():
        path = root / folder / "solution.rb"
        path.write_bytes(content.encode("utf-8"))
        written += 1
    print(f"wrote {written}")


if __name__ == "__main__":
    write_all(files)
