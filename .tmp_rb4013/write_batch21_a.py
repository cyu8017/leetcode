#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3822_design_order_management_system", r'''
# LeetCode 3822 - Design Order Management System
# https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem
  def initialize
    @order_type_map = {}
    @price_map = {}
    @t = {}
  end

  def add_order(order_id, order_type, price)
    @order_type_map[order_id] = order_type
    @price_map[order_id] = price
    key = _key(order_type, price)
    @t[key] ||= []
    @t[key] << order_id
    nil
  end

  def modify_order(order_id, new_price)
    order_type = @order_type_map[order_id]
    old_price = @price_map[order_id]
    @price_map[order_id] = new_price
    old_key = _key(order_type, old_price)
    old_list = @t[old_key]
    old_list.each_with_index do |id, i|
      if id == order_id
        old_list.delete_at(i)
        break
      end
    end
    key = _key(order_type, new_price)
    @t[key] ||= []
    @t[key] << order_id
    nil
  end

  def cancel_order(order_id)
    order_type = @order_type_map.delete(order_id)
    price = @price_map.delete(order_id)
    key = _key(order_type, price)
    lst = @t[key]
    lst.each_with_index do |id, i|
      if id == order_id
        lst.delete_at(i)
        break
      end
    end
    nil
  end

  def get_orders_at_price(order_type, price)
    key = _key(order_type, price)
    lst = @t[key]
    return [] if lst.nil? || lst.empty?
    lst.dup
  end

  def _key(order_type, price)
    "#{order_type}##{price}"
  end
end
''')

add("3823_reverse_letters_then_special_characters_in_a_string", r'''
# LeetCode 3823 - Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

# @param {String} s
# @return {String}
def reverse_by_type(s)
  a = []
  b = []
  s.each_char do |c|
    if (c >= "A" && c <= "Z") || (c >= "a" && c <= "z")
      a << c
    else
      b << c
    end
  end
  j = a.length
  k = b.length
  arr = s.chars
  arr.each_index do |i|
    if (arr[i] >= "A" && arr[i] <= "Z") || (arr[i] >= "a" && arr[i] <= "z")
      j -= 1
      arr[i] = a[j]
    else
      k -= 1
      arr[i] = b[k]
    end
  end
  arr.join
end
''')

add("3824_minimum_k_to_reduce_array_within_limit", r'''
# LeetCode 3824 - Minimum K to Reduce Array Within Limit
# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

