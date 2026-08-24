#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3049_earliest_second_to_mark_indices_ii", r'''
# LeetCode 3049 - Earliest Second to Mark Indices II
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

# @param {Integer[]} nums
# @param {Integer[]} change_indices
# @return {Integer}
def earliest_second_to_mark_indices(nums, change_indices)
  second_to_index = get_second_to_index(nums, change_indices)
  nums_sum = nums.sum
  l = 0
  r = change_indices.length + 1
  while l < r
    m = (l + r) / 2
    if can_mark(nums, second_to_index, m, nums_sum)
      r = m
    else
      l = m + 1
    end
  end
  l <= change_indices.length ? l : -1
end

def get_second_to_index(nums, change_indices)
  index_to_first_second = {}
  change_indices.each_with_index do |ci, second|
    index = ci - 1
    if nums[index] > 0 && !index_to_first_second.key?(index)
      index_to_first_second[index] = second
    end
  end
  second_to_index = {}
  index_to_first_second.each { |idx, sec| second_to_index[sec] = idx }
  second_to_index
end

def can_mark(nums, second_to_index, max_second, nums_sum)
  h = []
  marks = 0
  (max_second - 1).downto(0) do |second|
    if second_to_index.key?(second)
      heap_push(h, nums[second_to_index[second]])
      if marks == 0
        heap_pop(h)
        marks += 1
      else
        marks -= 1
      end
    else
      marks += 1
    end
  end
  heap_size = h.length
  heap_sum = 0
  heap_sum += heap_pop(h) while h.length > 0
  decrement_and_mark_cost = nums_sum - heap_sum + (nums.length - heap_size)
  zero_and_mark_cost = heap_size + heap_size
  decrement_and_mark_cost + zero_and_mark_cost <= max_second
end

def heap_push(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] < a[s]
      s = r if r < n && a[r] < a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end
''')

add("3062_winner_of_the_linked_list_game", r'''
# LeetCode 3062 - Winner of the Linked List Game
# https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {String}
def game_result(head)
  odd = 0
  even = 0
  while head
    a = head.val
    b = head.next.val
    odd += 1 if a < b
    even += 1 if a > b
    head = head.next.next
  end
  return "Odd" if odd > even
  return "Even" if odd < even
  "Tie"
end
''')

add("3063_linked_list_frequency", r'''
# LeetCode 3063 - Linked List Frequency
# https://leetcode.com/problems/linked-list-frequency/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def frequencies_of_elements(head)
  cnt = Hash.new(0)
  while head
    cnt[head.val] += 1
    head = head.next
  end
  dummy = ListNode.new(0)
  cnt.each_value do |val|
    dummy.next = ListNode.new(val, dummy.next)
  end
  dummy.next
end
''')

add("3064_guess_the_number_using_bitwise_questions_i", r'''
# LeetCode 3064 - Guess the Number Using Bitwise Questions I
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

# The commonSetBits API is provided by the judge.

# @return {Integer}
def find_number
  n = 0
  32.times do |i|
    n |= 1 << i if common_set_bits(1 << i) > 0
  end
  n
end
''')

add("3065_minimum_operations_to_exceed_threshold_value_i", r'''
# LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  nums.count { |x| x < k }
end
''')

add("3066_minimum_operations_to_exceed_threshold_value_ii", r'''
# LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  pq = []
  nums.each { |x| heap_push(pq, x) }
  ans = 0
  while pq.length > 1 && pq[0] < k
    x = heap_pop(pq)
    y = heap_pop(pq)
    heap_push(pq, x * 2 + y)
    ans += 1
  end
  ans
end

def heap_push(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] < a[s]
      s = r if r < n && a[r] < a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end
''')

add("3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network", r'''
# LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

# @param {Integer[][]} edges
# @param {Integer} signal_speed
# @return {Integer[]}
def count_pairs_of_connectable_servers(edges, signal_speed)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end

  dfs = lambda do |a, fa, ws|
    cnt = ws % signal_speed == 0 ? 1 : 0
    g[a].each do |b, w|
      cnt += dfs.call(b, a, ws + w) if b != fa
    end
    cnt
  end

  ans = Array.new(n, 0)
  n.times do |a|
    s = 0
    g[a].each do |b, w|
      t = dfs.call(b, a, w)
      ans[a] += s * t
      s += t
    end
  end
  ans
