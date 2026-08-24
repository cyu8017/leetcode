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

files["2060_check_if_an_original_string_exists_given_two_encoded_strings"] = hdr("2060", "Check if an Original String Exists Given Two Encoded Strings", "check-if-an-original-string-exists-given-two-encoded-strings") + """# @param {String} s1
# @param {String} s2
# @return {Boolean}
def possibly_equals(s1, s2)
  memo = {}
  is_digit = ->(c) { c >= "0" && c <= "9" }

  dfs = lambda do |i, j, diff|
    key = [i, j, diff]
    return memo[key] if memo.key?(key)

    n = s1.length
    m = s2.length
    if i == n && j == m
      memo[key] = diff.zero?
      return diff.zero?
    end
    res = false
    if diff.zero? && i < n && j < m && !is_digit.call(s1[i]) && !is_digit.call(s2[j])
      res = dfs.call(i + 1, j + 1, 0) if s1[i] == s2[j]
    elsif diff > 0 && i < n && !is_digit.call(s1[i])
      res = dfs.call(i + 1, j, diff - 1)
    elsif diff < 0 && j < m && !is_digit.call(s2[j])
      res = dfs.call(i, j + 1, diff + 1)
    end
    if !res && i < n && is_digit.call(s1[i])
      val = 0
      p = i
      while p < n && is_digit.call(s1[p])
        val = val * 10 + (s1[p].ord - 48)
        if dfs.call(p + 1, j, diff + val)
          res = true
          break
        end
        p += 1
      end
    end
    if !res && j < m && is_digit.call(s2[j])
      val = 0
      p = j
      while p < m && is_digit.call(s2[p])
        val = val * 10 + (s2[p].ord - 48)
        if dfs.call(i, p + 1, diff - val)
          res = true
          break
        end
        p += 1
      end
    end
    memo[key] = res
    res
  end
  dfs.call(0, 0, 0)
end
"""

files["2061_number_of_spaces_cleaning_robot_cleaned"] = hdr("2061", "Number of Spaces Cleaning Robot Cleaned", "number-of-spaces-cleaning-robot-cleaned") + """# @param {Integer[][]} room
# @return {Integer}
def number_of_clean_rooms(room)
  m = room.length
  n = room[0].length
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  vis = {}
  cleaned = { 0 => true }
  r = c = d = 0
  loop do
    state = r * 10000 + c * 10 + d
    break if vis[state]

    vis[state] = true
    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if nr.between?(0, m - 1) && nc.between?(0, n - 1) && room[nr][nc].zero?
      r = nr
      c = nc
      cleaned[(r << 32) ^ (c & 0xFFFFFFFF)] = true
    else
      d = (d + 1) % 4
    end
  end
  cleaned.length
end
"""

files["2062_count_vowel_substrings_of_a_string"] = hdr("2062", "Count Vowel Substrings of a String", "count-vowel-substrings-of-a-string") + """# @param {String} word
# @return {Integer}
def count_vowel_substrings(word)
  vowels = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  ans = 0
  n = word.length
  n.times do |i|
    seen = {}
    (i...n).each do |j|
      break unless vowels[word[j]]

      seen[word[j]] = true
      ans += 1 if seen.length == 5
    end
  end
  ans
end
"""

files["2063_vowels_of_all_substrings"] = hdr("2063", "Vowels of All Substrings", "vowels-of-all-substrings") + """# @param {String} word
# @return {Integer}
def count_vowels(word)
  vowels = { "a" => true, "e" => true, "i" => true, "o" => true, "u" => true }
  n = word.length
  ans = 0
  word.each_char.with_index do |c, i|
    ans += (i + 1) * (n - i) if vowels[c]
  end
  ans
end
"""

