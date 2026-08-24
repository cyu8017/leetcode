#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2495_number_of_subarrays_having_even_product", r'''
# LeetCode 2495 - Number of Subarrays Having Even Product
# https://leetcode.com/problems/number-of-subarrays-having-even-product/

# @param {Integer[]} nums
# @return {Integer}
def even_product(nums)
  n = nums.length
  total = n * (n + 1) / 2
  odd_len = 0
  odd = 0
  nums.each do |x|
    if x.odd?
      odd += 1
      odd_len += odd
    else
      odd = 0
    end
  end
  total - odd_len
end
''')

add("2496_maximum_value_of_a_string_in_an_array", r'''
# LeetCode 2496 - Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

# @param {String[]} strs
# @return {Integer}
def maximum_value(strs)
  ans = 0
  strs.each do |s|
    all_digit = true
    val = 0
    s.each_char do |c|
      if c < "0" || c > "9"
        all_digit = false
        break
      end
      val = val * 10 + (c.ord - 48)
    end
    val = s.length unless all_digit
    ans = val if val > ans
  end
  ans
end
''')

add("2497_maximum_star_sum_of_a_graph", r'''
# LeetCode 2497 - Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

# @param {Integer[]} vals
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def max_star_sum(vals, edges, k)
  n = vals.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = vals[0]
  (0...n).each do |i|
    neigh = []
    g[i].each { |v| neigh << vals[v] if vals[v] > 0 }
    neigh.sort!.reverse!
    s = vals[i]
    [neigh.length, k].min.times { |j| s += neigh[j] }
    ans = s if s > ans
  end
  ans
end
''')

add("2498_frog_jump_ii", r'''
# LeetCode 2498 - Frog Jump II
# https://leetcode.com/problems/frog-jump-ii/

# @param {Integer[]} stones
# @return {Integer}
def max_jump(stones)
  ans = stones[1] - stones[0]
  (2...stones.length).each do |i|
    diff = stones[i] - stones[i - 2]
    ans = diff if diff > ans
  end
  ans
end
''')

add("2499_minimum_total_cost_to_make_arrays_unequal", r'''
# LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_total_cost(nums1, nums2)
  n = nums1.length
  freq = Hash.new(0)
  ans = 0
  same = 0
  (0...n).each do |i|
    next unless nums1[i] == nums2[i]

    same += 1
    freq[nums1[i]] += 1
    ans += i
  end
  max_freq = 0
  max_val = 0
  freq.each do |key, value|
    if value > max_freq
      max_freq = value
      max_val = key
    end
  end
  need = max_freq * 2 - same
  return ans if need <= 0

  i = 0
  while i < n && need > 0
    if nums1[i] != nums2[i] && nums1[i] != max_val && nums2[i] != max_val
      ans += i
      need -= 1
    end
    i += 1
  end
  need > 0 ? -1 : ans
end
''')

add("2500_delete_greatest_value_in_each_row", r'''
# LeetCode 2500 - Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

# @param {Integer[][]} grid
# @return {Integer}
def delete_greatest_value(grid)
  grid.each(&:sort!)
  ans = 0
  n = grid[0].length
  (0...n).each do |c|
    mx = 0
    grid.each { |row| mx = row[c] if row[c] > mx }
    ans += mx
  end
  ans
end
''')

add("2501_longest_square_streak_in_an_array", r'''
# LeetCode 2501 - Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def longest_square_streak(nums)
  seen = {}
  nums.each { |x| seen[x] = true }
  best = -1
  nums.each do |x|
    next unless seen[x]

    length = 0
    cur = x
    while seen[cur]
      length += 1
      seen.delete(cur)
      break if cur > 100_000

      cur = cur * cur
    end
    best = length if length >= 2 && length > best
  end
  best
end
''')

add("2502_design_memory_allocator", r'''
# LeetCode 2502 - Design Memory Allocator
# https://leetcode.com/problems/design-memory-allocator/

