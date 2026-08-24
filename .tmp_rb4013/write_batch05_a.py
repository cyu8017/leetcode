#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2090_k_radius_subarray_averages", r'''
# LeetCode 2090 - K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def get_averages(nums, k)
  n = nums.length
  ans = Array.new(n, -1)
  return ans if 2 * k + 1 > n

  window = 2 * k + 1
  s = nums[0...window].sum
  ans[k] = s / window
  (k + 1).upto(n - k - 1) do |i|
    s += nums[i + k] - nums[i - k - 1]
    ans[i] = s / window
  end
  ans
end
''')

add("2091_removing_minimum_and_maximum_from_array", r'''
# LeetCode 2091 - Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_deletions(nums)
  n = nums.length
  mi = ma = 0
  nums.each_with_index do |x, i|
    mi = i if x < nums[mi]
    ma = i if x > nums[ma]
  end
  mi, ma = ma, mi if mi > ma
  [ma + 1, n - mi, mi + 1 + n - ma].min
end
''')

add("2092_find_all_people_with_secret", r'''
# LeetCode 2092 - Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/

# @param {Integer} n
# @param {Integer[][]} meetings
# @param {Integer} first_person
# @return {Integer[]}
def find_all_people(n, meetings, first_person)
  meetings.sort_by! { |m| m[2] }
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

  know = Array.new(n, false)
  know[0] = know[first_person] = true
  unite.call(0, first_person)
  i = 0
  while i < meetings.length
    j = i
    j += 1 while j < meetings.length && meetings[j][2] == meetings[i][2]
    (i...j).each { |k| unite.call(meetings[k][0], meetings[k][1]) }
    root0 = find.call(0)
    reset = []
    (i...j).each do |k|
      a = meetings[k][0]
      b = meetings[k][1]
      if find.call(a) != root0
        reset << a
        reset << b
      else
        know[a] = know[b] = true
      end
    end
    reset.each { |x| parent[x] = x }
    i = j
  end
  (0...n).select { |x| find.call(x) == find.call(0) || know[x] }
end
''')

add("2093_minimum_cost_to_reach_city_with_discounts", r'''
# LeetCode 2093 - Minimum Cost to Reach City With Discounts
# https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

class _MinHeap2093
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i > 0
      p = (i - 1) / 2
      break if @a[p] <= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    n = @a.length
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= n

      smallest = r < n && @a[r] < @a[l] ? r : l
      break if @a[i] <= @a[smallest]

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer} n
# @param {Integer[][]} highways
# @param {Integer} discounts
# @return {Integer}
def minimum_cost(n, highways, discounts)
  g = Array.new(n) { [] }
  highways.each do |a, b, c|
    g[a] << [b, c]
    g[b] << [a, c]
  end
  inf = 1 << 30
  dist = Array.new(n) { Array.new(discounts + 1, inf) }
  dist[0][discounts] = 0
  pq = _MinHeap2093.new
  pq.push([0, 0, discounts])
  until pq.empty?
    cost, city, disc = pq.pop
    return cost if city == n - 1
    next if cost > dist[city][disc]

    g[city].each do |v, w|
      if cost + w < dist[v][disc]
        dist[v][disc] = cost + w
        pq.push([dist[v][disc], v, disc])
      end
      if disc > 0 && cost + w / 2 < dist[v][disc - 1]
        dist[v][disc - 1] = cost + w / 2
        pq.push([dist[v][disc - 1], v, disc - 1])
      end
    end
  end
  -1
end
''')

add("2094_finding_3_digit_even_numbers", r'''
# LeetCode 2094 - Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

# @param {Integer[]} digits
# @return {Integer[]}
def find_even_numbers(digits)
  freq = Array.new(10, 0)
  digits.each { |d| freq[d] += 1 }
  ans = []
  100.step(998, 2) do |x|
    a = x / 100
    b = (x / 10) % 10
    c = x % 10
    freq[a] -= 1
    freq[b] -= 1
    freq[c] -= 1
    ans << x if freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0
    freq[a] += 1
    freq[b] += 1
    freq[c] += 1
  end
  ans
