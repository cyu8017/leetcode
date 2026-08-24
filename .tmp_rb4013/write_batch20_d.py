#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3795_minimum_subarray_length_with_distinct_sum_at_least_k", r'''
# LeetCode 3795 - Minimum Subarray Length with Distinct Sum at Least K
# https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_length(nums, k)
  n = nums.length
  ans = n + 1
  l = 0
  cnt = Hash.new(0)
  s = 0
  (0...n).each do |r|
    c = cnt[nums[r]] + 1
    cnt[nums[r]] = c
    s += nums[r] if c == 1
    while s >= k
      ans = r - l + 1 if r - l + 1 < ans
      left = nums[l]
      nc = cnt[left] - 1
      if nc == 0
        cnt.delete(left)
        s -= left
      else
        cnt[left] = nc
      end
      l += 1
    end
  end
  ans > n ? -1 : ans
end
''')

add("3796_find_maximum_value_in_a_constrained_sequence", r'''
# LeetCode 3796 - Find Maximum Value in a Constrained Sequence
# https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

# @param {Integer} n
# @param {Integer[][]} restrictions
# @param {Integer[]} diff
# @return {Integer}
def max_value(n, restrictions, diff)
  inf = 2147483647 / 4
  bound = Array.new(n, inf)
  bound[0] = 0
  restrictions.each { |r| bound[r[0]] = r[1] }
  (1...n).each { |i| bound[i] = [bound[i], bound[i - 1] + diff[i - 1]].min }
  (n - 2).downto(0) { |i| bound[i] = [bound[i], bound[i + 1] + diff[i]].min }
  ans = bound[0]
  (1...n).each { |i| ans = [ans, bound[i]].max }
  ans
end
''')

add("3797_count_routes_to_climb_a_rectangular_grid", r'''
# LeetCode 3797 - Count Routes to Climb a Rectangular Grid
# https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

# @param {String[][]} grid
# @param {Integer} d
# @return {Integer}
def count_routes(grid, d)
  mod = 1_000_000_007
  n = grid.length
  m = grid[0].length
  up_radius = 0
  up_radius += 1 while (up_radius + 1) * (up_radius + 1) + 1 <= d * d
  arrived = Array.new(m, 0)
  (0...m).each { |c| arrived[c] = 1 if grid[n - 1][c] == "." }
  (n - 1).downto(0) do |r|
    pref = Array.new(m + 1, 0)
    (0...m).each { |i| pref[i + 1] = (pref[i] + arrived[i]) % mod }
    horizontal = Array.new(m, 0)
    (0...m).each do |c|
      next if grid[r][c] == "#"
      l = [0, c - d].max
      rr = [m - 1, c + d].min
      horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % mod
      horizontal[c] += mod if horizontal[c] < 0
    end
    if r == 0
      ans = 0
      (0...m).each { |c| ans = (ans + arrived[c] + horizontal[c]) % mod }
      return ans
    end
    pref2 = Array.new(m + 1, 0)
    (0...m).each { |c| pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % mod }
    nxt = Array.new(m, 0)
    (0...m).each do |c|
      next if grid[r - 1][c] == "#"
      l = [0, c - up_radius].max
      rr = [m - 1, c + up_radius].min
      nxt[c] = pref2[rr + 1] - pref2[l]
      nxt[c] += mod if nxt[c] < 0
    end
    arrived = nxt
  end
  0
end
''')

add("3798_largest_even_number", r'''
# LeetCode 3798 - Largest Even Number
# https://leetcode.com/problems/largest-even-number/

# @param {String} s
# @return {String}
def largest_even(s)
  s = s[0...-1] while s.length > 0 && s[-1] == "1"
  s
end
''')

add("3799_word_squares_ii", r'''
# LeetCode 3799 - Word Squares II
# https://leetcode.com/problems/word-squares-ii/

# @param {String[]} words
# @return {String[][]}
def word_squares(words)
  words = words.sort
  n = words.length
  ans = []
  (0...n).each do |i|
    top = words[i]
    (0...n).each do |j|
      next if j == i
      left = words[j]
      (0...n).each do |k|
        next if k == j || k == i
        right = words[k]
        (0...n).each do |h|
          next if h == k || h == j || h == i
          bottom = words[h]
          if top[0] == left[0] && top[3] == right[0] &&
             bottom[0] == left[3] && bottom[3] == right[3]
            ans << [top, left, right, bottom]
          end
        end
      end
    end
  end
  ans
