#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2396_strictly_palindromic_number"] = r'''# LeetCode 2396 - Strictly Palindromic Number
# https://leetcode.com/problems/strictly-palindromic-number/

# @param {Integer} n
# @return {Boolean}
def is_strictly_palindromic(n)
  false
end
'''

FILES["2397_maximum_rows_covered_by_columns"] = r'''# LeetCode 2397 - Maximum Rows Covered by Columns
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

# @param {Integer[][]} matrix
# @param {Integer} num_select
# @return {Integer}
def maximum_rows(matrix, num_select)
  m = matrix.length
  n = matrix[0].length
  ans = [0]
  dfs = lambda do |col, chosen, mask|
    if chosen == num_select
      covered = 0
      (0...m).each do |i|
        ok = true
        (0...n).each do |j|
          if matrix[i][j] == 1 && ((mask >> j) & 1) == 0
            ok = false
            break
          end
        end
        covered += 1 if ok
      end
      ans[0] = covered if covered > ans[0]
      return
    end
    return if col == n
    dfs.call(col + 1, chosen + 1, mask | (1 << col))
    dfs.call(col + 1, chosen, mask)
  end
  dfs.call(0, 0, 0)
  ans[0]
end
'''

FILES["2398_maximum_number_of_robots_within_budget"] = r'''# LeetCode 2398 - Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

# @param {Integer[]} charge_times
# @param {Integer[]} running_costs
# @param {Integer} budget
# @return {Integer}
def maximum_robots(charge_times, running_costs, budget)
  n = charge_times.length
  left = 0
  s = 0
  dq = []
  ans = 0
  (0...n).each do |right|
    dq.pop while !dq.empty? && charge_times[dq[-1]] <= charge_times[right]
    dq << right
    s += running_costs[right]
    while left <= right && charge_times[dq[0]] + (right - left + 1) * s > budget
      dq.shift if dq[0] == left
      s -= running_costs[left]
      left += 1
    end
    cand = right - left + 1
    ans = cand if cand > ans
  end
  ans
end
'''

FILES["2399_check_distances_between_same_letters"] = r'''# LeetCode 2399 - Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters/

# @param {String} s
# @param {Integer[]} distance
# @return {Boolean}
def check_distances(s, distance)
  first = Array.new(26, -1)
  s.each_char.with_index do |ch, i|
    c = ch.ord - 97
    if first[c] == -1
      first[c] = i
    elsif i - first[c] - 1 != distance[c]
      return false
    end
  end
  true
end
'''

FILES["2400_number_of_ways_to_reach_a_position_after_exactly_k_steps"] = r'''# LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

# @param {Integer} start_pos
# @param {Integer} end_pos
# @param {Integer} k
# @return {Integer}
def number_of_ways(start_pos, end_pos, k)
  mod = 1_000_000_007
  mod_pow = lambda do |a, e|
    res = 1
    base = a % mod
    while e > 0
      res = res * base % mod if e & 1 != 0
      base = base * base % mod
      e >>= 1
    end
    res
  end
  comb = lambda do |n, r|
    return 0 if r < 0 || r > n
    num = 1
    den = 1
    r.times do |i|
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
    end
    num * mod_pow.call(den, mod - 2) % mod
  end
  diff = (end_pos - start_pos).abs
  return 0 if diff > k || (k - diff) % 2 != 0
  r = (k + diff) / 2
  comb.call(k, r)
end
'''

FILES["2401_longest_nice_subarray"] = r'''# LeetCode 2401 - Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_nice_subarray(nums)
  used = 0
  left = 0
  ans = 0
  nums.each_index do |right|
    while (used & nums[right]) != 0
      used ^= nums[left]
      left += 1
    end
    used |= nums[right]
    cand = right - left + 1
    ans = cand if cand > ans
  end
  ans
end
'''

FILES["2402_meeting_rooms_iii"] = r'''# LeetCode 2402 - Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/