end
''')

add("3068_find_the_maximum_sum_of_node_values", r'''
# LeetCode 3068 - Find the Maximum Sum of Node Values
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer[][]} edges
# @return {Integer}
def maximum_value_sum(nums, k, edges)
  f0 = 0
  f1 = -(1 << 53)
  nums.each do |x|
    nf0 = [f0 + x, f1 + (x ^ k)].max
    nf1 = [f1 + x, f0 + (x ^ k)].max
    f0 = nf0
    f1 = nf1
  end
  f0
end
''')

add("3069_distribute_elements_into_two_arrays_i", r'''
# LeetCode 3069 - Distribute Elements Into Two Arrays I
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

# @param {Integer[]} nums
# @return {Integer[]}
def result_array(nums)
  arr1 = [nums[0]]
  arr2 = [nums[1]]
  (2...nums.length).each do |i|
    if arr1[-1] > arr2[-1]
      arr1 << nums[i]
    else
      arr2 << nums[i]
    end
  end
  arr1 + arr2
end
''')

add("3070_count_submatrices_with_top_left_element_and_sum_less_than_k", r'''
# LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_submatrices(grid, k)
  n = grid.length
  m = grid[0].length
  ans = 0
  s = Array.new(n + 1) { Array.new(m + 1, 0) }
  n.times do |i|
    m.times do |j|
      s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]
      ans += 1 if s[i + 1][j + 1] <= k
    end
  end
  ans
end
''')

add("3071_minimum_operations_to_write_the_letter_y_on_a_grid", r'''
# LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations_to_write_y(grid)
  n = grid.length
  cnt1 = [0, 0, 0]
  cnt2 = [0, 0, 0]
  n.times do |i|
    n.times do |j|
      x = grid[i][j]
      a = i == j && i <= n / 2
      b = i + j == n - 1 && i <= n / 2
      c = j == n / 2 && i >= n / 2
      if a || b || c
        cnt1[x] += 1
      else
        cnt2[x] += 1
      end
    end
  end
  ans = n * n
  3.times do |i|
    3.times do |j|
      ans = [ans, n * n - cnt1[i] - cnt2[j]].min if i != j
    end
  end
  ans
