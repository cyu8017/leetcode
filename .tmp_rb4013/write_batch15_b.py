#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3206_alternating_groups_i", r'''
# LeetCode 3206 - Alternating Groups I
# https://leetcode.com/problems/alternating-groups-i/

# @param {Integer[]} colors
# @return {Integer}
def number_of_alternating_groups(colors)
  k = 3
  n = colors.length
  cnt = 0
  ans = 0
  (0...(n * 2)).each do |i|
    if i > 0 && colors[i % n] == colors[(i - 1) % n]
      cnt = 1
    else
      cnt += 1
    end
    ans += 1 if i >= n && cnt >= k
  end
  ans
end
''')

add("3207_maximum_points_after_enemy_battles", r'''
# LeetCode 3207 - Maximum Points After Enemy Battles
# https://leetcode.com/problems/maximum-points-after-enemy-battles/

# @param {Integer[]} enemy_energies
# @param {Integer} current_energy
# @return {Integer}
def maximum_points(enemy_energies, current_energy)
  enemy_energies.sort!
  return 0 if current_energy < enemy_energies[0]
  ans = 0
  (enemy_energies.length - 1).downto(0) do |i|
    ans += current_energy / enemy_energies[0]
    current_energy %= enemy_energies[0]
    current_energy += enemy_energies[i]
  end
  ans
end
''')

add("3208_alternating_groups_ii", r'''
# LeetCode 3208 - Alternating Groups II
# https://leetcode.com/problems/alternating-groups-ii/

# @param {Integer[]} colors
# @param {Integer} k
# @return {Integer}
def number_of_alternating_groups(colors, k)
  n = colors.length
  cnt = 0
  ans = 0
  (0...(n * 2)).each do |i|
    if i > 0 && colors[i % n] == colors[(i - 1) % n]
      cnt = 1
    else
      cnt += 1
    end
    ans += 1 if i >= n && cnt >= k
  end
  ans
end
''')

add("3209_number_of_subarrays_with_and_value_of_k", r'''
# LeetCode 3209 - Number of Subarrays With AND Value of K
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  pre = {}
  ans = 0
  nums.each do |x|
    cur = {}
    pre.each do |key, val|
      nk = x & key
      cur[nk] = cur.fetch(nk, 0) + val
    end
    cur[x] = cur.fetch(x, 0) + 1
    ans += cur.fetch(k, 0)
    pre = cur
  end
  ans
end
''')

add("3210_find_the_encrypted_string", r'''
# LeetCode 3210 - Find the Encrypted String
# https://leetcode.com/problems/find-the-encrypted-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def get_encrypted_string(s, k)
  n = s.length
  out = []
  (0...n).each { |i| out << s[(i + k) % n] }
  out.join
end
''')

add("3211_generate_binary_strings_without_adjacent_zeros", r'''
# LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

# @param {Integer} n
# @return {String[]}
def valid_strings(n)
  ans = []
  t = []
  dfs = lambda do |i|
    if i >= n
      ans << t.join
      return
    end
    (0...2).each do |j|
      if (j == 0 && (i == 0 || t[i - 1] == "1")) || j == 1
        t << j.to_s
        dfs.call(i + 1)
        t.pop
      end
    end
  end
  dfs.call(0)
  ans
end
''')

add("3212_count_submatrices_with_equal_frequency_of_x_and_y", r'''
# LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

# @param {Character[][]} grid
# @return {Integer}
def number_of_submatrices(grid)
  m = grid.length
  n = grid[0].length
  s = Array.new(m + 1) { Array.new(n + 1) { [0, 0] } }
  ans = 0
  (1..m).each do |i|
    (1..n).each do |j|
      s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
      s[i][j][0] += 1 if grid[i - 1][j - 1] == "X"
      s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
      s[i][j][1] += 1 if grid[i - 1][j - 1] == "Y"
      ans += 1 if s[i][j][0] > 0 && s[i][j][0] == s[i][j][1]
    end
  end
  ans
end
''')

add("3213_construct_string_with_minimum_cost", r'''
# LeetCode 3213 - Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/

# @param {String} target
# @param {String[]} words
# @param {Integer[]} costs
# @return {Integer}
def minimum_cost(target, words, costs)
  bas = 13331
  mod = 998244353
  inf = 10**18
  n = target.length
  p = Array.new(n + 1, 0)
  h = Array.new(n + 1, 0)
  p[0] = 1
  (1..n).each do |i|
    p[i] = (p[i - 1] * bas) % mod
    h[i] = (h[i - 1] * bas + target[i - 1].ord) % mod
  end
  query = lambda do |l, r|
    (h[r] - (h[l - 1] * p[r - l + 1]) % mod + mod) % mod
  end
  f = Array.new(n + 1, inf)
  f[0] = 0
  lengths = words.map(&:length).uniq.sort
  d = {}
  words.each_with_index do |w, i|
    x = 0
    w.each_char { |ch| x = (x * bas + ch.ord) % mod }
    d[x] = costs[i] if !d.key?(x) || costs[i] < d[x]
  end
  (1..n).each do |i|
    lengths.each do |j|
      break if j > i
      x = query.call(i - j + 1, i)
      f[i] = [f[i], f[i - j] + d[x]].min if d.key?(x)
    end
  end
  f[n] >= inf ? -1 : f[n]
