#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end
"""

LISTN = """class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end
"""


def header(num, title, slug):
    return (
        f"# LeetCode {num} - {title}\n"
        f"# https://leetcode.com/problems/{slug}/\n\n"
    )


FILES = {}

FILES["0780_reaching_points"] = header("0780", "Reaching Points", "reaching-points") + """# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Boolean}
def reaching_points(sx, sy, tx, ty)
  while tx >= sx && ty >= sy
    return true if tx == sx && ty == sy
    break if tx == ty

    if tx > ty
      if ty > sy
        tx %= ty
      else
        return (tx - sx) % ty == 0
      end
    elsif tx > sx
      ty %= tx
    else
      return (ty - sy) % tx == 0
    end
  end
  tx == sx && ty == sy
end
"""

FILES["0781_rabbits_in_forest"] = header("0781", "Rabbits in Forest", "rabbits-in-forest") + """# @param {Integer[]} answers
# @return {Integer}
def num_rabbits(answers)
  total = 0
  answers.tally.each do |answer, count|
    group = answer + 1
    groups = (count + group - 1) / group
    total += groups * group
  end
  total
end
"""

FILES["0782_transform_to_chessboard"] = header("0782", "Transform to Chessboard", "transform-to-chessboard") + """# @param {Integer[][]} board
# @return {Integer}
def moves_to_chessboard(board)
  n = board.length
  n.times do |i|
    n.times do |j|
      if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0
        return -1
      end
    end
  end

  row_sum = board[0].sum
  col_sum = board.sum { |row| row[0] }
  return -1 unless (n / 2) <= row_sum && row_sum <= (n + 1) / 2
  return -1 unless (n / 2) <= col_sum && col_sum <= (n + 1) / 2

  row_swap = (0...n).count { |i| board[0][i] != i % 2 }
  col_swap = (0...n).count { |i| board[i][0] != i % 2 }
  if n.odd?
    row_swap = n - row_swap if row_swap.odd?
    col_swap = n - col_swap if col_swap.odd?
  else
    row_swap = [row_swap, n - row_swap].min
    col_swap = [col_swap, n - col_swap].min
  end
  (row_swap + col_swap) / 2
end
"""

FILES["0783_minimum_distance_between_bst_nodes"] = header("0783", "Minimum Distance Between BST Nodes", "minimum-distance-between-bst-nodes") + TREE + """
# @param {TreeNode} root
# @return {Integer}
def min_diff_in_bst(root)
  prev = nil
  best = Float::INFINITY

  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    best = [best, node.val - prev].min unless prev.nil?
    prev = node.val
    inorder.call(node.right)
  end

  inorder.call(root)
  best.to_i
end
"""

FILES["0784_letter_case_permutation"] = header("0784", "Letter Case Permutation", "letter-case-permutation") + """# @param {String} s
# @return {String[]}
def letter_case_permutation(s)
  result = [""]
  s.each_char do |ch|
    result = if ch.match?(/[A-Za-z]/)
               result.flat_map { |prefix| [prefix + ch.downcase, prefix + ch.upcase] }
             else
               result.map { |prefix| prefix + ch }
             end
  end
  result
end
"""

FILES["0785_is_graph_bipartite"] = header("0785", "Is Graph Bipartite?", "is-graph-bipartite") + """# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
  color = Array.new(graph.length, -1)

  dfs = lambda do |node, c|
    color[node] = c
    graph[node].each do |nei|
      if color[nei] == -1
        return false unless dfs.call(nei, c ^ 1)
      elsif color[nei] == c
        return false
      end
    end
    true
  end

  graph.length.times do |node|
    return false if color[node] == -1 && !dfs.call(node, 0)
  end
  true
