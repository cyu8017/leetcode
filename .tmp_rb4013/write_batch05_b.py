#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2115_find_all_possible_recipes_from_given_supplies", r'''
# LeetCode 2115 - Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# @param {String[]} recipes
# @param {String[][]} ingredients
# @param {String[]} supplies
# @return {String[]}
def find_all_recipes(recipes, ingredients, supplies)
  have = {}
  supplies.each { |s| have[s] = true }
  indeg = {}
  graph = Hash.new { |h, k| h[k] = [] }
  recipes.each_with_index do |r, i|
    indeg[r] = ingredients[i].length
    ingredients[i].each { |ing| graph[ing] << r }
  end
  q = supplies.dup
  ans = []
  until q.empty?
    cur = q.shift
    next unless graph.key?(cur)

    graph[cur].each do |nxt|
      indeg[nxt] -= 1
      if indeg[nxt] == 0
        ans << nxt
        q << nxt
      end
    end
  end
  ans
end
''')

add("2116_check_if_a_parentheses_string_can_be_valid", r'''
# LeetCode 2116 - Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

# @param {String} s
# @param {String} locked
# @return {Boolean}
def can_be_valid(s, locked)
  n = s.length
  return false if n.odd?

  bal = 0
  n.times do |i|
    bal += locked[i] == "0" || s[i] == "(" ? 1 : -1
    return false if bal < 0
  end
  bal = 0
  (n - 1).downto(0) do |i|
    bal += locked[i] == "0" || s[i] == ")" ? 1 : -1
    return false if bal < 0
  end
  true
end
''')

add("2117_abbreviating_the_product_of_a_range", r'''
# LeetCode 2117 - Abbreviating the Product of a Range
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/

# @param {Integer} left
# @param {Integer} right
# @return {String}
def abbreviate_product(left, right)
  twos = 0
  fives = 0
  (left..right).each do |i|
    x = i
    while x.even?
      twos += 1
      x /= 2
    end
    while x % 5 == 0
      fives += 1
      x /= 5
    end
  end
  zeros = [twos, fives].min
  mod = 100_000_000_000
  prod = 1
  extra2 = twos - zeros
  extra5 = fives - zeros
  log_sum = 0.0
  (left..right).each do |i|
    x = i
    x /= 2 while x.even?
    x /= 5 while x % 5 == 0
    prod = (prod * x) % mod
    log_sum += Math.log10(x)
  end
  extra2.times do
    prod = (prod * 2) % mod
    log_sum += Math.log10(2)
  end
  extra5.times do
    prod = (prod * 5) % mod
    log_sum += Math.log10(5)
  end
  full_log = 0.0
  (left..right).each { |i| full_log += Math.log10(i) }
  digits = full_log.floor + 1
  if digits <= 10
    p = 1
    (left..right).each { |i| p *= i }
    return p.to_s
  end
  frac = log_sum - log_sum.floor
  prefix = (10**(frac + 4)).floor
  suffix = prod % 100_000
  "#{prefix}e#{zeros}#{suffix.to_s.rjust(5, '0')}"
end
''')

add("2119_a_number_after_a_double_reversal", r'''
# LeetCode 2119 - A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal/

# @param {Integer} num
# @return {Boolean}
def is_same_after_reversals(num)
  num == 0 || num % 10 != 0
end
''')

add("2120_execution_of_all_suffix_instructions_staying_in_a_grid", r'''
# LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

# @param {Integer} n
# @param {Integer[]} start_pos
# @param {String} s
# @return {Integer[]}
def execute_instructions(n, start_pos, s)
  m = s.length
  ans = Array.new(m, 0)
  m.times do |i|
    r = start_pos[0]
    c = start_pos[1]
    cnt = 0
    (i...m).each do |j|
      ch = s[j]
      case ch
      when "L" then c -= 1
      when "R" then c += 1
      when "U" then r -= 1
      else r += 1
      end
      break if r < 0 || r >= n || c < 0 || c >= n

      cnt += 1
    end
    ans[i] = cnt
  end
  ans
end
''')

add("2121_intervals_between_identical_elements", r'''
# LeetCode 2121 - Intervals Between Identical Elements
# https://leetcode.com/problems/intervals-between-identical-elements/

# @param {Integer[]} arr
# @return {Integer[]}
def get_distances(arr)
  n = arr.length
  pos = Hash.new { |h, k| h[k] = [] }
  n.times { |i| pos[arr[i]] << i }
  ans = Array.new(n, 0)
  pos.each_value do |idxs|
    m = idxs.length
    pref = Array.new(m + 1, 0)
    m.times { |i| pref[i + 1] = pref[i] + idxs[i] }
    m.times do |i|
      left = i * idxs[i] - pref[i]
      right = (pref[m] - pref[i + 1]) - (m - i - 1) * idxs[i]
      ans[idxs[i]] = left + right
    end
  end
  ans
