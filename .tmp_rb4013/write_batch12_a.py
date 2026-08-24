#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2832_maximal_range_that_each_element_is_maximum_in_it", r'''
# LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
# https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

# @param {Integer[]} nums
# @return {Integer[]}
def maximum_length(nums)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  st = []
  (0...n).each do |i|
    while !st.empty? && nums[st[-1]] < nums[i]
      st.pop
    end
    left[i] = st.empty? ? -1 : st[-1]
    st << i
  end
  st.clear
  (n - 1).downto(0) do |i|
    while !st.empty? && nums[st[-1]] <= nums[i]
      st.pop
    end
    right[i] = st.empty? ? n : st[-1]
    st << i
  end
  (0...n).map { |i| right[i] - left[i] - 1 }
end
''')

add("2833_furthest_point_from_origin", r'''
# LeetCode 2833 - Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/

# @param {String} moves
# @return {Integer}
def furthest_distance_from_origin(moves)
  left = right = u = 0
  moves.each_char do |c|
    if c == "L"
      left += 1
    elsif c == "R"
      right += 1
    else
      u += 1
    end
  end
  (left - right).abs + u
end
''')

add("2834_find_the_minimum_possible_sum_of_a_beautiful_array", r'''
# LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def minimum_possible_sum(n, target)
  mod = 1_000_000_007
  m = target / 2
  return (n * (n + 1) / 2) % mod if n <= m

  total = m * (m + 1) / 2
  remain = n - m
  total += remain * target + remain * (remain - 1) / 2
  total % mod
end
''')

add("2835_minimum_operations_to_form_subsequence_with_target_sum", r'''
# LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_operations(nums, target)
  cnt = Array.new(32, 0)
  total = 0
  nums.each do |v|
    total += v
    b = 0
    b += 1 while (1 << b) < v
    cnt[b] += 1
  end
  return -1 if total < target

  ans = 0
  (0...31).each do |i|
    if (target & (1 << i)) != 0
      if cnt[i] > 0
        cnt[i] -= 1
      else
        j = i + 1
        j += 1 while j < 32 && cnt[j] == 0
        return -1 if j == 32

        while j > i
          cnt[j] -= 1
          cnt[j - 1] += 2
          ans += 1
          j -= 1
        end
        cnt[i] -= 1
      end
    end
    cnt[i + 1] += cnt[i] / 2
  end
  ans
end
''')

add("2836_maximize_value_of_function_in_a_ball_passing_game", r'''
# LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

# @param {Integer[]} receiver
# @param {Integer} k
# @return {Integer}
def get_max_function_value(receiver, k)
  n = receiver.length
  log = 36
  up = Array.new(log) { Array.new(n, 0) }
  sm = Array.new(log) { Array.new(n, 0) }
  (0...n).each do |i|
    up[0][i] = receiver[i]
    sm[0][i] = receiver[i]
  end
  (1...log).each do |j|
    (0...n).each do |i|
      mid = up[j - 1][i]
      up[j][i] = up[j - 1][mid]
      sm[j][i] = sm[j - 1][i] + sm[j - 1][mid]
    end
  end
  ans = 0
  (0...n).each do |i|
    cur = i
    total = i
    kk = k
    (0...log).each do |j|
      if (kk & (1 << j)) != 0
        total += sm[j][cur]
        cur = up[j][cur]
      end
    end
    ans = total if total > ans
  end
  ans
end
''')

add("2838_maximum_coins_heroes_can_collect", r'''
# LeetCode 2838 - Maximum Coins Heroes Can Collect
# https://leetcode.com/problems/maximum-coins-heroes-can-collect/

# @param {Integer[]} heroes
# @param {Integer[]} monsters
# @param {Integer[]} coins
# @return {Integer[]}
def maximum_coins(heroes, monsters, coins)
  n = monsters.length
  idx = (0...n).to_a
  idx.sort_by! { |i| monsters[i] }
  pref = Array.new(n + 1, 0)
  ms = Array.new(n, 0)
  (0...n).each do |i|
    ms[i] = monsters[idx[i]]
    pref[i + 1] = pref[i] + coins[idx[i]]
  end

  upper_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  heroes.map { |h| pref[upper_bound.call(ms, h)] }
end
''')

add("2839_check_if_strings_can_be_made_equal_with_operations_i", r'''
# LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def can_be_equal(s1, s2)
  a = [s1[0], s1[2]].sort.join
  b = [s2[0], s2[2]].sort.join
  c = [s1[1], s1[3]].sort.join
  d = [s2[1], s2[3]].sort.join
  a == b && c == d