end
"""

FILES["0786_k_th_smallest_prime_fraction"] = header("0786", "K-th Smallest Prime Fraction", "k-th-smallest-prime-fraction") + """class MinHeap
  def initialize
    @a = []
  end

  def push(item)
    @a << item
    i = @a.size - 1
    while i.positive?
      p = (i - 1) / 2
      break if @a[p] <= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= @a.size

      smallest = r < @a.size && @a[r] < @a[l] ? r : l
      break if @a[i] <= @a[smallest]

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer[]}
def kth_smallest_prime_fraction(arr, k)
  n = arr.length
  heap = MinHeap.new
  (0...n - 1).each { |i| heap.push([arr[i].to_f / arr[-1], i, n - 1]) }
  (k - 1).times do
    _, i, j = heap.pop
    heap.push([arr[i].to_f / arr[j - 1], i, j - 1]) if j - 1 > i
  end
  _, i, j = heap.pop
  [arr[i], arr[j]]
end
"""

FILES["0787_cheapest_flights_within_k_stops"] = header("0787", "Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops") + """# @param {Integer} n
# @param {Integer[][]} flights
# @param {Integer} src
# @param {Integer} dst
# @param {Integer} k
# @return {Integer}
def find_cheapest_price(n, flights, src, dst, k)
  dist = Array.new(n, Float::INFINITY)
  dist[src] = 0
  (k + 1).times do
    nxt = dist.dup
    flights.each do |u, v, price|
      nxt[v] = dist[u] + price if dist[u] != Float::INFINITY && dist[u] + price < nxt[v]
    end
    dist = nxt
  end
  dist[dst] == Float::INFINITY ? -1 : dist[dst].to_i
end
"""

FILES["0788_rotated_digits"] = header("0788", "Rotated Digits", "rotated-digits") + """# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
  valid = %w[0 1 2 5 6 8 9]
  changing = %w[2 5 6 9]
  count = 0
  (1..n).each do |num|
    s = num.to_s.chars
    count += 1 if s.all? { |ch| valid.include?(ch) } && s.any? { |ch| changing.include?(ch) }
  end
  count
end
"""

FILES["0789_escape_the_ghosts"] = header("0789", "Escape The Ghosts", "escape-the-ghosts") + """# @param {Integer[][]} ghosts
# @param {Integer[]} target
# @return {Boolean}
def escape_ghosts(ghosts, target)
  target_dist = target[0].abs + target[1].abs
  ghosts.all? { |gx, gy| (gx - target[0]).abs + (gy - target[1]).abs > target_dist }
end
"""

FILES["0790_domino_and_tromino_tiling"] = header("0790", "Domino and Tromino Tiling", "domino-and-tromino-tiling") + """# @param {Integer} n
# @return {Integer}
def num_tilings(n)
  mod = 10**9 + 7
  return 1 if n == 1
  return 2 if n == 2

  dp = Array.new(n + 1, 0)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 5
  (4..n).each { |i| dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod }
  dp[n]
end
"""

FILES["0791_custom_sort_string"] = header("0791", "Custom Sort String", "custom-sort-string") + """# @param {String} order
# @param {String} s
# @return {String}
def custom_sort_string(order, s)
  counts = Hash.new(0)
  s.each_char { |ch| counts[ch] += 1 }
  parts = []
  order.each_char do |ch|
    if counts[ch].positive?
      parts << (ch * counts[ch])
      counts[ch] = 0
    end
  end
  counts.each { |ch, count| parts << (ch * count) if count.positive? }
  parts.join
end
"""

FILES["0792_number_of_matching_subsequences"] = header("0792", "Number of Matching Subsequences", "number-of-matching-subsequences") + """# @param {String} s
# @param {String[]} words
# @return {Integer}
def num_matching_subseq(s, words)
  waiting = Hash.new { |h, k| h[k] = [] }
  words.each { |word| waiting[word[0]] << [word, 1] }

  count = 0
  s.each_char do |ch|
    advance = waiting[ch]
    waiting[ch] = []
    advance.each do |word, idx|
      if idx == word.length
        count += 1
      else
        waiting[word[idx]] << [word, idx + 1]
      end
    end
  end
  count
