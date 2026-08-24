#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3555_smallest_subarray_to_sort_in_every_sliding_window", r'''
# LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def min_subarray_sort(nums, k)
  f = lambda do |arr, i, j, inf|
    mi = inf
    mx = -inf
    l = -1
    r = -1
    (i..j).each do |p|
      if arr[p] < mx
        r = p
      else
        mx = arr[p]
      end
      q = j - p + i
      if arr[q] > mi
        l = q
      else
        mi = arr[q]
      end
    end
    return 0 if r == -1
    r - l + 1
  end
  inf = 1 << 30
  n = nums.length
  (0..(n - k)).map { |i| f.call(nums, i, i + k - 1, inf) }
end
''')

add("3556_sum_of_largest_prime_substrings", r'''
# LeetCode 3556 - Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/

# @param {String} s
# @return {Integer}
def sum_of_largest_primes(s)
  is_prime = lambda do |x|
    return false if x < 2
    sqrt_x = Math.sqrt(x).to_i
    (2..sqrt_x).each { |i| return false if x % i == 0 }
    true
  end
  st = {}
  n = s.length
  (0...n).each do |i|
    x = 0
    (i...n).each do |j|
      x = x * 10 + (s[j].ord - 48)
      st[x] = true if is_prime.call(x)
    end
  end
  nums = st.keys.sort
  ans = 0
  i = nums.length - 1
  while i >= 0 && nums.length - i <= 3
    ans += nums[i]
    i -= 1
  end
  ans
end
''')

add("3557_find_maximum_number_of_non_intersecting_substrings", r'''
# LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

# @param {String} word
# @return {Integer}
def max_substrings(word)
  ans = 0
  first = {}
  word.each_char.with_index do |c, i|
    if !first.key?(c)
      first[c] = i
    elsif i - first[c] + 1 >= 4
      ans += 1
      first.clear
    end
  end
  ans
end
''')

add("3558_number_of_ways_to_assign_edge_weights_i", r'''
# LeetCode 3558 - Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

# @param {Integer[][]} edges
# @return {Integer}
def assign_edge_weights(edges)
  mod = 1000000007
  n = edges.length + 1
  g = Array.new(n + 1) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  dfs = nil
  dfs = lambda do |i, fa|
    res = 0
    g[i].each do |j|
      res = [res, dfs.call(j, i) + 1].max if j != fa
    end
    res
  end
  pow2 = lambda do |exp|
    a = 2
    res = 1
    while exp > 0
      res = res * a % mod if (exp & 1) != 0
      a = a * a % mod
      exp >>= 1
    end
    res
  end
  pow2.call(dfs.call(1, 0) - 1)
end
''')

add("3559_number_of_ways_to_assign_edge_weights_ii", r'''
# LeetCode 3559 - Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def assign_edge_weights(edges, queries)
  mod = 1000000007
  log = 17
  n = edges.length + 1
  depth = Array.new(n + 1, 0)
  graph = Array.new(n + 1) { [] }
  parent = Array.new(log) { Array.new(n + 1, -1) }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  dfs = nil
  dfs = lambda do |u, p|
    parent[0][u] = p
    graph[u].each do |v|
      if v != p
        depth[v] = depth[u] + 1
        dfs.call(v, u)
      end
    end
  end
  lca = lambda do |u, v|
    u, v = v, u if depth[u] < depth[v]
    (log - 1).downto(0) do |k|
      u = parent[k][u] if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]
    end
    return u if u == v
    (log - 1).downto(0) do |k|
      if parent[k][u] != -1 && parent[k][u] != parent[k][v]
        u = parent[k][u]
        v = parent[k][v]
      end
    end
    parent[0][u]
  end
  mod_pow = lambda do |exp|
    base = 2
    res = 1
    while exp > 0
      res = res * base % mod if (exp & 1) != 0
      base = base * base % mod
      exp >>= 1
    end
    res
  end
  dfs.call(1, -1)
  (1...log).each do |k|
    (1..n).each do |v|
      parent[k][v] = parent[k - 1][parent[k - 1][v]] if parent[k - 1][v] != -1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    u, v = q[0], q[1]
    if u == v
      ans[i] = 0
      next
    end
    a = lca.call(u, v)
    d = depth[u] + depth[v] - 2 * depth[a]
    ans[i] = mod_pow.call(d - 1)
  end
  ans
