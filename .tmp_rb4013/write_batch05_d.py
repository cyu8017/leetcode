#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2166_design_bitset", r'''
# LeetCode 2166 - Design Bitset
# https://leetcode.com/problems/design-bitset/

class Bitset
  def initialize(size)
    @size = size
    @bits = Array.new(size, 0)
    @ones = 0
    @flipped = false
  end

  def fix(idx)
    target = @flipped ? 0 : 1
    if @bits[idx] != target
      @bits[idx] = target
      @ones += 1
    end
  end

  def unfix(idx)
    target = @flipped ? 1 : 0
    if @bits[idx] != target
      @bits[idx] = target
      @ones -= 1
    end
  end

  def flip
    @flipped = !@flipped
    @ones = @size - @ones
  end

  def all
    @ones == @size
  end

  def one
    @ones > 0
  end

  def count
    @ones
  end

  def to_string
    b = Array.new(@size)
    @size.times do |i|
      v = @bits[i]
      v ^= 1 if @flipped
      b[i] = v.to_s
    end
    b.join
  end
  alias toString to_string
end
''')

add("2167_minimum_time_to_remove_all_cars_containing_illegal_goods", r'''
# LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

# @param {String} s
# @return {Integer}
def minimum_time(s)
  n = s.length
  left = Array.new(n, 0)
  left[0] = 1 if s[0] == "1"
  (1...n).each do |i|
    left[i] = left[i - 1]
    left[i] = [i + 1, left[i - 1] + 2].min if s[i] == "1"
  end
  ans = left[n - 1]
  right = 0
  (n - 1).downto(0) do |i|
    right = [n - i, right + 2].min if s[i] == "1"
    left_cost = i > 0 ? left[i - 1] : 0
    ans = [ans, left_cost + right].min
  end
  ans
end
''')

add("2168_unique_substrings_with_equal_digit_frequency", r'''
# LeetCode 2168 - Unique Substrings With Equal Digit Frequency
# https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

# @param {String} s
# @return {Integer}
def equal_digit_frequency(s)
  n = s.length
  seen = {}
  n.times do |i|
    freq = Array.new(10, 0)
    maxf = 0
    kinds = 0
    (i...n).each do |j|
      d = s[j].ord - 48
      kinds += 1 if freq[d] == 0
      freq[d] += 1
      maxf = [maxf, freq[d]].max
      seen[s[i..j]] = true if maxf * kinds == j - i + 1
    end
  end
  seen.length
end
''')

add("2169_count_operations_to_obtain_zero", r'''
# LeetCode 2169 - Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def count_operations(num1, num2)
  ans = 0
  while num1 > 0 && num2 > 0
    if num1 >= num2
      ans += num1 / num2
      num1 %= num2
    else
      ans += num2 / num1
      num2 %= num1
    end
  end
  ans
end
''')

add("2170_minimum_operations_to_make_the_array_alternating", r'''
# LeetCode 2170 - Minimum Operations to Make the Array Alternating
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  n = nums.length
  return 0 if n == 1

  top2 = lambda do |idxs|
    freq = Hash.new(0)
    idxs.each { |i| freq[nums[i]] += 1 }
    a = ac = b = bc = 0
    freq.each do |v, c|
      if c > ac
        b = a
        bc = ac
        a = v
        ac = c
      elsif c > bc
        b = v
        bc = c
      end
    end
    [a, ac, b, bc]
  end

  even = []
  odd = []
  n.times { |i| (i.even? ? even : odd) << i }
  e = top2.call(even)
  o = top2.call(odd)
  return n - e[1] - o[1] if e[0] != o[0]

  [n - e[1] - o[3], n - e[3] - o[1]].min
end
''')

add("2171_removing_minimum_number_of_magic_beans", r'''
# LeetCode 2171 - Removing Minimum Number of Magic Beans
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

# @param {Integer[]} beans
# @return {Integer}
def minimum_removal(beans)
  beans = beans.sort
  n = beans.length
  sum = beans.sum
  ans = sum
  n.times do |i|
    remain = (n - i) * beans[i]
    ans = [ans, sum - remain].min
  end
  ans
end
''')

add("2172_maximum_and_sum_of_array", r'''
# LeetCode 2172 - Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array/