end
"""

FILES["0793_preimage_size_of_factorial_zeroes_function"] = header("0793", "Preimage Size of Factorial Zeroes Function", "preimage-size-of-factorial-zeroes-function") + """# @param {Integer} k
# @return {Integer}
def preimage_size_fzf(k)
  zeros = lambda do |x|
    count = 0
    while x.positive?
      x /= 5
      count += x
    end
    count
  end

  first_ge = lambda do |target|
    lo = 0
    hi = 5 * (target + 1)
    while lo < hi
      mid = (lo + hi) / 2
      if zeros.call(mid) < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  zeros.call(first_ge.call(k)) == k ? 5 : 0
end
"""

FILES["0794_valid_tic_tac_toe_state"] = header("0794", "Valid Tic-Tac-Toe State", "valid-tic-tac-toe-state") + """# @param {String[]} board
# @return {Boolean}
def valid_tic_tac_toe(board)
  flat = board.join
  x_count = flat.count("X")
  o_count = flat.count("O")
  return false unless [x_count, x_count - 1].include?(o_count)

  win = lambda do |player|
    lines = board.dup
    3.times { |c| lines << (0...3).map { |r| board[r][c] }.join }
    lines << board[0][0] + board[1][1] + board[2][2]
    lines << board[0][2] + board[1][1] + board[2][0]
    lines.any? { |line| line == player * 3 }
  end

  x_win = win.call("X")
  o_win = win.call("O")
  return false if x_win && o_win
  return false if x_win && x_count != o_count + 1
  return false if o_win && x_count != o_count

  true
end
"""

FILES["0795_number_of_subarrays_with_bounded_maximum"] = header("0795", "Number of Subarrays with Bounded Maximum", "number-of-subarrays-with-bounded-maximum") + """# @param {Integer[]} nums
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def num_subarray_bounded_max(nums, left, right)
  count_at_most = lambda do |bound|
    ans = 0
    cur = 0
    nums.each do |num|
      if num <= bound
        cur += 1
        ans += cur
      else
        cur = 0
      end
    end
    ans
  end

  count_at_most.call(right) - count_at_most.call(left - 1)
end
"""

FILES["0796_rotate_string"] = header("0796", "Rotate String", "rotate-string") + """# @param {String} s
# @param {String} goal
# @return {Boolean}
def rotate_string(s, goal)
  s.length == goal.length && (s + s).include?(goal)
end
"""

FILES["0797_all_paths_from_source_to_target"] = header("0797", "All Paths From Source to Target", "all-paths-from-source-to-target") + """# @param {Integer[][]} graph
# @return {Integer[][]}
def all_paths_source_target(graph)
  target = graph.length - 1
  answer = []

  dfs = lambda do |node, path|
    if node == target
      answer << path.dup
      return
    end
    graph[node].each do |nei|
      path << nei
      dfs.call(nei, path)
      path.pop
    end
  end

  dfs.call(0, [0])
  answer
end
"""

FILES["0798_smallest_rotation_with_highest_score"] = header("0798", "Smallest Rotation with Highest Score", "smallest-rotation-with-highest-score") + """# @param {Integer[]} nums
# @return {Integer}
def best_rotation(nums)
  n = nums.length
  change = Array.new(n, 1)
  nums.each_with_index { |value, i| change[(i - value + 1) % n] -= 1 }
  (1...n).each { |i| change[i] += change[i - 1] }
  change.index(change.max)
end
"""

FILES["0799_champagne_tower"] = header("0799", "Champagne Tower", "champagne-tower") + """# @param {Integer} poured
# @param {Integer} query_row
# @param {Integer} query_glass
# @return {Float}
def champagne_tower(poured, query_row, query_glass)
  row = [poured.to_f]
  query_row.times do |r|
    next_row = Array.new(r + 2, 0.0)
    row.each_with_index do |amount, i|
      overflow = (amount - 1.0) / 2.0
      if overflow > 0
        next_row[i] += overflow
        next_row[i + 1] += overflow
      end
    end
    row = next_row
  end
  [1.0, row[query_glass]].min