end
''')

add("2840_check_if_strings_can_be_made_equal_with_operations_ii", r'''
# LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_strings(s1, s2)
  even1 = Array.new(26, 0)
  odd1 = Array.new(26, 0)
  even2 = Array.new(26, 0)
  odd2 = Array.new(26, 0)
  (0...s1.length).each do |i|
    if i.even?
      even1[s1[i].ord - 97] += 1
      even2[s2[i].ord - 97] += 1
    else
      odd1[s1[i].ord - 97] += 1
      odd2[s2[i].ord - 97] += 1
    end
  end
  even1 == even2 && odd1 == odd2
end
''')

add("2841_maximum_sum_of_almost_unique_subarray", r'''
# LeetCode 2841 - Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def max_sum(nums, m, k)
  freq = {}
  total = 0
  ans = 0
  nums.each_with_index do |v, i|
    freq[v] = freq.fetch(v, 0) + 1
    total += v
    if i >= k
      out = nums[i - k]
      total -= out
      c = freq.fetch(out, 0) - 1
      if c == 0
        freq.delete(out)
      else
        freq[out] = c
      end
    end
    ans = [ans, total].max if i >= k - 1 && freq.length >= m
  end
  ans
end
''')

add("2842_count_k_subsequences_of_a_string_with_maximum_beauty", r'''
# LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_subsequences_with_max_beauty(s, k)
  mod = 1_000_000_007
  freq = Array.new(26, 0)
  s.each_char { |ch| freq[ch.ord - 97] += 1 }
  vals = freq.select { |f| f > 0 }.sort.reverse
  return 0 if vals.length < k

  threshold = vals[k - 1]
  need = 0
  avail = 0
  prod = 1
  vals.each do |v|
    if v > threshold
      prod = (prod * v) % mod
      need += 1
    elsif v == threshold
      avail += 1
    end
  end
  remain = k - need

  mod_pow = lambda do |a, b|
    res = 1
    a %= mod
    while b > 0
      res = (res * a) % mod if (b & 1) != 0
      a = (a * a) % mod
      b >>= 1
    end
    res
  end

  comb = lambda do |n, r|
    return 0 if r < 0 || r > n

    num = 1
    den = 1
    r.times do |i|
      num = (num * (n - i)) % mod
      den = (den * (i + 1)) % mod
    end
    (num * mod_pow.call(den, mod - 2)) % mod
  end

  prod = (prod * comb.call(avail, remain)) % mod
  remain.times { prod = (prod * threshold) % mod }
  prod
end
''')

add("2843_count_symmetric_integers", r'''
# LeetCode 2843 - Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/

# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_symmetric_integers(low, high)
  ans = 0
  (low..high).each do |x|
    s = x.to_s
    next if s.length.odd?

    mid = s.length / 2
    a = b = 0
    (0...mid).each do |i|
      a += s[i].ord - 48
      b += s[mid + i].ord - 48
    end
    ans += 1 if a == b
  end
  ans
end
''')

add("2844_minimum_operations_to_make_a_special_number", r'''
# LeetCode 2844 - Minimum Operations to Make a Special Number
# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

# @param {String} num
# @return {Integer}
def minimum_operations(num)
  n = num.length
  ans = n
  ans = [ans, n - 1].min if num.include?("0")
  %w[00 25 50 75].each do |t|
    j = n - 1
    j -= 1 while j >= 0 && num[j] != t[1]
    next if j < 0

    i = j - 1
    i -= 1 while i >= 0 && num[i] != t[0]
    next if i < 0

    ans = [ans, n - i - 2].min
  end
  ans
end
''')

add("2845_count_of_interesting_subarrays", r'''
# LeetCode 2845 - Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays/

# @param {Integer[]} nums
# @param {Integer} modulo
# @param {Integer} k
# @return {Integer}
def count_interesting_subarrays(nums, modulo, k)
  freq = { 0 => 1 }
  ans = 0
  pref = 0
  nums.each do |v|
    pref += 1 if v % modulo == k
    need = (pref - k) % modulo
    need += modulo if need < 0
    ans += freq.fetch(need, 0)
    key = pref % modulo
    freq[key] = freq.fetch(key, 0) + 1
  end
  ans