# @param {Integer[]} nums
# @param {Integer} num_slots
# @return {Integer}
def maximum_and_sum(nums, num_slots)
  n = nums.length
  slots = num_slots
  max_mask = 3**slots
  dp = Array.new(max_mask, 0)
  max_mask.times do |mask|
    cnt = 0
    x = mask
    while x > 0
      cnt += x % 3
      x /= 3
    end
    next if cnt >= n

    v = nums[cnt]
    bas = 1
    (1..slots).each do |s|
      occ = mask / bas % 3
      if occ < 2
        nm = mask + bas
        dp[nm] = [dp[nm], dp[mask] + (v & s)].max
      end
      bas *= 3
    end
  end
  dp.max
end
''')

add("2174_remove_all_ones_with_row_and_column_flips_ii", r'''
# LeetCode 2174 - Remove All Ones With Row and Column Flips II
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

# @param {Integer[][]} grid
# @return {Integer}
def remove_ones(grid)
  m = grid.length
  n = grid[0].length
  ones = []
  m.times do |i|
    n.times { |j| ones << [i, j] if grid[i][j] == 1 }
  end
  return 0 if ones.empty?

  ans = m + n
  dfs = nil
  dfs = lambda do |idx, flips|
    return if flips >= ans

    idx += 1 while idx < ones.length && grid[ones[idx][0]][ones[idx][1]] == 0
    if idx == ones.length
      ans = flips
      return
    end
    r, c = ones[idx]
    changed = []
    n.times do |j|
      if grid[r][j] == 1
        grid[r][j] = 0
        changed << [r, j]
      end
    end
    dfs.call(idx + 1, flips + 1)
    changed.each { |x, y| grid[x][y] = 1 }
    changed = []
    m.times do |i|
      if grid[i][c] == 1
        grid[i][c] = 0
        changed << [i, c]
      end
    end
    dfs.call(idx + 1, flips + 1)
    changed.each { |x, y| grid[x][y] = 1 }
  end
  dfs.call(0, 0)
  ans
end
''')

add("2176_count_equal_and_divisible_pairs_in_an_array", r'''
# LeetCode 2176 - Count Equal and Divisible Pairs in an Array
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
  ans = 0
  nums.each_index do |i|
    ((i + 1)...nums.length).each do |j|
      ans += 1 if nums[i] == nums[j] && (i * j) % k == 0
    end
  end
  ans
end
''')

add("2177_find_three_consecutive_integers_that_sum_to_a_given_number", r'''
# LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

# @param {Integer} num
# @return {Integer[]}
def sum_of_three(num)
  return [] if num % 3 != 0

  x = num / 3
  [x - 1, x, x + 1]
end
''')

add("2178_maximum_split_of_positive_even_integers", r'''
# LeetCode 2178 - Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

# @param {Integer} final_sum
# @return {Integer[]}
def maximum_even_split(final_sum)
  return [] if final_sum.odd?

  ans = []
  x = 2
  while x <= final_sum
    ans << x
    final_sum -= x
    x += 2
  end
  ans[-1] += final_sum
  ans
end
''')

add("2179_count_good_triplets_in_an_array", r'''
# LeetCode 2179 - Count Good Triplets in an Array
# https://leetcode.com/problems/count-good-triplets-in-an-array/

class Fenwick
  def initialize(sz)
    @bit = Array.new(sz, 0)
  end

  def add(i, v)
    while i < @bit.length
      @bit[i] += v
      i += i & -i
    end
  end

  def sum(i)
    s = 0
    while i > 0
      s += @bit[i]
      i -= i & -i
    end
    s
  end
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def good_triplets(nums1, nums2)
  n = nums1.length
  pos2 = Array.new(n, 0)
  n.times { |i| pos2[nums2[i]] = i }
  mapped = Array.new(n, 0)
  n.times { |i| mapped[i] = pos2[nums1[i]] }
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  fw = Fenwick.new(n + 2)
  n.times do |i|
    left[i] = fw.sum(mapped[i])
    fw.add(mapped[i] + 1, 1)
  end
  fw = Fenwick.new(n + 2)
  (n - 1).downto(0) do |i|
    right[i] = fw.sum(n) - fw.sum(mapped[i] + 1)
    fw.add(mapped[i] + 1, 1)
  end
  ans = 0
  n.times { |i| ans += left[i] * right[i] }
  ans
end
''')

add("2180_count_integers_with_even_digit_sum", r'''
# LeetCode 2180 - Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/

# @param {Integer} num
# @return {Integer}
def count_even(num)
  ans = 0
  (1..num).each do |x|
    s = 0
    y = x
    while y > 0
      s += y % 10
      y /= 10
    end
    ans += 1 if s.even?
  end
  ans