class Allocator
  def initialize(n)
    @mem = Array.new(n, 0)
  end

  def allocate(size, m_id)
    free_cnt = 0
    @mem.each_index do |i|
      if @mem[i] == 0
        free_cnt += 1
        if free_cnt == size
          start = i - size + 1
          (start..i).each { |j| @mem[j] = m_id }
          return start
        end
      else
        free_cnt = 0
      end
    end
    -1
  end

  def free_memory(m_id)
    cnt = 0
    @mem.each_index do |i|
      if @mem[i] == m_id
        @mem[i] = 0
        cnt += 1
      end
    end
    cnt
  end
end
''')

add("2503_maximum_number_of_points_from_grid_queries", r'''
# LeetCode 2503 - Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

# @param {Integer[][]} grid
# @param {Integer[]} queries
# @return {Integer[]}
def max_points(grid, queries)
  m = grid.length
  n = grid[0].length
  order = (0...queries.length).to_a
  order.sort_by! { |i| queries[i] }
  ans = Array.new(queries.length, 0)
  visited = Array.new(m) { Array.new(n, false) }
  pq = [[grid[0][0], 0, 0]]
  visited[0][0] = true
  points = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

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

  order.each do |qi|
    q = queries[qi]
    while !pq.empty? && pq[0][0] < q
      _, r, c = heap_pop.call(pq)
      points += 1
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]

        visited[nr][nc] = true
        heap_push.call(pq, [grid[nr][nc], nr, nc])
      end
    end
    ans[qi] = points
  end
  ans
end
''')

add("2505_bitwise_or_of_all_subsequence_sums", r'''
# LeetCode 2505 - Bitwise OR of All Subsequence Sums
# https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

# @param {Integer[]} nums
# @return {Integer}
def subsequence_sum_or(nums)
  ans = 0
  prefix = 0
  nums.each do |x|
    prefix += x
    ans |= x | prefix
  end
  ans
end
''')

add("2506_count_pairs_of_similar_strings", r'''
# LeetCode 2506 - Count Pairs Of Similar Strings
# https://leetcode.com/problems/count-pairs-of-similar-strings/

# @param {String[]} words
# @return {Integer}
def similar_pairs(words)
  freq = Hash.new(0)
  ans = 0
  words.each do |w|
    mask = 0
    w.each_byte { |b| mask |= 1 << (b - 97) }
    ans += freq[mask]
    freq[mask] += 1
  end
  ans
end
''')

add("2507_smallest_value_after_replacing_with_sum_of_prime_factors", r'''
# LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

# @param {Integer} n
# @return {Integer}
def smallest_value(n)
  sum_prime_factors = lambda do |x|
    s = 0
    i = 2
    while i * i <= x
      while x % i == 0
        s += i
        x /= i
      end
      i += 1
    end
    s += x if x > 1
    s
  end

  loop do
    s = sum_prime_factors.call(n)
    return n if s == n

    n = s
  end
end
''')

add("2508_add_edges_to_make_degrees_of_all_nodes_even", r'''
# LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean}
def is_possible(n, edges)
  deg = Array.new(n + 1, 0)
  adj = Array.new(n + 1) { {} }
  edges.each do |e|
    u = e[0]
    v = e[1]
    deg[u] += 1
    deg[v] += 1
    adj[u][v] = true
    adj[v][u] = true
  end
  odd = (1..n).select { |i| deg[i].odd? }
  return true if odd.empty?

  if odd.length == 2
    a, b = odd
    return true unless adj[a][b]

    (1..n).each do |i|
      return true if i != a && i != b && !adj[a][i] && !adj[b][i]
    end
    return false
  end
  if odd.length == 4
    a, b, c, d = odd
    return (!adj[a][b] && !adj[c][d]) || (!adj[a][c] && !adj[b][d]) || (!adj[a][d] && !adj[b][c])
  end
  false
end
''')

add("2509_cycle_length_queries_in_a_tree", r'''
# LeetCode 2509 - Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def cycle_length_queries(n, queries)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    a = q[0]
    b = q[1]
    steps = 0
    while a != b
      if a > b
        a /= 2
      else
        b /= 2
      end
      steps += 1
    end
    ans[i] = steps + 1
  end
  ans