end
"""

FILES["0800_similar_rgb_color"] = header("0800", "Similar RGB Color", "similar-rgb-color") + """# @param {String} color
# @return {String}
def similar_rgb(color)
  closest = lambda do |component|
    value = component.to_i(16)
    rounded = (value + 8) / 17
    format("%x%x", rounded, rounded)
  end

  "#" + closest.call(color[1, 2]) + closest.call(color[3, 2]) + closest.call(color[5, 2])
end
"""

FILES["0801_minimum_swaps_to_make_sequences_increasing"] = header("0801", "Minimum Swaps To Make Sequences Increasing", "minimum-swaps-to-make-sequences-increasing") + """# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_swap(nums1, nums2)
  n = nums1.length
  swap = Array.new(n, n)
  keep = Array.new(n, n)
  swap[0] = 1
  keep[0] = 0
  (1...n).each do |i|
    if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]
      keep[i] = keep[i - 1]
      swap[i] = swap[i - 1] + 1
    end
    if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]
      keep[i] = [keep[i], swap[i - 1]].min
      swap[i] = [swap[i], keep[i - 1] + 1].min
    end
  end
  [swap[-1], keep[-1]].min
end
"""

FILES["0802_find_eventual_safe_states"] = header("0802", "Find Eventual Safe States", "find-eventual-safe-states") + """# @param {Integer[][]} graph
# @return {Integer[]}
def eventual_safe_nodes(graph)
  n = graph.length
  color = Array.new(n, 0)

  dfs = lambda do |node|
    return color[node] == 2 if color[node] != 0

    color[node] = 1
    graph[node].each { |nei| return false unless dfs.call(nei) }
    color[node] = 2
    true
  end

  (0...n).select { |i| dfs.call(i) }
end
"""

FILES["0803_bricks_falling_when_hit"] = header("0803", "Bricks Falling When Hit", "bricks-falling-when-hit") + """# @param {Integer[][]} grid
# @param {Integer[][]} hits
# @return {Integer[]}
def hit_bricks(grid, hits)
  m = grid.length
  n = grid[0].length
  roof = m * n
  parent = (0..roof).to_a
  size = Array.new(roof + 1, 1)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb

    parent[ra] = rb
    size[rb] += size[ra]
  end

  idx = ->(r, c) { r * n + c }

  neighbors = lambda do |r, c|
    [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].select do |nr, nc|
      nr >= 0 && nr < m && nc >= 0 && nc < n
    end
  end

  status = grid.map(&:dup)
  hits.each { |r, c| status[r][c] = 0 }

  m.times do |r|
    n.times do |c|
      next if status[r][c] == 0

      union.call(idx.call(r, c), roof) if r == 0
      neighbors.call(r, c).each do |nr, nc|
        union.call(idx.call(r, c), idx.call(nr, nc)) if status[nr][nc] == 1
      end
    end
  end

  answer = Array.new(hits.length, 0)
  (hits.length - 1).downto(0) do |i|
    r, c = hits[i]
    next if grid[r][c] == 0

    prev = size[find.call(roof)]
    status[r][c] = 1
    union.call(idx.call(r, c), roof) if r == 0
    neighbors.call(r, c).each do |nr, nc|
      union.call(idx.call(r, c), idx.call(nr, nc)) if status[nr][nc] == 1
    end
    curr = size[find.call(roof)]
    answer[i] = [0, curr - prev - 1].max
  end
  answer
end
"""

FILES["0804_unique_morse_code_words"] = header("0804", "Unique Morse Code Words", "unique-morse-code-words") + """# @param {String[]} words
# @return {Integer}
def unique_morse_representations(words)
  codes = %w[
    .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. ---
    .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
  ]
  words.map { |word| word.chars.map { |ch| codes[ch.ord - 97] }.join }.uniq.length