end
''')

add("2095_delete_the_middle_node_of_a_linked_list", r'''
# LeetCode 2095 - Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def delete_middle(head)
  return nil if head.next.nil?

  slow = head
  fast = head
  prev = nil
  while fast && fast.next
    prev = slow
    slow = slow.next
    fast = fast.next.next
  end
  prev.next = slow.next
  head
end
''')

add("2096_step_by_step_directions_from_a_binary_tree_node_to_another", r'''
# LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} start_value
# @param {Integer} dest_value
# @return {String}
def get_directions(root, start_value, dest_value)
  path = lambda do |node, target, p|
    return false if node.nil?
    return true if node.val == target

    p << "L"
    return true if path.call(node.left, target, p)

    p[-1] = "R"
    return true if path.call(node.right, target, p)

    p.pop
    false
  end

  ps = []
  pd = []
  path.call(root, start_value, ps)
  path.call(root, dest_value, pd)
  i = 0
  i += 1 while i < ps.length && i < pd.length && ps[i] == pd[i]
  ("U" * (ps.length - i)) + pd[i..].join
end
''')

add("2097_valid_arrangement_of_pairs", r'''
# LeetCode 2097 - Valid Arrangement of Pairs
# https://leetcode.com/problems/valid-arrangement-of-pairs/

# @param {Integer[][]} pairs
# @return {Integer[][]}
def valid_arrangement(pairs)
  g = Hash.new { |h, k| h[k] = [] }
  indeg = Hash.new(0)
  outdeg = Hash.new(0)
  pairs.each do |u, v|
    g[u] << v
    outdeg[u] += 1
    indeg[v] += 1
  end
  start = pairs[0][0]
  outdeg.each do |u, o|
    if o - indeg[u] == 1
      start = u
      break
    end
  end
  path = []
  dfs = lambda do |u|
    nbrs = g[u]
    dfs.call(nbrs.pop) until nbrs.empty?
    path << u
  end
  dfs.call(start)
  path.reverse!
  (0...path.length - 1).map { |i| [path[i], path[i + 1]] }
end
''')

add("2098_subsequence_of_size_k_with_the_largest_even_sum", r'''
# LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
# https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_even_sum(nums, k)
  arr = nums.sort.reverse
  s = arr[0...k].sum
  return s if s.even?

  ans = -1
  odd_in = even_in = odd_out = even_out = -1
  (k - 1).downto(0) do |i|
    odd_in = i if arr[i].odd? && odd_in == -1
    even_in = i if arr[i].even? && even_in == -1
  end
  (k...arr.length).each do |i|
    odd_out = i if arr[i].odd? && odd_out == -1
    even_out = i if arr[i].even? && even_out == -1
  end
  ans = [ans, s - arr[odd_in] + arr[even_out]].max if odd_in != -1 && even_out != -1
  ans = [ans, s - arr[even_in] + arr[odd_out]].max if even_in != -1 && odd_out != -1
  ans
end
''')

add("2099_find_subsequence_of_length_k_with_the_largest_sum", r'''
# LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_subsequence(nums, k)
  arr = nums.each_with_index.map { |v, i| [v, i] }
  arr.sort_by! { |v, _| -v }
  idx = arr[0...k].map { |_, i| i }.sort
  idx.map { |i| nums[i] }
end
''')

add("2100_find_good_days_to_rob_the_bank", r'''
# LeetCode 2100 - Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

# @param {Integer[]} security
# @param {Integer} time
# @return {Integer[]}
def good_days_to_rob_bank(security, time)
  n = security.length
  return (0...n).to_a if time == 0

  left = Array.new(n, 0)
  right = Array.new(n, 0)
  (1...n).each { |i| left[i] = left[i - 1] + 1 if security[i] <= security[i - 1] }
  (n - 2).downto(0) { |i| right[i] = right[i + 1] + 1 if security[i] <= security[i + 1] }
  (time...n - time).select { |i| left[i] >= time && right[i] >= time }
end
''')

add("2101_detonate_the_maximum_bombs", r'''
# LeetCode 2101 - Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/