end
''')

add("2510_check_if_there_is_a_path_with_equal_number_of_0s_and_1s", r'''
# LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
# https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

# @param {Integer[][]} grid
# @return {Boolean}
def is_there_a_path(grid)
  m = grid.length
  n = grid[0].length
  return false if (m + n - 1).odd?

  target = (m + n - 1) / 2
  memo = {}

  dfs = lambda do |r, c, bal|
    return false if r >= m || c >= n

    bal += grid[r][c]
    return false if bal > target || bal + (m - 1 - r) + (n - 1 - c) < target
    return bal == target if r == m - 1 && c == n - 1

    key = [r, c, bal]
    return memo[key] if memo.key?(key)

    ok = dfs.call(r + 1, c, bal) || dfs.call(r, c + 1, bal)
    memo[key] = ok
    ok
  end

  dfs.call(0, 0, 0)
end
''')

add("2511_maximum_enemy_forts_that_can_be_captured", r'''
# LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

# @param {Integer[]} forts
# @return {Integer}
def capture_forts(forts)
  ans = 0
  prev = -1
  forts.each_with_index do |f, i|
    next if f == 0

    ans = i - prev - 1 if prev >= 0 && forts[prev] == -f && i - prev - 1 > ans
    prev = i
  end
  ans
end
''')

add("2512_reward_top_k_students", r'''
# LeetCode 2512 - Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/

# @param {String[]} positive_feedback
# @param {String[]} negative_feedback
# @param {String[]} report
# @param {Integer[]} student_id
# @param {Integer} k
# @return {Integer[]}
def top_students(positive_feedback, negative_feedback, report, student_id, k)
  pos = {}
  neg = {}
  positive_feedback.each { |w| pos[w] = true }
  negative_feedback.each { |w| neg[w] = true }
  arr = Array.new(report.length)
  report.each_with_index do |r, i|
    score = 0
    r.split(" ").each do |w|
      next if w.empty?

      if pos[w]
        score += 3
      elsif neg[w]
        score -= 1
      end
    end
    arr[i] = [student_id[i], score]
  end
  arr.sort_by! { |x| [-x[1], x[0]] }
  arr[0, k].map { |x| x[0] }
end
''')

add("2513_minimize_the_maximum_of_two_arrays", r'''
# LeetCode 2513 - Minimize the Maximum of Two Arrays
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

# @param {Integer} divisor1
# @param {Integer} divisor2
# @param {Integer} unique_cnt1
# @param {Integer} unique_cnt2
# @return {Integer}
def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  lcm = (divisor1 / gcd.call(divisor1, divisor2)) * divisor2
  ok = lambda do |x|
    a = x - x / divisor1
    b = x - x / divisor2
    both = x - x / lcm
    a >= unique_cnt1 && b >= unique_cnt2 && both >= unique_cnt1 + unique_cnt2
  end

  lo = 1
  hi = 2**62
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

add("2514_count_anagrams", r'''
# LeetCode 2514 - Count Anagrams
# https://leetcode.com/problems/count-anagrams/

# @param {String} s
# @return {Integer}
def count_anagrams(s)
  mod = 1_000_000_007

  mod_pow = lambda do |a, e|
    res = 1
    a %= mod
    while e > 0
      res = res * a % mod if (e & 1) != 0
      a = a * a % mod
      e >>= 1
    end
    res
  end

  words = s.strip.empty? ? [] : s.strip.split(/\s+/)
  max_n = 0
  words.each { |w| max_n = w.length if w.length > max_n }
  fact = Array.new(max_n + 1, 0)
  inv_fact = Array.new(max_n + 1, 0)
  fact[0] = 1
  (1..max_n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact[max_n] = mod_pow.call(fact[max_n], mod - 2)
  max_n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }
  ans = 1
  words.each do |word|
    cnt = Array.new(26, 0)
    word.each_byte { |b| cnt[b - 97] += 1 }
    cur = fact[word.length]
    cnt.each { |c| cur = cur * inv_fact[c] % mod }
    ans = ans * cur % mod
  end
  ans
end
''')