# @param {Integer[]} nums
# @return {Integer}
def minimum_k(nums)
  lo = 1
  hi = 100000
  while lo < hi
    mid = (lo + hi) / 2
    if check_k_limit(nums, mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end

def check_k_limit(nums, k)
  t = 0
  nums.each { |x| t += (x + k - 1) / k }
  t <= k * k
end
''')

add("3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and", r'''
# LeetCode 3825 - Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
# https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  ans = 0
  mx = nums.max
  m = bit_len_3825(mx)
  (0...m).each do |i|
    arr = []
    nums.each { |x| arr << x if ((x >> i) & 1) != 0 }
    ans = [ans, lis_3825(arr)].max
  end
  ans
end

def bit_len_3825(x)
  return 0 if x == 0
  n = 0
  while x > 0
    n += 1
    x >>= 1
  end
  n
end

def lis_3825(arr)
  g = []
  arr.each do |x|
    lo = 0
    hi = g.length
    while lo < hi
      mid = (lo + hi) >> 1
      if g[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == g.length
      g << x
    else
      g[lo] = x
    end
  end
  g.length
end
''')

add("3826_minimum_partition_score", r'''
# LeetCode 3826 - Minimum Partition Score
# https://leetcode.com/problems/minimum-partition-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_partition_score(nums, k)
  n = nums.length
  inf = 10**18
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }
  previous = Array.new(n + 1, inf)
  previous[0] = 0
  current = []

  value = lambda do |left, right|
    s = prefix[right] - prefix[left]
    s * (s + 1) / 2
  end

  compute = nil
  compute = lambda do |lo, hi, opt_lo, opt_hi|
    return if lo > hi
    mid = (lo + hi) >> 1
    best_index = -1
    last = [opt_hi, mid - 1].min
    (opt_lo..last).each do |split|
      next if previous[split] == inf
      candidate = previous[split] + value.call(split, mid)
      if candidate < current[mid]
        current[mid] = candidate
        best_index = split
      end
    end
    best_index = opt_lo if best_index == -1
    compute.call(lo, mid - 1, opt_lo, best_index)
    compute.call(mid + 1, hi, best_index, opt_hi)
  end

  (1..k).each do |parts|
    current = Array.new(n + 1, inf)
    compute.call(parts, n, parts - 1, n - 1)
    previous = current
  end
  previous[n]
end
''')

add("3827_count_monobit_integers", r'''
# LeetCode 3827 - Count Monobit Integers
# https://leetcode.com/problems/count-monobit-integers/

# @param {Integer} n
# @return {Integer}
def count_monobit(n)
  ans = 1
  i = 1
  x = 1
  while x <= n
    ans += 1
    x += 1 << i
    i += 1
  end
  ans
end
''')

add("3828_final_element_after_subarray_deletions", r'''
# LeetCode 3828 - Final Element After Subarray Deletions
# https://leetcode.com/problems/final-element-after-subarray-deletions/

# @param {Integer[]} nums
# @return {Integer}
def final_element(nums)
  [nums[0], nums[-1]].max
end
''')

add("3829_design_ride_sharing_system", r'''
# LeetCode 3829 - Design Ride Sharing System
# https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem
  def initialize
    @t = 0
    @riders = {}
    @drivers = {}
    @d = {}
    @rider_keys = []
    @driver_keys = []
  end

  def add_rider(rider_id)
    @d[rider_id] = @t
    @riders[@t] = rider_id
    @rider_keys << @t
    @t += 1
    nil
  end

  def add_driver(driver_id)
    @drivers[@t] = driver_id
    @driver_keys << @t
    @t += 1
    nil
  end

  def match_driver_with_rider
    @rider_keys.shift while !@rider_keys.empty? && !@riders.key?(@rider_keys[0])
    @driver_keys.shift while !@driver_keys.empty? && !@drivers.key?(@driver_keys[0])
    return [-1, -1] if @rider_keys.empty? || @driver_keys.empty?
    d_key = @driver_keys.shift
    r_key = @rider_keys.shift
    driver_id = @drivers.delete(d_key)
    rider_id = @riders.delete(r_key)
    [driver_id, rider_id]
  end

  def cancel_rider(rider_id)
    return nil unless @d.key?(rider_id)
    @riders.delete(@d[rider_id])
    nil
  end
end
''')

add("3830_longest_alternating_subarray_after_removing_at_most_one_element", r'''
# LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
# https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_alternating(nums)
  n = nums.length
  l1 = Array.new(n, 1)
  l2 = Array.new(n, 1)
  r1 = Array.new(n, 1)
  r2 = Array.new(n, 1)
  ans = 0
  (1...n).each do |i|
    if nums[i - 1] < nums[i]
      l1[i] = l2[i - 1] + 1
    elsif nums[i - 1] > nums[i]
      l2[i] = l1[i - 1] + 1
    end
    ans = [ans, [l1[i], l2[i]].max].max
  end
  (n - 2).downto(0) do |i|
    if nums[i + 1] > nums[i]
      r1[i] = r2[i + 1] + 1
    elsif nums[i + 1] < nums[i]
      r2[i] = r1[i + 1] + 1
    end
  end
  (1...(n - 1)).each do |i|
    if nums[i - 1] < nums[i + 1]
      ans = [ans, l2[i - 1] + r2[i + 1]].max
    elsif nums[i - 1] > nums[i + 1]
      ans = [ans, l1[i - 1] + r1[i + 1]].max
    end
  end
  ans
end
''')

add("3831_median_of_a_binary_search_tree_level", r'''
# LeetCode 3831 - Median of a Binary Search Tree Level
# https://leetcode.com/problems/median-of-a-binary-search-tree-level/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} level
# @return {Integer}
def level_median(root, level)
  nums = []
  dfs = nil
  dfs = lambda do |node, i|
    return if node.nil?
    dfs.call(node.left, i + 1)
    nums << node.val if i == level
    dfs.call(node.right, i + 1)
  end
  dfs.call(root, 0)
  return -1 if nums.empty?
  nums[nums.length / 2]
end
''')

add("3833_count_dominant_indices", r'''
# LeetCode 3833 - Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/

# @param {Integer[]} nums
# @return {Integer}
def dominant_indices(nums)
  n = nums.length
  ans = 0
  suf = nums[n - 1]
  (n - 2).downto(0) do |i|
    ans += 1 if nums[i] * (n - i - 1) > suf
    suf += nums[i]
  end
  ans
end
''')

add("3834_merge_adjacent_equal_elements", r'''
# LeetCode 3834 - Merge Adjacent Equal Elements
# https://leetcode.com/problems/merge-adjacent-equal-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def merge_adjacent(nums)
  stk = []
  nums.each do |x|
    stk << x
    while stk.length > 1 && stk[-1] == stk[-2]
      a = stk.pop
      b = stk.pop
      stk << a + b
    end
  end
  stk
end
''')

add("3835_count_subarrays_with_cost_less_than_or_equal_to_k", r'''
# LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
# https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  ans = 0
  q1 = []
  q2 = []
  l = 0
  nums.each_with_index do |x, r|
    q1.pop while !q1.empty? && nums[q1[-1]] <= x
    q2.pop while !q2.empty? && nums[q2[-1]] >= x
    q1 << r
    q2 << r
    while l < r && (nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k
      l += 1
      q1.shift if q1[0] < l
      q2.shift if q2[0] < l
    end
    ans += r - l + 1
  end
  ans
end
''')

add("3836_maximum_score_using_exactly_k_pairs", r'''
# LeetCode 3836 - Maximum Score Using Exactly K Pairs
# https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def max_score(nums1, nums2, k_lim)
  n = nums1.length
  m = nums2.length
  neg = -(10**18)
  f = Array.new(n + 1) { Array.new(m + 1) { Array.new(k_lim + 1, neg) } }
  f[0][0][0] = 0
  (0..n).each do |i|
    (0..m).each do |j|
      (0..k_lim).each do |k|
        f[i][j][k] = [f[i][j][k], f[i - 1][j][k]].max if i > 0
        f[i][j][k] = [f[i][j][k], f[i][j - 1][k]].max if j > 0
        if i > 0 && j > 0 && k > 0
          f[i][j][k] = [f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1] * nums2[j - 1]].max
        end
      end
    end
  end
  f[n][m][k_lim]
end
''')

add("3837_delayed_count_of_equal_elements", r'''
# LeetCode 3837 - Delayed Count of Equal Elements
# https://leetcode.com/problems/delayed-count-of-equal-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def delayed_count(nums, k)
  n = nums.length
  cnt = Hash.new(0)
  ans = Array.new(n, 0)
  (n - k - 2).downto(0) do |i|
    key = nums[i + k + 1]
    cnt[key] += 1
    ans[i] = cnt[nums[i]]
  end
  ans
end
''')

add("3838_weighted_word_mapping", r'''
# LeetCode 3838 - Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/

# @param {String[]} words
# @param {Integer[]} weights
# @return {String}
def map_word_weights(words, weights)
  ans = []
  words.each do |w|
    s = 0
    w.each_byte { |c| s = (s + weights[c - 97]) % 26 }
    ans << (97 + (25 - s)).chr
  end
  ans.join
end
''')

add("3839_number_of_prefix_connected_groups", r'''
# LeetCode 3839 - Number of Prefix Connected Groups
# https://leetcode.com/problems/number-of-prefix-connected-groups/

# @param {String[]} words
# @param {Integer} k
# @return {Integer}
def prefix_connected(words, k)
  cnt = Hash.new(0)
  words.each do |w|
    cnt[w[0, k]] += 1 if w.length >= k
  end
  ans = 0
  cnt.each_value { |v| ans += 1 if v > 1 }
  ans
end
''')

add("3840_house_robber_v", r'''
# LeetCode 3840 - House Robber V
# https://leetcode.com/problems/house-robber-v/

# @param {Integer[]} nums
# @param {Integer[]} colors
# @return {Integer}
def rob(nums, colors)
  n = nums.length
  f = 0
  g = nums[0]
  (1...n).each do |i|
    if colors[i - 1] == colors[i]
      nf = [f, g].max
      g = f + nums[i]
      f = nf
    else
      nf = [f, g].max
      g = nf + nums[i]
      f = nf
    end
  end
  [f, g].max
end
''')

add("3841_palindromic_path_queries_in_a_tree", r'''
# LeetCode 3841 - Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} s
# @param {String[]} queries
# @return {Boolean[]}
def palindromic_path_queries(n, edges, s, queries)
  graph = Array.new(n) { [] }
  edges.each do |edge|
    graph[edge[0]] << edge[1]
    graph[edge[1]] << edge[0]
  end
  parent = Array.new(n, -2)
  depth = Array.new(n, 0)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        depth[v] = depth[u] + 1
        order << v
      end
    end
    i += 1
  end
  size = Array.new(n, 0)
  heavy = Array.new(n, -1)
  (n - 1).downto(0) do |idx|
    u = order[idx]
    size[u] = 1
    graph[u].each do |v|
      if parent[v] == u
        size[u] += size[v]
        heavy[u] = v if heavy[u] == -1 || size[v] > size[heavy[u]]
      end
    end
  end
  head = Array.new(n, 0)
  position = Array.new(n, 0)
  stack = [[0, 0]]
  next_position = 0
  until stack.empty?
    chain = stack.pop
    u = chain[0]
    while u != -1
      head[u] = chain[1]
      position[u] = next_position
      next_position += 1
      graph[u].each do |v|
        stack << [v, v] if parent[v] == u && v != heavy[u]
      end
      u = heavy[u]
    end
  end
  bit = Array.new(n + 1, 0)

  update = lambda do |index, value|
    index += 1
    while index <= n
      bit[index] ^= value
      index += index & -index
    end
  end

  prefix = lambda do |index|
    result = 0
    while index > 0
      result ^= bit[index]
      index -= index & -index
    end
    result
  end

  path_mask = lambda do |u, v|
    result = 0
    while head[u] != head[v]
      u, v = v, u if depth[head[u]] < depth[head[v]]
      result ^= prefix.call(position[u] + 1) ^ prefix.call(position[head[u]])
      u = parent[head[u]]
    end
    u, v = v, u if position[u] > position[v]
    result ^ prefix.call(position[v] + 1) ^ prefix.call(position[u])
  end

  current = s.chars
  (0...n).each do |node|
    update.call(position[node], 1 << (current[node].ord - 97))
  end
  answer = []
  queries.each do |query|
    parts = query.split(" ")
    op = parts[0]
    node = parts[1].to_i
    if op == "update"
      new_character = parts[2][0]
      delta = (1 << (current[node].ord - 97)) ^ (1 << (new_character.ord - 97))
      update.call(position[node], delta)
      current[node] = new_character
    else
      other = parts[2].to_i
      mask = path_mask.call(node, other)
      answer << ((mask & (mask - 1)) == 0)
    end
  end
  answer
end
''')

add("3842_toggle_light_bulbs", r'''
# LeetCode 3842 - Toggle Light Bulbs
# https://leetcode.com/problems/toggle-light-bulbs/

# @param {Integer[]} bulbs
# @return {Integer[]}
def toggle_light_bulbs(bulbs)
  st = Array.new(101, 0)
  bulbs.each { |x| st[x] ^= 1 }
  ans = []
  (0...101).each { |i| ans << i if st[i] == 1 }
  ans
end
''')

add("3843_first_element_with_unique_frequency", r'''
# LeetCode 3843 - First Element with Unique Frequency
# https://leetcode.com/problems/first-element-with-unique-frequency/

# @param {Integer[]} nums
# @return {Integer}
def first_unique_freq(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  freq = Hash.new(0)
  cnt.each_value { |v| freq[v] += 1 }
  nums.each { |x| return x if freq[cnt[x]] == 1 }
  -1
end
''')

add("3844_longest_almost_palindromic_substring", r'''
# LeetCode 3844 - Longest Almost-Palindromic Substring
# https://leetcode.com/problems/longest-almost-palindromic-substring/

# @param {String} s
# @return {Integer}
def almost_palindromic(s)
  n = s.length
  ans = 0
  (0...n).each do |i|
    ans = [ans, [expand_3844(s, i, i), expand_3844(s, i, i + 1)].max].max
  end
  ans
end

def expand_3844(s, l, r)
  n = s.length
  while l >= 0 && r < n && s[l] == s[r]
    l -= 1
    r += 1
  end
  l1 = l - 1
  r1 = r
  l2 = l
  r2 = r + 1
  while l1 >= 0 && r1 < n && s[l1] == s[r1]
    l1 -= 1
    r1 += 1
  end
  while l2 >= 0 && r2 < n && s[l2] == s[r2]
    l2 -= 1
    r2 += 1
  end
  [n, [r1 - l1 - 1, r2 - l2 - 1].max].min
end
''')

add("3845_maximum_subarray_xor_with_bounded_range", r'''
# LeetCode 3845 - Maximum Subarray XOR with Bounded Range
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_xor(nums, k)
  nodes = [{ next: [0, 0], count: 0 }]

  add = lambda do |x, delta|
    u = 0
    nodes[u][:count] += delta
    15.downto(0) do |b|
      bit = (x >> b) & 1
      if nodes[u][:next][bit] == 0
        nodes[u][:next][bit] = nodes.length
        nodes << { next: [0, 0], count: 0 }
      end
      u = nodes[u][:next][bit]
      nodes[u][:count] += delta
    end
  end

  query = lambda do |x|
    u = 0
    res = 0
    15.downto(0) do |b|
      bit = (x >> b) & 1
      want = bit ^ 1
      v = nodes[u][:next][want]
      if v != 0 && nodes[v][:count] > 0
        res |= 1 << b
        u = v
      else
        u = nodes[u][:next][bit]
      end
    end
    res
  end

  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] ^ nums[i] }
  max_q = []
  min_q = []
  left = 0
  trie_left = 0
  ans = 0
  (0...n).each do |r|
    x = nums[r]
    max_q.pop while !max_q.empty? && nums[max_q[-1]] <= x
    max_q << r
    min_q.pop while !min_q.empty? && nums[min_q[-1]] >= x
    min_q << r
    while nums[max_q[0]] - nums[min_q[0]] > k
      max_q.shift if max_q[0] == left
      min_q.shift if min_q[0] == left
      left += 1
    end
    add.call(pref[r], 1)
    while trie_left < left
      add.call(pref[trie_left], -1)
      trie_left += 1
    end
    cur = query.call(pref[r + 1])
    ans = cur if cur > ans
  end
  ans