end
"""

FILES["0805_split_array_with_same_average"] = header("0805", "Split Array With Same Average", "split-array-with-same-average") + """# @param {Integer[]} nums
# @return {Boolean}
def split_array_same_average(nums)
  n = nums.length
  total = nums.sum
  nums = nums.sort
  memo = {}

  find = lambda do |target, count, index|
    key = [target, count, index]
    return memo[key] if memo.key?(key)
    if count == 0
      return memo[key] = (target == 0)
    end
    if index == n || count + index > n || target < 0
      return memo[key] = false
    end

    memo[key] = find.call(target - nums[index], count - 1, index + 1) ||
                find.call(target, count, index + 1)
  end

  (1...n).each do |size|
    return true if (total * size) % n == 0 && find.call(total * size / n, size, 0)
  end
  false
end
"""

FILES["0806_number_of_lines_to_write_string"] = header("0806", "Number of Lines To Write String", "number-of-lines-to-write-string") + """# @param {Integer[]} widths
# @param {String} s
# @return {Integer[]}
def number_of_lines(widths, s)
  lines = 1
  width = 0
  s.each_char do |ch|
    w = widths[ch.ord - 97]
    if width + w > 100
      lines += 1
      width = w
    else
      width += w
    end
  end
  [lines, width]
end
"""

FILES["0807_max_increase_to_keep_city_skyline"] = header("0807", "Max Increase to Keep City Skyline", "max-increase-to-keep-city-skyline") + """# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
  row_max = grid.map(&:max)
  col_max = grid.transpose.map(&:max)
  grid.each_with_index.sum do |row, r|
    row.each_with_index.sum { |h, c| [row_max[r], col_max[c]].min - h }
  end
end
"""

FILES["0808_soup_servings"] = header("0808", "Soup Servings", "soup-servings") + """# @param {Integer} n
# @return {Float}
def soup_servings(n)
  return 1.0 if n >= 4800

  units = (n + 24) / 25
  memo = {}
  dp = lambda do |a, b|
    key = [a, b]
    return memo[key] if memo.key?(key)
    return memo[key] = 0.5 if a <= 0 && b <= 0
    return memo[key] = 1.0 if a <= 0
    return memo[key] = 0.0 if b <= 0

    memo[key] = 0.25 * (
      dp.call(a - 4, b) +
      dp.call(a - 3, b - 1) +
      dp.call(a - 2, b - 2) +
      dp.call(a - 1, b - 3)
    )
  end

  dp.call(units, units)
end
"""

FILES["0809_expressive_words"] = header("0809", "Expressive Words", "expressive-words") + """# @param {String} s
# @param {String[]} words
# @return {Integer}
def expressive_words(s, words)
  groups = lambda do |text|
    result = []
    i = 0
    while i < text.length
      j = i
      j += 1 while j < text.length && text[j] == text[i]
      result << [text[i], j - i]
      i = j
    end
    result
  end

  target = groups.call(s)
  words.count do |word|
    source = groups.call(word)
    next false if source.length != target.length

    source.zip(target).all? do |(ch1, c1), (ch2, c2)|
      ch1 == ch2 && c1 <= c2 && (c1 == c2 || c2 >= 3)
    end
  end
end
"""

FILES["0810_chalkboard_xor_game"] = header("0810", "Chalkboard XOR Game", "chalkboard-xor-game") + """# @param {Integer[]} nums
# @return {Boolean}
def xor_game(nums)
  nums.reduce(0, :^).zero? || nums.length.even?
end
"""

FILES["0811_subdomain_visit_count"] = header("0811", "Subdomain Visit Count", "subdomain-visit-count") + """# @param {String[]} cpdomains
# @return {String[]}
def subdomain_visits(cpdomains)
  counts = Hash.new(0)
  cpdomains.each do |item|
    count_str, domain = item.split
    count = count_str.to_i
    parts = domain.split(".")
    parts.length.times { |i| counts[parts[i..].join(".")] += count }
  end
  counts.map { |domain, count| "#{count} #{domain}" }