end
''')

add("3800_minimum_cost_to_make_two_binary_strings_equal", r'''
# LeetCode 3800 - Minimum Cost to Make Two Binary Strings Equal
# https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

# @param {String} s
# @param {String} t
# @param {Integer} flip_cost
# @param {Integer} swap_cost
# @param {Integer} cross_cost
# @return {Integer}
def minimum_cost(s, t, flip_cost, swap_cost, cross_cost)
  diff = [0, 0]
  n = s.length
  (0...n).each { |i| diff[s[i].ord - 48] += 1 if s[i] != t[i] }
  ans = (diff[0] + diff[1]) * flip_cost
  mx = [diff[0], diff[1]].max
  mn = [diff[0], diff[1]].min
  ans = [ans, mn * swap_cost + (mx - mn) * flip_cost].min
  avg = (mx + mn) / 2
  ans = [ans, (avg - mn) * cross_cost + avg * swap_cost + (mx + mn - avg * 2) * flip_cost].min
  ans
end
''')

add("3801_minimum_cost_to_merge_sorted_lists", r'''
# LeetCode 3801 - Minimum Cost to Merge Sorted Lists
# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

# @param {Integer[][]} lists
# @return {Integer}
def min_merge_cost(lists)
  m = lists.length
  total_masks = 1 << m
  merged = Array.new(total_masks) { [] }
  length = Array.new(total_masks, 0)
  median = Array.new(total_masks, 0)
  trailing_zeros = lambda do |bit|
    n = 0
    while (bit & 1) == 0
      bit >>= 1
      n += 1
    end
    n
  end
  (1...total_masks).each do |mask|
    bit = mask & -mask
    index = trailing_zeros.call(bit)
    previous = merged[mask ^ bit]
    current = lists[index]
    out = []
    i = 0
    j = 0
    while i < previous.length || j < current.length
      if j == current.length || (i < previous.length && previous[i] <= current[j])
        out << previous[i]
        i += 1
      else
        out << current[j]
        j += 1
      end
    end
    merged[mask] = out
    length[mask] = out.length
    median[mask] = out[(out.length - 1) / 2]
  end
  inf = 10**18
  dp = Array.new(total_masks, 0)
  (1...total_masks).each do |mask|
    next if (mask & (mask - 1)) == 0
    dp[mask] = inf
    first_bit = mask & -mask
    left = (mask - 1) & mask
    while left > 0
      if (left & first_bit) != 0
        right = mask ^ left
        if right != 0
          diff = median[left] - median[right]
          diff = -diff if diff < 0
          candidate = dp[left] + dp[right] + length[mask] + diff
          dp[mask] = candidate if candidate < dp[mask]
        end
      end
      left = (left - 1) & mask
    end
  end
  dp[total_masks - 1]
end
''')

add("3802_number_of_ways_to_paint_sheets", r'''
# LeetCode 3802 - Number of Ways to Paint Sheets
# https://leetcode.com/problems/number-of-ways-to-paint-sheets/

