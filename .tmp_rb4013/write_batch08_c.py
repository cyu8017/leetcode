#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2466_count_ways_to_build_good_strings", r'''
# LeetCode 2466 - Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/

# @param {Integer} low
# @param {Integer} high
# @param {Integer} zero
# @param {Integer} one
# @return {Integer}
def count_good_strings(low, high, zero, one)
  mod = 1_000_000_007
  dp = Array.new(high + 1, 0)
  dp[0] = 1
  ans = 0
  (1..high).each do |i|
    dp[i] = (dp[i] + dp[i - zero]) % mod if i >= zero
    dp[i] = (dp[i] + dp[i - one]) % mod if i >= one
    ans = (ans + dp[i]) % mod if i >= low
  end
  ans
end
''')

add("2467_most_profitable_path_in_a_tree", r'''
# LeetCode 2467 - Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

# @param {Integer[][]} edges
# @param {Integer} bob
# @param {Integer[]} amount
# @return {Integer}
def most_profitable_path(edges, bob, amount)
  n = amount.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  bob_time = Array.new(n, n)

  find_bob = lambda do |u, p, t|
    if u == 0
      bob_time[u] = t
      return true
    end
    g[u].each do |v|
      next if v == p
      next unless find_bob.call(v, u, t + 1)

      bob_time[u] = t
      return true
    end
    false
  end

  find_bob.call(bob, -1, 0)
  ans = [-(10**18)]

  dfs = lambda do |u, p, t, income|
    cur = amount[u]
    if t > bob_time[u]
      cur = 0
    elsif t == bob_time[u]
      cur /= 2
    end
    income += cur
    is_leaf = true
    g[u].each do |v|
      next if v == p

      is_leaf = false
      dfs.call(v, u, t + 1, income)
    end
    ans[0] = income if is_leaf && income > ans[0]
  end

  dfs.call(0, -1, 0, 0)
  ans[0]
end
''')

add("2468_split_message_based_on_limit", r'''
# LeetCode 2468 - Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/

# @param {String} message
# @param {Integer} limit
# @return {String[]}
def split_message(message, limit)
  n = message.length
  (1..n).each do |parts|
    sb_digits = parts.to_s.length
    ok = true
    idx = 0
    res = []
    (1..parts).each do |i|
      tail = 3 + i.to_s.length + sb_digits
      cap = limit - tail
      if cap <= 0 || idx >= n
        ok = false
        break
      end
      take = cap
      take = n - idx if take > n - idx
      res << message[idx, take] + "<" + i.to_s + "/" + parts.to_s + ">"
      idx += take
    end
    return res if ok && idx == n
  end
  []
end
''')

add("2469_convert_the_temperature", r'''
# LeetCode 2469 - Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/

# @param {Float} celsius
# @return {Float[]}
def convert_temperature(celsius)
  [celsius + 273.15, celsius * 1.80 + 32.00]
end
''')

add("2470_number_of_subarrays_with_lcm_equal_to_k", r'''
# LeetCode 2470 - Number of Subarrays With LCM Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_lcm(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 0
  n = nums.length
  (0...n).each do |i|
    cur = 1
    (i...n).each do |j|
      cur = (cur / gcd.call(cur, nums[j])) * nums[j]
      break if cur > k

      ans += 1 if cur == k
    end
  end
  ans
end
''')

add("2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level", r'''
# LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def minimum_operations(root)
  return 0 if root.nil?

  ans = 0
  q = [root]
  until q.empty?
    sz = q.length
    vals = Array.new(sz, 0)
    (0...sz).each do |i|
      node = q.shift
      vals[i] = node.val
      q << node.left if node.left
      q << node.right if node.right
    end
    sorted_vals = vals.sort
    pos = {}
    vals.each_with_index { |v, i| pos[v] = i }
    (0...sz).each do |i|
      next if vals[i] == sorted_vals[i]

      j = pos[sorted_vals[i]]
      vals[i], vals[j] = vals[j], vals[i]
      pos[vals[j]] = j
      pos[vals[i]] = i
      ans += 1
    end
  end
  ans
