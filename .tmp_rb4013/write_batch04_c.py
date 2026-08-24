#!/usr/bin/env python3
from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

LIST = """class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end
"""


def hdr(num, title, slug):
    return f"# LeetCode {num} - {title}\n# https://leetcode.com/problems/{slug}/\n\n"


files = {}

files["2034_stock_price_fluctuation"] = hdr("2034", "Stock Price Fluctuation", "stock-price-fluctuation") + """class StockPrice
  def initialize
    @latest_ts = 0
    @price_at = {}
    @max_heap = []
    @min_heap = []
  end

  def update(timestamp, price)
    @price_at[timestamp] = price
    @latest_ts = timestamp if timestamp >= @latest_ts
    heap_push(@max_heap, [-price, timestamp])
    heap_push(@min_heap, [price, timestamp])
  end

  def current
    @price_at[@latest_ts]
  end

  def maximum
    loop do
      price, ts = @max_heap[0]
      price = -price
      return price if @price_at[ts] == price

      heap_pop(@max_heap)
    end
  end

  def minimum
    loop do
      price, ts = @min_heap[0]
      return price if @price_at[ts] == price

      heap_pop(@min_heap)
    end
  end

  private

  def heap_push(heap, item)
    heap << item
    i = heap.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if heap[p][0] < heap[i][0] || (heap[p][0] == heap[i][0] && heap[p][1] <= heap[i][1])

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  def heap_pop(heap)
    return heap.pop if heap.length == 1

    top = heap[0]
    heap[0] = heap.pop
    i = 0
    loop do
      l = 2 * i + 1
      r = l + 1
      smallest = i
      smallest = l if l < heap.length && (heap[l][0] < heap[smallest][0] || (heap[l][0] == heap[smallest][0] && heap[l][1] < heap[smallest][1]))
      smallest = r if r < heap.length && (heap[r][0] < heap[smallest][0] || (heap[r][0] == heap[smallest][0] && heap[r][1] < heap[smallest][1]))
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end
end
"""

files["2035_partition_array_into_two_arrays_to_minimize_sum_difference"] = hdr("2035", "Partition Array Into Two Arrays to Minimize Sum Difference", "partition-array-into-two-arrays-to-minimize-sum-difference") + """# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
  n = nums.length / 2
  total = nums.sum
  left = nums[0...n]
  right = nums[n..]

  sums_by_count = lambda do |arr|
    m = arr.length
    res = Array.new(m + 1) { [] }
    (0...(1 << m)).each do |mask|
      s = c = 0
      m.times do |i|
        if (mask & (1 << i)) != 0
          s += arr[i]
          c += 1
        end
      end
      res[c] << s
    end
    res.each(&:sort!)
    res
  end

  left_sums = sums_by_count.call(left)
  right_sums = sums_by_count.call(right)
  ans = 10**18
  (0..n).each do |k|
    arr = right_sums[n - k]
    left_sums[k].each do |s1|
      need = total / 2 - s1
      lo = 0
      hi = arr.length
      while lo < hi
        mid = (lo + hi) >> 1
        if arr[mid] < need
          lo = mid + 1
        else
          hi = mid
        end
      end
      [lo - 1, lo].each do |j|
        next unless j >= 0 && j < arr.length

        s2 = arr[j]
        ans = [ans, (total - 2 * (s1 + s2)).abs].min
      end
    end
  end
  ans
end
"""

files["2036_maximum_alternating_subarray_sum"] = hdr("2036", "Maximum Alternating Subarray Sum", "maximum-alternating-subarray-sum") + """# @param {Integer[]} nums
# @return {Integer}
def maximum_alternating_subarray_sum(nums)
  ans = -10**18
  even = 0
  nums.each_with_index do |x, i|
    if i.even?
      even += x
    else
      even = [0, even - x].max
    end
    ans = [ans, even].max
  end
  odd = 0
  (1...nums.length).each do |i|
    x = nums[i]
    if i.odd?
      odd += x
    else
      odd = [0, odd - x].max
    end
    ans = [ans, odd].max
  end
  ans
end
"""

