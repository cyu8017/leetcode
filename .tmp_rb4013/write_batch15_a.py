#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3171_find_subarray_with_bitwise_or_closest_to_k", r'''
# LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_difference(nums, k)
  mx = nums.max
  m = mx == 0 ? 1 : 32 - leading_zero_count(mx)
  cnt = Array.new(m, 0)
  ans = 10**18
  s = 0
  i = 0
  nums.each_with_index do |x, j|
    s |= x
    ans = [ans, (s - k).abs].min
    (0...m).each do |h|
      cnt[h] += 1 if ((x >> h) & 1) != 0
    end
    while i < j && s > k
      y = nums[i]
      (0...m).each do |h|
        if ((y >> h) & 1) != 0
          cnt[h] -= 1
          s ^= 1 << h if cnt[h] == 0
        end
      end
      ans = [ans, (s - k).abs].min
      i += 1
    end
  end
  ans
end

def leading_zero_count(x)
  return 32 if x == 0
  n = 0
  31.downto(0) do |bit|
    break if ((x >> bit) & 1) != 0
    n += 1
  end
  n
end
''')

add("3173_bitwise_or_of_adjacent_elements", r'''
# LeetCode 3173 - Bitwise OR of Adjacent Elements
# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def or_array(nums)
  ans = Array.new(nums.length - 1, 0)
  (1...nums.length).each { |i| ans[i - 1] = nums[i] | nums[i - 1] }
  ans
end
''')

add("3174_clear_digits", r'''
# LeetCode 3174 - Clear Digits
# https://leetcode.com/problems/clear-digits/

# @param {String} s
# @return {String}
def clear_digits(s)
  stk = []
  s.each_char do |c|
    if c >= "0" && c <= "9"
      stk.pop
    else
      stk << c
    end
  end
  stk.join
end
''')

add("3175_find_the_first_player_to_win_k_games_in_a_row", r'''
# LeetCode 3175 - Find The First Player to win K Games in a Row
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

# @param {Integer[]} skills
# @param {Integer} k
# @return {Integer}
def find_winning_player(skills, k)
  n = skills.length
  k = [k, n - 1].min
  i = 0
  cnt = 0
  (1...n).each do |j|
    if skills[i] < skills[j]
      i = j
      cnt = 1
    else
      cnt += 1
    end
    break if cnt == k
  end
  i
end
''')

add("3176_find_the_maximum_length_of_a_good_subsequence_i", r'''
# LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  n = nums.length
  f = Array.new(n) { Array.new(k + 1, 0) }
  ans = 0
  (0...n).each do |i|
    (0..k).each do |h|
      (0...i).each do |j|
        if nums[i] == nums[j]
          f[i][h] = [f[i][h], f[j][h]].max
        elsif h > 0
          f[i][h] = [f[i][h], f[j][h - 1]].max
        end
      end
      f[i][h] += 1
    end
    ans = [ans, f[i][k]].max
  end
  ans
end
''')

add("3177_find_the_maximum_length_of_a_good_subsequence_ii", r'''
# LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  n = nums.length
  f = Array.new(n) { Array.new(k + 1, 0) }
  mp = Array.new(k + 1) { {} }
  g = Array.new(k + 1) { [0, 0, 0] }
  ans = 0
  (0...n).each do |i|
    (0..k).each do |h|
      f[i][h] = mp[h].fetch(nums[i], 0)
      if h > 0
        if g[h - 1][0] != nums[i]
          f[i][h] = [f[i][h], g[h - 1][1]].max
        else
          f[i][h] = [f[i][h], g[h - 1][2]].max
        end
      end
      f[i][h] += 1
      mp[h][nums[i]] = [mp[h].fetch(nums[i], 0), f[i][h]].max
      if g[h][0] != nums[i]
        if f[i][h] >= g[h][1]
          g[h][2] = g[h][1]
          g[h][1] = f[i][h]
          g[h][0] = nums[i]
        elsif f[i][h] > g[h][2]
          g[h][2] = f[i][h]
        end
      elsif f[i][h] > g[h][1]
        g[h][1] = f[i][h]
      end
      ans = [ans, f[i][h]].max
    end
  end
  ans