end
''')

add("3072_distribute_elements_into_two_arrays_ii", r'''
# LeetCode 3072 - Distribute Elements Into Two Arrays II
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

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
# @return {Integer[]}
def result_array(nums)
  st = nums.sort
  n = st.length
  tree1 = BIT.new(n + 1)
  tree2 = BIT.new(n + 1)

  idx = lambda do |x|
    lo = 0
    hi = st.length
    while lo < hi
      mid = (lo + hi) / 2
      if st[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  arr1 = [nums[0]]
  arr2 = [nums[1]]
  tree1.update(idx.call(nums[0]), 1)
  tree2.update(idx.call(nums[1]), 1)
  (2...nums.length).each do |i|
    x = nums[i]
    id = idx.call(x)
    a = arr1.length - tree1.query(id)
    b = arr2.length - tree2.query(id)
    if a > b || (a == b && arr1.length <= arr2.length)
      arr1 << x
      tree1.update(id, 1)
    else
      arr2 << x
      tree2.update(id, 1)
    end
  end
  arr1 + arr2
end
''')

add("3073_maximum_increasing_triplet_value", r'''
# LeetCode 3073 - Maximum Increasing Triplet Value
# https://leetcode.com/problems/maximum-increasing-triplet-value/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [nums[i], right[i + 1]].max }
  ts = []

  add = lambda do |x|
    lo = 0
    hi = ts.length
    while lo < hi
      mid = (lo + hi) >> 1
      if ts[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    ts.insert(lo, x) if lo == ts.length || ts[lo] != x
  end

  lower = lambda do |x|
    lo = 0
    hi = ts.length
    while lo < hi
      mid = (lo + hi) >> 1
      if ts[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo > 0 ? ts[lo - 1] : nil
  end

  add.call(nums[0])
  ans = 0
  (1...n - 1).each do |j|
    if right[j + 1] > nums[j]
      it = lower.call(nums[j])
      ans = [ans, it - nums[j] + right[j + 1]].max if it
    end
    add.call(nums[j])
  end
  ans
end
''')

add("3074_apple_redistribution_into_boxes", r'''
# LeetCode 3074 - Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/

# @param {Integer[]} apple
# @param {Integer[]} capacity
# @return {Integer}
def minimum_boxes(apple, capacity)
  capacity.sort!
  s = apple.sum
  i = 1
  loop do
    s -= capacity[capacity.length - i]
    return i if s <= 0
    i += 1
  end
end
''')

add("3075_maximize_happiness_of_selected_children", r'''
# LeetCode 3075 - Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/

# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
  happiness.sort!
  ans = 0
  k.times do |i|
    x = happiness[happiness.length - i - 1] - i
    ans += [x, 0].max
  end
  ans
end
''')

add("3076_shortest_uncommon_substring_in_an_array", r'''
# LeetCode 3076 - Shortest Uncommon Substring in an Array
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

# @param {String[]} arr
# @return {String[]}
def shortest_substrings(arr)
  n = arr.length
  ans = Array.new(n, "")
  n.times do |i|
    s = arr[i]
    m = s.length
    j = 1
    while j <= m && ans[i] == ""
      (0..m - j).each do |l|
        sub = s[l, j]
        if ans[i] == "" || ans[i] > sub
          ok = true
          n.times do |k|
            if k != i && arr[k].include?(sub)
              ok = false
              break
            end
          end
          ans[i] = sub if ok
        end
      end
      j += 1
    end
  end
  ans
end
''')

add("3077_maximum_strength_of_k_disjoint_subarrays", r'''
# LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_strength(nums, k)
  n = nums.length
  inf = -(1 << 53) / 2
  f = Array.new(n + 1) { Array.new(k + 1) { [inf, inf] } }
  f[0][0][0] = 0
  (1..n).each do |i|
    x = nums[i - 1]
    (0..k).each do |j|
      sign = (j & 1) != 0 ? 1 : -1
      val = sign * x * (k - j + 1)
      f[i][j][0] = [f[i - 1][j][0], f[i - 1][j][1]].max
      f[i][j][1] = [f[i][j][1], f[i - 1][j][1] + val].max
      if j > 0
        t = [f[i - 1][j - 1][0], f[i - 1][j - 1][1]].max + val
        f[i][j][1] = [f[i][j][1], t].max
      end
    end
  end
  [f[n][k][0], f[n][k][1]].max
end
''')

add("3078_match_alphanumerical_pattern_in_matrix_i", r'''
# LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
# https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

# @param {Integer[][]} board
# @param {String[]} pattern
# @return {Integer[]}
def find_pattern(board, pattern)
  m = board.length
  n = board[0].length
  r = pattern.length
  c = pattern[0].length

  check = lambda do |i, j|
    d1 = Array.new(26, 0)
    d2 = Array.new(10, 0)
    r.times do |a|
      c.times do |b|
        x = i + a
        y = j + b
        ch = pattern[a][b]
        if ch >= "0" && ch <= "9"
          return false if ch.ord - 48 != board[x][y]
        else
          v = ch.ord - 97
          return false if d1[v] > 0 && d1[v] - 1 != board[x][y]
          return false if d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v
          d1[v] = board[x][y] + 1
          d2[board[x][y]] = v + 1
        end
      end
    end
    true
  end

  (0..m - r).each do |i|
    (0..n - c).each do |j|
      return [i, j] if check.call(i, j)
    end
  end
  [-1, -1]
end
''')

add("3079_find_the_sum_of_encrypted_integers", r'''
# LeetCode 3079 - Find the Sum of Encrypted Integers
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_encrypted_int(nums)
  encrypt = lambda do |x|
    mx = 0
    p = 0
    while x > 0
      mx = [mx, x % 10].max
      p = p * 10 + 1
      x /= 10
    end
    mx * p
  end
  nums.sum { |x| encrypt.call(x) }
end
''')

add("3080_mark_elements_on_array_by_performing_queries", r'''
# LeetCode 3080 - Mark Elements on Array by Performing Queries
# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def unmarked_sum_array(nums, queries)
  n = nums.length
  s = nums.sum
  mark = Array.new(n, false)
  arr = nums.each_with_index.map { |v, i| [v, i] }
  arr.sort_by! { |a| [a[0], a[1]] }
  ans = Array.new(queries.length, 0)
  j = 0
  queries.each_with_index do |q, qi|
    index = q[0]
    k = q[1]
    unless mark[index]
      mark[index] = true
      s -= nums[index]
    end
    while k > 0 && j < n
      unless mark[arr[j][1]]
        mark[arr[j][1]] = true
        s -= arr[j][0]
        k -= 1
      end
      j += 1
    end
    ans[qi] = s
  end
  ans
end
''')

add("3081_replace_question_marks_in_string_to_minimize_its_value", r'''
# LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

# @param {String} s
# @return {String}
def minimize_string_value(s)
  cnt = Array.new(26, 0)
  k = 0
  s.each_char do |c|
    if c == "?"
      k += 1
    else
      cnt[c.ord - 97] += 1
    end
  end
  pq = []
  26.times { |i| heap_push_pair(pq, [cnt[i], i]) }
  t = Array.new(k, 0)
  k.times do |i|
    p = heap_pop_pair(pq)
    t[i] = p[1]
    p[0] += 1
    heap_push_pair(pq, p)
  end
  t.sort!
  arr = s.chars
  j = 0
  arr.each_index do |i|
    if arr[i] == "?"
      arr[i] = (t[j] + 97).chr
      j += 1
    end
  end
  arr.join
end

def heap_push_pair(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if cmp_pair(a[i], a[p]) >= 0
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_pair(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp_pair(a[l], a[s]) < 0
      s = r if r < n && cmp_pair(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end

def cmp_pair(a, b)
  a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
end
''')

add("3082_find_the_sum_of_the_power_of_all_subsequences", r'''
# LeetCode 3082 - Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_power(nums, k)
  mod = 1_000_000_007
  n = nums.length
  f = Array.new(n + 1) { Array.new(k + 1, 0) }
  f[0][0] = 1
  (1..n).each do |i|
    (0..k).each do |j|
      f[i][j] = (f[i - 1][j] * 2) % mod
      f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % mod if j >= nums[i - 1]
    end
  end
  f[n][k]
end
''')

add("3083_existence_of_a_substring_in_a_string_and_its_reverse", r'''
# LeetCode 3083 - Existence of a Substring in a String and Its Reverse
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

# @param {String} s
# @return {Boolean}
def is_substring_present(s)
  st = Array.new(26) { Array.new(26, false) }
  (0...s.length - 1).each do |i|
    st[s[i + 1].ord - 97][s[i].ord - 97] = true
  end
  (0...s.length - 1).each do |i|
    return true if st[s[i].ord - 97][s[i + 1].ord - 97]
  end
  false
end
''')

add("3084_count_substrings_starting_and_ending_with_given_character", r'''
# LeetCode 3084 - Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

# @param {String} s
# @param {String} c
# @return {Integer}
def count_substrings(s, c)
  cnt = s.chars.count { |ch| ch == c }
  cnt * (cnt + 1) / 2
end
''')

add("3085_minimum_deletions_to_make_string_k_special", r'''
# LeetCode 3085 - Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_deletions(word, k)
  freq = Array.new(26, 0)
  word.each_char { |ch| freq[ch.ord - 97] += 1 }
  nums = freq.select { |v| v > 0 }
  ans = word.length
  (0..word.length).each do |i|
    cur = 0
    nums.each do |x|
      if x < i
        cur += x
      elsif x > i + k
        cur += x - i - k
      end
    end
    ans = [ans, cur].min
  end
  ans
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        written += 1
        print(f"wrote {name}")
    print(f"batch_a written={written}")


if __name__ == "__main__":
    main()