files["2064_minimized_maximum_of_products_distributed_to_any_store"] = hdr("2064", "Minimized Maximum of Products Distributed to Any Store", "minimized-maximum-of-products-distributed-to-any-store") + """# @param {Integer} n
# @param {Integer[]} quantities
# @return {Integer}
def minimized_maximum(n, quantities)
  can = lambda do |x|
    need = 0
    quantities.each do |q|
      need += (q + x - 1) / x
      return false if need > n
    end
    true
  end
  lo = 1
  hi = quantities.max
  while lo < hi
    mid = (lo + hi) >> 1
    if can.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
"""

files["2065_maximum_path_quality_of_a_graph"] = hdr("2065", "Maximum Path Quality of a Graph", "maximum-path-quality-of-a-graph") + """# @param {Integer[]} values
# @param {Integer[][]} edges
# @param {Integer} max_time
# @return {Integer}
def maximal_path_quality(values, edges, max_time)
  n = values.length
  g = Array.new(n) { [] }
  edges.each do |u, v, t|
    g[u] << [v, t]
    g[v] << [u, t]
  end
  ans = 0
  vis = Array.new(n, 0)
  dfs = lambda do |u, time, quality|
    return if time > max_time

    first = vis[u].zero?
    quality += values[u] if first
    vis[u] += 1
    ans = [ans, quality].max if u.zero?
    g[u].each { |v, w| dfs.call(v, time + w, quality) }
    vis[u] -= 1
  end
  dfs.call(0, 0, 0)
  ans
end
"""

files["2067_number_of_equal_count_substrings"] = hdr("2067", "Number of Equal Count Substrings", "number-of-equal-count-substrings") + """# @param {String} s
# @param {Integer} count
# @return {Integer}
def equal_count_substrings(s, count)
  ans = 0
  n = s.length
  seen = Array.new(26, false)
  max_unique = 0
  s.each_char do |c|
    i = c.ord - 97
    unless seen[i]
      seen[i] = true
      max_unique += 1
    end
  end
  (1..max_unique).each do |u|
    need_len = u * count
    break if need_len > n

    freq = Array.new(26, 0)
    have = 0
    n.times do |i|
      c = s[i].ord - 97
      freq[c] += 1
      if freq[c] == count
        have += 1
      elsif freq[c] == count + 1
        have -= 1
      end
      if i >= need_len
        p = s[i - need_len].ord - 97
        if freq[p] == count
          have -= 1
        elsif freq[p] == count + 1
          have += 1
        end
        freq[p] -= 1
      end
      ans += 1 if i + 1 >= need_len && have == u
    end
  end
  ans
end
"""

files["2068_check_whether_two_strings_are_almost_equivalent"] = hdr("2068", "Check Whether Two Strings are Almost Equivalent", "check-whether-two-strings-are-almost-equivalent") + """# @param {String} word1
# @param {String} word2
# @return {Boolean}
def check_almost_equivalent(word1, word2)
  freq = Array.new(26, 0)
  word1.length.times do |i|
    freq[word1[i].ord - 97] += 1
    freq[word2[i].ord - 97] -= 1
  end
  freq.all? { |v| v.between?(-3, 3) }
end
"""

files["2069_walking_robot_simulation_ii"] = hdr("2069", "Walking Robot Simulation II", "walking-robot-simulation-ii") + """class Robot
  def initialize(width, height)
    @w = width
    @h = height
    @peri = 2 * (width + height) - 4
    @pos = 0
    @moved = false
  end

  def step(num)
    @moved = true
    @pos = (@pos + num) % @peri
  end

  def get_pos
    pd = pos_dir
    [pd[0], pd[1]]
  end

  def get_dir
    %w[East North West South][pos_dir[2]]
  end

  private

  def pos_dir
    p = @pos
    return [0, 0, 0] if p.zero? && !@moved
    return [0, 0, 3] if p.zero?

    return [p, 0, 0] if p <= @w - 1

    p -= @w - 1
    return [@w - 1, p, 1] if p <= @h - 1

    p -= @h - 1
    return [@w - 1 - p, @h - 1, 2] if p <= @w - 1

    p -= @w - 1
    [0, @h - 1 - p, 3]
  end
end
"""