end
''')

add("2122_recover_the_original_array", r'''
# LeetCode 2122 - Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/

# @param {Integer[]} nums
# @return {Integer[]}
def recover_array(nums)
  nums = nums.sort
  n = nums.length
  (1...n).each do |i|
    diff = nums[i] - nums[0]
    next if diff == 0 || diff.odd?

    k = diff / 2
    used = Array.new(n, false)
    used[0] = used[i] = true
    ans = [(nums[0] + nums[i]) / 2]
    l = 0
    r = i
    ok = true
    while ans.length < n / 2
      l += 1 while l < n && used[l]
      if l == n
        ok = false
        break
      end
      need = nums[l] + 2 * k
      r += 1 while r < n && (used[r] || nums[r] < need)
      if r == n || nums[r] != need
        ok = false
        break
      end
      used[l] = used[r] = true
      ans << nums[l] + k
    end
    return ans if ok
  end
  []
end
''')

add("2123_minimum_operations_to_remove_adjacent_ones_in_matrix", r'''
# LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
# https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  ids = Array.new(m) { Array.new(n, -1) }
  cnt = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        ids[i][j] = cnt
        cnt += 1
      end
    end
  end
  g = Array.new(cnt) { [] }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  m.times do |i|
    n.times do |j|
      next if grid[i][j] != 1 || (i + j).odd?

      u = ids[i][j]
      dirs.each do |di, dj|
        ni = i + di
        nj = j + dj
        g[u] << ids[ni][nj] if ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1
      end
    end
  end
  match = Array.new(cnt, -1)
  dfs = nil
  dfs = lambda do |u, seen|
    g[u].each do |v|
      next if seen[v]

      seen[v] = true
      if match[v] == -1 || dfs.call(match[v], seen)
        match[v] = u
        return true
      end
    end
    false
  end

  ans = 0
  cnt.times do |u|
    ok = false
    i = 0
    while i < m && !ok
      n.times do |j|
        if ids[i][j] == u && (i + j).even?
          ok = true
          break
        end
      end
      i += 1
    end
    next unless ok

    seen = Array.new(cnt, false)
    ans += 1 if dfs.call(u, seen)
  end
  ans
end
''')

add("2124_check_if_all_as_appears_before_all_bs", r'''
# LeetCode 2124 - Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# @param {String} s
# @return {Boolean}
def check_string(s)
  seen_b = false
  s.each_char do |c|
    if c == "b"
      seen_b = true
    elsif seen_b
      return false
    end
  end
  true
end
''')

add("2125_number_of_laser_beams_in_a_bank", r'''
# LeetCode 2125 - Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# @param {String[]} bank
# @return {Integer}
def number_of_beams(bank)
  ans = 0
  prev = 0
  bank.each do |row|
    cnt = row.count("1")
    if cnt > 0
      ans += prev * cnt
      prev = cnt
    end
  end
  ans
end
''')

add("2126_destroying_asteroids", r'''
# LeetCode 2126 - Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/

# @param {Integer} mass
# @param {Integer[]} asteroids
# @return {Boolean}
def asteroids_destroyed(mass, asteroids)
  cur = mass
  asteroids.sort.each do |a|
    return false if cur < a

    cur += a
  end
  true
end
''')

add("2127_maximum_employees_to_be_invited_to_a_meeting", r'''
# LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

# @param {Integer[]} favorite
# @return {Integer}
def maximum_invitations(favorite)
  n = favorite.length
  indeg = Array.new(n, 0)
  depth = Array.new(n, 1)
  favorite.each { |f| indeg[f] += 1 }
  q = []
  n.times { |i| q << i if indeg[i] == 0 }
  until q.empty?
    u = q.shift
    v = favorite[u]
    depth[v] = [depth[v], depth[u] + 1].max
    indeg[v] -= 1
    q << v if indeg[v] == 0
  end
  pair_sum = 0
  max_cycle = 0
  vis = Array.new(n, false)
  n.times do |i|
    next if indeg[i] == 0 || vis[i]

    u = i
    len_cycle = 0
    until vis[u]
      vis[u] = true
      u = favorite[u]
      len_cycle += 1
    end
    if len_cycle == 2
      pair_sum += depth[i] + depth[favorite[i]]
    else
      max_cycle = [max_cycle, len_cycle].max
    end
  end
  [pair_sum, max_cycle].max
end
''')

add("2128_remove_all_ones_with_row_and_column_flips", r'''
# LeetCode 2128 - Remove All Ones With Row and Column Flips
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