end
''')

add("3560_find_minimum_log_transportation_cost", r'''
# LeetCode 3560 - Find Minimum Log Transportation Cost
# https://leetcode.com/problems/find-minimum-log-transportation-cost/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_cutting_cost(n, m, k)
  x = [n, m].max
  return 0 if x <= k
  k * (x - k)
end
''')

add("3561_resulting_string_after_adjacent_removals", r'''
# LeetCode 3561 - Resulting String After Adjacent Removals
# https://leetcode.com/problems/resulting-string-after-adjacent-removals/

# @param {String} s
# @return {String}
def resulting_string(s)
  is_contiguous = lambda do |a, b|
    x = (a.ord - b.ord).abs
    x == 1 || x == 25
  end
  stk = []
  s.each_char do |c|
    if !stk.empty? && is_contiguous.call(stk[-1], c)
      stk.pop
    else
      stk << c
    end
  end
  stk.join
end
''')

add("3562_maximum_profit_from_trading_stocks_with_discounts", r'''
# LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

# @param {Integer} n
# @param {Integer[]} present
# @param {Integer[]} future
# @param {Integer[][]} hierarchy
# @param {Integer} budget
# @return {Integer}
def max_profit(n, present, future, hierarchy, budget)
  g = Array.new(n + 1) { [] }
  hierarchy.each { |e| g[e[0]] << e[1] }
  dfs = nil
  dfs = lambda do |u|
    nxt = Array.new(budget + 1) { [0, 0] }
    g[u].each do |v|
      fv = dfs.call(v)
      budget.downto(0) do |j|
        (0..j).each do |jv|
          (0...2).each do |pre|
            nxt[j][pre] = [nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre]].max
          end
        end
      end
    end
    f = Array.new(budget + 1) { [0, 0] }
    price = future[u - 1]
    (0..budget).each do |j|
      (0...2).each do |pre|
        cost = present[u - 1] / (pre + 1)
        if j >= cost
          buy_profit = nxt[j - cost][1] + (price - cost)
          f[j][pre] = [nxt[j][0], buy_profit].max
        else
          f[j][pre] = nxt[j][0]
        end
      end
    end
    f
  end
  dfs.call(1)[budget][0]
end
''')

add("3563_lexicographically_smallest_string_after_adjacent_removals", r'''
# LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

