#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3923_minimum_generations_to_target_point", r'''
# LeetCode 3923 - Minimum Generations to Target Point
# https://leetcode.com/problems/minimum-generations-to-target-point/

# @param {Integer[][]} points
# @param {Integer[]} target
# @return {Integer}
def min_generations(points, target)
  target_key = "#{target[0]},#{target[1]},#{target[2]}"
  generation = {}
  all_pts = []
  points.each do |values|
    key = "#{values[0]},#{values[1]},#{values[2]}"
    generation[key] = 0
    all_pts << values.dup
  end
  return generation[target_key] if generation.key?(target_key)
  current = 1
  loop do
    limit = all_pts.length
    added = []
    (0...limit).each do |i|
      ((i + 1)...limit).each do |j|
        pi = all_pts[i]
        pj = all_pts[j]
        next if pi[0] == pj[0] && pi[1] == pj[1] && pi[2] == pj[2]
        p = [(pi[0] + pj[0]) / 2, (pi[1] + pj[1]) / 2, (pi[2] + pj[2]) / 2]
        key = "#{p[0]},#{p[1]},#{p[2]}"
        unless generation.key?(key)
          generation[key] = current
          added << p
        end
      end
    end
    return generation[target_key] if generation.key?(target_key)
    return -1 if added.empty?
    added.each { |p| all_pts << p }
    current += 1
  end
end
''')

add("3924_minimum_threshold_path_with_limited_heavy_edges", r'''
# LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} target
# @param {Integer} k
# @return {Integer}
def min_threshold(n, edges, source, target, k)
  can = lambda do |threshold|
    inf = 1_000_000_000
    dist = Array.new(n, inf)
    dist[source] = 0
    dq = [source]
    until dq.empty?
      u = dq.shift
      g[u].each do |to, weight|
        cost = weight > threshold ? 1 : 0
        next if dist[u] + cost >= dist[to] || dist[u] + cost > k
        dist[to] = dist[u] + cost
        if cost == 0
          dq.unshift(to)
        else
          dq << to
        end
      end
    end
    dist[target] <= k
  end
  return 0 if source == target
  g = Array.new(n) { [] }
  max_weight = 0
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
    max_weight = e[2] if e[2] > max_weight
  end
  return -1 unless can.call(max_weight)
  lo = 0
  hi = max_weight
  while lo < hi
    mid = lo + (hi - lo) / 2
    if can.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3925_concatenate_array_with_reverse", r'''
# LeetCode 3925 - Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/

# @param {Integer[]} nums
# @return {Integer[]}
def concat_with_reverse(nums)
  n = nums.length
  ans = Array.new(2 * n, 0)
  n.times do |i|
    ans[i] = nums[i]
    ans[i + n] = nums[n - i - 1]
  end
  ans
end
''')

add("3926_count_valid_word_occurrences", r'''
# LeetCode 3926 - Count Valid Word Occurrences
# https://leetcode.com/problems/count-valid-word-occurrences/

# @param {String[]} chunks
# @param {String[]} queries
# @return {Integer[]}
def count_word_occurrences(chunks, queries)
  s = chunks.join
  n = s.length
  cnt = {}
  i = 0
  while i < n
    if s[i] == " " || s[i] == "-"
      i += 1
      next
    end
    j = i
    while j < n && s[j] != " " && (s[j] != "-" || (j + 1 < n && s[j + 1] != " " && s[j + 1] != "-"))
      j += 1
    end
    word = s[i...j]
    cnt[word] = cnt.fetch(word, 0) + 1
    i = j
  end
  queries.map { |q| cnt.fetch(q, 0) }
end
''')

add("3927_minimize_array_sum_using_divisible_replacements", r'''
# LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
# https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

# @param {Integer[]} nums
# @return {Integer}
def min_array_sum(nums)
  maximum = 0
  present = Array.new(100001, false)
  nums.each do |value|
    present[value] = true
    maximum = value if value > maximum
  end
  best = Array.new(maximum + 1, 0)
  (1..maximum).each do |divisor|
    next unless present[divisor]
    multiple = divisor
    while multiple <= maximum
      best[multiple] = divisor if best[multiple] == 0
      multiple += divisor
    end
  end
  nums.sum { |value| best[value] }