# @param {Integer[][]} grid
# @return {Boolean}
def remove_ones(grid)
  m = grid.length
  n = grid[0].length
  (1...m).each do |i|
    same = grid[i][0] == grid[0][0]
    n.times do |j|
      return false if (grid[i][j] == grid[0][j]) != same
    end
  end
  true
end
''')

add("2129_capitalize_the_title", r'''
# LeetCode 2129 - Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

# @param {String} title
# @return {String}
def capitalize_title(title)
  title.strip.split.map do |w|
    w = w.downcase
    w.length > 2 ? w[0].upcase + w[1..] : w
  end.join(" ")
end
''')

add("2130_maximum_twin_sum_of_a_linked_list", r'''
# LeetCode 2130 - Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {Integer}
def pair_sum(head)
  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end
  prev = nil
  while slow
    nxt = slow.next
    slow.next = prev
    prev = slow
    slow = nxt
  end
  ans = 0
  a = head
  b = prev
  while b
    ans = [ans, a.val + b.val].max
    a = a.next
    b = b.next
  end
  ans
end
''')

add("2131_longest_palindrome_by_concatenating_two_letter_words", r'''
# LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

# @param {String[]} words
# @return {Integer}
def longest_palindrome(words)
  freq = Hash.new(0)
  words.each { |w| freq[w] += 1 }
  ans = 0
  center = false
  freq.each do |w, c|
    rev = w[1] + w[0]
    if w[0] == w[1]
      ans += (c / 2) * 4
      center = true if c.odd?
    elsif w < rev
      ans += [c, freq[rev]].min * 4
    end
  end
  ans += 2 if center
  ans
end
''')

add("2132_stamping_the_grid", r'''
# LeetCode 2132 - Stamping the Grid
# https://leetcode.com/problems/stamping-the-grid/

# @param {Integer[][]} grid
# @param {Integer} stamp_height
# @param {Integer} stamp_width
# @return {Boolean}
def possible_to_stamp(grid, stamp_height, stamp_width)
  m = grid.length
  n = grid[0].length
  pref = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |i|
    n.times do |j|
      pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j]
    end
  end
  diff = Array.new(m + 1) { Array.new(n + 1, 0) }
  i = 0
  while i + stamp_height - 1 < m
    j = 0
    while j + stamp_width - 1 < n
      sum = pref[i + stamp_height][j + stamp_width] - pref[i][j + stamp_width] - pref[i + stamp_height][j] + pref[i][j]
      if sum == 0
        diff[i][j] += 1
        diff[i][j + stamp_width] -= 1
        diff[i + stamp_height][j] -= 1
        diff[i + stamp_height][j + stamp_width] += 1
      end
      j += 1
    end
    i += 1
  end
  cur = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      v = diff[i][j]
      v += cur[i - 1][j] if i > 0
      v += cur[i][j - 1] if j > 0
      v -= cur[i - 1][j - 1] if i > 0 && j > 0
      cur[i][j] = v
      return false if grid[i][j] == 0 && v == 0
    end
  end
  true
end
''')

add("2133_check_if_every_row_and_column_contains_all_numbers", r'''
# LeetCode 2133 - Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

# @param {Integer[][]} matrix
# @return {Boolean}
def check_valid(matrix)
  n = matrix.length
  n.times do |i|
    row = Array.new(n + 1, false)
    col = Array.new(n + 1, false)
    n.times do |j|
      return false if row[matrix[i][j]] || col[matrix[j][i]]

      row[matrix[i][j]] = col[matrix[j][i]] = true
    end
  end
  true
end
''')

add("2134_minimum_swaps_to_group_all_1s_together_ii", r'''
# LeetCode 2134 - Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  ones = nums.sum
  return 0 if ones == 0

  n = nums.length
  window = nums[0...ones].sum
  best = window
  n.times do |i|
    window -= nums[i]
    window += nums[(i + ones) % n]
    best = [best, window].max
  end
  ones - best
end
''')

add("2135_count_words_obtained_after_adding_a_letter", r'''
# LeetCode 2135 - Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

# @param {String[]} start_words
# @param {String[]} target_words
# @return {Integer}
def word_count(start_words, target_words)
  mask = lambda do |w|
    m = 0
    w.each_byte { |b| m |= 1 << (b - 97) }
    m
  end

  have = {}
  start_words.each { |w| have[mask.call(w)] = true }
  ans = 0
  target_words.each do |w|
    m = mask.call(w)
    w.each_byte do |b|
      if have[m ^ (1 << (b - 97))]
        ans += 1
        break
      end
    end
  end
  ans
end
''')

add("2136_earliest_possible_day_of_full_bloom", r'''
# LeetCode 2136 - Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