add("2515_shortest_distance_to_target_string_in_a_circular_array", r'''
# LeetCode 2515 - Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

# @param {String[]} words
# @param {String} target
# @param {Integer} start_index
# @return {Integer}
def closest_target(words, target, start_index)
  n = words.length
  best = -1
  words.each_with_index do |w, i|
    next unless w == target

    d = i - start_index
    d = -d if d < 0
    d = n - d if n - d < d
    best = d if best < 0 || d < best
  end
  best
end
''')

add("2516_take_k_of_each_character_from_left_and_right", r'''
# LeetCode 2516 - Take K of Each Character From Left and Right
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def take_characters(s, k)
  n = s.length
  cnt = [0, 0, 0]
  s.each_byte { |b| cnt[b - 97] += 1 }
  return -1 if cnt[0] < k || cnt[1] < k || cnt[2] < k

  need = [cnt[0] - k, cnt[1] - k, cnt[2] - k]
  window = [0, 0, 0]
  left = 0
  max_mid = 0
  (0...n).each do |right|
    window[s[right].ord - 97] += 1
    while window[0] > need[0] || window[1] > need[1] || window[2] > need[2]
      window[s[left].ord - 97] -= 1
      left += 1
    end
    max_mid = right - left + 1 if right - left + 1 > max_mid
  end
  n - max_mid
end
''')

add("2517_maximum_tastiness_of_candy_basket", r'''
# LeetCode 2517 - Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

# @param {Integer[]} price
# @param {Integer} k
# @return {Integer}
def maximum_tastiness(price, k)
  price = price.sort
  ok = lambda do |d|
    cnt = 1
    last = price[0]
    (1...price.length).each do |i|
      if price[i] - last >= d
        cnt += 1
        last = price[i]
        return true if cnt >= k
      end
    end
    false
  end

  lo = 0
  hi = price[-1] - price[0]
  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("2518_number_of_great_partitions", r'''
# LeetCode 2518 - Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_partitions(nums, k)
  mod = 1_000_000_007
  total = nums.sum
  return 0 if total < 2 * k

  dp = Array.new(k, 0)
  dp[0] = 1
  nums.each do |x|
    (k - 1).downto(x) { |s| dp[s] = (dp[s] + dp[s - x]) % mod }
  end
  bad = 0
  dp.each { |v| bad = (bad + v) % mod }
  all_ways = 1
  nums.length.times { all_ways = all_ways * 2 % mod }
  (all_ways - 2 * bad % mod + mod) % mod
end
''')

add("2519_count_the_number_of_k_big_indices", r'''
# LeetCode 2519 - Count the Number of K-Big Indices
# https://leetcode.com/problems/count-the-number-of-k-big-indices/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_big_indices(nums, k)
  n = nums.length
  uniq = nums.sort
  m = 0
  uniq.each_index do |i|
    if i == 0 || uniq[i] != uniq[i - 1]
      uniq[m] = uniq[i]
      m += 1
    end
  end
  rank = {}
  (0...m).each { |i| rank[uniq[i]] = i + 1 }
  left = Array.new(n, 0)
  right = Array.new(n, 0)

  add = lambda do |bit, i, v|
    while i < bit.length
      bit[i] += v
      i += i & -i
    end
  end

  sum_ft = lambda do |bit, i|
    s = 0
    while i > 0
      s += bit[i]
      i -= i & -i
    end
    s
  end

  ft = Array.new(m + 2, 0)
  (0...n).each do |i|
    r = rank[nums[i]]
    left[i] = sum_ft.call(ft, r - 1)
    add.call(ft, r, 1)
  end
  ft = Array.new(m + 2, 0)
  (n - 1).downto(0) do |i|
    r = rank[nums[i]]
    right[i] = sum_ft.call(ft, r - 1)
    add.call(ft, r, 1)
  end
  ans = 0
  (0...n).each { |i| ans += 1 if left[i] >= k && right[i] >= k }
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