end
''')

add("2472_maximum_number_of_non_overlapping_palindrome_substrings", r'''
# LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_palindromes(s, k)
  n = s.length
  is_pal = Array.new(n) { Array.new(n, false) }
  (0...n).each { |i| is_pal[i][i] = true }
  (0...(n - 1)).each { |i| is_pal[i][i + 1] = s[i] == s[i + 1] }
  (3..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      is_pal[i][j] = s[i] == s[j] && is_pal[i + 1][j - 1]
    end
  end
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    dp[i] = dp[i + 1]
    (i + k - 1...n).each do |j|
      dp[i] = 1 + dp[j + 1] if is_pal[i][j] && 1 + dp[j + 1] > dp[i]
    end
  end
  dp[0]
end
''')

add("2473_minimum_cost_to_buy_apples", r'''
# LeetCode 2473 - Minimum Cost to Buy Apples
# https://leetcode.com/problems/minimum-cost-to-buy-apples/

# @param {Integer} n
# @param {Integer[][]} roads
# @param {Integer[]} apple_cost
# @param {Integer} k
# @return {Integer[]}
def min_cost(n, roads, apple_cost, k)
  g = Array.new(n + 1) { [] }
  roads.each do |r|
    g[r[0]] << [r[1], r[2]]
    g[r[1]] << [r[0], r[2]]
  end

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    return top if heap.empty?

    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left] < heap[smallest]
      smallest = right if right < heap.length && heap[right] < heap[smallest]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  ans = Array.new(n, 0)
  inf = 10**18
  (1..n).each do |start|
    dist = Array.new(n + 1, inf)
    dist[start] = 0
    pq = [[0, start]]
    until pq.empty?
      d, u = heap_pop.call(pq)
      next if d != dist[u]

      g[u].each do |v, w|
        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          heap_push.call(pq, [nd, v])
        end
      end
    end
    best = inf
    (1..n).each do |city|
      cost = dist[city] * (k + 1) + apple_cost[city - 1]
      best = cost if cost < best
    end
    ans[start - 1] = best
  end
  ans
end
''')

add("2475_number_of_unequal_triplets_in_array", r'''
# LeetCode 2475 - Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