end
''')

add("2846_minimum_edge_weight_equilibrium_queries_in_a_tree", r'''
# LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def min_operations_queries(n, edges, queries)
  log = 15
  g = Array.new(n) { [] }
  edges.each do |a, b, w|
    g[a] << [b, w]
    g[b] << [a, w]
  end
  up = Array.new(log) { Array.new(n, 0) }
  depth = Array.new(n, 0)
  cnt = Array.new(n) { Array.new(27, 0) }

  dfs = lambda do |u, p|
    up[0][u] = p
    g[u].each do |v, w|
      next if v == p

      depth[v] = depth[u] + 1
      (0...27).each { |i| cnt[v][i] = cnt[u][i] }
      cnt[v][w] += 1
      dfs.call(v, u)
    end
  end

  dfs.call(0, 0)
  (1...log).each do |j|
    (0...n).each { |i| up[j][i] = up[j - 1][up[j - 1][i]] }
  end

  lca = lambda do |a, b|
    a, b = b, a if depth[a] < depth[b]
    diff = depth[a] - depth[b]
    (0...log).each { |j| a = up[j][a] if (diff & (1 << j)) != 0 }
    return a if a == b

    (log - 1).downto(0) do |j|
      if up[j][a] != up[j][b]
        a = up[j][a]
        b = up[j][b]
      end
    end
    up[0][a]
  end

  queries.map do |a, b|
    c = lca.call(a, b)
    total = depth[a] + depth[b] - 2 * depth[c]
    best = 0
    (1...27).each do |w|
      f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
      best = f if f > best
    end
    total - best
  end
end
''')

add("2847_smallest_number_with_given_digit_product", r'''
# LeetCode 2847 - Smallest Number With Given Digit Product
# https://leetcode.com/problems/smallest-number-with-given-digit-product/

# @param {Integer} n
# @return {String}
def smallest_number(n)
  return "0" if n == 0
  return "1" if n == 1

  digits = []
  9.downto(2) do |d|
    while n % d == 0
      digits << d.to_s
      n /= d
    end
  end
  return "-1" if n > 1

  digits.reverse.join
end
''')

add("2848_points_that_intersect_with_cars", r'''
# LeetCode 2848 - Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/

# @param {Integer[][]} nums
# @return {Integer}
def number_of_points(nums)
  cov = Array.new(102, 0)
  nums.each do |a, b|
    (a..b).each { |x| cov[x] = 1 }
  end
  cov.sum
end
''')

add("2849_determine_if_a_cell_is_reachable_at_a_given_time", r'''
# LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} fx
# @param {Integer} fy
# @param {Integer} t
# @return {Boolean}
def is_reachable_at_time(sx, sy, fx, fy, t)
  need = [(sx - fx).abs, (sy - fy).abs].max
  return t != 1 if need == 0

  t >= need
end
''')

add("2850_minimum_moves_to_spread_stones_over_grid", r'''
# LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_moves(grid)
  extras = []
  zeros = []
  (0...3).each do |i|
    (0...3).each do |j|
      if grid[i][j] == 0
        zeros << [i, j]
      elsif grid[i][j] > 1
        (grid[i][j] - 1).times { extras << [i, j] }
      end
    end
  end
  return 0 if zeros.empty?

  best = 1 << 30
  dfs = lambda do |i, cost|
    return if cost >= best
    if i == zeros.length
      best = cost
      return
    end
    extras.each_with_index do |e, j|
      next if e[0] < 0

      extras[j] = [-1, e[1]]
      d = (e[0] - zeros[i][0]).abs + (e[1] - zeros[i][1]).abs
      dfs.call(i + 1, cost + d)
      extras[j] = e
    end
  end
  dfs.call(0, 0)
  best
end
''')

add("2851_string_transformation", r'''
# LeetCode 2851 - String Transformation
# https://leetcode.com/problems/string-transformation/

# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Integer}
def number_of_ways(s, t, k)
  mod = 1_000_000_007
  n = s.length
  ss = s + s
  return 0 unless ss[0, 2 * n - 1].include?(t)

  cnt = 0
  (0...n).each { |i| cnt += 1 if ss[i, n] == t }
  same = s == t

  mod_pow = lambda do |a, b|
    res = 1
    a %= mod
    bb = b
    while bb > 0
      res = (res * a) % mod if (bb & 1) != 0
      a = (a * a) % mod
      bb >>= 1
    end
    res
  end

  pk = mod_pow.call(n - 1, k)
  invn = mod_pow.call(n, mod - 2)
  sign = k.odd? ? (mod - 1) : 1
  ways_same = ((pk + (n - 1) * sign % mod) % mod * invn) % mod
  ways_diff = ((pk - sign + mod) % mod * invn) % mod
  return (ways_same + ways_diff * (cnt - 1)) % mod if same

  (ways_diff * cnt) % mod