# @param {String} s
# @return {String}
def lexicographically_smallest_string(s)
  is_consec = lambda do |a, b|
    d = (a.ord - b.ord).abs
    d == 1 || d == 25
  end
  n = s.length
  dp = Array.new(n + 1) { Array.new(n + 1, "") }
  (1..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length
      min_str = s[i] + dp[i + 1][j]
      ((i + 1)...j).each do |k|
        if is_consec.call(s[i], s[k]) && dp[i + 1][k] == ""
          cand = dp[k + 1][j]
          min_str = cand if cand < min_str
        end
      end
      dp[i][j] = min_str
    end
  end
  dp[0][n]
end
''')

add("3565_sequential_grid_path_cover", r'''
# LeetCode 3565 - Sequential Grid Path Cover
# https://leetcode.com/problems/sequential-grid-path-cover/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def find_path(grid, k)
  m = grid.length
  n = grid[0].length
  dirs = [-1, 0, 1, 0, -1]
  st = [0]
  path = []
  f = lambda { |i, j| i * n + j }
  dfs = nil
  dfs = lambda do |i, j, v|
    path << [i, j]
    return true if path.length == m * n
    idx = f.call(i, j)
    st[0] |= 1 << idx
    v += 1 if grid[i][j] == v
    (0...4).each do |t|
      x = i + dirs[t]
      y = j + dirs[t + 1]
      if x >= 0 && x < m && y >= 0 && y < n
        idx2 = f.call(x, y)
        if ((st[0] >> idx2) & 1) == 0 && (grid[x][y] == 0 || grid[x][y] == v)
          return true if dfs.call(x, y, v)
        end
      end
    end
    path.pop
    st[0] ^= 1 << idx
    false
  end
  (0...m).each do |i|
    (0...n).each do |j|
      if grid[i][j] == 0 || grid[i][j] == 1
        return path if dfs.call(i, j, 1)
        path.clear
        st[0] = 0
      end
    end
  end
  []
end
''')

add("3566_partition_array_into_two_equal_product_subsets", r'''
# LeetCode 3566 - Partition Array into Two Equal Product Subsets
# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def check_equal_partitions(nums, target)
  n = nums.length
  (0...(1 << n)).each do |i|
    x = 1
    y = 1
    (0...n).each do |j|
      if ((i >> j) & 1) != 0
        x *= nums[j]
      else
        y *= nums[j]
      end
      break if x > target || y > target
    end
    return true if x == target && y == target
  end
  false
end
''')

add("3567_minimum_absolute_difference_in_sliding_submatrix", r'''
# LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def min_abs_diff(grid, k)
  m = grid.length
  n = grid[0].length
  ans = Array.new(m - k + 1) { Array.new(n - k + 1, 0) }
  (0..(m - k)).each do |i|
    (0..(n - k)).each do |j|
      nums = []
      (i...(i + k)).each { |x| (j...(j + k)).each { |y| nums << grid[x][y] } }
      nums.sort!
      d = 2147483647
      (1...nums.length).each do |t|
        d = [d, (nums[t] - nums[t - 1]).abs].min if nums[t] != nums[t - 1]
      end
      ans[i][j] = d if d != 2147483647
    end
  end
  ans
end
''')

add("3568_minimum_moves_to_clean_the_classroom", r'''
# LeetCode 3568 - Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

# @param {String[]} classroom
# @param {Integer} energy
# @return {Integer}
def min_moves(classroom, energy)
  m = classroom.length
  n = classroom[0].length
  d = Array.new(m) { Array.new(n, 0) }
  x = 0
  y = 0
  cnt = 0
  (0...m).each do |i|
    (0...n).each do |j|
      c = classroom[i][j]
      if c == "S"
        x = i
        y = j
      elsif c == "L"
        d[i][j] = cnt
        cnt += 1
      end
    end
  end
  return 0 if cnt == 0
  vis = Array.new(m) { Array.new(n) { Array.new(energy + 1) { Array.new(1 << cnt, false) } } }
  q = [[x, y, energy, (1 << cnt) - 1]]
  vis[x][y][energy][(1 << cnt) - 1] = true
  dirs = [-1, 0, 1, 0, -1]
  ans = 0
  until q.empty?
    t = q
    q = []
    t.each do |s|
      i, j, cur_energy, mask = s
      return ans if mask == 0
      next if cur_energy <= 0
      (0...4).each do |kk|
        nx = i + dirs[kk]
        ny = j + dirs[kk + 1]
        next unless nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != "X"
        nxt_energy = classroom[nx][ny] == "R" ? energy : cur_energy - 1
        nxt_mask = mask
        nxt_mask &= ~(1 << d[nx][ny]) if classroom[nx][ny] == "L"
        unless vis[nx][ny][nxt_energy][nxt_mask]
          vis[nx][ny][nxt_energy][nxt_mask] = true
          q << [nx, ny, nxt_energy, nxt_mask]
        end
      end
    end
    ans += 1
  end
  -1
end
''')

add("3569_maximize_count_of_distinct_primes_after_split", r'''
# LeetCode 3569 - Maximize Count of Distinct Primes After Split
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_count(nums, queries)
  mx = nums.max
  queries.each { |q| mx = [mx, q[1]].max }
  is_p = Array.new(mx + 1, false)
  (2..mx).each { |i| is_p[i] = true }
  i = 2
  while i * i <= mx
    if is_p[i]
      (i * i).step(mx, i) { |j| is_p[j] = false }
    end
    i += 1
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    nums[q[0]] = q[1]
    best = 0
    left = {}
    right = {}
    nums.each do |v|
      right[v] = (right[v] || 0) + 1 if v <= mx && is_p[v]
    end
    (0...(nums.length - 1)).each do |ii|
      v = nums[ii]
      if v <= mx && is_p[v]
        left[v] = (left[v] || 0) + 1
        c = right[v] - 1
        if c == 0
          right.delete(v)
        else
          right[v] = c
        end
      end
      best = [best, left.length + right.length].max
    end
    ans[qi] = best
  end
  ans
end
''')

add("3571_find_the_shortest_superstring_ii", r'''
# LeetCode 3571 - Find the Shortest Superstring II
# https://leetcode.com/problems/find-the-shortest-superstring-ii/

# @param {String} s1
# @param {String} s2
# @return {String}
def shortest_superstring(s1, s2)
  return shortest_superstring(s2, s1) if s1.length > s2.length
  m = s1.length
  return s2 if s2.include?(s1)
  (0...m).each do |i|
    return s1[0...i] + s2 if s2.start_with?(s1[i..])
    length = m - i
    if s2.length >= length && s2[-length..] == s1[0...length]
      return s2 + s1[(m - i)..]
    end
  end
  s1 + s2
end
''')

add("3572_maximize_ysum_by_picking_a_triplet_of_distinct_xvalues", r'''
# LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

# @param {Integer[]} x
# @param {Integer[]} y
# @return {Integer}
def max_sum_distinct_triplet(x, y)
  n = x.length
  arr = (0...n).map { |i| [x[i], y[i]] }
  arr.sort_by! { |p| -p[1] }
  ans = 0
  vis = {}
  arr.each do |a, b|
    next if vis[a]
    vis[a] = true
    ans += b
    return ans if vis.length == 3
  end
  -1
end
''')

add("3573_best_time_to_buy_and_sell_stock_v", r'''
# LeetCode 3573 - Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

# @param {Integer[]} prices
# @param {Integer} k
# @return {Integer}
def maximum_profit(prices, k)
  n = prices.length
  f = Array.new(n) { Array.new(k + 1) { [0, 0, 0] } }
  (1..k).each do |j|
    f[0][j][1] = -prices[0]
    f[0][j][2] = prices[0]
  end
  (1...n).each do |i|
    (1..k).each do |j|
      f[i][j][0] = [f[i - 1][j][0], [f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]].max].max
      f[i][j][1] = [f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]].max
      f[i][j][2] = [f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]].max
    end
  end
  f[n - 1][k][0]