end
''')

add("3846_total_distance_to_type_a_string_using_one_finger", r'''
# LeetCode 3846 - Total Distance to Type a String Using One Finger
# https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

POS_3846 = {}
KEYS_3846 = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
3.times do |i|
  KEYS_3846[i].length.times { |j| POS_3846[KEYS_3846[i][j]] = [i, j] }
end

# @param {String} s
# @return {Integer}
def total_distance(s)
  pre = "a"
  ans = 0
  s.each_char do |cur|
    p1 = POS_3846[pre]
    p2 = POS_3846[cur]
    ans += (p1[0] - p2[0]).abs + (p1[1] - p2[1]).abs
    pre = cur
  end
  ans
end
''')

add("3847_find_the_score_difference_in_a_game", r'''
# LeetCode 3847 - Find the Score Difference in a Game
# https://leetcode.com/problems/find-the-score-difference-in-a-game/

# @param {Integer[]} nums
# @return {Integer}
def score_difference(nums)
  ans = 0
  k = 1
  nums.each_with_index do |x, i|
    k = -k if x.odd?
    k = -k if i % 6 == 5
    ans += k * x
  end
  ans
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        if body.startswith("\ufeff"):
            raise SystemExit(f"BOM in {name}")
        written += 1
        print(f"wrote {name}")
    print(f"batch21_a written={written}")


if __name__ == "__main__":
    main()