files["2037_minimum_number_of_moves_to_seat_everyone"] = hdr("2037", "Minimum Number of Moves to Seat Everyone", "minimum-number-of-moves-to-seat-everyone") + """# @param {Integer[]} seats
# @param {Integer[]} students
# @return {Integer}
def min_moves_to_seat(seats, students)
  seats.sort!
  students.sort!
  seats.zip(students).sum { |a, b| (a - b).abs }
end
"""

files["2038_remove_colored_pieces_if_both_neighbors_are_the_same_color"] = hdr("2038", "Remove Colored Pieces if Both Neighbors are the Same Color", "remove-colored-pieces-if-both-neighbors-are-the-same-color") + """# @param {String} colors
# @return {Boolean}
def winner_of_game(colors)
  a = b = 0
  (1...colors.length - 1).each do |i|
    next unless colors[i - 1] == colors[i] && colors[i] == colors[i + 1]

    if colors[i] == "A"
      a += 1
    else
      b += 1
    end
  end
  a > b
end
"""

files["2039_the_time_when_the_network_becomes_idle"] = hdr("2039", "The Time When the Network Becomes Idle", "the-time-when-the-network-becomes-idle") + """# @param {Integer[][]} edges
# @param {Integer[]} patience
# @return {Integer}
def network_becomes_idle(edges, patience)
  n = patience.length
  g = Array.new(n) { [] }
  edges.each do |u, v|
    g[u] << v
    g[v] << u
  end
  dist = Array.new(n, -1)
  q = [0]
  dist[0] = 0
  until q.empty?
    u = q.shift
    g[u].each do |v|
      next unless dist[v] == -1

      dist[v] = dist[u] + 1
      q << v
    end
  end
  ans = 0
  (1...n).each do |i|
    rnd = dist[i] * 2
    last_send = ((rnd - 1) / patience[i]) * patience[i]
    ans = [ans, last_send + rnd].max
  end
  ans + 1
end
"""

files["2040_kth_smallest_product_of_two_sorted_arrays"] = hdr("2040", "Kth Smallest Product of Two Sorted Arrays", "kth-smallest-product-of-two-sorted-arrays") + """# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def kth_smallest_product(nums1, nums2, k)
  count_le = lambda do |x|
    cnt = 0
    nums1.each do |a|
      if a > 0
        lo = 0
        hi = nums2.length
        while lo < hi
          mid = (lo + hi) >> 1
          if a * nums2[mid] <= x
            lo = mid + 1
          else
            hi = mid
          end
        end
        cnt += lo
      elsif a < 0
        lo = 0
        hi = nums2.length
        while lo < hi
          mid = (lo + hi) >> 1
          if a * nums2[mid] <= x
            hi = mid
          else
            lo = mid + 1
          end
        end
        cnt += nums2.length - lo
      elsif x >= 0
        cnt += nums2.length
      end
    end
    cnt
  end

  lo = -10**10
  hi = 10**10
  while lo < hi
    mid = lo + (hi - lo) / 2
    if count_le.call(mid) >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
"""

files["2042_check_if_numbers_are_ascending_in_a_sentence"] = hdr("2042", "Check if Numbers Are Ascending in a Sentence", "check-if-numbers-are-ascending-in-a-sentence") + """# @param {String} s
# @return {Boolean}
def are_numbers_ascending(s)
  prev = -1
  s.split(" ").each do |tok|
    next if tok.empty?
    next unless tok[0] >= "0" && tok[0] <= "9"

    v = tok.to_i
    return false if v <= prev

    prev = v
  end
  true
end
"""

files["2043_simple_bank_system"] = hdr("2043", "Simple Bank System", "simple-bank-system") + """class Bank
  def initialize(balance)
    @bal = balance.dup
  end

  def transfer(account1, account2, money)
    return false unless valid(account1) && valid(account2) && @bal[account1 - 1] >= money

    @bal[account1 - 1] -= money
    @bal[account2 - 1] += money
    true
  end

  def deposit(account, money)
    return false unless valid(account)

    @bal[account - 1] += money
    true
  end

  def withdraw(account, money)
    return false unless valid(account) && @bal[account - 1] >= money

    @bal[account - 1] -= money
    true
  end

  private

  def valid(account)
    account >= 1 && account <= @bal.length
  end
end
"""