end
''')

add("3178_find_the_child_who_has_the_ball_after_k_seconds", r'''
# LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_child(n, k)
  mod = k % (n - 1)
  k = k / (n - 1)
  return n - mod - 1 if k.odd?
  mod
end
''')

add("3179_find_the_n_th_value_after_k_seconds", r'''
# LeetCode 3179 - Find the N-th Value After K Seconds
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def value_after_k_seconds(n, k)
  mod = 1_000_000_007
  a = Array.new(n, 1)
  while k > 0
    (1...n).each { |i| a[i] = (a[i] + a[i - 1]) % mod }
    k -= 1
  end
  a[n - 1]
end
''')

add("3180_maximum_total_reward_using_operations_i", r'''
# LeetCode 3180 - Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

# @param {Integer[]} reward_values
# @return {Integer}
def max_total_reward(reward_values)
  reward_values.sort!
  n = reward_values.length
  f = Array.new(reward_values[n - 1] << 1, -1)
  dfs = lambda do |x|
    return f[x] if f[x] != -1
    idx = reward_values.bsearch_index { |v| v > x } || n
    f[x] = 0
    (idx...n).each do |it|
      f[x] = [f[x], reward_values[it] + dfs.call(x + reward_values[it])].max
    end
    f[x]
  end
  dfs.call(0)
end
''')

add("3181_maximum_total_reward_using_operations_ii", r'''
# LeetCode 3181 - Maximum Total Reward Using Operations II
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

# @param {Integer[]} reward_values
# @return {Integer}
def max_total_reward(reward_values)
  reward_values.sort!
  uniq = 0
  reward_values.each_index do |i|
    if uniq == 0 || reward_values[i] != reward_values[uniq - 1]
      reward_values[uniq] = reward_values[i]
      uniq += 1
    end
  end
  f = 1
  (0...uniq).each do |i|
    v = reward_values[i]
    mask = f & ((1 << v) - 1)
    f |= mask << v
  end
  100000.downto(0) { |i| return i if ((f >> i) & 1) != 0 }
  0
end
''')

add("3183_the_number_of_ways_to_make_the_sum", r'''
# LeetCode 3183 - The Number of Ways to Make the Sum
# https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

# @param {Integer} n
# @return {Integer}
def number_of_ways(n)
  mod = 1_000_000_007
  coins = [1, 2, 6]
  f = Array.new(n + 1, 0)
  f[0] = 1
  coins.each do |x|
    (x..n).each { |j| f[j] = (f[j] + f[j - x]) % mod }
  end
  ans = f[n]
  ans = (ans + f[n - 4]) % mod if n >= 4
  ans = (ans + f[n - 8]) % mod if n >= 8
  ans
end
''')

add("3184_count_pairs_that_form_a_complete_day_i", r'''
# LeetCode 3184 - Count Pairs That Form a Complete Day I
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

# @param {Integer[]} hours
# @return {Integer}
def count_complete_day_pairs(hours)
  cnt = Array.new(24, 0)
  ans = 0
  hours.each do |x|
    ans += cnt[(24 - x % 24) % 24]
    cnt[x % 24] += 1
  end
  ans
end
''')

add("3185_count_pairs_that_form_a_complete_day_ii", r'''
# LeetCode 3185 - Count Pairs That Form a Complete Day II
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

# @param {Integer[]} hours
# @return {Integer}
def count_complete_day_pairs(hours)
  cnt = Array.new(24, 0)
  ans = 0
  hours.each do |x|
    ans += cnt[(24 - x % 24) % 24]
    cnt[x % 24] += 1
  end
  ans