end
''')

add("2181_merge_nodes_in_between_zeros", r'''
# LeetCode 2181 - Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def merge_nodes(head)
  dummy = ListNode.new
  cur = dummy
  sum = 0
  p = head.next
  while p
    if p.val == 0
      cur.next = ListNode.new(sum)
      cur = cur.next
      sum = 0
    else
      sum += p.val
    end
    p = p.next
  end
  dummy.next
end
''')

add("2182_construct_string_with_repeat_limit", r'''
# LeetCode 2182 - Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/

# @param {String} s
# @param {Integer} repeat_limit
# @return {String}
def repeat_limited_string(s, repeat_limit)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  ans = []
  loop do
    placed = false
    25.downto(0) do |c|
      next if freq[c] == 0

      if !ans.empty? && ans[-1].ord - 97 == c
        found = false
        (c - 1).downto(0) do |d|
          next if freq[d] == 0

          ans << (97 + d).chr
          freq[d] -= 1
          found = placed = true
          break
        end
        return ans.join unless found

        break
      end
      use = [freq[c], repeat_limit].min
      use.times { ans << (97 + c).chr }
      freq[c] -= use
      placed = true
      break
    end
    break unless placed
  end
  ans.join
end
''')

add("2183_count_array_pairs_divisible_by_k", r'''
# LeetCode 2183 - Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  freq = Hash.new(0)
  ans = 0
  nums.each do |x|
    g1 = gcd.call(x, k)
    freq.each { |g2, cnt| ans += cnt if (g1 * g2) % k == 0 }
    freq[g1] += 1
  end
  ans
end
''')

add("2184_number_of_ways_to_build_sturdy_brick_wall", r'''
# LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
# https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

# @param {Integer} height
# @param {Integer} width
# @param {Integer[]} bricks
# @return {Integer}
def build_wall(height, width, bricks)
  mod = 1_000_000_007
  masks = []
  gen = nil
  gen = lambda do |remain, mask|
    if remain == 0
      masks << mask
      return
    end
    bricks.each do |b|
      next if b > remain

      nm = mask
      nm |= 1 << (remain - b) if remain - b > 0
      gen.call(remain - b, nm)
    end
  end
  gen.call(width, 0)
  m = masks.length
  compat = Array.new(m) { [] }
  m.times do |i|
    m.times { |j| compat[i] << j if (masks[i] & masks[j]).zero? }
  end
  dp = Array.new(m, 1)
  (1...height).each do
    ndp = Array.new(m, 0)
    m.times do |i|
      compat[i].each { |j| ndp[j] = (ndp[j] + dp[i]) % mod }
    end
    dp = ndp
  end
  dp.sum % mod
end
''')

add("2185_counting_words_with_a_given_prefix", r'''
# LeetCode 2185 - Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

# @param {String[]} words
# @param {String} pref
# @return {Integer}
def prefix_count(words, pref)
  words.count { |w| w.start_with?(pref) }
end
''')

add("2186_minimum_number_of_steps_to_make_two_strings_anagram_ii", r'''
# LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

# @param {String} s
# @param {String} t
# @return {Integer}
def min_steps(s, t)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  t.each_byte { |b| freq[b - 97] -= 1 }
  freq.sum(&:abs)
end
''')

add("2187_minimum_time_to_complete_trips", r'''
# LeetCode 2187 - Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/

# @param {Integer[]} time
# @param {Integer} total_trips
# @return {Integer}
def minimum_time(time, total_trips)
  mn = time.min
  lo = 1
  hi = mn * total_trips
  while lo < hi
    mid = (lo + hi) / 2
    trips = 0
    ok = false
    time.each do |t|
      trips += mid / t
      if trips >= total_trips
        ok = true
        break
      end
    end
    if ok
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("2188_minimum_time_to_finish_the_race", r'''
# LeetCode 2188 - Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/

# @param {Integer[][]} tires
# @param {Integer} change_time
# @param {Integer} num_laps
# @return {Integer}
def minimum_finish_time(tires, change_time, num_laps)
  inf = 1 << 30
  min_time = Array.new(20, inf)
  tires.each do |f, r|
    t = f
    lap = f
    x = 1
    while x < 20 && t < min_time[x]
      min_time[x] = t
      lap *= r
      break if lap > change_time + f

      t += lap
      x += 1
    end
  end
  dp = Array.new(num_laps + 1, inf)
  dp[0] = -change_time
  (1..num_laps).each do |i|
    j = 1
    while j <= i && j < 20
      dp[i] = [dp[i], dp[i - j] + change_time + min_time[j]].min
      j += 1
    end
  end
  dp[num_laps]
end
''')