# @param {Integer[][]} bombs
# @return {Integer}
def maximum_detonation(bombs)
  n = bombs.length
  g = Array.new(n) { [] }
  n.times do |i|
    x1, y1, r1 = bombs[i]
    n.times do |j|
      next if i == j

      dx = bombs[j][0] - x1
      dy = bombs[j][1] - y1
      g[i] << j if dx * dx + dy * dy <= r1 * r1
    end
  end
  ans = 0
  n.times do |i|
    vis = Array.new(n, false)
    q = [i]
    vis[i] = true
    cnt = 0
    until q.empty?
      u = q.shift
      cnt += 1
      g[u].each do |v|
        unless vis[v]
          vis[v] = true
          q << v
        end
      end
    end
    ans = [ans, cnt].max
  end
  ans
end
''')

add("2102_sequentially_ordinal_rank_tracker", r'''
# LeetCode 2102 - Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class _HeapItem2102
  include Comparable
  attr_reader :score, :name

  def initialize(score, name)
    @score = score
    @name = name
  end

  def <=>(other)
    if @score != other.score
      @score <=> other.score
    else
      other.name <=> @name
    end
  end
end

class _MinHeap2102
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def size
    @a.length
  end

  def peek
    @a[0]
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i > 0
      p = (i - 1) / 2
      break if @a[p] <= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    n = @a.length
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= n

      smallest = r < n && @a[r] < @a[l] ? r : l
      break if @a[i] <= @a[smallest]

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

class SORTracker
  def initialize
    @best = _MinHeap2102.new
    @rest = _MinHeap2102.new
    @k = 0
  end

  def add(name, score)
    @best.push(_HeapItem2102.new(score, name))
    if @best.size > @k
      item = @best.pop
      @rest.push([-item.score, item.name])
    end
  end

  def get
    @k += 1
    unless @rest.empty?
      sc, nm = @rest.pop
      @best.push(_HeapItem2102.new(-sc, nm))
    end
    @best.peek.name
  end
end
''')

add("2103_rings_and_rods", r'''
# LeetCode 2103 - Rings and Rods
# https://leetcode.com/problems/rings-and-rods/

# @param {String} rings
# @return {Integer}
def count_points(rings)
  mask = Array.new(10, 0)
  0.step(rings.length - 1, 2) do |i|
    c = rings[i]
    r = rings[i + 1].ord - 48
    bit = c == "R" ? 1 : c == "G" ? 2 : 4
    mask[r] |= bit
  end
  mask.count { |m| m == 7 }
end
''')

add("2104_sum_of_subarray_ranges", r'''
# LeetCode 2104 - Sum of Subarray Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/