end
''')

add("3928_minimum_cost_to_buy_apples_ii", r'''
# LeetCode 3928 - Minimum Cost to Buy Apples II
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

# @param {Integer} n
# @param {Integer[]} prices
# @param {Integer[][]} roads
# @return {Integer[]}
def min_cost_to_buy_apples(n, prices, roads)
  dijkstra = lambda do |source, carrying, inf|
    dist = Array.new(n, inf)
    dist[source] = 0
    pq = [[0, source]]
    until pq.empty?
      pq.sort_by! { |a| a[0] }
      d, node = pq.shift
      next if d != dist[node]
      g[node].each do |e|
        weight = carrying ? e[:full] : e[:empty]
        nxt = d + weight
        if nxt < dist[e[:to]]
          dist[e[:to]] = nxt
          pq << [nxt, e[:to]]
        end
      end
    end
    dist
  end
  g = Array.new(n) { [] }
  roads.each do |road|
    empty = road[2]
    full = road[2] * road[3]
    g[road[0]] << { to: road[1], empty: empty, full: full }
    g[road[1]] << { to: road[0], empty: empty, full: full }
  end
  inf = 1 << 62
  answer = Array.new(n, 0)
  n.times do |source|
    empty_dist = dijkstra.call(source, false, inf)
    full_dist = dijkstra.call(source, true, inf)
    best = prices[source]
    n.times do |shop|
      next if empty_dist[shop] == inf || full_dist[shop] == inf
      total = empty_dist[shop] + full_dist[shop] + prices[shop]
      best = total if total < best
    end
    answer[source] = best
  end
  answer
end
''')

add("3929_minimum_partition_score_ii", r'''
# LeetCode 3929 - Minimum Partition Score II
# https://leetcode.com/problems/minimum-partition-score-ii/

class Line
  attr_accessor :slope, :intercept, :count, :valid

  def initialize(slope = 0, intercept = 0, count = 0, valid = false)
    @slope = slope
    @intercept = intercept
    @count = count
    @valid = valid
  end
end

class State
  attr_accessor :value, :count, :valid

  def initialize(value = 0, count = 0, valid = false)
    @value = value
    @count = count
    @valid = valid
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_partition_score(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }

  better = lambda do |a, b|
    return b unless a.valid
    return a unless b.valid
    return a.value < b.value ? a : b if a.value != b.value
    a.count >= b.count ? a : b
  end

  evaluate = lambda do |line, x|
    return State.new unless line.valid
    State.new(line.slope * x + line.intercept, line.count, true)
  end

  insert = nil
  insert = lambda do |tree, node, left, right, line|
    unless tree[node].valid
      tree[node] = line
      return
    end
    mid = (left + right) / 2
    x_left = prefix[left]
    x_mid = prefix[mid]
    left_better = better.call(evaluate.call(line, x_left), evaluate.call(tree[node], x_left))
    mid_better = better.call(evaluate.call(line, x_mid), evaluate.call(tree[node], x_mid))
    line_wins_left = left_better.value == evaluate.call(line, x_left).value && left_better.count == line.count
    line_wins_mid = mid_better.value == evaluate.call(line, x_mid).value && mid_better.count == line.count
    if line_wins_mid
      tmp = tree[node]
      tree[node] = line
      line = tmp
    end
    return if left == right
    if line_wins_left != line_wins_mid
      insert.call(tree, node * 2, left, mid, line)
    else
      insert.call(tree, node * 2 + 1, mid + 1, right, line)
    end
  end

  query = nil
  query = lambda do |tree, node, left, right, index|
    result = evaluate.call(tree[node], prefix[index])
    return result if left == right
    mid = (left + right) / 2
    if index <= mid
      better.call(result, query.call(tree, node * 2, left, mid, index))
    else
      better.call(result, query.call(tree, node * 2 + 1, mid + 1, right, index))
    end
  end

  run = lambda do |penalty|
    tree = Array.new(4 * (n + 1)) { Line.new }
    insert.call(tree, 1, 0, n, Line.new(0, 0, 0, true))
    current = State.new
    (1..n).each do |i|
      best = query.call(tree, 1, 0, n, i)
      x = prefix[i]
      current = State.new(best.value + x * x + x + penalty, best.count + 1, true)
      insert.call(tree, 1, 0, n, Line.new(-2 * x, current.value + x * x - x, current.count, true))
    end
    current
  end

  bound = prefix[n] * prefix[n] + prefix[n] + 1
  low = 0
  high = bound
  while low < high
    mid = low + (high - low + 1) / 2
    if run.call(mid).count >= k
      low = mid
    else
      high = mid - 1
    end
  end
  state = run.call(low)
  (state.value - low * k) / 2