files["2070_most_beautiful_item_for_each_query"] = hdr("2070", "Most Beautiful Item for Each Query", "most-beautiful-item-for-each-query") + """# @param {Integer[][]} items
# @param {Integer[]} queries
# @return {Integer[]}
def maximum_beauty(items, queries)
  items.sort_by! { |it| it[0] }
  max_b = 0
  items.each do |it|
    max_b = [max_b, it[1]].max
    it[1] = max_b
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 0
    hi = items.length
    while lo < hi
      mid = (lo + hi) >> 1
      if items[mid][0] <= q
        lo = mid + 1
      else
        hi = mid
      end
    end
    ans[i] = lo.zero? ? 0 : items[lo - 1][1]
  end
  ans
end
"""

files["2071_maximum_number_of_tasks_you_can_assign"] = hdr("2071", "Maximum Number of Tasks You Can Assign", "maximum-number-of-tasks-you-can-assign") + """# @param {Integer[]} tasks
# @param {Integer[]} workers
# @param {Integer} pills
# @param {Integer} strength
# @return {Integer}
def max_task_assign(tasks, workers, pills, strength)
  tasks.sort!
  workers.sort!

  remove = lambda do |ws, x|
    ws[x] -= 1
    ws.delete(x) if ws[x].zero?
  end

  can = lambda do |k|
    return true if k.zero?

    ws = Hash.new(0)
    workers[workers.length - k..].each { |w| ws[w] += 1 }
    p = pills
    (k - 1).downto(0) do |i|
      task = tasks[i]
      ks = ws.keys.sort
      strongest = ks[-1]
      if strongest >= task
        remove.call(ws, strongest)
        next
      end
      return false if p.zero?

      need = task - strength
      found = ks.find { |key| key >= need }
      return false if found.nil?

      remove.call(ws, found)
      p -= 1
    end
    true
  end

  lo = 0
  hi = [tasks.length, workers.length].min
  while lo < hi
    mid = (lo + hi + 1) >> 1
    if can.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
"""

files["2073_time_needed_to_buy_tickets"] = hdr("2073", "Time Needed to Buy Tickets", "time-needed-to-buy-tickets") + """# @param {Integer[]} tickets
# @param {Integer} k
# @return {Integer}
def time_required_to_buy(tickets, k)
  ans = 0
  tickets.each_with_index do |t, i|
    ans += i <= k ? [t, tickets[k]].min : [t, tickets[k] - 1].min
  end
  ans
end
"""

files["2074_reverse_nodes_in_even_length_groups"] = hdr("2074", "Reverse Nodes in Even Length Groups", "reverse-nodes-in-even-length-groups") + LIST + """
# @param {ListNode} head
# @return {ListNode}
def reverse_even_length_groups(head)
  dummy = ListNode.new(0, head)
  prev = dummy
  group = 1
  while prev.next
    cur = prev.next
    cnt = 0
    node = cur
    while node && cnt < group
      node = node.next
      cnt += 1
    end
    if cnt.even?
      rev_prev = node
      p = cur
      cnt.times do
        nxt = p.next
        p.next = rev_prev
        rev_prev = p
        p = nxt
      end
      prev.next = rev_prev
      prev = cur
    else
      cnt.times { prev = prev.next }
    end
    group += 1
  end
  dummy.next
end
"""

files["2075_decode_the_slanted_ciphertext"] = hdr("2075", "Decode the Slanted Ciphertext", "decode-the-slanted-ciphertext") + """# @param {String} encoded_text
# @param {Integer} rows
# @return {String}
def decode_ciphertext(encoded_text, rows)
  return encoded_text if rows == 1

  cols = encoded_text.length / rows
  b = []
  cols.times do |c|
    rows.times do |r|
      break if c + r >= cols

      b << encoded_text[r * cols + c + r]
    end
  end
  b.pop while !b.empty? && b[-1] == " "
  b.join
end
"""