# @param {Integer} n
# @param {Integer[][]} meetings
# @return {Integer}
def most_booked(n, meetings)
  meetings = meetings.sort_by { |x| x[0] }
  free = []
  busy = []
  push_free = lambda do |x|
    free << x
    i = free.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if free[p] <= free[i]
      free[p], free[i] = free[i], free[p]
      i = p
    end
  end
  pop_free = lambda do
    top = free[0]
    last = free.pop
    unless free.empty?
      free[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = i * 2 + 2
        s = l if l < free.length && free[l] < free[s]
        s = r if r < free.length && free[r] < free[s]
        break if s == i
        free[s], free[i] = free[i], free[s]
        i = s
      end
    end
    top
  end
  cmp_busy = lambda do |a, b|
    return a[0] - b[0] if a[0] != b[0]
    a[1] - b[1]
  end
  push_busy = lambda do |x|
    busy << x
    i = busy.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if cmp_busy.call(busy[p], busy[i]) <= 0
      busy[p], busy[i] = busy[i], busy[p]
      i = p
    end
  end
  pop_busy = lambda do
    top = busy[0]
    last = busy.pop
    unless busy.empty?
      busy[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = i * 2 + 2
        s = l if l < busy.length && cmp_busy.call(busy[l], busy[s]) < 0
        s = r if r < busy.length && cmp_busy.call(busy[r], busy[s]) < 0
        break if s == i
        busy[s], busy[i] = busy[i], busy[s]
        i = s
      end
    end
    top
  end
  (0...n).each { |i| push_free.call(i) }
  cnt = Array.new(n, 0)
  meetings.each do |start, finish|
    push_free.call(pop_busy.call[1]) while !busy.empty? && busy[0][0] <= start
    dur = finish - start
    if !free.empty?
      room = pop_free.call
      begin_t = start
    else
      top = pop_busy.call
      begin_t = top[0]
      room = top[1]
    end
    push_busy.call([begin_t + dur, room])
    cnt[room] += 1
  end
  ans = 0
  (1...n).each { |i| ans = i if cnt[i] > cnt[ans] }
  ans
end
'''

FILES["2403_minimum_time_to_kill_all_monsters"] = r'''# LeetCode 2403 - Minimum Time to Kill All Monsters
# https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

# @param {Integer[]} power
# @return {Integer}
def minimum_time(power)
  bit_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  n = power.length
  nmask = 1 << n
  dp = Array.new(nmask, 10**18)
  dp[0] = 0
  (0...nmask).each do |mask|
    killed = bit_count.call(mask)
    gain = killed + 1
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      need = (power[i] + gain - 1) / gain
      nm = mask | (1 << i)
      cand = dp[mask] + need
      dp[nm] = cand if cand < dp[nm]
    end
  end
  dp[nmask - 1]
end
'''

FILES["2404_most_frequent_even_element"] = r'''# LeetCode 2404 - Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/

# @param {Integer[]} nums
# @return {Integer}
def most_frequent_even(nums)
  cnt = Hash.new(0)
  ans = -1
  best = 0
  nums.each do |x|
    next if x % 2 != 0
    cnt[x] += 1
    c = cnt[x]
    if c > best || (c == best && (ans == -1 || x < ans))
      best = c
      ans = x
    end
  end
  ans
end
'''

FILES["2405_optimal_partition_of_string"] = r'''# LeetCode 2405 - Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

# @param {String} s
# @return {Integer}
def partition_string(s)
  ans = 1
  seen = 0
  s.each_char do |c|
    bit = 1 << (c.ord - 97)
    if (seen & bit) != 0
      ans += 1
      seen = 0
    end
    seen |= bit
  end
  ans
end
'''

FILES["2406_divide_intervals_into_minimum_number_of_groups"] = r'''# LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

# @param {Integer[][]} intervals
# @return {Integer}
def min_groups(intervals)
  events = []
  intervals.each do |it|
    events << [it[0], 1]
    events << [it[1] + 1, -1]
  end
  events.sort_by! { |e| [e[0], e[1]] }
  cur = 0
  ans = 0
  events.each do |_, d|
    cur += d
    ans = cur if cur > ans
  end
  ans
end
'''

FILES["2407_longest_increasing_subsequence_ii"] = r'''# LeetCode 2407 - Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def length_of_lis(nums, k)
  max_v = nums.max
  tree = Array.new(4 * (max_v + 1), 0)
  update = nil
  query = nil
  update = lambda do |idx, l, r, pos, val|
    if l == r
      tree[idx] = val if val > tree[idx]
      return
    end
    mid = (l + r) >> 1
    if pos <= mid
      update.call(idx * 2, l, mid, pos, val)
    else
      update.call(idx * 2 + 1, mid + 1, r, pos, val)
    end
    tree[idx] = [tree[idx * 2], tree[idx * 2 + 1]].max
  end
  query = lambda do |idx, l, r, ql, qr|
    return 0 if qr < l || r < ql
    return tree[idx] if ql <= l && r <= qr
    mid = (l + r) >> 1
    [query.call(idx * 2, l, mid, ql, qr), query.call(idx * 2 + 1, mid + 1, r, ql, qr)].max
  end
  ans = 0
  nums.each do |x|
    lo = [1, x - k].max
    best = 1
    best = query.call(1, 1, max_v, lo, x - 1) + 1 if lo <= x - 1
    update.call(1, 1, max_v, x, best)
    ans = best if best > ans
  end
  ans
end
'''

FILES["2408_design_sql"] = r'''# LeetCode 2408 - Design SQL
# https://leetcode.com/problems/design-sql/

class SQL
  def initialize(names, columns)
    @tables = {}
    @next_id = {}
    names.each do |name|
      @tables[name] = []
      @next_id[name] = 1
    end
  end

  def ins(name, row)
    return false unless @tables.key?(name)
    row_id = @next_id[name]
    @next_id[name] = row_id + 1
    full = [row_id.to_s] + row
    @tables[name] << full
    true
  end

  def rmv(name, row_id)
    rows = @tables[name]
    rows.each_index do |i|
      if rows[i][0].to_i == row_id
        rows.delete_at(i)
        return
      end
    end
  end

  def sel(name, row_id, column_id)
    @tables[name].each do |r|
      if r[0].to_i == row_id
        return "<null>" if column_id < 1 || column_id >= r.length
        return r[column_id]
      end
    end
    "<null>"
  end

  def exp(name)
    @tables[name].map { |r| r.join(",") }
  end
end
'''

FILES["2409_count_days_spent_together"] = r'''# LeetCode 2409 - Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

# @param {String} arrive_alice
# @param {String} leave_alice
# @param {String} arrive_bob
# @param {String} leave_bob
# @return {Integer}
def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  to_day = lambda do |s|
    m = (s[0].ord - 48) * 10 + (s[1].ord - 48)
    d = (s[3].ord - 48) * 10 + (s[4].ord - 48)
    res = d
    (0...m - 1).each { |i| res += days[i] }
    res
  end
  a1 = to_day.call(arrive_alice)
  a2 = to_day.call(leave_alice)
  b1 = to_day.call(arrive_bob)
  b2 = to_day.call(leave_bob)
  start = [a1, b1].max
  finish = [a2, b2].min
  return 0 if finish < start
  finish - start + 1
end
'''

FILES["2410_maximum_matching_of_players_with_trainers"] = r'''# LeetCode 2410 - Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

# @param {Integer[]} players
# @param {Integer[]} trainers
# @return {Integer}
def match_players_and_trainers(players, trainers)
  players = players.sort
  trainers = trainers.sort
  i = 0
  j = 0
  ans = 0
  while i < players.length && j < trainers.length
    if players[i] <= trainers[j]
      ans += 1
      i += 1
      j += 1
    else
      j += 1
    end
  end
  ans
end
'''

FILES["2411_smallest_subarrays_with_maximum_bitwise_or"] = r'''# LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

# @param {Integer[]} nums
# @return {Integer[]}
def smallest_subarrays(nums)
  n = nums.length
  ans = Array.new(n, 0)
  last = Array.new(32, -1)
  (n - 1).downto(0) do |i|
    (0...32).each { |b| last[b] = i if ((nums[i] >> b) & 1) != 0 }
    far = i
    (0...32).each { |b| far = last[b] if last[b] > far }
    ans[i] = far - i + 1
  end
  ans
end
'''

FILES["2412_minimum_money_required_before_transactions"] = r'''# LeetCode 2412 - Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/

# @param {Integer[][]} transactions
# @return {Integer}
def minimum_money(transactions)
  total_loss = 0
  max_cashback = 0
  max_cost = 0
  transactions.each do |cost, cashback|
    if cost > cashback
      total_loss += cost - cashback
      max_cashback = cashback if cashback > max_cashback
    elsif cost > max_cost
      max_cost = cost
    end
  end
  [total_loss + max_cashback, total_loss + max_cost].max
end
'''

FILES["2413_smallest_even_multiple"] = r'''# LeetCode 2413 - Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/

# @param {Integer} n
# @return {Integer}
def smallest_even_multiple(n)
  n.even? ? n : n * 2
end
'''

FILES["2414_length_of_the_longest_alphabetical_continuous_substring"] = r'''# LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

# @param {String} s
# @return {Integer}
def longest_continuous_substring(s)
  ans = 1
  cur = 1
  (1...s.length).each do |i|
    if s[i].ord == s[i - 1].ord + 1
      cur += 1
      ans = cur if cur > ans
    else
      cur = 1
    end
  end
  ans
end
'''

FILES["2415_reverse_odd_levels_of_binary_tree"] = r'''# LeetCode 2415 - Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def reverse_odd_levels(root)
  dfs = lambda do |a, b, level|
    return if a.nil? || b.nil?
    a.val, b.val = b.val, a.val if level.odd?
    dfs.call(a.left, b.right, level + 1)
    dfs.call(a.right, b.left, level + 1)
  end
  dfs.call(root.left, root.right, 1) unless root.nil?
  root
end
'''

for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {folder}")
print(f"done {len(FILES)}")