files["2044_count_number_of_maximum_bitwise_or_subsets"] = hdr("2044", "Count Number of Maximum Bitwise-OR Subsets", "count-number-of-maximum-bitwise-or-subsets") + """# @param {Integer[]} nums
# @return {Integer}
def count_max_or_subsets(nums)
  max_or = 0
  nums.each { |x| max_or |= x }
  ans = 0
  dfs = lambda do |i, cur|
    if i == nums.length
      ans += 1 if cur == max_or
      return
    end
    dfs.call(i + 1, cur)
    dfs.call(i + 1, cur | nums[i])
  end
  dfs.call(0, 0)
  ans
end
"""

files["2045_second_minimum_time_to_reach_destination"] = hdr("2045", "Second Minimum Time to Reach Destination", "second-minimum-time-to-reach-destination") + """# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} time
# @param {Integer} change
# @return {Integer}
def second_minimum(n, edges, time, change)
  g = Array.new(n + 1) { [] }
  edges.each do |u, v|
    g[u] << v
    g[v] << u
  end
  dist1 = Array.new(n + 1, -1)
  dist2 = Array.new(n + 1, -1)
  q = [[1, 0]]
  dist1[1] = 0
  until q.empty?
    u, d = q.shift
    g[u].each do |v|
      nd = d + 1
      if dist1[v] == -1
        dist1[v] = nd
        q << [v, nd]
      elsif dist2[v] == -1 && nd > dist1[v]
        dist2[v] = nd
        q << [v, nd]
      end
    end
  end
  steps = dist2[n]
  ans = 0
  steps.times do
    ans += change - ans % change if (ans / change).odd?
    ans += time
  end
  ans
end
"""

files["2046_sort_linked_list_already_sorted_using_absolute_values"] = hdr("2046", "Sort Linked List Already Sorted Using Absolute Values", "sort-linked-list-already-sorted-using-absolute-values") + LIST + """
# @param {ListNode} head
# @return {ListNode}
def sort_linked_list(head)
  return nil if head.nil?

  prev = head
  cur = head.next
  while cur
    if cur.val < 0
      prev.next = cur.next
      cur.next = head
      head = cur
      cur = prev.next
    else
      prev = cur
      cur = cur.next
    end
  end
  head
end
"""

files["2047_number_of_valid_words_in_a_sentence"] = hdr("2047", "Number of Valid Words in a Sentence", "number-of-valid-words-in-a-sentence") + """# @param {String} sentence
# @return {Integer}
def count_valid_words(sentence)
  valid = lambda do |w|
    return false if w.empty?

    hyphen = 0
    w.each_char.with_index do |c, i|
      return false if c >= "0" && c <= "9"

      if c == "-"
        hyphen += 1
        return false if hyphen > 1 || i.zero? || i == w.length - 1
        return false unless w[i - 1] >= "a" && w[i - 1] <= "z" && w[i + 1] >= "a" && w[i + 1] <= "z"
      elsif "!.,".include?(c)
        return false if i != w.length - 1
      else
        return false unless c >= "a" && c <= "z"
      end
    end
    true
  end
  sentence.split(" ").count { |tok| valid.call(tok) }
end
"""

files["2048_next_greater_numerically_balanced_number"] = hdr("2048", "Next Greater Numerically Balanced Number", "next-greater-numerically-balanced-number") + """# @param {Integer} n
# @return {Integer}
def next_beautiful_number(n)
  balanced = lambda do |x|
    cnt = Array.new(10, 0)
    while x > 0
      cnt[x % 10] += 1
      x /= 10
    end
    10.times { |d| return false if !cnt[d].zero? && cnt[d] != d }
    true
  end
  x = n + 1
  loop do
    return x if balanced.call(x)

    x += 1
  end
end
"""

