#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3639_minimum_time_to_activate_string", r'''
# LeetCode 3639 - Minimum Time to Activate String
# https://leetcode.com/problems/minimum-time-to-activate-string/

# @param {String} s
# @param {Integer[]} order
# @param {Integer} k
# @return {Integer}
def min_time(s, order, k)
  n = s.length
  total = n * (n + 1) / 2
  return -1 if k > total

  count_valid = lambda do |t|
    star = Array.new(n, false)
    (0..t).each { |i| star[order[i]] = true }
    invalid = 0
    i = 0
    while i < n
      if star[i]
        i += 1
        next
      end
      j = i
      j += 1 while j < n && !star[j]
      l = j - i
      invalid += l * (l + 1) / 2
      i = j
    end
    total - invalid
  end

  lo = 0
  hi = n - 1
  ans = -1
  while lo <= hi
    mid = (lo + hi) >> 1
    if count_valid.call(mid) >= k
      ans = mid
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  ans
end
''')

add("3640_trionic_array_ii", r'''
# LeetCode 3640 - Trionic Array II
# https://leetcode.com/problems/trionic-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_sum_trionic(nums)
  n = nums.length
  i = 0
  ans = -Float::INFINITY
  while i < n
    l = i
    i += 1
    i += 1 while i < n && nums[i - 1] < nums[i]
    next if i == l + 1

    p = i - 1
    s = nums[p - 1] + nums[p]
    while i < n && nums[i - 1] > nums[i]
      s += nums[i]
      i += 1
    end
    next if i == p + 1 || i == n || nums[i - 1] == nums[i]

    q = i - 1
    s += nums[i]
    i += 1
    mx = 0
    t = 0
    while i < n && nums[i - 1] < nums[i]
      t += nums[i]
      i += 1
      mx = t if t > mx
    end
    s += mx
    mx = 0
    t = 0
    (p - 2).downto(l) do |j|
      t += nums[j]
      mx = t if t > mx
    end
    s += mx
    ans = s if s > ans
    i = q
  end
  ans.to_i
end
''')

add("3641_longest_semi_repeating_subarray", r'''
# LeetCode 3641 - Longest Semi-Repeating Subarray
# https://leetcode.com/problems/longest-semi-repeating-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_subarray(nums, k)
  cnt = Hash.new(0)
  ans = 0
  cur = 0
  l = 0
  nums.each_with_index do |x, r|
    c = cnt[x] + 1
    cnt[x] = c
    cur += 1 if c == 2
    while cur > k
      c2 = cnt[nums[l]] - 1
      cnt[nums[l]] = c2
      cur -= 1 if c2 == 1
      l += 1
    end
    ans = r - l + 1 if r - l + 1 > ans
  end
  ans
end
''')

add("3643_flip_square_submatrix_vertically", r'''
# LeetCode 3643 - Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/

# @param {Integer[][]} grid
# @param {Integer} x
# @param {Integer} y
# @param {Integer} k
# @return {Integer[][]}
def reverse_submatrix(grid, x, y, k)
  (x...(x + k / 2)).each do |i|
    i2 = x + k - 1 - (i - x)
    (y...(y + k)).each do |j|
      grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
    end
  end
  grid
end
''')

add("3644_maximum_k_to_sort_a_permutation", r'''
# LeetCode 3644 - Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

# @param {Integer[]} nums
# @return {Integer}
def sort_permutation(nums)
  ans = -1
  nums.each_with_index do |v, i|
    ans &= v if i != v
  end
  [ans, 0].max
end
''')

add("3645_maximum_total_from_optimal_activation_order", r'''
# LeetCode 3645 - Maximum Total from Optimal Activation Order
# https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

# @param {Integer[]} value
# @param {Integer[]} limit
# @return {Integer}
def max_total(value, limit)
  g = {}
  limit.each_with_index do |lim, i|
    (g[lim] ||= []) << value[i]
  end
  ans = 0
  g.each do |lim, vs|
    vs.sort!.reverse!
    ans += vs[0, lim].sum
  end
  ans
end
''')

add("3646_next_special_palindrome_number", r'''
# LeetCode 3646 - Next Special Palindrome Number
# https://leetcode.com/problems/next-special-palindrome-number/