end
''')

add("3930_power_update_after_k_th_largest_insertion_ii", r'''
# LeetCode 3930 - Power Update After K Th Largest Insertion Ii
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer[]}
def power_update(nums, p, queries)
  sl = nums.sort
  mod = 10**9 + 7
  ans = []
  queries.each do |val, k|
    lo = 0
    hi = sl.length
    while lo < hi
      mid = (lo + hi) / 2
      if sl[mid] < val
        lo = mid + 1
      else
        hi = mid
      end
    end
    sl.insert(lo, val)
    exp = sl[-k]
    p = p.to_i.pow(exp, mod)
    ans << p
  end
  ans
end
''')

add("3931_check_adjacent_digit_differences", r'''
# LeetCode 3931 - Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/

# @param {String} s
# @return {Boolean}
def is_adjacent_diff_at_most_two(s)
  (1...s.length).each do |i|
    return false if (s[i - 1].ord - s[i].ord).abs > 2
  end
  true
end
''')

add("3932_count_k_th_roots_in_a_range", r'''
# LeetCode 3932 - Count K Th Roots In A Range
# https://leetcode.com/problems/count-k-th-roots-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def count_kth_roots(l, r, k)
  return r - l + 1 if k == 1
  ans = 0
  x = 0
  loop do
    y = 1
    too_big = false
    k.times do
      if x != 0 && y > r / x
        too_big = true
        break
      end
      y *= x
      break if y > r
    end
    break if too_big || y > r
    ans += 1 if l <= y && y <= r
    x += 1
  end
  ans
end
''')

add("3933_largest_local_values_in_a_matrix_ii", r'''
# LeetCode 3933 - Largest Local Values in a Matrix II
# https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

# @param {Integer[][]} matrix
# @return {Integer}
def count_local_maximums(matrix)
  rows = matrix.length
  cols = matrix[0].length
  positions = Array.new(201) { [] }
  rows.times do |row|
    cols.times do |col|
      value = matrix[row][col]
      positions[value] << [row, col] if value > 0
    end
  end
  answer = 0
  (1..200).each do |value|
    next if positions[value].empty?
    prefix = Array.new(rows + 1) { Array.new(cols + 1, 0) }
    rows.times do |row|
      cols.times do |col|
        add = matrix[row][col] > value ? 1 : 0
        prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
      end
    end
    positions[value].each do |row, col|
      top = [0, row - value].max
      bottom = [rows - 1, row + value].min
      left = [0, col - value].max
      right = [cols - 1, col + value].min
      greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left]
      [-value, value].each do |dr|
        [-value, value].each do |dc|
          rr = row + dr
          cc = col + dc
          greater -= 1 if rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value
        end
      end
      answer += 1 if greater == 0
    end
  end
  answer
end
''')

add("3934_smallest_unique_subarray", r'''
# LeetCode 3934 - Smallest Unique Subarray
# https://leetcode.com/problems/smallest-unique-subarray/