files["2076_process_restricted_friend_requests"] = hdr("2076", "Process Restricted Friend Requests", "process-restricted-friend-requests") + """# @param {Integer} n
# @param {Integer[][]} restrictions
# @param {Integer[][]} requests
# @return {Boolean[]}
def friend_requests(n, restrictions, requests)
  parent = (0...n).to_a
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    a = find.call(a)
    b = find.call(b)
    parent[a] = b if a != b
  end
  ans = Array.new(requests.length, false)
  requests.each_with_index do |(ru, rv), i|
    u = find.call(ru)
    v = find.call(rv)
    ok = true
    if u != v
      restrictions.each do |x0, y0|
        x = find.call(x0)
        y = find.call(y0)
        if (x == u && y == v) || (x == v && y == u)
          ok = false
          break
        end
      end
    end
    ans[i] = ok
    unite.call(u, v) if ok
  end
  ans
end
"""

files["2077_paths_in_maze_that_lead_to_same_room"] = hdr("2077", "Paths in Maze That Lead to Same Room", "paths-in-maze-that-lead-to-same-room") + """# @param {Integer} n
# @param {Integer[][]} corridors
# @return {Integer}
def number_of_paths(n, corridors)
  g = Array.new(n + 1) { {} }
  corridors.each do |a, b|
    g[a][b] = true
    g[b][a] = true
  end
  ans = 0
  corridors.each do |a, b|
    g[a].each_key { |c| ans += 1 if g[b][c] }
  end
  ans / 3
end
"""

files["2078_two_furthest_houses_with_different_colors"] = hdr("2078", "Two Furthest Houses With Different Colors", "two-furthest-houses-with-different-colors") + """# @param {Integer[]} colors
# @return {Integer}
def max_distance(colors)
  n = colors.length
  ans = 0
  colors.each_with_index do |c, i|
    ans = [ans, i].max if c != colors[0]
    ans = [ans, n - 1 - i].max if c != colors[n - 1]
  end
  ans
end
"""

files["2079_watering_plants"] = hdr("2079", "Watering Plants", "watering-plants") + """# @param {Integer[]} plants
# @param {Integer} capacity
# @return {Integer}
def watering_plants(plants, capacity)
  ans = 0
  cur = capacity
  plants.each_with_index do |p, i|
    if cur < p
      ans += i * 2
      cur = capacity
    end
    cur -= p
    ans += 1
  end
  ans
end
"""

files["2080_range_frequency_queries"] = hdr("2080", "Range Frequency Queries", "range-frequency-queries") + """class RangeFreqQuery
  def initialize(arr)
    @pos = {}
    arr.each_with_index do |v, i|
      (@pos[v] ||= []) << i
    end
  end

  def query(left, right, value)
    p = @pos[value]
    return 0 if p.nil?

    upper(p, right) - lower(p, left)
  end

  private

  def lower(p, x)
    lo = 0
    hi = p.length
    while lo < hi
      mid = (lo + hi) >> 1
      if p[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  def upper(p, x)
    lo = 0
    hi = p.length
    while lo < hi
      mid = (lo + hi) >> 1
      if p[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end
"""

files["2081_sum_of_k_mirror_numbers"] = hdr("2081", "Sum of k-Mirror Numbers", "sum-of-k-mirror-numbers") + """# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def k_mirror(k, n)
  is_pal_base = lambda do |x, bas|
    digits = []
    while x > 0
      digits << x % bas
      x /= bas
    end
    l = 0
    r = digits.length - 1
    while l < r
      return false if digits[l] != digits[r]

      l += 1
      r -= 1
    end
    true
  end

  ans = 0
  count = 0
  length = 1
  while count < n
    start = 1
    ((length + 1) / 2 - 1).times { start *= 10 }
    finish = start * 10
    half = start
    while half < finish && count < n
      pal = half
      if length.even?
        x = half
        while x > 0
          pal = pal * 10 + x % 10
          x /= 10
        end
      else
        x = half / 10
        while x > 0
          pal = pal * 10 + x % 10
          x /= 10
        end
      end
      if is_pal_base.call(pal, k)
        ans += pal
        count += 1
      end
      half += 1
    end
    length += 1
  end
  ans
end
"""