# @param {Integer[]} nums
# @return {Integer}
def sub_array_ranges(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    mn = mx = nums[i]
    (i...n).each do |j|
      mn = [mn, nums[j]].min
      mx = [mx, nums[j]].max
      ans += mx - mn
    end
  end
  ans
end
''')

add("2105_watering_plants_ii", r'''
# LeetCode 2105 - Watering Plants II
# https://leetcode.com/problems/watering-plants-ii/

# @param {Integer[]} plants
# @param {Integer} capacity_a
# @param {Integer} capacity_b
# @return {Integer}
def minimum_refill(plants, capacity_a, capacity_b)
  i = 0
  j = plants.length - 1
  a = capacity_a
  b = capacity_b
  ans = 0
  while i < j
    if a < plants[i]
      ans += 1
      a = capacity_a
    end
    a -= plants[i]
    i += 1
    if b < plants[j]
      ans += 1
      b = capacity_b
    end
    b -= plants[j]
    j -= 1
  end
  if i == j
    if a >= b
      ans += 1 if a < plants[i]
    elsif b < plants[i]
      ans += 1
    end
  end
  ans
end
''')

add("2106_maximum_fruits_harvested_after_at_most_k_steps", r'''
# LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

# @param {Integer[][]} fruits
# @param {Integer} start_pos
# @param {Integer} k
# @return {Integer}
def max_total_fruits(fruits, start_pos, k)
  min_steps = lambda do |left, right, start|
    return start - left if right <= start
    return right - start if left >= start

    [(start - left) + (right - left), (right - start) + (right - left)].min
  end

  n = fruits.length
  pref = Array.new(n + 1, 0)
  pos = Array.new(n, 0)
  fruits.each_with_index do |(p, amt), i|
    pos[i] = p
    pref[i + 1] = pref[i] + amt
  end
  ans = 0
  j = 0
  n.times do |i|
    j += 1 while j < n && min_steps.call(pos[i], pos[j], start_pos) > k
    ans = [ans, pref[i + 1] - pref[j]].max if j <= i
  end
  j = 0
  n.times do |i|
    j += 1 while j <= i && min_steps.call(pos[j], pos[i], start_pos) > k
    ans = [ans, pref[i + 1] - pref[j]].max
  end
  ans
end
''')

add("2107_number_of_unique_flavors_after_sharing_k_candies", r'''
# LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

# @param {Integer[]} candies
# @param {Integer} k
# @return {Integer}
def share_candies(candies, k)
  n = candies.length
  freq = Hash.new(0)
  candies.each { |c| freq[c] += 1 }
  return freq.length if k == 0

  k.times do |i|
    c = candies[i]
    freq[c] -= 1
    freq.delete(c) if freq[c] == 0
  end
  ans = freq.length
  (k...n).each do |i|
    freq[candies[i - k]] += 1
    c = candies[i]
    freq[c] -= 1
    freq.delete(c) if freq[c] == 0
    ans = [ans, freq.length].max
  end
  ans
end
''')

add("2108_find_first_palindromic_string_in_the_array", r'''
# LeetCode 2108 - Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# @param {String[]} words
# @return {String}
def first_palindrome(words)
  words.each { |w| return w if w == w.reverse }
  ""
end
''')

add("2109_adding_spaces_to_a_string", r'''
# LeetCode 2109 - Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

# @param {String} s
# @param {Integer[]} spaces
# @return {String}
def add_spaces(s, spaces)
  b = []
  j = 0
  s.chars.each_with_index do |ch, i|
    if j < spaces.length && spaces[j] == i
      b << " "
      j += 1
    end
    b << ch
  end
  b.join
end
''')

add("2110_number_of_smooth_descent_periods_of_a_stock", r'''
# LeetCode 2110 - Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

# @param {Integer[]} prices
# @return {Integer}
def get_descent_periods(prices)
  ans = cur = 1
  (1...prices.length).each do |i|
    cur = prices[i] == prices[i - 1] - 1 ? cur + 1 : 1
    ans += cur
  end
  ans
end
''')

add("2111_minimum_operations_to_make_the_array_k_increasing", r'''
# LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def k_increasing(arr, k)
  ans = 0
  n = arr.length
  k.times do |start|
    seq = []
    start.step(n - 1, k) { |i| seq << arr[i] }
    tails = []
    seq.each do |x|
      lo = 0
      hi = tails.length
      while lo < hi
        mid = (lo + hi) >> 1
        if tails[mid] <= x
          lo = mid + 1
        else
          hi = mid
        end
      end
      if lo == tails.length
        tails << x
      else
        tails[lo] = x
      end
    end
    ans += seq.length - tails.length
  end
  ans
end
''')

add("2113_elements_in_array_after_removing_and_replacing_elements", r'''
# LeetCode 2113 - Elements in Array After Removing and Replacing Elements
# https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def element_in_nums(nums, queries)
  n = nums.length
  queries.map do |t, idx|
    cycle = t % (2 * n)
    if cycle < n
      size = n - cycle
      offset = cycle
    else
      size = cycle - n
      offset = 0
    end
    idx >= size ? -1 : nums[offset + idx]
  end
end
''')

add("2114_maximum_number_of_words_found_in_sentences", r'''
# LeetCode 2114 - Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# @param {String[]} sentences
# @return {Integer}
def most_words_found(sentences)
  sentences.map { |s| s.count(" ") + 1 }.max
end
''')

written = 0
for folder, body in S.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