end
"""

FILES["0812_largest_triangle_area"] = header("0812", "Largest Triangle Area", "largest-triangle-area") + """# @param {Integer[][]} points
# @return {Float}
def largest_triangle_area(points)
  best = 0.0
  n = points.length
  n.times do |i|
    x1, y1 = points[i]
    ((i + 1)...n).each do |j|
      x2, y2 = points[j]
      ((j + 1)...n).each do |k|
        x3, y3 = points[k]
        area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs / 2.0
        best = area if area > best
      end
    end
  end
  best
end
"""

FILES["0813_largest_sum_of_averages"] = header("0813", "Largest Sum of Averages", "largest-sum-of-averages") + """# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def largest_sum_of_averages(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0.0)
  nums.each_with_index { |num, i| prefix[i + 1] = prefix[i] + num }

  average = ->(i, j) { (prefix[j] - prefix[i]) / (j - i) }

  dp = (1..n).map { |i| average.call(0, i) }
  (2..k).each do |groups|
    nxt = Array.new(n, 0.0)
    (groups - 1...n).each do |i|
      best = 0.0
      (groups - 2...i).each do |j|
        cand = dp[j] + average.call(j + 1, i + 1)
        best = cand if cand > best
      end
      nxt[i] = best
    end
    dp = nxt
  end
  dp[-1]
end
"""

FILES["0814_binary_tree_pruning"] = header("0814", "Binary Tree Pruning", "binary-tree-pruning") + TREE + """
# @param {TreeNode} root
# @return {TreeNode}
def prune_tree(root)
  return nil if root.nil?

  root.left = prune_tree(root.left)
  root.right = prune_tree(root.right)
  return nil if root.val == 0 && root.left.nil? && root.right.nil?

  root
end
"""

FILES["0815_bus_routes"] = header("0815", "Bus Routes", "bus-routes") + """# @param {Integer[][]} routes
# @param {Integer} source
# @param {Integer} target
# @return {Integer}
def num_buses_to_destination(routes, source, target)
  return 0 if source == target

  stop_to_buses = Hash.new { |h, k| h[k] = [] }
  routes.each_with_index do |stops, bus|
    stops.each { |stop| stop_to_buses[stop] << bus }
  end

  queue = [[source, 0]]
  seen_stops = { source => true }
  seen_buses = {}
  until queue.empty?
    stop, buses_taken = queue.shift
    stop_to_buses[stop].each do |bus|
      next if seen_buses[bus]

      seen_buses[bus] = true
      routes[bus].each do |nxt|
        return buses_taken + 1 if nxt == target
        next if seen_stops[nxt]

        seen_stops[nxt] = true
        queue << [nxt, buses_taken + 1]
      end
    end
  end
  -1
end
"""

FILES["0816_ambiguous_coordinates"] = header("0816", "Ambiguous Coordinates", "ambiguous-coordinates") + """# @param {String} s
# @return {String[]}
def ambiguous_coordinates(s)
  digits = s[1...-1]

  candidates = lambda do |frag|
    options = []
    return options if frag.empty? || (frag.length > 1 && frag[0] == "0" && frag[-1] == "0")
    return frag[-1] != "0" ? ["0.#{frag[1..]}"] : [] if frag[0] == "0" && frag.length > 1

    options << frag
    return options if frag[-1] == "0"

    (1...frag.length).each { |i| options << "#{frag[0...i]}.#{frag[i..]}" }
    options
  end

  answer = []
  (1...digits.length).each do |i|
    candidates.call(digits[0...i]).each do |left|
      candidates.call(digits[i..]).each do |right|
        answer << "(#{left}, #{right})"
      end
    end
  end
  answer