add("2189_number_of_ways_to_build_house_of_cards", r'''
# LeetCode 2189 - Number of Ways to Build House of Cards
# https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

# @param {Integer} n
# @return {Integer}
def house_of_cards(n)
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  k = 1
  while 3 * k - 1 <= n
    cost = 3 * k - 1
    n.downto(cost) { |j| dp[j] += dp[j - cost] }
    k += 1
  end
  dp[n]
end
''')

add("2190_most_frequent_number_following_key_in_an_array", r'''
# LeetCode 2190 - Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

# @param {Integer[]} nums
# @param {Integer} key
# @return {Integer}
def most_frequent(nums, key)
  freq = Hash.new(0)
  best = 0
  ans = 0
  i = 0
  while i + 1 < nums.length
    if nums[i] == key
      v = freq[nums[i + 1]] + 1
      freq[nums[i + 1]] = v
      if v > best
        best = v
        ans = nums[i + 1]
      end
    end
    i += 1
  end
  ans
end
''')

add("2191_sort_the_jumbled_numbers", r'''
# LeetCode 2191 - Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/

# @param {Integer[]} mapping
# @param {Integer[]} nums
# @return {Integer[]}
def sort_jumbled(mapping, nums)
  map_val = lambda do |x|
    return mapping[0] if x == 0

    digits = []
    while x > 0
      digits << x % 10
      x /= 10
    end
    res = 0
    (digits.length - 1).downto(0) { |i| res = res * 10 + mapping[digits[i]] }
    res
  end

  arr = nums.each_with_index.map { |v, i| [map_val.call(v), i, v] }
  arr.sort_by! { |x| [x[0], x[1]] }
  arr.map { |x| x[2] }
end
''')

add("2192_all_ancestors_of_a_node_in_a_directed_acyclic_graph", r'''
# LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def get_ancestors(n, edges)
  g = Array.new(n) { [] }
  indeg = Array.new(n, 0)
  edges.each do |a, b|
    g[a] << b
    indeg[b] += 1
  end
  anc = Array.new(n) { {} }
  q = []
  n.times { |i| q << i if indeg[i] == 0 }
  until q.empty?
    u = q.shift
    g[u].each do |v|
      anc[v][u] = true
      anc[u].each_key { |x| anc[v][x] = true }
      indeg[v] -= 1
      q << v if indeg[v] == 0
    end
  end
  anc.map { |s| s.keys.sort }
end
''')

add("2193_minimum_number_of_moves_to_make_palindrome", r'''
# LeetCode 2193 - Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

# @param {String} s
# @return {Integer}
def min_moves_to_make_palindrome(s)
  b = s.chars
  ans = 0
  while b.length > 1
    j = b.length - 1
    j -= 1 while j > 0 && b[j] != b[0]
    if j == 0
      ans += b.length / 2
      b.shift
      next
    end
    ans += b.length - 1 - j
    b.delete_at(j)
    b.shift
  end
  ans
end
''')

add("2194_cells_in_a_range_on_an_excel_sheet", r'''
# LeetCode 2194 - Cells in a Range on an Excel Sheet
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

# @param {String} s
# @return {String[]}
def cells_in_range(s)
  ans = []
  (s[0].ord..s[3].ord).each do |c|
    (s[1].ord..s[4].ord).each { |r| ans << c.chr + r.chr }
  end
  ans
end
''')

add("2195_append_k_integers_with_minimal_sum", r'''
# LeetCode 2195 - Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimal_k_sum(nums, k)
  nums = nums.sort
  ans = 0
  prev = 0
  nums.each do |x|
    next if x <= prev

    start = prev + 1
    finish = x - 1
    if start <= finish
      cnt = finish - start + 1
      if cnt > k
        finish = start + k - 1
        cnt = k
      end
      ans += (start + finish) * cnt / 2
      k -= cnt
      return ans if k == 0
    end
    prev = x
  end
  s = prev + 1
  e = s + k - 1
  ans + (s + e) * k / 2
end
''')

add("2196_create_binary_tree_from_descriptions", r'''
# LeetCode 2196 - Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[][]} descriptions
# @return {TreeNode}
def create_binary_tree(descriptions)
  nodes = {}
  child = {}
  descriptions.each do |p, c, is_left|
    nodes[p] ||= TreeNode.new(p)
    nodes[c] ||= TreeNode.new(c)
    if is_left == 1
      nodes[p].left = nodes[c]
    else
      nodes[p].right = nodes[c]
    end
    child[c] = true
  end
  nodes.each { |k, v| return v unless child[k] }
  nil
end
''')

written = 0
for folder, body in S.items():
    (ROOT / folder / "solution.rb").write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