files["2049_count_nodes_with_the_highest_score"] = hdr("2049", "Count Nodes With the Highest Score", "count-nodes-with-the-highest-score") + """# @param {Integer[]} parents
# @return {Integer}
def count_highest_score_nodes(parents)
  n = parents.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parents[i]] << i }
  size = Array.new(n, 0)
  dfs = lambda do |u|
    size[u] = 1
    children[u].each { |v| size[u] += dfs.call(v) }
    size[u]
  end
  dfs.call(0)
  best = 0
  ans = 0
  n.times do |u|
    score = 1
    children[u].each { |v| score *= size[v] }
    up = n - size[u]
    score *= up if up > 0
    if score > best
      best = score
      ans = 1
    elsif score == best
      ans += 1
    end
  end
  ans
end
"""

files["2050_parallel_courses_iii"] = hdr("2050", "Parallel Courses III", "parallel-courses-iii") + """# @param {Integer} n
# @param {Integer[][]} relations
# @param {Integer[]} time
# @return {Integer}
def minimum_time(n, relations, time)
  g = Array.new(n + 1) { [] }
  indeg = Array.new(n + 1, 0)
  dist = Array.new(n + 1, 0)
  relations.each do |u, v|
    g[u] << v
    indeg[v] += 1
  end
  q = []
  (1..n).each do |i|
    dist[i] = time[i - 1]
    q << i if indeg[i].zero?
  end
  until q.empty?
    u = q.shift
    g[u].each do |v|
      dist[v] = [dist[v], dist[u] + time[v - 1]].max
      indeg[v] -= 1
      q << v if indeg[v].zero?
    end
  end
  dist[1..].max
end
"""

files["2052_minimum_cost_to_separate_sentence_into_rows"] = hdr("2052", "Minimum Cost to Separate Sentence Into Rows", "minimum-cost-to-separate-sentence-into-rows") + """# @param {String} sentence
# @param {Integer} k
# @return {Integer}
def minimum_cost(sentence, k)
  words = sentence.strip.split
  n = words.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[n] = 0
  (n - 1).downto(0) do |i|
    length = -1
    (i...n).each do |j|
      length += 1 + words[j].length
      break if length > k

      cost = 0
      if j < n - 1
        extra = k - length
        cost = extra * extra
      end
      dp[i] = [dp[i], cost + dp[j + 1]].min
    end
  end
  dp[0]
end
"""

files["2053_kth_distinct_string_in_an_array"] = hdr("2053", "Kth Distinct String in an Array", "kth-distinct-string-in-an-array") + """# @param {String[]} arr
# @param {Integer} k
# @return {String}
def kth_distinct(arr, k)
  freq = Hash.new(0)
  arr.each { |s| freq[s] += 1 }
  arr.each do |s|
    next unless freq[s] == 1

    k -= 1
    return s if k.zero?
  end
  ""
end
"""

files["2054_two_best_non_overlapping_events"] = hdr("2054", "Two Best Non-Overlapping Events", "two-best-non-overlapping-events") + """# @param {Integer[][]} events
# @return {Integer}
def max_two_events(events)
  events.sort_by! { |e| e[0] }
  n = events.length
  suffix = Array.new(n + 1, 0)
  (n - 1).downto(0) { |i| suffix[i] = [suffix[i + 1], events[i][2]].max }
  ans = 0
  n.times do |i|
    ans = [ans, events[i][2]].max
    lo = i + 1
    hi = n
    while lo < hi
      mid = (lo + hi) >> 1
      if events[mid][0] > events[i][1]
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans = [ans, events[i][2] + suffix[lo]].max if lo < n
  end
  ans
end
"""

files["2055_plates_between_candles"] = hdr("2055", "Plates Between Candles", "plates-between-candles") + """# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def plates_between_candles(s, queries)
  n = s.length
  pref = Array.new(n + 1, 0)
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  last = -1
  s.each_char.with_index do |ch, i|
    pref[i + 1] = pref[i] + (ch == "*" ? 1 : 0)
    last = i if ch == "|"
    left[i] = last
  end
  last = -1
  (n - 1).downto(0) do |i|
    last = i if s[i] == "|"
    right[i] = last
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(ql, qr), i|
    l = right[ql]
    r = left[qr]
    ans[i] = pref[r] - pref[l] if l != -1 && r != -1 && l < r
  end
  ans
end
"""