# @param {Integer} n
# @param {Integer[]} limit
# @return {Integer}
def number_of_ways(n, limit)
  mod = 1_000_000_007
  limit = limit.sort
  points = [1, n]
  limit.each do |x|
    points << x + 1 if x + 1 > 1 && x + 1 < n
    points << n - x if n - x > 1 && n - x < n
  end
  points.sort!
  u = 0
  (0...points.length).each do |i|
    if u == 0 || points[i] != points[u - 1]
      points[u] = points[i]
      u += 1
    end
  end
  points = points[0, u]
  count_ge = lambda do |lim, x|
    lo = 0
    hi = lim.length
    while lo < hi
      mid = (lo + hi) >> 1
      if lim[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lim.length - lo
  end
  ans = 0
  (0...(points.length - 1)).each do |i|
    x = points[i]
    a = count_ge.call(limit, x)
    b = count_ge.call(limit, n - x)
    same = count_ge.call(limit, [x, n - x].max)
    ways = (a * b - same) % mod
    length = points[i + 1] - x
    ans = (ans + ways * length) % mod
  end
  ans += mod if ans < 0
  ans
end
''')

add("3803_count_residue_prefixes", r'''
# LeetCode 3803 - Count Residue Prefixes
# https://leetcode.com/problems/count-residue-prefixes/

# @param {String} s
# @return {Integer}
def residue_prefixes(s)
  st = {}
  ans = 0
  s.each_char.with_index do |ch, i|
    st[ch] = true
    ans += 1 if st.length == (i + 1) % 3
  end
  ans
end
''')

add("3804_number_of_centered_subarrays", r'''
# LeetCode 3804 - Number of Centered Subarrays
# https://leetcode.com/problems/number-of-centered-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def centered_subarrays(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    st = {}
    s = 0
    (i...n).each do |j|
      s += nums[j]
      st[nums[j]] = true
      ans += 1 if st.key?(s)
    end
  end
  ans
end
''')

add("3805_count_caesar_cipher_pairs", r'''
# LeetCode 3805 - Count Caesar Cipher Pairs
# https://leetcode.com/problems/count-caesar-cipher-pairs/

# @param {String[]} words
# @return {Integer}
def count_pairs(words)
  cnt = Hash.new(0)
  words.each do |word|
    s = word.chars
    k = "z".ord - s[0].ord
    (1...s.length).each { |i| s[i] = (97 + (s[i].ord - 97 + k) % 26).chr }
    s[0] = "z"
    cnt[s.join] += 1
  end
  ans = 0
  cnt.each_value { |v| ans += v * (v - 1) / 2 }
  ans
end
''')

add("3806_maximum_bitwise_and_after_increment_operations", r'''
# LeetCode 3806 - Maximum Bitwise AND After Increment Operations
# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def maximum_and(nums, k, m)
  bit_len = lambda do |x|
    return 0 if x == 0
    n = 0
    while x > 0
      n += 1
      x >>= 1
    end
    n
  end
  mx_val = nums[0]
  nums.each { |v| mx_val = v if v > mx_val }
  mx_val += k
  mx = bit_len.call(mx_val)
  ans = 0
  cost = Array.new(nums.length, 0)
  (mx - 1).downto(0) do |bit|
    target = ans | (1 << bit)
    nums.each_with_index do |x, i|
      j = bit_len.call(target & ~x)
      mask = (1 << j) - 1
      cost[i] = (target & mask) - (x & mask)
    end
    cost.sort!
    total = 0
    (0...m).each { |i| total += cost[i] }
    ans = target if total <= k
  end
  ans
end
''')

add("3807_minimum_cost_to_repair_edges_to_traverse_a_graph", r'''
# LeetCode 3807 - Minimum Cost to Repair Edges to Traverse a Graph
# https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_cost(n, edges, k)
  edges = edges.sort_by { |e| e[2] }
  m = edges.length
  return -1 if m == 0
  check = lambda do |idx|
    g = Array.new(n) { [] }
    (0..idx).each do |i|
      g[edges[i][0]] << edges[i][1]
      g[edges[i][1]] << edges[i][0]
    end
    q = [0]
    vis = Array.new(n, false)
    vis[0] = true
    dist = 0
    while !q.empty?
      nq = []
      q.each do |u|
        return dist <= k if u == n - 1
        g[u].each do |v|
          unless vis[v]
            vis[v] = true
            nq << v
          end
        end
      end
      q = nq
      dist += 1
    end
    false
  end
  l = 0
  r = m - 1
  while l < r
    mid = (l + r) >> 1
    if check.call(mid)
      r = mid
    else
      l = mid + 1
    end
  end
  return edges[l][2] if check.call(l)
  -1
end
''')

add("3809_best_reachable_tower", r'''
# LeetCode 3809 - Best Reachable Tower
# https://leetcode.com/problems/best-reachable-tower/

# @param {Integer[][]} towers
# @param {Integer[]} center
# @param {Integer} radius
# @return {Integer[]}
def best_tower(towers, center, radius)
  cx, cy = center[0], center[1]
  idx = -1
  towers.each_with_index do |(x, y, q), i|
    dist = (x - cx).abs + (y - cy).abs
    next if dist > radius
    if idx == -1 || towers[idx][2] < q ||
       (towers[idx][2] == q &&
        (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))
      idx = i
    end
  end
  return [-1, -1] if idx == -1
  [towers[idx][0], towers[idx][1]]
end
''')

add("3810_minimum_operations_to_reach_target_array", r'''
# LeetCode 3810 - Minimum Operations to Reach Target Array
# https://leetcode.com/problems/minimum-operations-to-reach-target-array/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def min_operations(nums, target)
  s = {}
  (0...nums.length).each { |i| s[nums[i]] = true if nums[i] != target[i] }
  s.length
end
''')

add("3811_number_of_alternating_xor_partitions", r'''
# LeetCode 3811 - Number of Alternating XOR Partitions
# https://leetcode.com/problems/number-of-alternating-xor-partitions/

# @param {Integer[]} nums
# @param {Integer} target1
# @param {Integer} target2
# @return {Integer}
def alternating_xor(nums, target1, target2)
  mod = 1_000_000_007
  cnt1 = Hash.new(0)
  cnt2 = Hash.new(0)
  cnt2[0] = 1
  pre = 0
  ans = 0
  nums.each do |x|
    pre ^= x
    a = cnt2[pre ^ target1]
    b = cnt1[pre ^ target2]
    ans = (a + b) % mod
    cnt1[pre] = (cnt1[pre] + a) % mod
    cnt2[pre] = (cnt2[pre] + b) % mod
  end
  ans
end
''')

add("3812_minimum_edge_toggles_on_a_tree", r'''
# LeetCode 3812 - Minimum Edge Toggles on a Tree
# https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} start
# @param {Integer[]} target
# @return {Integer[]}
def minimum_flips(n, edges, start, target)
  g = Array.new(n) { [] }
  (0...(n - 1)).each do |i|
    a = edges[i][0]
    b = edges[i][1]
    g[a] << [b, i]
    g[b] << [a, i]
  end
  ans = []
  dfs = nil
  dfs = lambda do |a, fa|
    rev = start[a] != target[a]
    g[a].each do |b, i|
      if b != fa && dfs.call(b, a)
        ans << i
        rev = !rev
      end
    end
    rev
  end
  return [-1] if dfs.call(0, -1)
  ans.sort
end
''')

add("3813_vowel_consonant_score", r'''
# LeetCode 3813 - Vowel Consonant Score
# https://leetcode.com/problems/vowel-consonant-score/

# @param {String} s
# @return {Integer}
def vowel_consonant_score(s)
  v = 0
  c = 0
  s.each_char do |ch|
    if (ch >= "a" && ch <= "z") || (ch >= "A" && ch <= "Z")
      c += 1
      v += 1 if "aeiou".include?(ch)
    end
  end
  c -= v
  return 0 if c == 0
  v / c
end
''')

add("3814_maximum_capacity_within_budget", r'''
# LeetCode 3814 - Maximum Capacity Within Budget
# https://leetcode.com/problems/maximum-capacity-within-budget/

class CapHeap
  def initialize
    @a = []
  end

  def size
    @a.length
  end

  def peek
    @a[0]
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def cmp(a, b)
    return b[0] - a[0] if a[0] != b[0]
    b[1] - a[1]
  end

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if cmp(a[i], a[p]) >= 0
      a[i], a[p] = a[p], a[i]
      i = p
    end
  end

  def down(i)
    a = @a
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp(a[l], a[s]) < 0
      s = r if r < n && cmp(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer[]} costs
# @param {Integer[]} capacity
# @param {Integer} budget
# @return {Integer}
def max_capacity(costs, capacity, budget)
  arr = []
  (0...costs.length).each { |k| arr << [costs[k], capacity[k]] if costs[k] < budget }
  return 0 if arr.empty?
  arr.sort_by! { |x| x[0] }
  m = arr.length
  alive = Array.new(m, true)
  h = CapHeap.new
  (0...m).each { |i| h.push([arr[i][1], i]) }
  h.pop while h.size > 0 && !alive[h.peek[1]]
  ans = h.peek[0]
  i = 0
  j = m - 1
  while i < j
    alive[i] = false
    while i < j && arr[i][0] + arr[j][0] >= budget
      alive[j] = false
      j -= 1
    end
    h.pop while h.size > 0 && !alive[h.peek[1]]
    ans = [ans, arr[i][1] + h.peek[0]].max if h.size > 0
    i += 1
  end
  ans
end
''')

add("3815_design_auction_system", r'''
# LeetCode 3815 - Design Auction System
# https://leetcode.com/problems/design-auction-system/

class AuctionSystem
  def initialize
    @items = Hash.new { |h, k| h[k] = [] }
    @users = {}
  end

  def add_bid(user_id, item_id, bid_amount)
    @users[user_id] ||= {}
    remove_bid(user_id, item_id) if @users[user_id].key?(item_id)
    @users[user_id][item_id] = bid_amount
    insert_sorted(@items[item_id], [bid_amount, user_id])
    nil
  end

  def update_bid(user_id, item_id, new_amount)
    old_amount = @users[user_id][item_id]
    remove_sorted(@items[item_id], [old_amount, user_id])
    insert_sorted(@items[item_id], [new_amount, user_id])
    @users[user_id][item_id] = new_amount
    nil
  end

  def remove_bid(user_id, item_id)
    old_amount = @users[user_id][item_id]
    remove_sorted(@items[item_id], [old_amount, user_id])
    @users[user_id].delete(item_id)
    nil
  end

  def get_highest_bidder(item_id)
    ls = @items[item_id]
    ls.empty? ? -1 : ls[-1][1]
  end

  private

  def insert_sorted(arr, pair)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < pair
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.insert(lo, pair)
  end

  def remove_sorted(arr, pair)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < pair
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.delete_at(lo) if lo < arr.length && arr[lo] == pair
  end
end
''')

add("3816_lexicographically_smallest_string_after_deleting_duplicate_characters", r'''
# LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

# @param {String} s
# @return {String}
def lex_smallest_after_deletion(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  stk = []
  s.each_char do |c|
    while !stk.empty? && stk[-1] > c && cnt[stk[-1].ord - 97] > 1
      cnt[stk[-1].ord - 97] -= 1
      stk.pop
    end
    stk << c
  end
  while cnt[stk[-1].ord - 97] > 1
    cnt[stk[-1].ord - 97] -= 1
    stk.pop
  end
  stk.join
end
''')

add("3817_good_indices_in_a_digit_string", r'''
# LeetCode 3817 - Good Indices in a Digit String
# https://leetcode.com/problems/good-indices-in-a-digit-string/

# @param {String} s
# @return {Integer[]}
def good_indices(s)
  ans = []
  (0...s.length).each do |i|
    t = i.to_s
    k = t.length
    ans << i if i + 1 - k >= 0 && s[i + 1 - k, k] == t
  end
  ans
end
''')

add("3818_minimum_prefix_removal_to_make_array_strictly_increasing", r'''
# LeetCode 3818 - Minimum Prefix Removal to Make Array Strictly Increasing
# https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

# @param {Integer[]} nums
# @return {Integer}
def minimum_prefix_length(nums)
  (nums.length - 1).downto(1) { |i| return i if nums[i - 1] >= nums[i] }
  0
end
''')

add("3819_rotate_non_negative_elements", r'''
# LeetCode 3819 - Rotate Non Negative Elements
# https://leetcode.com/problems/rotate-non-negative-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def rotate_elements(nums, k)
  t = nums.select { |x| x >= 0 }
  m = t.length
  return nums if m == 0
  d = Array.new(m, 0)
  (0...m).each { |i| d[((i - k) % m + m) % m] = t[i] }
  j = 0
  (0...nums.length).each do |i|
    if nums[i] >= 0
      nums[i] = d[j]
      j += 1
    end
  end
  nums
end
''')

add("3820_pythagorean_distance_nodes_in_a_tree", r'''
# LeetCode 3820 - Pythagorean Distance Nodes in a Tree
# https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def special_nodes(n, edges, x, y, z)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  bfs = lambda do |start|
    dist = Array.new(n, 1_000_000_000)
    q = [start]
    dist[start] = 0
    qi = 0
    while qi < q.length
      u = q[qi]
      qi += 1
      g[u].each do |v|
        if dist[v] > dist[u] + 1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    dist
  end
  d1 = bfs.call(x)
  d2 = bfs.call(y)
  d3 = bfs.call(z)
  ans = 0
  (0...n).each do |i|
    a = [d1[i], d2[i], d3[i]].sort
    x0, x1, x2 = a[0], a[1], a[2]
    ans += 1 if x0 * x0 + x1 * x1 == x2 * x2
  end
  ans
end
''')

add("3821_find_nth_smallest_integer_with_k_one_bits", r'''
# LeetCode 3821 - Find Nth Smallest Integer with K One Bits
# https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def nth_smallest(n, k)
  mx = 50
  c = Array.new(mx) { Array.new(mx + 1, 0) }
  (0...mx).each do |i|
    c[i][0] = 1
    (1..i).each { |j| c[i][j] = c[i - 1][j - 1] + c[i - 1][j] }
  end
  ans = 0
  nn = n
  49.downto(0) do |i|
    if k >= 0 && nn > c[i][k]
      nn -= c[i][k]
      ans |= 1 << i
      k -= 1
      break if k == 0
    end
  end
  ans
end
''')


def main() -> None:
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        print(f"wrote {name}")
    print(f"total {len(S)}")


if __name__ == "__main__":
    main()