files["2083_substrings_that_begin_and_end_with_the_same_letter"] = hdr("2083", "Substrings That Begin and End With the Same Letter", "substrings-that-begin-and-end-with-the-same-letter") + """# @param {String} s
# @return {Integer}
def number_of_substrings(s)
  freq = Array.new(26, 0)
  ans = 0
  s.each_char do |c|
    i = c.ord - 97
    freq[i] += 1
    ans += freq[i]
  end
  ans
end
"""

files["2085_count_common_words_with_one_occurrence"] = hdr("2085", "Count Common Words With One Occurrence", "count-common-words-with-one-occurrence") + """# @param {String[]} words1
# @param {String[]} words2
# @return {Integer}
def count_words(words1, words2)
  f1 = Hash.new(0)
  f2 = Hash.new(0)
  words1.each { |w| f1[w] += 1 }
  words2.each { |w| f2[w] += 1 }
  f1.count { |k, v| v == 1 && f2[k] == 1 }
end
"""

files["2086_minimum_number_of_food_buckets_to_feed_the_hamsters"] = hdr("2086", "Minimum Number of Food Buckets to Feed the Hamsters", "minimum-number-of-food-buckets-to-feed-the-hamsters") + """# @param {String} hamsters
# @return {Integer}
def minimum_buckets(hamsters)
  b = hamsters.chars
  ans = 0
  b.each_index do |i|
    next unless b[i] == "H"
    next if i > 0 && b[i - 1] == "B"

    if i + 1 < b.length && b[i + 1] == "."
      b[i + 1] = "B"
      ans += 1
    elsif i > 0 && b[i - 1] == "."
      b[i - 1] = "B"
      ans += 1
    else
      return -1
    end
  end
  ans
end
"""

files["2087_minimum_cost_homecoming_of_a_robot_in_a_grid"] = hdr("2087", "Minimum Cost Homecoming of a Robot in a Grid", "minimum-cost-homecoming-of-a-robot-in-a-grid") + """# @param {Integer[]} start_pos
# @param {Integer[]} home_pos
# @param {Integer[]} row_costs
# @param {Integer[]} col_costs
# @return {Integer}
def min_cost(start_pos, home_pos, row_costs, col_costs)
  ans = 0
  sr, sc = start_pos
  hr, hc = home_pos
  if sr < hr
    (sr + 1).upto(hr) { |r| ans += row_costs[r] }
  else
    (sr - 1).downto(hr) { |r| ans += row_costs[r] }
  end
  if sc < hc
    (sc + 1).upto(hc) { |c| ans += col_costs[c] }
  else
    (sc - 1).downto(hc) { |c| ans += col_costs[c] }
  end
  ans
end
"""

files["2088_count_fertile_pyramids_in_a_land"] = hdr("2088", "Count Fertile Pyramids in a Land", "count-fertile-pyramids-in-a-land") + """# @param {Integer[][]} grid
# @return {Integer}
def count_pyramids(grid)
  count = lambda do |g|
    m = g.length
    n = g[0].length
    dp = g.map(&:dup)
    ans = 0
    (m - 2).downto(0) do |i|
      (1...n - 1).each do |j|
        next unless g[i][j] == 1

        dp[i][j] = 1 + [dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]].min
        ans += dp[i][j] - 1
      end
    end
    ans
  end
  count.call(grid) + count.call(grid.reverse)
end
"""

files["2089_find_target_indices_after_sorting_array"] = hdr("2089", "Find Target Indices After Sorting Array", "find-target-indices-after-sorting-array") + """# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def target_indices(nums, target)
  less = eq = 0
  nums.each do |x|
    if x < target
      less += 1
    elsif x == target
      eq += 1
    end
  end
  (0...eq).map { |i| less + i }
end
"""

written = 0
for folder, content in files.items():
    (root / folder / "solution.rb").write_bytes(content.encode("utf-8"))
    written += 1
print(f"wrote {written}")