files["2056_number_of_valid_move_combinations_on_chessboard"] = hdr("2056", "Number of Valid Move Combinations On Chessboard", "number-of-valid-move-combinations-on-chessboard") + """# @param {String[]} pieces
# @param {Integer[][]} positions
# @return {Integer}
def count_combinations(pieces, positions)
  dirs = {
    "rook" => [[1, 0], [-1, 0], [0, 1], [0, -1]],
    "bishop" => [[1, 1], [1, -1], [-1, 1], [-1, -1]],
    "queen" => [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
  }
  n = pieces.length
  all_moves = []
  n.times do |i|
    ms = [{ dr: 0, dc: 0, steps: 0 }]
    r, c = positions[i]
    dirs[pieces[i]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      step = 1
      while nr.between?(1, 8) && nc.between?(1, 8)
        ms << { dr: dr, dc: dc, steps: step }
        nr += dr
        nc += dc
        step += 1
      end
    end
    all_moves << ms
  end
  chosen = Array.new(n)
  ans = 0

  ok_combo = lambda do |last|
    max_t = (0..last).map { |i| chosen[i][:steps] }.max
    (1..max_t).each do |t|
      seen = {}
      (0..last).each do |i|
        m = chosen[i]
        if m[:steps].zero?
          pr, pc = positions[i]
        else
          use = [t, m[:steps]].min
          pr = positions[i][0] + m[:dr] * use
          pc = positions[i][1] + m[:dc] * use
        end
        key = (pr << 32) ^ (pc & 0xFFFFFFFF)
        return false if seen[key]

        seen[key] = true
      end
    end
    true
  end

  dfs = lambda do |i|
    if i == pieces.length
      ans += 1
      return
    end
    all_moves[i].each do |m|
      chosen[i] = m
      dfs.call(i + 1) if ok_combo.call(i)
    end
  end
  dfs.call(0)
  ans
end
"""

files["2057_smallest_index_with_equal_value"] = hdr("2057", "Smallest Index With Equal Value", "smallest-index-with-equal-value") + """# @param {Integer[]} nums
# @return {Integer}
def smallest_equal(nums)
  nums.each_with_index { |v, i| return i if i % 10 == v }
  -1
end
"""

files["2058_find_the_minimum_and_maximum_number_of_nodes_between_critical_points"] = hdr("2058", "Find the Minimum and Maximum Number of Nodes Between Critical Points", "find-the-minimum-and-maximum-number-of-nodes-between-critical-points") + LIST + """
# @param {ListNode} head
# @return {Integer[]}
def nodes_between_critical_points(head)
  crit = []
  prev = head
  cur = head.next
  idx = 1
  while cur && cur.next
    if (cur.val > prev.val && cur.val > cur.next.val) || (cur.val < prev.val && cur.val < cur.next.val)
      crit << idx
    end
    prev = cur
    cur = cur.next
    idx += 1
  end
  return [-1, -1] if crit.length < 2

  mn = crit[1] - crit[0]
  (2...crit.length).each { |i| mn = [mn, crit[i] - crit[i - 1]].min }
  [mn, crit[-1] - crit[0]]
end
"""

files["2059_minimum_operations_to_convert_number"] = hdr("2059", "Minimum Operations to Convert Number", "minimum-operations-to-convert-number") + """# @param {Integer[]} nums
# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def minimum_operations(nums, start, goal)
  return 0 if start == goal

  vis = { start => true }
  q = [start]
  steps = 0
  until q.empty?
    steps += 1
    q.length.times do
      cur = q.shift
      nums.each do |x|
        [cur + x, cur - x, cur ^ x].each do |nxt|
          return steps if nxt == goal

          if nxt.between?(0, 1000) && !vis[nxt]
            vis[nxt] = true
            q << nxt
          end
        end
      end
    end
  end
  -1
end
"""

written = 0
for folder, content in files.items():
    (root / folder / "solution.rb").write_bytes(content.encode("utf-8"))
    written += 1
print(f"wrote {written}")