# @param {Integer[]} nums
# @return {Integer}
def unequal_triplets(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ans = 0
  left = 0
  n = nums.length
  cnt.each_value do |c|
    right = n - left - c
    ans += left * c * right
    left += c
  end
  ans
end
''')

add("2476_closest_nodes_queries_in_a_binary_search_tree", r'''
# LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer[]} queries
# @return {Integer[][]}
def closest_nodes(root, queries)
  vals = []
  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    vals << node.val
    inorder.call(node.right)
  end
  inorder.call(root)

  lower_bound = lambda do |q|
    lo = 0
    hi = vals.length
    while lo < hi
      mid = (lo + hi) >> 1
      if vals[mid] < q
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  ans = []
  queries.each do |q|
    j = lower_bound.call(q)
    mx = j < vals.length ? vals[j] : -1
    mn = -1
    if j < vals.length && vals[j] == q
      mn = q
    elsif j > 0
      mn = vals[j - 1]
    end
    ans << [mn, mx]
  end
  ans
end
''')

add("2477_minimum_fuel_cost_to_report_to_the_capital", r'''
# LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

# @param {Integer[][]} roads
# @param {Integer} seats
# @return {Integer}
def minimum_fuel_cost(roads, seats)
  n = roads.length + 1
  g = Array.new(n) { [] }
  roads.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = [0]

  dfs = lambda do |u, p|
    people = 1
    g[u].each { |v| people += dfs.call(v, u) if v != p }
    ans[0] += (people + seats - 1) / seats if u != 0
    people
  end

  dfs.call(0, -1)
  ans[0]
end
''')

add("2478_number_of_beautiful_partitions", r'''
# LeetCode 2478 - Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/

# @param {String} s
# @param {Integer} k
# @param {Integer} min_length
# @return {Integer}
def beautiful_partitions(s, k, min_length)
  mod = 1_000_000_007
  is_prime = lambda { |c| c == "2" || c == "3" || c == "5" || c == "7" }
  n = s.length
  return 0 if !is_prime.call(s[0]) || is_prime.call(s[n - 1])

  dp = Array.new(k + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1
  (1..k).each do |p|
    pref = 0
    j = 0
    (1..n).each do |i|
      while j <= i - min_length
        pref = (pref + dp[p - 1][j]) % mod if j == 0 || (is_prime.call(s[j]) && !is_prime.call(s[j - 1]))
        j += 1
      end
      dp[p][i] = pref unless is_prime.call(s[i - 1])
    end
  end
  dp[k][n]
end
''')

add("2479_maximum_xor_of_two_non_overlapping_subtrees", r'''
# LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
# https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} values
# @return {Integer}
def max_xor(n, edges, values)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  subtree = Array.new(n, 0)

  dfs_sum = lambda do |u, p|
    s = values[u]
    g[u].each { |v| s += dfs_sum.call(v, u) if v != p }
    subtree[u] = s
    s
  end
  dfs_sum.call(0, -1)

  root = { "child" => [nil, nil] }

  insert = lambda do |x|
    cur = root
    46.downto(0) do |b|
      bit = (x >> b) & 1
      cur["child"][bit] = { "child" => [nil, nil] } if cur["child"][bit].nil?
      cur = cur["child"][bit]
    end
  end

  query = lambda do |x|
    cur = root
    return 0 if cur["child"][0].nil? && cur["child"][1].nil?

    res = 0
    46.downto(0) do |b|
      bit = (x >> b) & 1
      want = bit ^ 1
      if cur["child"][want]
        res |= 1 << b
        cur = cur["child"][want]
      elsif cur["child"][bit]
        cur = cur["child"][bit]
      else
        return res
      end
    end
    res
  end

  ans = [0]
  dfs = lambda do |u, p|
    g[u].each do |v|
      next if v == p

      xorv = query.call(subtree[v])
      ans[0] = xorv if xorv > ans[0]
      dfs.call(v, u)
      insert.call(subtree[v])
    end
  end
  dfs.call(0, -1)
  ans[0]
end
''')

add("2481_minimum_cuts_to_divide_a_circle", r'''
# LeetCode 2481 - Minimum Cuts to Divide a Circle
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

# @param {Integer} n
# @return {Integer}
def number_of_cuts(n)
  return 0 if n == 1
  return n / 2 if n.even?

  n
end
''')

add("2482_difference_between_ones_and_zeros_in_row_and_column", r'''
# LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

# @param {Integer[][]} grid
# @return {Integer[][]}
def ones_minus_zeros(grid)
  m = grid.length
  n = grid[0].length
  row = Array.new(m, 0)
  col = Array.new(n, 0)
  (0...m).each do |i|
    (0...n).each do |j|
      row[i] += grid[i][j]
      col[j] += grid[i][j]
    end
  end
  ans = Array.new(m) { Array.new(n, 0) }
  (0...m).each do |i|
    (0...n).each do |j|
      ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
    end
  end
  ans
end
''')

add("2483_minimum_penalty_for_a_shop", r'''
# LeetCode 2483 - Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# @param {String} customers
# @return {Integer}
def best_closing_time(customers)
  n = customers.length
  penalty = 0
  customers.each_char { |c| penalty += 1 if c == "Y" }
  best = penalty
  ans = 0
  (0...n).each do |i|
    if customers[i] == "Y"
      penalty -= 1
    else
      penalty += 1
    end
    if penalty < best
      best = penalty
      ans = i + 1
    end
  end
  ans
end
''')

add("2484_count_palindromic_subsequences", r'''
# LeetCode 2484 - Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/

# @param {String} s
# @return {Integer}
def count_palindromes(s)
  mod = 1_000_000_007
  n = s.length
  pref = Array.new(n) { Array.new(10) { Array.new(10, 0) } }
  suf = Array.new(n) { Array.new(10) { Array.new(10, 0) } }
  cnt = Array.new(10, 0)
  (0...n).each do |i|
    if i > 0
      (0...10).each do |a|
        (0...10).each { |b| pref[i][a][b] = pref[i - 1][a][b] }
      end
    end
    d = s[i].ord - 48
    (0...10).each { |a| pref[i][a][d] += cnt[a] }
    cnt[d] += 1
  end
  cnt = Array.new(10, 0)
  (n - 1).downto(0) do |i|
    if i + 1 < n
      (0...10).each do |a|
        (0...10).each { |b| suf[i][a][b] = suf[i + 1][a][b] }
      end
    end
    d = s[i].ord - 48
    (0...10).each { |a| suf[i][a][d] += cnt[a] }
    cnt[d] += 1
  end
  ans = 0
  (2...(n - 2)).each do |i|
    (0...10).each do |a|
      (0...10).each { |b| ans = (ans + pref[i - 1][a][b] * suf[i + 1][a][b]) % mod }
    end
  end
  ans
end
''')

add("2485_find_the_pivot_integer", r'''
# LeetCode 2485 - Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/

# @param {Integer} n
# @return {Integer}
def pivot_integer(n)
  total = n * (n + 1) / 2
  s = 0
  (1..n).each do |x|
    s += x
    return x if s == total - s + x
  end
  -1
end
''')

add("2486_append_characters_to_string_to_make_subsequence", r'''
# LeetCode 2486 - Append Characters to String to Make Subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

# @param {String} s
# @param {String} t
# @return {Integer}
def append_characters(s, t)
  j = 0
  i = 0
  while i < s.length && j < t.length
    j += 1 if s[i] == t[j]
    i += 1
  end
  t.length - j
end
''')

add("2487_remove_nodes_from_linked_list", r'''
# LeetCode 2487 - Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def remove_nodes(head)
  rev = lambda do |node|
    prev = nil
    while node
      nxt = node.next
      node.next = prev
      prev = node
      node = nxt
    end
    prev
  end

  head = rev.call(head)
  mx = 0
  dummy = ListNode.new(0, head)
  prev = dummy
  while prev.next
    if prev.next.val >= mx
      mx = prev.next.val
      prev = prev.next
    else
      prev.next = prev.next.next
    end
  end
  rev.call(dummy.next)
end
''')

add("2488_count_subarrays_with_median_k", r'''
# LeetCode 2488 - Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  pos = 0
  nums.each_with_index do |x, i|
    if x == k
      pos = i
      break
    end
  end
  bal = Hash.new(0)
  bal[0] = 1
  cur = 0
  (pos - 1).downto(0) do |i|
    cur += nums[i] < k ? -1 : 1
    bal[cur] += 1
  end
  ans = bal[0] + bal[1]
  cur = 0
  ((pos + 1)...nums.length).each do |i|
    cur += nums[i] < k ? -1 : 1
    ans += bal[-cur] + bal[1 - cur]
  end
  ans
end
''')

add("2489_number_of_substrings_with_fixed_ratio", r'''
# LeetCode 2489 - Number of Substrings With Fixed Ratio
# https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

# @param {String} s
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def fixed_ratio(s, num1, num2)
  pref = Hash.new(0)
  pref[0] = 1
  zeros = ones = ans = 0
  s.each_char do |c|
    if c == "0"
      zeros += 1
    else
      ones += 1
    end
    key = zeros * num2 - ones * num1
    ans += pref[key]
    pref[key] += 1
  end
  ans
end
''')

add("2490_circular_sentence", r'''
# LeetCode 2490 - Circular Sentence
# https://leetcode.com/problems/circular-sentence/

# @param {String} sentence
# @return {Boolean}
def is_circular_sentence(sentence)
  n = sentence.length
  return false if sentence[0] != sentence[n - 1]

  (0...n).each do |i|
    return false if sentence[i] == " " && sentence[i - 1] != sentence[i + 1]
  end
  true
end
''')

add("2491_divide_players_into_teams_of_equal_skill", r'''
# LeetCode 2491 - Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

# @param {Integer[]} skill
# @return {Integer}
def divide_players(skill)
  skill = skill.sort
  n = skill.length
  target = skill[0] + skill[n - 1]
  chem = 0
  (n / 2).times do |i|
    return -1 if skill[i] + skill[n - 1 - i] != target

    chem += skill[i] * skill[n - 1 - i]
  end
  chem
end
''')

add("2492_minimum_score_of_a_path_between_two_cities", r'''
# LeetCode 2492 - Minimum Score of a Path Between Two Cities
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def min_score(n, roads)
  g = Array.new(n + 1) { [] }
  roads.each do |r|
    g[r[0]] << [r[1], r[2]]
    g[r[1]] << [r[0], r[2]]
  end
  vis = Array.new(n + 1, false)
  ans = 1 << 30
  q = [1]
  vis[1] = true
  until q.empty?
    u = q.shift
    g[u].each do |v, w|
      ans = w if w < ans
      unless vis[v]
        vis[v] = true
        q << v
      end
    end
  end
  ans
end
''')

add("2493_divide_nodes_into_the_maximum_number_of_groups", r'''
# LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def magnificent_sets(n, edges)
  g = Array.new(n + 1) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  bfs_depth = lambda do |start|
    dist = Array.new(n + 1, -1)
    q = [start]
    dist[start] = 1
    best = 1
    until q.empty?
      u = q.shift
      best = dist[u] if dist[u] > best
      g[u].each do |v|
        if dist[v] == -1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    best
  end

  color = Array.new(n + 1, -1)
  components = []
  (1..n).each do |i|
    next if color[i] != -1

    comp = []
    q = [i]
    color[i] = 0
    bipartite = true
    until q.empty?
      u = q.shift
      comp << u
      g[u].each do |v|
        if color[v] == -1
          color[v] = color[u] ^ 1
          q << v
        elsif color[v] == color[u]
          bipartite = false
        end
      end
    end
    return -1 unless bipartite

    components << comp
  end
  ans = 0
  components.each do |comp|
    best = 0
    comp.each { |u| best = [best, bfs_depth.call(u)].max }
    ans += best
  end
  ans
end
''')


def write_all() -> None:
    written = 0
    for folder, content in S.items():
        path = ROOT / folder / "solution.rb"
        path.write_bytes(content.encode("utf-8"))
        written += 1
        print(folder)
    print(f"wrote {written}")


if __name__ == "__main__":
    write_all()