end
''')

add("2852_sum_of_remoteness_of_all_cells", r'''
# LeetCode 2852 - Sum of Remoteness of All Cells
# https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

# @param {Integer[][]} grid
# @return {Integer}
def sum_remoteness(grid)
  m = grid.length
  n = grid[0].length
  seen = Array.new(m) { Array.new(n, false) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  total = 0
  (0...m).each do |i|
    (0...n).each { |j| total += grid[i][j] if grid[i][j] != -1 }
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == -1 || seen[i][j]

      q = [[i, j]]
      seen[i][j] = true
      sm = 0
      cnt = 0
      h = 0
      while h < q.length
        x, y = q[h]
        h += 1
        sm += grid[x][y]
        cnt += 1
        dirs.each do |dx, dy|
          ni = x + dx
          nj = y + dy
          if ni >= 0 && ni < m && nj >= 0 && nj < n && !seen[ni][nj] && grid[ni][nj] != -1
            seen[ni][nj] = true
            q << [ni, nj]
          end
        end
      end
      ans += (total - sm) * cnt
    end
  end
  ans
end
''')

add("2855_minimum_right_shifts_to_sort_the_array", r'''
# LeetCode 2855 - Minimum Right Shifts to Sort the Array
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_right_shifts(nums)
  n = nums.length
  drops = 0
  idx = -1
  (0...n).each do |i|
    if nums[i] > nums[(i + 1) % n]
      drops += 1
      idx = i
    end
  end
  return 0 if drops == 0
  return -1 if drops > 1

  n - 1 - idx
end
''')

add("2856_minimum_array_length_after_pair_removals", r'''
# LeetCode 2856 - Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/

# @param {Integer[]} nums
# @return {Integer}
def min_length_after_removals(nums)
  n = nums.length
  freq = {}
  mx = 0
  nums.each do |v|
    c = freq.fetch(v, 0) + 1
    freq[v] = c
    mx = c if c > mx
  end
  return n % 2 if mx <= n / 2

  2 * mx - n
end
''')

add("2857_count_pairs_of_points_with_distance_k", r'''
# LeetCode 2857 - Count Pairs of Points With Distance k
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

# @param {Integer[][]} coordinates
# @param {Integer} k
# @return {Integer}
def count_pairs(coordinates, k)
  freq = {}
  ans = 0
  coordinates.each do |x, y|
    (0..k).each do |a|
      b = k - a
      ans += freq.fetch([x ^ a, y ^ b], 0)
    end
    key = [x, y]
    freq[key] = freq.fetch(key, 0) + 1
  end
  ans
end
''')

add("2858_minimum_edge_reversals_so_every_node_is_reachable", r'''
# LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def min_edge_reversals(n, edges)
  g = Array.new(n) { [] }
  edges.each do |u, v|
    g[u] << [v, 0]
    g[v] << [u, 1]
  end
  ans = Array.new(n, 0)

  dfs1 = lambda do |u, p|
    g[u].each do |v, ww|
      next if v == p

      ans[0] += ww
      dfs1.call(v, u)
    end
  end

  dfs2 = lambda do |u, p|
    g[u].each do |v, ww|
      next if v == p

      ans[v] = ww == 0 ? ans[u] + 1 : ans[u] - 1
      dfs2.call(v, u)
    end
  end

  dfs1.call(0, -1)
  dfs2.call(0, -1)
  ans
end
''')

add("2859_sum_of_values_at_indices_with_k_set_bits", r'''
# LeetCode 2859 - Sum of Values at Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_indices_with_k_set_bits(nums, k)
  ans = 0
  nums.each_with_index do |val, i|
    x = i
    bits = 0
    while x > 0
      bits += x & 1
      x >>= 1
    end
    ans += val if bits == k
  end
  ans
end
''')


def main() -> None:
    written = 0
    missing = []
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        if not path.parent.exists():
            missing.append(name)
            continue
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
    print(f"wrote={written} missing={missing}")


if __name__ == "__main__":
    main()