# @param {Integer} n
# @return {Integer}
def special_palindrome(n)
  cands = []
  half_cnt = Array.new(10, 0)
  mid = 0
  half_len = 0
  dfs = nil
  dfs = lambda do |pos, cur|
    if pos == half_len
      left = cur.join
      s = left
      s += mid.to_s if mid > 0
      s += left.reverse
      cands << s.to_i
      return
    end
    (1..9).each do |d|
      next if half_cnt[d] == 0

      half_cnt[d] -= 1
      cur << d
      dfs.call(pos + 1, cur)
      cur.pop
      half_cnt[d] += 1
    end
  end
  gen = lambda do |mask|
    total = 0
    odd = 0
    (1..9).each do |d|
      next unless (mask >> d) & 1 == 1

      total += d
      odd += 1 if d.odd?
    end
    return if total == 0 || total > 18 || odd > 1

    10.times { |i| half_cnt[i] = 0 }
    mid = 0
    (1..9).each do |d|
      next if ((mask >> d) & 1) == 0

      half_cnt[d] = d / 2
      mid = d if d.odd?
    end
    half_len = total / 2
    dfs.call(0, [])
  end
  (1...(1 << 10)).each do |mask|
    next if mask & 1 != 0

    gen.call(mask)
  end
  cands.sort!
  cands.each { |v| return v if v > n }
  -1
end
''')

add("3647_maximum_weight_in_two_bags", r'''
# LeetCode 3647 - Maximum Weight in Two Bags
# https://leetcode.com/problems/maximum-weight-in-two-bags/

# @param {Integer[]} weights
# @param {Integer} w1
# @param {Integer} w2
# @return {Integer}
def max_weight(weights, w1, w2)
  f = Array.new(w1 + 1) { Array.new(w2 + 1, 0) }
  weights.each do |x|
    w1.downto(0) do |j|
      w2.downto(0) do |k|
        f[j][k] = [f[j][k], f[j - x][k] + x].max if x <= j
        f[j][k] = [f[j][k], f[j][k - x] + x].max if x <= k
      end
    end
  end
  f[w1][w2]
end
''')

add("3648_minimum_sensors_to_cover_grid", r'''
# LeetCode 3648 - Minimum Sensors to Cover Grid
# https://leetcode.com/problems/minimum-sensors-to-cover-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_sensors(n, m, k)
  cover = 2 * k + 1
  ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
end
''')

add("3649_number_of_perfect_pairs", r'''
# LeetCode 3649 - Number of Perfect Pairs
# https://leetcode.com/problems/number-of-perfect-pairs/

# @param {Integer[]} nums
# @return {Integer}
def perfect_pairs(nums)
  n = nums.length
  abs_nums = nums.map(&:abs).sort
  ans = 0
  j = 0
  (0...n).each do |i|
    j = i + 1 if j < i + 1
    j += 1 while j < n && abs_nums[j] <= 2 * abs_nums[i]
    ans += j - i - 1
  end
  ans
end
''')

add("3650_minimum_cost_path_with_edge_reversals", r'''
# LeetCode 3650 - Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_cost(n, edges)
  g = Array.new(n) { [] }
  edges.each do |u, v, w|
    g[u] << [v, w]
    g[v] << [u, w * 2]
  end
  inf = 1073741823
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    d, u = pq.shift
    next if d > dist[u]
    return d if u == n - 1

    g[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        pq << [nd, v]
      end
    end
  end
  -1
end
''')

add("3651_minimum_cost_path_with_teleportations", r'''
# LeetCode 3651 - Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def min_cost(grid, k)
  m = grid.length
  n = grid[0].length
  inf = 536870911
  f = Array.new(k + 1) { Array.new(m) { Array.new(n, inf) } }
  f[0][0][0] = 0
  (0...m).each do |i|
    (0...n).each do |j|
      f[0][i][j] = [f[0][i][j], f[0][i - 1][j] + grid[i][j]].min if i > 0
      f[0][i][j] = [f[0][i][j], f[0][i][j - 1] + grid[i][j]].min if j > 0
    end
  end
  g = {}
  (0...m).each do |i|
    (0...n).each do |j|
      (g[grid[i][j]] ||= []) << [i, j]
    end
  end
  keys = g.keys.sort.reverse
  (1..k).each do |t|
    mn = inf
    keys.each do |key|
      pos = g[key]
      pos.each { |p| mn = f[t - 1][p[0]][p[1]] if f[t - 1][p[0]][p[1]] < mn }
      pos.each { |p| f[t][p[0]][p[1]] = mn }
    end
    (0...m).each do |i|
      (0...n).each do |j|
        f[t][i][j] = [f[t][i][j], f[t][i - 1][j] + grid[i][j]].min if i > 0
        f[t][i][j] = [f[t][i][j], f[t][i][j - 1] + grid[i][j]].min if j > 0
      end
    end
  end
  ans = inf
  (0..k).each { |t| ans = f[t][m - 1][n - 1] if f[t][m - 1][n - 1] < ans }
  ans
end
''')

add("3652_best_time_to_buy_and_sell_stock_using_strategy", r'''
# LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

# @param {Integer[]} prices
# @param {Integer[]} strategy
# @param {Integer} k
# @return {Integer}
def max_profit(prices, strategy, k)
  n = prices.length
  s = Array.new(n + 1, 0)
  t = Array.new(n + 1, 0)
  (1..n).each do |i|
    s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
    t[i] = t[i - 1] + prices[i - 1]
  end
  ans = s[n]
  (k..n).each do |i|
    v = s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2])
    ans = v if v > ans
  end
  ans