end
"""

FILES["0817_linked_list_components"] = header("0817", "Linked List Components", "linked-list-components") + LISTN + """
# @param {ListNode} head
# @param {Integer[]} nums
# @return {Integer}
def num_components(head, nums)
  present = nums.each_with_object({}) { |x, h| h[x] = true }
  count = 0
  connected = false
  while head
    if present[head.val]
      unless connected
        count += 1
        connected = true
      end
    else
      connected = false
    end
    head = head.next
  end
  count
end
"""

FILES["0818_race_car"] = header("0818", "Race Car", "race-car") + """# @param {Integer} target
# @return {Integer}
def racecar(target)
  queue = [[0, 1, 0]]
  seen = { [0, 1] => true }
  until queue.empty?
    pos, speed, steps = queue.shift
    return steps if pos == target

    nxt_pos = pos + speed
    nxt_speed = speed * 2
    if !seen[[nxt_pos, nxt_speed]] && nxt_pos.abs < target * 2
      seen[[nxt_pos, nxt_speed]] = true
      queue << [nxt_pos, nxt_speed, steps + 1]
    end
    rev_speed = speed > 0 ? -1 : 1
    unless seen[[pos, rev_speed]]
      seen[[pos, rev_speed]] = true
      queue << [pos, rev_speed, steps + 1]
    end
  end
  -1
end
"""

FILES["0819_most_common_word"] = header("0819", "Most Common Word", "most-common-word") + """# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
  banned_set = banned.each_with_object({}) { |w, h| h[w] = true }
  words = paragraph.downcase.scan(/[a-z]+/).reject { |word| banned_set[word] }
  words.tally.max_by { |_, count| count }[0]
end
"""

FILES["0820_short_encoding_of_words"] = header("0820", "Short Encoding of Words", "short-encoding-of-words") + """# @param {String[]} words
# @return {Integer}
def minimum_length_encoding(words)
  good = words.each_with_object({}) { |w, h| h[w] = true }
  words.each do |word|
    (1...word.length).each { |i| good.delete(word[i..]) }
  end
  good.keys.sum { |word| word.length + 1 }
end
"""

FILES["0821_shortest_distance_to_a_character"] = header("0821", "Shortest Distance to a Character", "shortest-distance-to-a-character") + """# @param {String} s
# @param {String} c
# @return {Integer[]}
def shortest_to_char(s, c)
  n = s.length
  ans = Array.new(n, 0)
  prev = -n
  s.each_char.with_index do |ch, i|
    prev = i if ch == c
    ans[i] = i - prev
  end
  prev = 2 * n
  (n - 1).downto(0) do |i|
    prev = i if s[i] == c
    ans[i] = [ans[i], prev - i].min
  end
  ans
end
"""

FILES["0822_card_flipping_game"] = header("0822", "Card Flipping Game", "card-flipping-game") + """# @param {Integer[]} fronts
# @param {Integer[]} backs
# @return {Integer}
def flipgame(fronts, backs)
  same = {}
  fronts.zip(backs).each { |f, b| same[f] = true if f == b }
  best = Float::INFINITY
  (fronts + backs).each { |x| best = x if !same[x] && x < best }
  best == Float::INFINITY ? 0 : best
end
"""

FILES["0823_binary_trees_with_factors"] = header("0823", "Binary Trees With Factors", "binary-trees-with-factors") + """# @param {Integer[]} arr
# @return {Integer}
def num_factored_binary_trees(arr)
  mod = 10**9 + 7
  arr = arr.sort
  dp = {}
  arr.each_with_index do |x, i|
    ways = 1
    i.times do |j|
      left = arr[j]
      next unless x % left == 0

      right = x / left
      ways = (ways + dp[left] * dp[right]) % mod if dp.key?(right)
    end
    dp[x] = ways
  end
  dp.values.sum % mod