end
''')

add("3574_maximize_subarray_gcd_score", r'''
# LeetCode 3574 - Maximize Subarray GCD Score
# https://leetcode.com/problems/maximize-subarray-gcd-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_gcd_score(nums, k)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  n = nums.length
  cnt = Array.new(n, 0)
  (0...n).each do |i|
    x = nums[i]
    while x.even?
      cnt[i] += 1
      x /= 2
    end
  end
  ans = 0
  (0...n).each do |l|
    g = 0
    mi = 2147483647
    t = 0
    (l...n).each do |r|
      g = gcd.call(g, nums[r])
      if cnt[r] < mi
        mi = cnt[r]
        t = 1
      elsif cnt[r] == mi
        t += 1
      end
      score = g * (r - l + 1)
      score *= 2 if t <= k
      ans = [ans, score].max
    end
  end
  ans
end
''')

add("3575_maximum_good_subtree_score", r'''
# LeetCode 3575 - Maximum Good Subtree Score
# https://leetcode.com/problems/maximum-good-subtree-score/

# @param {Integer[]} vals
# @param {Integer[]} par
# @return {Integer}
def good_subtree_sum(vals, par)
  mod = 1000000007
  n = vals.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[par[i]] << i }
  ans = [0]
  digit_mask = lambda do |x|
    v = x
    mask = 0
    return [1, 1, 0] if x == 0
    while x > 0
      d = x % 10
      return [0, 0, 0] if (mask & (1 << d)) != 0
      mask |= 1 << d
      x /= 10
    end
    [mask, 1, v]
  end
  dfs = nil
  dfs = lambda do |u|
    dp = { 0 => 0 }
    dm = digit_mask.call(vals[u])
    dp[dm[0]] = dm[2] if dm[1] == 1
    g[u].each do |c|
      child = dfs.call(c)
      ndp = {}
      dp.each do |k1, v1|
        child.each do |k2, v2|
          if (k1 & k2) == 0
            nm = k1 | k2
            ndp[nm] = [ndp[nm] || 0, v1 + v2].max
          end
        end
      end
      dp.each { |k, v| ndp[k] = [ndp[k] || 0, v].max }
      child.each { |k, v| ndp[k] = [ndp[k] || 0, v].max }
      dp = ndp
    end
    best = 0
    dp.each_value { |s| best = [best, s].max }
    ans[0] = (ans[0] + best) % mod
    dp
  end
  dfs.call(0)
  ans[0]
end
''')

add("3576_transform_array_to_all_equal_elements", r'''
# LeetCode 3576 - Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_make_equal(nums, k)
  check = lambda do |arr, target, kk|
    cnt = 0
    sign = 1
    (0...(arr.length - 1)).each do |i|
      x = arr[i] * sign
      if x == target
        sign = 1
      else
        sign = -1
        cnt += 1
      end
    end
    cnt <= kk && arr[-1] * sign == target
  end
  check.call(nums, nums[0], k) || check.call(nums, -nums[0], k)
end
''')

add("3577_count_the_number_of_computer_unlocking_permutations", r'''
# LeetCode 3577 - Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