end
''')

add("3653_xor_after_range_multiplication_queries_i", r'''
# LeetCode 3653 - XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def xor_after_queries(nums, queries)
  mod = 1_000_000_007
  queries.each do |l, r, k, v|
    idx = l
    while idx <= r
      nums[idx] = nums[idx] * v % mod
      idx += k
    end
  end
  ans = 0
  nums.each { |x| ans ^= x }
  ans
end
''')

add("3654_minimum_sum_after_divisible_sum_deletions", r'''
# LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
# https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_array_sum(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = (prefix[i] + nums[i]) % k }
  inf = 10**18
  dp = Array.new(n + 1, 0)
  best = Array.new(k, inf)
  best[0] = 0
  (1..n).each do |i|
    dp[i] = dp[i - 1] + nums[i - 1]
    dp[i] = best[prefix[i]] if best[prefix[i]] < dp[i]
    best[prefix[i]] = dp[i] if dp[i] < best[prefix[i]]
  end
  dp[n]
end
''')

add("3655_xor_after_range_multiplication_queries_ii", r'''
# LeetCode 3655 - XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def xor_after_queries(nums, queries)
  mod = 1_000_000_007
  n = nums.length
  by_k = {}
  queries.each { |q| (by_k[q[2]] ||= []) << q }
  res = nums.dup
  by_k.each_value do |lst|
    fac = Array.new(n, 1)
    lst.each do |u|
      i = u[0]
      while i <= u[1]
        fac[i] = fac[i] * u[3] % mod
        i += u[2]
      end
    end
    (0...n).each { |i| res[i] = res[i] * fac[i] % mod }
  end
  ans = 0
  res.each { |v| ans ^= v }
  ans
end
''')

add("3656_determine_if_a_simple_graph_exists", r'''
# LeetCode 3656 - Determine if a Simple Graph Exists
# https://leetcode.com/problems/determine-if-a-simple-graph-exists/

# @param {Integer[]} degrees
# @return {Boolean}
def simple_graph_exists(degrees)
  n = degrees.length
  d = degrees.sort.reverse
  total = 0
  d.each do |x|
    return false if x < 0 || x >= n

    total += x
  end
  return false if total.odd?

  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + d[i] }
  (1..n).each do |k|
    right = 0
    (k...n).each { |i| right += d[i] < k ? d[i] : k }
    return false if prefix[k] > k * (k - 1) + right
  end
  true
end
''')

add("3658_gcd_of_odd_and_even_sums", r'''
# LeetCode 3658 - GCD of Odd and Even Sums
# https://leetcode.com/problems/gcd-of-odd-and-even-sums/

# @param {Integer} n
# @return {Integer}
def gcd_of_odd_even_sums(n)
  n
end
''')

add("3659_partition_array_into_k_distinct_groups", r'''
# LeetCode 3659 - Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def partition_array(nums, k)
  n = nums.length
  return false if n % k != 0

  m = n / k
  mx = nums.max
  cnt = Array.new(mx + 1, 0)
  nums.each do |x|
    cnt[x] += 1
    return false if cnt[x] > m
  end
  true
end
''')

add("3660_jump_game_ix", r'''
# LeetCode 3660 - Jump Game IX
# https://leetcode.com/problems/jump-game-ix/

# @param {Integer[]} nums
# @return {Integer[]}
def max_value(nums)
  n = nums.length
  ans = Array.new(n, 0)
  pre_max = Array.new(n, 0)
  pre_max[0] = nums[0]
  (1...n).each { |i| pre_max[i] = [pre_max[i - 1], nums[i]].max }
  suf_min = 1073741823
  (n - 1).downto(0) do |i|
    ans[i] = pre_max[i] > suf_min ? ans[i + 1] : pre_max[i]
    suf_min = nums[i] if nums[i] < suf_min
  end
  ans