# @param {Integer[]} nums
# @return {Integer}
def smallest_unique_subarray(nums)
  base = 19
  modulo = 10**9 + 7
  powers = Array.new(nums.length + 1, 1)
  min_possible_len = nums.length
  min_len = 1
  max_len = nums.length
  while min_len <= max_len
    mid_len = (min_len + max_len) / 2
    powers[0] = 1
    (1..nums.length).each do |idx|
      powers[idx] = (powers[idx - 1] * base) % modulo
    end
    current_hash = 0
    mid_len.times do |idx|
      current_hash *= base
      current_hash += nums[idx]
      current_hash %= modulo
    end
    hash_values = {}
    hash_values[current_hash] = 1
    (1..(nums.length - mid_len)).each do |idx|
      current_hash -= powers[mid_len - 1] * nums[idx - 1]
      current_hash *= base
      current_hash += nums[idx + mid_len - 1]
      current_hash %= modulo
      hash_values[current_hash] = hash_values.fetch(current_hash, 0) + 1
    end
    if hash_values.value?(1)
      min_possible_len = mid_len if mid_len < min_possible_len
      max_len = mid_len - 1
    else
      min_len = mid_len + 1
    end
  end
  min_possible_len
end
''')

add("3935_power_update_after_k_th_largest_insertion_i", r'''
# LeetCode 3935 - Power Update After K Th Largest Insertion I
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer[]}
def power_update(nums, p, queries)
  merge = lambda do |st, x, v|
    c = st.fetch(x, 0)
    if c + v == 0
      st.delete(x)
    else
      st[x] = c + v
    end
  end
  first_key = lambda { |st| st.keys.min }
  last_key = lambda { |st| st.keys.max }
  qpow = lambda do |a, b, mod|
    ans = 1
    a = a.to_i
    while b > 0
      ans = (ans * a) % mod if (b & 1) != 0
      a = (a * a) % mod
      b >>= 1
    end
    ans
  end
  left = {}
  right = {}
  sz1 = 0
  sz2 = nums.length
  nums.each { |x| merge.call(right, x, 1) }
  mod = 1_000_000_007
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    val, k = q[0], q[1]
    merge.call(right, val, 1)
    sz2 += 1
    node = first_key.call(right)
    merge.call(right, node, -1)
    sz2 -= 1
    merge.call(left, node, 1)
    sz1 += 1
    while sz2 < k
      node = last_key.call(left)
      merge.call(left, node, -1)
      sz1 -= 1
      merge.call(right, node, 1)
      sz2 += 1
    end
    while sz2 > k
      node = first_key.call(right)
      merge.call(right, node, -1)
      sz2 -= 1
      merge.call(left, node, 1)
      sz1 += 1
    end
    x = first_key.call(right)
    p = qpow.call(p, x, mod)
    ans[qi] = p
  end
  ans
end
''')

add("3936_minimum_swaps_to_move_zeros_to_end", r'''
# LeetCode 3936 - Minimum Swaps To Move Zeros To End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

# @param {Integer[]} nums
# @return {Integer}
def minimum_swaps(nums)
  ans = 0
  n = nums.length
  i = 0
  j = n - 1
  while i < j
    i += 1 while i < n && nums[i] != 0
    j -= 1 while j > 0 && nums[j] == 0
    break if i >= j
    ans += 1
    i += 1
    j -= 1
  end
  ans
end
''')

add("3937_minimum_operations_to_make_array_modulo_alternating_i", r'''
# LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  vals = nums.map { |v| v % k }
  ans = 2_147_483_647
  k.times do |x|
    k.times do |y|
      next if x == y
      cnt = 0
      vals.each_with_index do |v, i|
        target = (i & 1) != 0 ? y : x
        diff = (target - v).abs
        cnt += [diff, k - diff].min
      end
      ans = cnt if cnt < ans
    end
  end
  ans