# @param {Integer[]} complexity
# @return {Integer}
def count_permutations(complexity)
  mod = 1000000007
  ans = 1
  (1...complexity.length).each do |i|
    return 0 if complexity[i] <= complexity[0]
    ans = ans * i % mod
  end
  ans
end
''')

add("3578_count_partitions_with_max_min_difference_at_most_k", r'''
# LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_partitions(nums, k)
  mod = 1000000007
  sl = {}
  n = nums.length
  f = Array.new(n + 1, 0)
  g = Array.new(n + 1, 0)
  f[0] = g[0] = 1
  keys = []
  add = lambda do |v|
    unless sl.key?(v)
      sl[v] = 0
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) >> 1
        if keys[mid] < v
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, v)
    end
    sl[v] += 1
  end
  rem = lambda do |v|
    c = sl[v] - 1
    if c == 0
      sl.delete(v)
      ix = keys.index(v)
      keys.delete_at(ix) if ix
    else
      sl[v] = c
    end
  end
  l = 1
  (1..n).each do |r|
    add.call(nums[r - 1])
    while keys[-1] - keys[0] > k
      rem.call(nums[l - 1])
      l += 1
    end
    f[r] = g[r - 1]
    f[r] = (f[r] - g[l - 2] + mod) % mod if l >= 2
    g[r] = (g[r - 1] + f[r]) % mod
  end
  f[n]
end
''')

add("3579_minimum_steps_to_convert_string_with_operations", r'''
# LeetCode 3579 - Minimum Steps to Convert String with Operations
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_operations(word1, word2)
  calc = lambda do |l, r, rev|
    cnt = Array.new(26) { Array.new(26, 0) }
    res = 0
    (l..r).each do |i|
      j = rev ? r - (i - l) : i
      a = word1[j].ord - 97
      b = word2[i].ord - 97
      if a != b
        if cnt[b][a] > 0
          cnt[b][a] -= 1
        else
          cnt[a][b] += 1
          res += 1
        end
      end
    end
    res
  end
  n = word1.length
  f = Array.new(n + 1, 2147483647 / 2)
  f[0] = 0
  (1..n).each do |i|
    (0...i).each do |j|
      a = calc.call(j, i - 1, false)
      b = 1 + calc.call(j, i - 1, true)
      f[i] = [f[i], f[j] + [a, b].min].min
    end
  end
  f[n]
end
''')

add("3581_count_odd_letters_from_number", r'''
# LeetCode 3581 - Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/

# @param {Integer} n
# @return {Integer}
def count_odd_letters(n)
  d = %w[zero one two three four five six seven eight nine]
  mask = 0
  while n > 0
    d[n % 10].each_char { |c| mask ^= 1 << (c.ord - 97) }
    n /= 10
  end
  cnt = 0
  while mask != 0
    cnt += mask & 1
    mask >>= 1
  end
  cnt
end
''')

add("3582_generate_tag_for_video_caption", r'''
# LeetCode 3582 - Generate Tag for Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption/

# @param {String} caption
# @return {String}
def generate_tag(caption)
  ans = "#"
  words = caption.strip.split
  i = 0
  words.each do |word|
    next if word.empty?
    w = word.downcase
    if i == 0
      ans += w
    else
      w = w[0].upcase + w[1..] if w.length > 0
      ans += w
    end
    break if ans.length >= 100
    i += 1
  end
  ans = ans[0, 100] if ans.length > 100
  ans
end
''')

add("3583_count_special_triplets", r'''
# LeetCode 3583 - Count Special Triplets
# https://leetcode.com/problems/count-special-triplets/

# @param {Integer[]} nums
# @return {Integer}
def special_triplets(nums)
  left = {}
  right = {}
  nums.each { |x| right[x] = (right[x] || 0) + 1 }
  ans = 0
  mod = 1000000007
  nums.each do |x|
    right[x] -= 1
    lv = left[x * 2] || 0
    rv = right[x * 2] || 0
    ans = (ans + lv * rv % mod) % mod
    left[x] = (left[x] || 0) + 1
  end
  ans
end
''')

add("3584_maximum_product_of_first_and_last_elements_of_a_subsequence", r'''
# LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer}
def maximum_product(nums, m)
  ans = -(10**18)
  mx = -(10**18)
  mi = 10**18
  ((m - 1)...nums.length).each do |i|
    x = nums[i]
    y = nums[i - m + 1]
    mi = [mi, y].min
    mx = [mx, y].max
    ans = [ans, [x * mi, x * mx].max].max
  end
  ans
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