end
''')

add("3215_count_triplets_with_even_xor_set_bits_ii", r'''
# LeetCode 3215 - Count Triplets with Even XOR Set Bits II
# https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

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

add("3216_lexicographically_smallest_string_after_a_swap", r'''
# LeetCode 3216 - Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

# @param {String} s
# @return {String}
def get_smallest_string(s)
  arr = s.chars
  n = arr.length
  (1...n).each do |i|
    a = arr[i - 1]
    b = arr[i]
    if a > b && (a.ord % 2) == (b.ord % 2)
      arr[i - 1] = b
      arr[i] = a
      return arr.join
    end
  end
  s
end
''')

add("3217_delete_nodes_from_linked_list_present_in_array", r'''
# LeetCode 3217 - Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {Integer[]} nums
# @param {ListNode} head
# @return {ListNode}
def modified_list(nums, head)
  s = {}
  nums.each { |x| s[x] = true }
  dummy = ListNode.new(0, head)
  pre = dummy
  while pre.next
    if s[pre.next.val]
      pre.next = pre.next.next
    else
      pre = pre.next
    end
  end
  dummy.next
end
''')

add("3218_minimum_cost_for_cutting_cake_i", r'''
# LeetCode 3218 - Minimum Cost for Cutting Cake I
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} horizontal_cut
# @param {Integer[]} vertical_cut
# @return {Integer}
def minimum_cost(m, n, horizontal_cut, vertical_cut)
  horizontal_cut.sort! { |a, b| b <=> a }
  vertical_cut.sort! { |a, b| b <=> a }
  i = j = 0
  h = v = 1
  ans = 0
  while i < m - 1 || j < n - 1
    if j == n - 1 || (i < m - 1 && horizontal_cut[i] > vertical_cut[j])
      ans += horizontal_cut[i] * v
      h += 1
      i += 1
    else
      ans += vertical_cut[j] * h
      v += 1
      j += 1
    end
  end
  ans
end
''')

add("3219_minimum_cost_for_cutting_cake_ii", r'''
# LeetCode 3219 - Minimum Cost for Cutting Cake II
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} horizontal_cut
# @param {Integer[]} vertical_cut
# @return {Integer}
def minimum_cost(m, n, horizontal_cut, vertical_cut)
  horizontal_cut.sort! { |a, b| b <=> a }
  vertical_cut.sort! { |a, b| b <=> a }
  i = j = 0
  h = v = 1
  ans = 0
  while i < m - 1 || j < n - 1
    if j == n - 1 || (i < m - 1 && horizontal_cut[i] > vertical_cut[j])
      ans += horizontal_cut[i] * v
      h += 1
      i += 1
    else
      ans += vertical_cut[j] * h
      v += 1
      j += 1
    end
  end
  ans
end
''')

add("3221_maximum_array_hopping_score_ii", r'''
# LeetCode 3221 - Maximum Array Hopping Score II
# https://leetcode.com/problems/maximum-array-hopping-score-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  stk = []
  nums.each_index do |i|
    stk.pop while !stk.empty? && nums[stk[-1]] <= nums[i]
    stk << i
  end
  ans = 0
  cur = 0
  stk.each do |j|
    ans += (j - cur) * nums[j]
    cur = j
  end
  ans
end
''')

add("3222_find_the_winning_player_in_coin_game", r'''
# LeetCode 3222 - Find the Winning Player in Coin Game
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

# @param {Integer} x
# @param {Integer} y
# @return {String}
def winning_player(x, y)
  k = [x / 2, y / 8].min
  x -= 2 * k
  y -= 8 * k
  return "Alice" if x > 0 && y >= 4
  "Bob"
end
''')

add("3223_minimum_length_of_string_after_operations", r'''
# LeetCode 3223 - Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/

# @param {String} s
# @return {Integer}
def minimum_length(s)
  cnt = Array.new(26, 0)
  s.each_char { |ch| cnt[ch.ord - 97] += 1 }
  ans = 0
  cnt.each do |x|
    next if x <= 0
    ans += (x & 1) != 0 ? 1 : 2
  end
  ans
end
''')