end
''')

add("3938_maximum_path_intersection_sum_in_a_grid", r'''
# LeetCode 3938 - Maximum Path Intersection Sum in a Grid
# https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_path_sum(grid)
  check_line = lambda do |length, value|
    answer = -2_147_483_648
    best_ending = value.call(0) + value.call(1)
    answer = best_ending if best_ending > answer
    (2...length).each do |i|
      if value.call(i - 1) + value.call(i) > best_ending + value.call(i)
        best_ending = value.call(i - 1) + value.call(i)
      else
        best_ending += value.call(i)
      end
      answer = best_ending if best_ending > answer
    end
    answer
  end
  rows = grid.length
  cols = grid[0].length
  answer = -2_147_483_648
  rows.times do |row|
    r = row
    v = check_line.call(cols, ->(col) { grid[r][col] })
    answer = v if v > answer
  end
  cols.times do |col|
    c = col
    v = check_line.call(rows, ->(row) { grid[row][c] })
    answer = v if v > answer
  end
  (1...(rows - 1)).each do |row|
    (1...(cols - 1)).each do |col|
      answer = grid[row][col] if grid[row][col] > answer
    end
  end
  answer
end
''')

add("3939_count_non_adjacent_subsets_in_a_rooted_tree", r'''
# LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

# @param {Integer[]} parent
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_non_adjacent_subsets(parent, nums, k)
  mod = 1_000_000_007
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parent[i]] << i }
  dp0 = Array.new(n)
  dp1 = Array.new(n)
  (n - 1).downto(0) do |u|
    a = Array.new(k, 0)
    b = Array.new(k, 0)
    a[0] = 1
    b[(((nums[u] % k) + k) % k)] = 1
    children[u].each do |v|
      na = Array.new(k, 0)
      nb = Array.new(k, 0)
      k.times do |x|
        k.times do |y|
          all_child = (dp0[v][y] + dp1[v][y]) % mod
          na[(x + y) % k] = (na[(x + y) % k] + a[x] * all_child) % mod
          nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
        end
      end
      a = na
      b = nb
    end
    dp0[u] = a
    dp1[u] = b
  end
  ans = (dp0[0][0] + dp1[0][0] - 1) % mod
  ans += mod if ans < 0
  ans
end
''')

add("3940_limit_occurrences_in_sorted_array", r'''
# LeetCode 3940 - Limit Occurrences In Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def limit_occurrences(nums, k)
  n = nums.length
  cnt = 1
  l = 1
  (1...n).each do |r|
    if nums[r] != nums[r - 1]
      cnt = 1
    else
      cnt += 1
    end
    if cnt <= k
      nums[l] = nums[r]
      l += 1
    end
  end
  nums[0...l]
end
''')

add("3941_password_strength", r'''
# LeetCode 3941 - Password Strength
# https://leetcode.com/problems/password-strength/

# @param {String} password
# @return {Integer}
def password_strength(password)
  ans = 0
  password.chars.uniq.each do |ch|
    if ch =~ /[a-z]/
      ans += 1
    elsif ch =~ /[A-Z]/
      ans += 2
    elsif ch =~ /[0-9]/
      ans += 3
    else
      ans += 5
    end
  end
  ans
end
''')

add("3942_minimum_operations_to_sort_a_permutation", r'''
# LeetCode 3942 - Minimum Operations To Sort A Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  check = lambda do |zero, step|
    n = nums.length
    (1...n).each do |i|
      prev = ((zero + (i - 1) * step) % n + n) % n
      curr = ((zero + i * step) % n + n) % n
      return false if nums[prev] > nums[curr]
    end
    true
  end
  n = nums.length
  zero = nums.index(0)
  ans = 2_147_483_647
  if check.call(zero, 1)
    ans = [ans, zero].min
    ans = [ans, n - zero + 2].min
  end
  if check.call(zero, -1)
    ans = [ans, zero + 2].min
    ans = [ans, n - zero].min
  end
  ans == 2_147_483_647 ? -1 : ans