end
''')

add("3661_maximum_walls_destroyed_by_robots", r'''
# LeetCode 3661 - Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

# @param {Integer[]} robots
# @param {Integer[]} distance
# @param {Integer[]} walls
# @return {Integer}
def max_walls(robots, distance, walls)
  n = robots.length
  arr = robots.zip(distance).sort_by { |a| a[0] }
  walls = walls.sort
  memo = {}
  bisect_left = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  dfs = nil
  dfs = lambda do |i, j|
    return 0 if i < 0

    key = (i << 1) | j
    return memo[key] if memo.key?(key)

    left = arr[i][0] - arr[i][1]
    left = [left, arr[i - 1][0] + 1].max if i > 0
    l = bisect_left.call(walls, left)
    r = bisect_left.call(walls, arr[i][0] + 1)
    ans = dfs.call(i - 1, 0) + (r - l)
    right = arr[i][0] + arr[i][1]
    if i + 1 < arr.length
      right = if j == 0
                [right, arr[i + 1][0] - arr[i + 1][1] - 1].min
              else
                [right, arr[i + 1][0] - 1].min
              end
    end
    l = bisect_left.call(walls, arr[i][0])
    r = bisect_left.call(walls, right + 1)
    v = dfs.call(i - 1, 1) + (r - l)
    ans = v if v > ans
    memo[key] = ans
    ans
  end
  dfs.call(n - 1, 1)
end
''')

add("3662_filter_characters_by_frequency", r'''
# LeetCode 3662 - Filter Characters by Frequency
# https://leetcode.com/problems/filter-characters-by-frequency/

# @param {String} s
# @param {Integer} k
# @return {String}
def filter_characters(s, k)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  s.chars.select { |c| cnt[c.ord - 97] < k }.join
end
''')

add("3663_find_the_least_frequent_digit", r'''
# LeetCode 3663 - Find The Least Frequent Digit
# https://leetcode.com/problems/find-the-least-frequent-digit/

# @param {Integer} n
# @return {Integer}
def get_least_frequent_digit(n)
  cnt = Array.new(10, 0)
  ans = 0
  f = 1 << 30
  while n > 0
    cnt[n % 10] += 1
    n /= 10
  end
  (0...10).each do |x|
    if cnt[x] > 0 && cnt[x] < f
      f = cnt[x]
      ans = x
    end
  end
  ans
end
''')

add("3664_two_letter_card_game", r'''
# LeetCode 3664 - Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/

# @param {String[]} cards
# @param {String} x
# @return {Integer}
def score(cards, x)
  pair_group = lambda do |arr|
    total = 0
    mx = 0
    26.times do |i|
      total += arr[i]
      mx = arr[i] if arr[i] > mx
    end
    pairs = total / 2
    pairs = total - mx if total - mx < pairs
    [pairs, total - 2 * pairs]
  end
  xx = 0
  left = Array.new(26, 0)
  right = Array.new(26, 0)
  cards.each do |c|
    a = c[0]
    b = c[1]
    if a == x && b == x
      xx += 1
    elsif a == x
      left[b.ord - 97] += 1
    elsif b == x
      right[a.ord - 97] += 1
    end
  end
  lp = pair_group.call(left)
  rp = pair_group.call(right)
  ans = lp[0] + rp[0]
  rem = lp[1] + rp[1]
  use = [xx, rem].min
  ans += use
  xx -= use
  ans + xx / 2
end
''')

add("3665_twisted_mirror_path_count", r'''
# LeetCode 3665 - Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/

# @param {Integer[][]} grid
# @return {Integer}
def unique_paths(grid)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  next_cell = lambda do |i, j, di, dj|
    ni = i + di
    nj = j + dj
    while ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1
      if dj == 1
        di = 1
        dj = 0
      else
        di = 0
        dj = 1
      end
      ni += di
      nj += dj
    end
    return nil if ni < 0 || nj < 0 || ni >= m || nj >= n

    [ni, nj]
  end
  dp = Array.new(m) { Array.new(n, 0) }
  return 0 if grid[0][0] == 1

  dp[0][0] = 1
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 1 || dp[i][j] == 0

      a = next_cell.call(i, j, 0, 1)
      dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % mod if a
      b = next_cell.call(i, j, 1, 0)
      dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % mod if b
    end
  end
  dp[m - 1][n - 1]
end
''')

if __name__ == "__main__":
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {name}")
    print(f"batch B written={written}")