add("3224_minimum_array_changes_to_make_differences_equal", r'''
# LeetCode 3224 - Minimum Array Changes to Make Differences Equal
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_changes(nums, k)
  d = Array.new(k + 2, 0)
  n = nums.length
  (0...(n / 2)).each do |i|
    x = nums[i]
    y = nums[n - 1 - i]
    x, y = y, x if x > y
    d[0] += 1
    d[y - x] -= 1
    d[y - x + 1] += 1
    mx = [y, k - x].max
    d[mx + 1] -= 1
    d[mx + 1] += 2
  end
  ans = n
  s = 0
  d.each do |x|
    s += x
    ans = [ans, s].min
  end
  ans
end
''')

add("3225_maximum_score_from_grid_operations", r'''
# LeetCode 3225 - Maximum Score From Grid Operations
# https://leetcode.com/problems/maximum-score-from-grid-operations/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_score(grid)
  n = grid.length
  prefix = Array.new(n) { Array.new(n + 1, 0) }
  (0...n).each do |j|
    (0...n).each { |i| prefix[j][i + 1] = prefix[j][i] + grid[i][j] }
  end
  prev_pick = Array.new(n + 1, 0)
  prev_skip = Array.new(n + 1, 0)
  (1...n).each do |j|
    curr_pick = Array.new(n + 1, 0)
    curr_skip = Array.new(n + 1, 0)
    (0..n).each do |curr|
      (0..n).each do |prev|
        if curr > prev
          score = prefix[j - 1][curr] - prefix[j - 1][prev]
          curr_pick[curr] = [curr_pick[curr], prev_skip[prev] + score].max
          curr_skip[curr] = [curr_skip[curr], prev_skip[prev] + score].max
        else
          score = prefix[j][prev] - prefix[j][curr]
          curr_pick[curr] = [curr_pick[curr], prev_pick[prev] + score].max
          curr_skip[curr] = [curr_skip[curr], prev_pick[prev]].max
        end
      end
    end
    prev_pick = curr_pick
    prev_skip = curr_skip
  end
  prev_pick.max
end
''')

add("3226_number_of_bit_changes_to_make_two_integers_equal", r'''
# LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def min_changes(n, k)
  return -1 if (n & k) != k
  x = n ^ k
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end
''')

add("3227_vowels_game_in_a_string", r'''
# LeetCode 3227 - Vowels Game in a String
# https://leetcode.com/problems/vowels-game-in-a-string/

# @param {String} s
# @return {Boolean}
def does_alice_win(s)
  s.each_char { |c| return true if "aeiou".include?(c) }
  false
end
''')

add("3228_maximum_number_of_operations_to_move_ones_to_the_end", r'''
# LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

# @param {String} s
# @return {Integer}
def max_operations(s)
  ans = 0
  cnt = 0
  s.each_char.with_index do |ch, i|
    if ch == "1"
      cnt += 1
    elsif i > 0 && s[i - 1] == "1"
      ans += cnt
    end
  end
  ans
end
''')

add("3229_minimum_operations_to_make_array_equal_to_target", r'''
# LeetCode 3229 - Minimum Operations to Make Array Equal to Target
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def minimum_operations(nums, target)
  f = (target[0] - nums[0]).abs
  (1...target.length).each do |i|
    x = target[i] - nums[i]
    y = target[i - 1] - nums[i - 1]
    if x * y > 0
      d = x.abs - y.abs
      f += d if d > 0
    else
      f += x.abs
    end
  end
  f
end
''')

add("3231_minimum_number_of_increasing_subsequence_to_be_removed", r'''
# LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
# https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  g = []
  nums.each do |x|
    l = 0
    r = g.length
    while l < r
      mid = (l + r) >> 1
      if g[mid] < x
        r = mid
      else
        l = mid + 1
      end
    end
    if l == g.length
      g << x
    else
      g[l] = x
    end
  end
  g.length
end
''')

add("3232_find_if_digit_game_can_be_won", r'''
# LeetCode 3232 - Find if Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/

# @param {Integer[]} nums
# @return {Boolean}
def can_alice_win(nums)
  a = b = 0
  nums.each do |x|
    if x < 10
      a += x
    else
      b += x
    end
  end
  a != b
end
''')

add("3233_find_the_count_of_numbers_which_are_not_special", r'''
# LeetCode 3233 - Find the Count of Numbers Which Are Not Special
# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def non_special_count(l, r)
  m = 31623
  primes = Array.new(m + 1, true)
  primes[0] = primes[1] = false
  (2..m).each do |i|
    next unless primes[i]
    (i * 2).step(m, i) { |j| primes[j] = false }
  end
  lo = Math.sqrt(l).ceil
  hi = Math.sqrt(r).floor
  cnt = 0
  (lo..hi).each { |i| cnt += 1 if primes[i] }
  r - l + 1 - cnt
end
''')