# @param {Integer[]} plant_time
# @param {Integer[]} grow_time
# @return {Integer}
def earliest_full_bloom(plant_time, grow_time)
  n = plant_time.length
  idx = (0...n).to_a
  idx.sort_by! { |a| -grow_time[a] }
  day = 0
  ans = 0
  idx.each do |i|
    day += plant_time[i]
    ans = [ans, day + grow_time[i]].max
  end
  ans
end
''')

add("2137_pour_water_between_buckets_to_make_water_levels_equal", r'''
# LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
# https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

# @param {Integer[]} buckets
# @param {Integer} loss
# @return {Float}
def equalize_water(buckets, loss)
  lo = 0.0
  hi = buckets.max.to_f
  60.times do
    mid = (lo + hi) / 2.0
    have = 0.0
    need = 0.0
    buckets.each do |b|
      if b >= mid
        have += b - mid
      else
        need += mid - b
      end
    end
    if have * (1 - loss / 100.0) >= need
      lo = mid
    else
      hi = mid
    end
  end
  lo
end
''')

add("2138_divide_a_string_into_groups_of_size_k", r'''
# LeetCode 2138 - Divide a String Into Groups of Size k
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

# @param {String} s
# @param {Integer} k
# @param {String} fill
# @return {String[]}
def divide_string(s, k, fill)
  ans = []
  0.step(s.length - 1, k) do |i|
    if i + k <= s.length
      ans << s[i, k]
    else
      chunk = s[i..]
      chunk += fill while chunk.length < k
      ans << chunk
    end
  end
  ans
end
''')

add("2139_minimum_moves_to_reach_target_score", r'''
# LeetCode 2139 - Minimum Moves to Reach Target Score
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

# @param {Integer} target
# @param {Integer} max_doubles
# @return {Integer}
def min_moves(target, max_doubles)
  ans = 0
  while target > 1 && max_doubles > 0
    if target.odd?
      target -= 1
      ans += 1
    else
      target /= 2
      max_doubles -= 1
      ans += 1
    end
  end
  ans + target - 1
end
''')

add("2140_solving_questions_with_brainpower", r'''
# LeetCode 2140 - Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/

# @param {Integer[][]} questions
# @return {Integer}
def most_points(questions)
  n = questions.length
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    pts, brain = questions[i]
    nxt = i + brain + 1
    take = pts + (nxt < n ? dp[nxt] : 0)
    dp[i] = [dp[i + 1], take].max
  end
  dp[0]
end
''')

add("2141_maximum_running_time_of_n_computers", r'''
# LeetCode 2141 - Maximum Running Time of N Computers
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

# @param {Integer} n
# @param {Integer[]} batteries
# @return {Integer}
def max_run_time(n, batteries)
  sum = batteries.sum
  lo = 1
  hi = sum / n
  while lo < hi
    mid = (lo + hi + 1) / 2
    need = batteries.sum { |b| [b, mid].min }
    if need >= mid * n
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
''')

add("2143_choose_numbers_from_two_arrays_in_range", r'''
# LeetCode 2143 - Choose Numbers From Two Arrays in Range
# https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def count_subranges(nums1, nums2)
  mod = 1_000_000_007
  n = nums1.length
  ans = 0
  dp = {}
  n.times do |i|
    ndp = Hash.new(0)
    ndp[nums1[i]] = (ndp[nums1[i]] + 1) % mod
    ndp[-nums2[i]] = (ndp[-nums2[i]] + 1) % mod
    dp.each do |diff, cnt|
      ndp[diff + nums1[i]] = (ndp[diff + nums1[i]] + cnt) % mod
      ndp[diff - nums2[i]] = (ndp[diff - nums2[i]] + cnt) % mod
    end
    dp = ndp
    ans = (ans + (dp[0] || 0)) % mod
  end
  ans
end
''')

add("2144_minimum_cost_of_buying_candies_with_discount", r'''
# LeetCode 2144 - Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(cost)
  arr = cost.sort.reverse
  ans = 0
  arr.each_with_index { |x, i| ans += x if i % 3 != 2 }
  ans
end
''')

add("2145_count_the_hidden_sequences", r'''
# LeetCode 2145 - Count the Hidden Sequences
# https://leetcode.com/problems/count-the-hidden-sequences/

# @param {Integer[]} differences
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def number_of_arrays(differences, lower, upper)
  cur = 0
  mn = 0
  mx = 0
  differences.each do |d|
    cur += d
    mn = [mn, cur].min
    mx = [mx, cur].max
  end
  res = (upper - lower) - (mx - mn) + 1
  res < 0 ? 0 : res
end
''')

written = 0
for folder, body in S.items():
    (ROOT / folder / "solution.rb").write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