end
''')

add("3943_number_of_pairs_after_increment", r'''
# LeetCode 3943 - Number of Pairs After Increment
# https://leetcode.com/problems/number-of-pairs-after-increment/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def number_of_pairs(nums1, nums2, queries)
  rebuild = lambda do |freq, nums2, b, block_size, n|
    freq[b] = {}
    finish = [(b + 1) * block_size, n].min
    (b * block_size...finish).each do |i|
      freq[b][nums2[i]] = freq[b].fetch(nums2[i], 0) + 1
    end
  end
  push = lambda do |lazy, nums2, b, block_size, n|
    if lazy[b] != 0
      finish = [(b + 1) * block_size, n].min
      (b * block_size...finish).each { |i| nums2[i] += lazy[b] }
      lazy[b] = 0
    end
  end
  block_size = 225
  n = nums2.length
  blocks = (n + block_size - 1) / block_size
  lazy = Array.new(blocks, 0)
  freq = Array.new(blocks) { {} }
  blocks.times { |b| rebuild.call(freq, nums2, b, block_size, n) }
  fixed = {}
  nums1.each { |x| fixed[x] = fixed.fetch(x, 0) + 1 }
  answer = []
  queries.each do |q|
    if q[0] == 1
      l, r, delta = q[1], q[2], q[3]
      first = l / block_size
      last = r / block_size
      if first == last
        push.call(lazy, nums2, first, block_size, n)
        (l..r).each { |i| nums2[i] += delta }
        rebuild.call(freq, nums2, first, block_size, n)
        next
      end
      push.call(lazy, nums2, first, block_size, n)
      (l...((first + 1) * block_size)).each { |i| nums2[i] += delta }
      rebuild.call(freq, nums2, first, block_size, n)
      push.call(lazy, nums2, last, block_size, n)
      ((last * block_size)..r).each { |i| nums2[i] += delta }
      rebuild.call(freq, nums2, last, block_size, n)
      ((first + 1)...last).each { |b| lazy[b] += delta }
    else
      total = 0
      fixed.each do |a, count_a|
        target = q[1] - a
        blocks.times do |b|
          c = freq[b][target - lazy[b]]
          total += count_a * c if c
        end
      end
      answer << total
    end
  end
  answer
end
''')

add("3944_minimum_operations_to_make_array_modulo_alternating_ii", r'''
# LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  costs = lambda do |freq, k|
    dbl = Array.new(2 * k, 0)
    (2 * k).times { |i| dbl[i] = freq[i % k] }
    count_prefix = Array.new(2 * k + 1, 0)
    weighted_prefix = Array.new(2 * k + 1, 0)
    (2 * k).times do |i|
      count_prefix[i + 1] = count_prefix[i] + dbl[i]
      weighted_prefix[i + 1] = weighted_prefix[i] + i * dbl[i]
    end
    res = Array.new(k, 0)
    cw = k / 2
    cc = (k - 1) / 2
    k.times do |t|
      cnt = count_prefix[t + cw + 1] - count_prefix[t]
      s = weighted_prefix[t + cw + 1] - weighted_prefix[t]
      res[t] += s - t * cnt
      if cc > 0
        cnt2 = count_prefix[t + k] - count_prefix[t + k - cc]
        sum2 = weighted_prefix[t + k] - weighted_prefix[t + k - cc]
        res[t] += (t + k) * cnt2 - sum2
      end
    end
    res
  end
  even_freq = Array.new(k, 0)
  odd_freq = Array.new(k, 0)
  nums.each_with_index do |v, i|
    if i.even?
      even_freq[v % k] += 1
    else
      odd_freq[v % k] += 1
    end
  end
  even_cost = costs.call(even_freq, k)
  odd_cost = costs.call(odd_freq, k)
  best1 = 1 << 62
  best2 = 1 << 62
  best_index = -1
  k.times do |i|
    x = odd_cost[i]
    if x < best1
      best2 = best1
      best1 = x
      best_index = i
    elsif x < best2
      best2 = x
    end
  end
  ans = 1 << 62
  k.times do |x|
    other = x == best_index ? best2 : best1
    v = even_cost[x] + other
    ans = v if v < ans
  end
  ans
end
''')

add("3945_digit_frequency_score", r'''
# LeetCode 3945 - Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/

# @param {Integer} n
# @return {Integer}
def digit_frequency_score(n)
  ans = 0
  while n > 0
    ans += n % 10
    n /= 10
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