add("3234_count_the_number_of_substrings_with_dominant_ones", r'''
# LeetCode 3234 - Count the Number of Substrings With Dominant Ones
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

# @param {String} s
# @return {Integer}
def number_of_substrings(s)
  n = s.length
  nxt = Array.new(n + 1, 0)
  nxt[n] = n
  (n - 1).downto(0) do |i|
    nxt[i] = nxt[i + 1]
    nxt[i] = i if s[i] == "0"
  end
  ans = 0
  (0...n).each do |i|
    cnt0 = s[i] == "0" ? 1 : 0
    j = i
    while j < n && cnt0 * cnt0 <= n
      cnt1 = nxt[j + 1] - i - cnt0
      ans += [nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1].min if cnt1 >= cnt0 * cnt0
      j = nxt[j + 1]
      cnt0 += 1
    end
  end
  ans
end
''')

add("3235_check_if_the_rectangle_corner_is_reachable", r'''
# LeetCode 3235 - Check if the Rectangle Corner Is Reachable
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

# @param {Integer} x_corner
# @param {Integer} y_corner
# @param {Integer[][]} circles
# @return {Boolean}
def can_reach_corner(x_corner, y_corner, circles)
  n = circles.length
  vis = Array.new(n, false)
  in_circle = lambda do |x, y, cx, cy, r|
    dx = x - cx
    dy = y - cy
    dx * dx + dy * dy <= r * r
  end
  cross_left_top = lambda do |cx, cy, r|
    a = cx.abs <= r && cy >= 0 && cy <= y_corner
    b = (cy - y_corner).abs <= r && cx >= 0 && cx <= x_corner
    a || b
  end
  cross_right_bottom = lambda do |cx, cy, r|
    a = (cx - x_corner).abs <= r && cy >= 0 && cy <= y_corner
    b = cy.abs <= r && cx >= 0 && cx <= x_corner
    a || b
  end
  dfs = nil
  dfs = lambda do |i|
    x1, y1, r1 = circles[i]
    return true if cross_right_bottom.call(x1, y1, r1)
    vis[i] = true
    (0...n).each do |j|
      next if vis[j]
      x2, y2, r2 = circles[j]
      next if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) > (r1 + r2) * (r1 + r2)
      if x1 * r2 + x2 * r1 < (r1 + r2) * x_corner && y1 * r2 + y2 * r1 < (r1 + r2) * y_corner && dfs.call(j)
        return true
      end
    end
    false
  end
  (0...n).each do |i|
    x, y, r = circles[i]
    return false if in_circle.call(0, 0, x, y, r) || in_circle.call(x_corner, y_corner, x, y, r)
    return false if !vis[i] && cross_left_top.call(x, y, r) && dfs.call(i)
  end
  true
end
''')

add("3237_alt_and_tab_simulation", r'''
# LeetCode 3237 - Alt and Tab Simulation
# https://leetcode.com/problems/alt-and-tab-simulation/

# @param {Integer[]} windows
# @param {Integer[]} queries
# @return {Integer[]}
def simulation_result(windows, queries)
  n = windows.length
  s = Array.new(n + 1, false)
  ans = []
  (queries.length - 1).downto(0) do |i|
    q = queries[i]
    unless s[q]
      s[q] = true
      ans << q
    end
  end
  windows.each { |w| ans << w unless s[w] }
  ans
end
''')

add("3238_find_the_number_of_winning_players", r'''
# LeetCode 3238 - Find the Number of Winning Players
# https://leetcode.com/problems/find-the-number-of-winning-players/

# @param {Integer} n
# @param {Integer[][]} pick
# @return {Integer}
def winning_player_count(n, pick)
  cnt = Array.new(n) { Array.new(11, 0) }
  s = {}
  pick.each do |p|
    x = p[0]
    y = p[1]
    cnt[x][y] += 1
    s[x] = true if cnt[x][y] > x
  end
  s.length
end
''')

add("3239_minimum_number_of_flips_to_make_binary_grid_palindromic_i", r'''
# LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

# @param {Integer[][]} grid
# @return {Integer}
def min_flips(grid)
  m = grid.length
  n = grid[0].length
  cnt1 = cnt2 = 0
  grid.each do |row|
    (0...(n / 2)).each { |j| cnt1 += 1 if row[j] != row[n - j - 1] }
  end
  (0...n).each do |j|
    (0...(m / 2)).each { |i| cnt2 += 1 if grid[i][j] != grid[m - i - 1][j] }
  end
  [cnt1, cnt2].min
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