end
''')

add("3186_maximum_total_damage_with_spell_casting", r'''
# LeetCode 3186 - Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

# @param {Integer[]} power
# @return {Integer}
def maximum_total_damage(power)
  n = power.length
  power.sort!
  cnt = Hash.new(0)
  nxt = Array.new(n, 0)
  f = Array.new(n, 0)
  (0...n).each do |i|
    cnt[power[i]] += 1
    nxt[i] = power.bsearch_index { |v| v >= power[i] + 3 } || n
  end
  dfs = lambda do |i|
    return 0 if i >= n
    return f[i] if f[i] != 0
    a = dfs.call(i + cnt[power[i]])
    b = power[i] * cnt[power[i]] + dfs.call(nxt[i])
    f[i] = [a, b].max
  end
  dfs.call(0)
end
''')

add("3187_peaks_in_array", r'''
# LeetCode 3187 - Peaks in Array
# https://leetcode.com/problems/peaks-in-array/

class BIT
  def initialize(n)
    @n = n
    @c = Array.new(n + 1, 0)
  end

  def update(x, delta)
    while x <= @n
      @c[x] += delta
      x += x & -x
    end
  end

  def query(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def count_of_peaks(nums, queries)
  n = nums.length
  tree = BIT.new(n - 1)
  update_peak = lambda do |i, val|
    return if i <= 0 || i >= n - 1
    tree.update(i, val) if nums[i - 1] < nums[i] && nums[i] > nums[i + 1]
  end
  (1...n - 1).each { |i| update_peak.call(i, 1) }
  ans = []
  queries.each do |q|
    if q[0] == 1
      l = q[1] + 1
      r = q[2] - 1
      t = 0
      t = tree.query(r) - tree.query(l - 1) if l <= r
      ans << t
    else
      idx = q[1]
      val = q[2]
      (idx - 1..idx + 1).each { |i| update_peak.call(i, -1) }
      nums[idx] = val
      (idx - 1..idx + 1).each { |i| update_peak.call(i, 1) }
    end
  end
  ans
end
''')

add("3189_minimum_moves_to_get_a_peaceful_board", r'''
# LeetCode 3189 - Minimum Moves to Get a Peaceful Board
# https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

# @param {Integer[][]} rooks
# @return {Integer}
def min_moves(rooks)
  ans = 0
  rooks.sort_by! { |a| a[0] }
  rooks.each_with_index { |r, i| ans += (r[0] - i).abs }
  rooks.sort_by! { |a| a[1] }
  rooks.each_with_index { |r, j| ans += (r[1] - j).abs }
  ans
end
''')

add("3190_find_minimum_operations_to_make_all_elements_divisible_by_three", r'''
# LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  nums.count { |x| x % 3 != 0 }
end
''')

add("3191_minimum_operations_to_make_binary_array_elements_equal_to_one_i", r'''
# LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  nums.each_index do |i|
    next if nums[i] != 0
    return -1 if i + 2 >= nums.length
    nums[i + 1] ^= 1
    nums[i + 2] ^= 1
    ans += 1
  end
  ans
end
''')

add("3192_minimum_operations_to_make_binary_array_elements_equal_to_one_ii", r'''
# LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  v = 0
  nums.each do |raw|
    x = raw ^ v
    if x == 0
      v ^= 1
      ans += 1
    end
  end
  ans
end
''')

add("3193_count_the_number_of_inversions", r'''
# LeetCode 3193 - Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/

# @param {Integer} n
# @param {Integer[][]} requirements
# @return {Integer}
def number_of_permutations(n, requirements)
  req = Array.new(n, -1)
  requirements.each { |r| req[r[0]] = r[1] }
  return 0 if req[0] > 0
  req[0] = 0
  m = req.max
  mod = 1_000_000_007
  f = Array.new(n) { Array.new(m + 1, 0) }
  f[0][0] = 1
  (1...n).each do |i|
    l = 0
    r = m
    if req[i] >= 0
      l = r = req[i]
    end
    (l..r).each do |j|
      (0..[i, j].min).each do |k|
        f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
      end
    end
  end
  f[n - 1][req[n - 1]]
end
''')

add("3194_minimum_average_of_smallest_and_largest_elements", r'''
# LeetCode 3194 - Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

# @param {Integer[]} nums
# @return {Float}
def minimum_average(nums)
  nums.sort!
  n = nums.length
  ans = 1 << 30
  (0...(n / 2)).each { |i| ans = [ans, nums[i] + nums[n - i - 1]].min }
  ans / 2.0
end
''')

add("3195_find_the_minimum_area_to_cover_all_ones_i", r'''
# LeetCode 3195 - Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_area(grid)
  x1 = grid.length
  y1 = grid[0].length
  x2 = y2 = 0
  grid.each_with_index do |row, i|
    row.each_with_index do |v, j|
      next if v != 1
      x1 = [x1, i].min
      y1 = [y1, j].min
      x2 = [x2, i].max
      y2 = [y2, j].max
    end
  end
  (x2 - x1 + 1) * (y2 - y1 + 1)
end
''')

add("3196_maximize_total_cost_of_alternating_subarrays", r'''
# LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def maximum_total_cost(nums)
  neg = -10**18
  n = nums.length
  memo = Array.new(n) { [neg, neg] }
  dfs = lambda do |i, j|
    return 0 if i >= n
    return memo[i][j] if memo[i][j] != neg
    res = nums[i] + dfs.call(i + 1, 1)
    res = [res, -nums[i] + dfs.call(i + 1, 0)].max if j > 0
    memo[i][j] = res
  end
  dfs.call(0, 0)
end
''')

add("3197_find_the_minimum_area_to_cover_all_ones_ii", r'''
# LeetCode 3197 - Find the Minimum Area to Cover All Ones II
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_sum(grid)
  m = grid.length
  n = grid[0].length
  ans = m * n
  area = lambda do |i1, j1, i2, j2|
    inf = 10**18
    x1 = y1 = inf
    x2 = y2 = -inf
    (i1..i2).each do |i|
      (j1..j2).each do |j|
        next if grid[i][j] != 1
        x1 = [x1, i].min
        y1 = [y1, j].min
        x2 = [x2, i].max
        y2 = [y2, j].max
      end
    end
    return 0 if x1 == inf
    (x2 - x1 + 1) * (y2 - y1 + 1)
  end
  (0...m - 1).each do |i1|
    ((i1 + 1)...m - 1).each do |i2|
      ans = [
        ans,
        area.call(0, 0, i1, n - 1) + area.call(i1 + 1, 0, i2, n - 1) + area.call(i2 + 1, 0, m - 1, n - 1)
      ].min
    end
  end
  (0...n - 1).each do |j1|
    ((j1 + 1)...n - 1).each do |j2|
      ans = [
        ans,
        area.call(0, 0, m - 1, j1) + area.call(0, j1 + 1, m - 1, j2) + area.call(0, j2 + 1, m - 1, n - 1)
      ].min
    end
  end
  (0...m - 1).each do |i|
    (0...n - 1).each do |j|
      ans = [ans, area.call(0, 0, i, j) + area.call(0, j + 1, i, n - 1) + area.call(i + 1, 0, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, i, n - 1) + area.call(i + 1, 0, m - 1, j) + area.call(i + 1, j + 1, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, i, j) + area.call(i + 1, 0, m - 1, j) + area.call(0, j + 1, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, m - 1, j) + area.call(0, j + 1, i, n - 1) + area.call(i + 1, j + 1, m - 1, n - 1)].min
    end
  end
  ans
end
''')

add("3199_count_triplets_with_even_xor_set_bits_i", r'''
# LeetCode 3199 - Count Triplets with Even XOR Set Bits I
# https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

# @param {Integer[]} a
# @param {Integer[]} b
# @param {Integer[]} c
# @return {Integer}
def triplet_count(a, b, c)
  bit_count = lambda do |x|
    n = 0
    while x > 0
      n += x & 1
      x >>= 1
    end
    n
  end
  cnt1 = [0, 0]
  cnt2 = [0, 0]
  cnt3 = [0, 0]
  a.each { |x| cnt1[bit_count.call(x) % 2] += 1 }
  b.each { |x| cnt2[bit_count.call(x) % 2] += 1 }
  c.each { |x| cnt3[bit_count.call(x) % 2] += 1 }
  ans = 0
  (0...2).each do |i|
    (0...2).each do |j|
      (0...2).each do |k|
        ans += cnt1[i] * cnt2[j] * cnt3[k] if (i + j + k).even?
      end
    end
  end
  ans
end
''')

add("3200_maximum_height_of_a_triangle", r'''
# LeetCode 3200 - Maximum Height of a Triangle
# https://leetcode.com/problems/maximum-height-of-a-triangle/

# @param {Integer} red
# @param {Integer} blue
# @return {Integer}
def max_height_of_triangle(red, blue)
  ans = 0
  (0...2).each do |k|
    colors = [red, blue]
    i = 1
    j = k
    while i <= colors[j]
      colors[j] -= i
      ans = [ans, i].max
      i += 1
      j ^= 1
    end
  end
  ans
end
''')

add("3201_find_the_maximum_length_of_valid_subsequence_i", r'''
# LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
  k = 2
  f = Array.new(k) { Array.new(k, 0) }
  ans = 0
  nums.each do |raw|
    x = raw % k
    (0...k).each do |j|
      y = (j - x + k) % k
      f[x][y] = f[y][x] + 1
      ans = [ans, f[x][y]].max
    end
  end
  ans
end
''')

add("3202_find_the_maximum_length_of_valid_subsequence_ii", r'''
# LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  f = Array.new(k) { Array.new(k, 0) }
  ans = 0
  nums.each do |raw|
    x = raw % k
    (0...k).each do |j|
      y = (j - x + k) % k
      f[x][y] = f[y][x] + 1
      ans = [ans, f[x][y]].max
    end
  end
  ans
end
''')

add("3203_find_minimum_diameter_after_merging_two_trees", r'''
# LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @return {Integer}
def minimum_diameter_after_merge(edges1, edges2)
  state = { ans: 0, a: 0, g: [] }
  dfs = lambda do |i, fa, t|
    state[:g][i].each do |j|
      dfs.call(j, i, t + 1) if j != fa
    end
    if state[:ans] < t
      state[:ans] = t
      state[:a] = i
    end
  end
  tree_diameter = lambda do |edges|
    nn = edges.length + 1
    state[:g] = Array.new(nn) { [] }
    edges.each do |e|
      state[:g][e[0]] << e[1]
      state[:g][e[1]] << e[0]
    end
    state[:ans] = 0
    state[:a] = 0
    dfs.call(0, -1, 0)
    dfs.call(state[:a], -1, 0)
    state[:ans]
  end
  d1 = tree_diameter.call(edges1)
  d2 = tree_diameter.call(edges2)
  [d1, d2, (d1 + 1) / 2 + (d2 + 1) / 2 + 1].max
end
''')

add("3205_maximum_array_hopping_score_i", r'''
# LeetCode 3205 - Maximum Array Hopping Score I
# https://leetcode.com/problems/maximum-array-hopping-score-i/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  n = nums.length
  f = Array.new(n, 0)
  dfs = lambda do |i|
    return f[i] if f[i] > 0
    ((i + 1)...n).each do |j|
      f[i] = [f[i], (j - i) * nums[j] + dfs.call(j)].max
    end
    f[i]
  end
  dfs.call(0)
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