end
"""

FILES["0824_goat_latin"] = header("0824", "Goat Latin", "goat-latin") + """# @param {String} sentence
# @return {String}
def to_goat_latin(sentence)
  vowels = "aeiouAEIOU"
  sentence.split.each_with_index.map do |word, idx|
    goat = if vowels.include?(word[0])
             word + "ma"
           else
             word[1..] + word[0] + "ma"
           end
    goat + ("a" * (idx + 1))
  end.join(" ")
end
"""

FILES["0825_friends_of_appropriate_ages"] = header("0825", "Friends Of Appropriate Ages", "friends-of-appropriate-ages") + """# @param {Integer[]} ages
# @return {Integer}
def num_friend_requests(ages)
  count = Array.new(121, 0)
  ages.each { |age| count[age] += 1 }
  ans = 0
  (1..120).each do |x|
    next if count[x] == 0

    (1..120).each do |y|
      next if count[y] == 0
      next if y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100)

      ans += count[x] * count[y]
      ans -= count[x] if x == y
    end
  end
  ans
end
"""

FILES["0826_most_profit_assigning_work"] = header("0826", "Most Profit Assigning Work", "most-profit-assigning-work") + """# @param {Integer[]} difficulty
# @param {Integer[]} profit
# @param {Integer[]} worker
# @return {Integer}
def max_profit_assignment(difficulty, profit, worker)
  jobs = difficulty.zip(profit).sort
  worker = worker.sort
  ans = 0
  best = 0
  i = 0
  worker.each do |ability|
    while i < jobs.length && jobs[i][0] <= ability
      best = [best, jobs[i][1]].max
      i += 1
    end
    ans += best
  end
  ans
end
"""

FILES["0827_making_a_large_island"] = header("0827", "Making A Large Island", "making-a-large-island") + """# @param {Integer[][]} grid
# @return {Integer}
def largest_island(grid)
  n = grid.length
  sizes = { 0 => 0 }
  island_id = 2

  dfs = lambda do |r, c, iid|
    return 0 if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1

    grid[r][c] = iid
    1 + dfs.call(r + 1, c, iid) + dfs.call(r - 1, c, iid) +
      dfs.call(r, c + 1, iid) + dfs.call(r, c - 1, iid)
  end

  n.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        sizes[island_id] = dfs.call(i, j, island_id)
        island_id += 1
      end
    end
  end

  ans = sizes.values.max || 0
  n.times do |i|
    n.times do |j|
      next unless grid[i][j] == 0

      seen = {}
      total = 1
      [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].each do |ni, nj|
        next unless ni >= 0 && ni < n && nj >= 0 && nj < n

        iid = grid[ni][nj]
        if iid > 1 && !seen[iid]
          seen[iid] = true
          total += sizes[iid]
        end
      end
      ans = total if total > ans
    end
  end
  ans
end
"""

FILES["0828_count_unique_characters_of_all_substrings_of_a_given_string"] = header(
    "0828",
    "Count Unique Characters of All Substrings of a Given String",
    "count-unique-characters-of-all-substrings-of-a-given-string",
) + """# @param {String} s
# @return {Integer}
def unique_letter_string(s)
  n = s.length
  last = {}
  s.each_char { |ch| last[ch] ||= [-1] }
  s.each_char.with_index { |ch, i| last[ch] << i }
  last.each_value { |indices| indices << n }
  ans = 0
  last.each_value do |indices|
    (1...indices.length - 1).each do |k|
      ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
    end
  end
  ans
end
"""

FILES["0829_consecutive_numbers_sum"] = header("0829", "Consecutive Numbers Sum", "consecutive-numbers-sum") + """# @param {Integer} n
# @return {Integer}
def consecutive_numbers_sum(n)
  ans = 0
  k = 1
  while k * (k - 1) / 2 < n
    ans += 1 if (n - k * (k - 1) / 2) % k == 0
    k += 1
  end
  ans
end
"""


def main():
    written = 0
    for folder, content in FILES.items():
        if content.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        path = ROOT / folder / "solution.rb"
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"total {written}")


if __name__ == "__main__":
    main()
