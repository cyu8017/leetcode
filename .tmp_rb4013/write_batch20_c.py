#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3769_sort_integers_by_binary_reflection", r'''
# LeetCode 3769 - Sort Integers by Binary Reflection
# https://leetcode.com/problems/sort-integers-by-binary-reflection/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_by_reflection(nums)
  f = lambda do |x|
    y = 0
    while x != 0
      y = (y << 1) | (x & 1)
      x >>= 1
    end
    y
  end
  arr = nums.dup
  arr.sort_by! { |a| [f.call(a), a] }
  (0...nums.length).each { |i| nums[i] = arr[i] }
  nums
end
''')

add("3770_largest_prime_from_consecutive_prime_sum", r'''
# LeetCode 3770 - Largest Prime from Consecutive Prime Sum
# https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

# @param {Integer} n
# @return {Integer}
def largest_prime(n)
  mx = 500000
  is_prime = Array.new(mx + 1, true)
  is_prime[0] = is_prime[1] = false
  primes = []
  (2..mx).each do |i|
    next unless is_prime[i]
    primes << i
    if i * i <= mx
      (i * i).step(mx, i) { |j| is_prime[j] = false }
    end
  end
  s = [0]
  t = 0
  primes.each do |x|
    t += x
    break if t > mx
    s << t if is_prime[t]
  end
  lo = 0
  hi = s.length
  while lo < hi
    mid = (lo + hi) >> 1
    if s[mid] <= n
      lo = mid + 1
    else
      hi = mid
    end
  end
  s[lo - 1]
end
''')

add("3771_total_score_of_dungeon_runs", r'''
# LeetCode 3771 - Total Score of Dungeon Runs
# https://leetcode.com/problems/total-score-of-dungeon-runs/

# @param {Integer} hp
# @param {Integer[]} damage
# @param {Integer[]} requirement
# @return {Integer}
def total_score(hp, damage, requirement)
  n = damage.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + damage[i] }
  answer = n * (n + 1) / 2
  (1..n).each do |j|
    threshold = prefix[j] + (requirement[j - 1] - hp)
    lo = 0
    hi = j
    while lo < hi
      mid = (lo + hi) >> 1
      if prefix[mid] < threshold
        lo = mid + 1
      else
        hi = mid
      end
    end
    answer -= lo
  end
  answer
end
''')

add("3772_maximum_subgraph_score_in_a_tree", r'''
# LeetCode 3772 - Maximum Subgraph Score in a Tree
# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} good
# @return {Integer[]}
def max_subgraph_score(n, edges, good)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    g[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  down = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    u = order[i]
    down[u] = 2 * good[u] - 1
    g[u].each { |v| down[u] += down[v] if parent[v] == u && down[v] > 0 }
  end
  ans = down.dup
  order.each do |u|
    g[u].each do |v|
      next unless parent[v] == u
      outside = ans[u]
      outside -= down[v] if down[v] > 0
      ans[v] = down[v]
      ans[v] += outside if outside > 0
    end
  end
  ans
end
''')

add("3773_maximum_number_of_equal_length_runs", r'''
# LeetCode 3773 - Maximum Number of Equal Length Runs
# https://leetcode.com/problems/maximum-number-of-equal-length-runs/

# @param {String} s
# @return {Integer}
def max_same_length_runs(s)
  cnt = Hash.new(0)
  n = s.length
  ans = 0
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && s[j] == s[i]
    m = j - i
    cnt[m] += 1
    ans = [ans, cnt[m]].max
    i = j
  end
  ans
end
''')

add("3774_absolute_difference_between_maximum_and_minimum_k_elements", r'''
# LeetCode 3774 - Absolute Difference Between Maximum and Minimum K Elements
# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def abs_difference(nums, k)
  a = nums.sort
  ans = 0
  n = a.length
  (0...k).each { |i| ans += a[n - i - 1] - a[i] }
  ans
end
''')

add("3775_reverse_words_with_same_vowel_count", r'''
# LeetCode 3775 - Reverse Words with Same Vowel Count
# https://leetcode.com/problems/reverse-words-with-same-vowel-count/

# @param {String} s
# @return {String}
def reverse_words(s)
  calc = lambda do |w|
    cnt = 0
    w.each_char { |c| cnt += 1 if "aeiou".include?(c) }
    cnt
  end
  words = s.strip.split
  cnt = calc.call(words[0])
  ans = words[0]
  (1...words.length).each do |i|
    w = words[i]
    w = w.reverse if calc.call(w) == cnt
    ans += " " + w
  end
  ans
end
''')

add("3776_minimum_moves_to_balance_circular_array", r'''
# LeetCode 3776 - Minimum Moves to Balance Circular Array
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

# @param {Integer[]} balance
# @return {Integer}
def min_moves(balance)
  total = balance.sum
  return -1 if total < 0
  n = balance.length
  mn = balance[0]
  idx = 0
  (1...n).each do |i|
    if balance[i] < mn
      mn = balance[i]
      idx = i
    end
  end
  return 0 if mn >= 0
  need = -mn
  ans = 0
  (1...n).each do |j|
    a = balance[(idx - j + n) % n]
    b = balance[(idx + j) % n]
    c1 = [a, need].min
    need -= c1
    ans += c1 * j
    c2 = [b, need].min
    need -= c2
    ans += c2 * j
  end
  ans
end
''')

add("3777_minimum_deletions_to_make_alternating_substring", r'''
# LeetCode 3777 - Minimum Deletions to Make Alternating Substring
# https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class AltBit
  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
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

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def min_deletions(s, queries)
  n = s.length
  nums = Array.new(n, 0)
  bit = AltBit.new(n)
  (1...n).each do |i|
    if s[i] == s[i - 1]
      nums[i] = 1
      bit.update(i + 1, 1)
    end
  end
  ans = []
  queries.each do |q|
    if q[0] == 1
      j = q[1]
      delta = (nums[j] ^ 1) - nums[j]
      nums[j] ^= 1
      bit.update(j + 1, delta)
      if j + 1 < n
        delta = (nums[j + 1] ^ 1) - nums[j + 1]
        nums[j + 1] ^= 1
        bit.update(j + 2, delta)
      end
    else
      l = q[1]
      r = q[2]
      ans << bit.query(r + 1) - bit.query(l + 1)
    end
  end
  ans
end
''')

add("3778_minimum_distance_excluding_one_maximum_weighted_edge", r'''
# LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
# https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class MinCostHeap
  def initialize
    @a = []
  end

  def size
    @a.length
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if a[i][0] >= a[p][0]
      a[i], a[p] = a[p], a[i]
      i = p
    end
  end

  def down(i)
    a = @a
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l][0] < a[s][0]
      s = r if r < n && a[r][0] < a[s][0]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_cost_excluding_max(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    g[u] << [v, w]
    g[v] << [u, w]
  end
  inf = 10**18
  dist = Array.new(n) { [inf, inf] }
  dist[0][0] = 0
  pq = MinCostHeap.new
  pq.push([0, 0, 0])
  while pq.size > 0
    c, u, used = pq.pop
    next if c > dist[u][used]
    return c if u == n - 1 && used == 1
    g[u].each do |v, w|
      nxt = c + w
      if nxt < dist[v][used]
        dist[v][used] = nxt
        pq.push([nxt, v, used])
      end
      if used == 0
        nxt = c
        if nxt < dist[v][1]
          dist[v][1] = nxt
          pq.push([nxt, v, 1])
        end
      end
    end
  end
  dist[n - 1][1]
end
''')

add("3779_minimum_number_of_operations_to_have_distinct_elements", r'''
# LeetCode 3779 - Minimum Number of Operations to Have Distinct Elements
# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  st = {}
  (nums.length - 1).downto(0) do |i|
    return i / 3 + 1 if st[nums[i]]
    st[nums[i]] = true
  end
  0
end
''')

add("3780_maximum_sum_of_three_numbers_divisible_by_three", r'''
# LeetCode 3780 - Maximum Sum of Three Numbers Divisible by Three
# https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  a = nums.sort
  g = [[], [], []]
  a.each { |x| g[x % 3] << x }
  ans = 0
  (0...3).each do |aa|
    next if g[aa].empty?
    x = g[aa].pop
    (0...3).each do |b|
      next if g[b].empty?
      y = g[b].pop
      c = (3 - (aa + b) % 3) % 3
      z = g[c][-1]
      ans = [ans, x + y + z].max if z
      g[b] << y
    end
    g[aa] << x
  end
  ans
end
''')

add("3781_maximum_score_after_binary_swaps", r'''
# LeetCode 3781 - Maximum Score After Binary Swaps
# https://leetcode.com/problems/maximum-score-after-binary-swaps/

class ScoreHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if a[i] <= a[p]
      a[i], a[p] = a[p], a[i]
      i = p
    end
  end

  def down(i)
    a = @a
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] > a[s]
      s = r if r < n && a[r] > a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {String} s
# @return {Integer}
def maximum_score(nums, s)
  ans = 0
  pq = ScoreHeap.new
  nums.each_with_index do |x, i|
    pq.push(x)
    ans += pq.pop if s[i] == "1"
  end
  ans
end
''')

add("3782_last_remaining_integer_after_alternating_deletion_operations", r'''
# LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
# https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

# @param {Integer} n
# @return {Integer}
def last_remaining(n)
  first = 1
  step = 2
  left = true
  while n > 1
    first += step if !left && n.even?
    n = (n + 1) / 2
    step *= 2
    left = !left
  end
  first
end
''')

add("3783_mirror_distance_of_an_integer", r'''
# LeetCode 3783 - Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/

# @param {Integer} n
# @return {Integer}
def mirror_distance(n)
  reverse = lambda do |x|
    y = 0
    while x > 0
      y = y * 10 + x % 10
      x /= 10
    end
    y
  end
  (n - reverse.call(n)).abs
end
''')

add("3784_minimum_deletion_cost_to_make_all_characters_equal", r'''
# LeetCode 3784 - Minimum Deletion Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

# @param {String} s
# @param {Integer[]} cost
# @return {Integer}
def min_cost(s, cost)
  tot = 0
  g = Hash.new(0)
  (0...cost.length).each do |i|
    tot += cost[i]
    g[s[i]] += cost[i]
  end
  ans = tot
  g.each_value { |x| ans = [ans, tot - x].min }
  ans
end
''')

add("3785_minimum_swaps_to_avoid_forbidden_values", r'''
# LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

# @param {Integer[]} nums
# @param {Integer[]} forbidden
# @return {Integer}
def min_swaps(nums, forbidden)
  n = nums.length
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  forbidden.each { |x| freq[x] += 1 }
  freq.each_value { |c| return -1 if c > n }
  bad = Hash.new(0)
  total = 0
  largest = 0
  (0...n).each do |i|
    next unless nums[i] == forbidden[i]
    bad[nums[i]] += 1
    total += 1
    largest = bad[nums[i]] if bad[nums[i]] > largest
  end
  return (total + 1) / 2 if (total + 1) / 2 > largest
  largest
end
''')

add("3786_total_sum_of_interaction_cost_in_tree_groups", r'''
# LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} group
# @return {Integer}
def interaction_cost(n, edges, group)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  total = Array.new(21, 0)
  group.each { |x| total[x] += 1 }
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    g[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  count = Array.new(n) { Array.new(21, 0) }
  ans = 0
  (n - 1).downto(0) do |i|
    u = order[i]
    count[u][group[u]] += 1
    g[u].each do |v|
      next unless parent[v] == u
      (1...21).each do |c|
        x = count[v][c]
        ans += x * (total[c] - x)
        count[u][c] += x
      end
    end
  end
  ans
end
''')

add("3787_find_diameter_endpoints_of_a_tree", r'''
# LeetCode 3787 - Find Diameter Endpoints of a Tree
# https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {String}
def find_special_nodes(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  bfs = lambda do |start|
    dist = Array.new(n, -1)
    dist[start] = 0
    q = [start]
    far = start
    head = 0
    while head < q.length
      u = q[head]
      head += 1
      far = u if dist[u] > dist[far]
      g[u].each do |v|
        if dist[v] == -1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    [far, dist]
  end
  a, = bfs.call(0)
  b, dist1 = bfs.call(a)
  _, dist2 = bfs.call(b)
  d = dist1[b]
  ans = Array.new(n, "0")
  (0...n).each { |i| ans[i] = "1" if dist1[i] == d || dist2[i] == d }
  ans.join
end
''')

add("3788_maximum_score_of_a_split", r'''
# LeetCode 3788 - Maximum Score of a Split
# https://leetcode.com/problems/maximum-score-of-a-split/

# @param {Integer[]} nums
# @return {Integer}
def maximum_score(nums)
  n = nums.length
  suf = Array.new(n, 0)
  suf[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| suf[i] = [nums[i], suf[i + 1]].min }
  pre = 0
  ans = -(10**18)
  (0...(n - 1)).each do |i|
    pre += nums[i]
    ans = [ans, pre - suf[i + 1]].max
  end
  ans
end
''')

add("3789_minimum_cost_to_acquire_required_items", r'''
# LeetCode 3789 - Minimum Cost to Acquire Required Items
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

# @param {Integer} cost1
# @param {Integer} cost2
# @param {Integer} cost_both
# @param {Integer} need1
# @param {Integer} need2
# @return {Integer}
def minimum_cost(cost1, cost2, cost_both, need1, need2)
  a = need1 * cost1 + need2 * cost2
  b = cost_both * [need1, need2].max
  mn = [need1, need2].min
  c = cost_both * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
  [a, b, c].min
end
''')

add("3790_smallest_all_ones_multiple", r'''
# LeetCode 3790 - Smallest All Ones Multiple
# https://leetcode.com/problems/smallest-all-ones-multiple/

# @param {Integer} k
# @return {Integer}
def min_all_one_multiple(k)
  return -1 if (k & 1) == 0
  x = 1 % k
  ans = 1
  k.times do
    x = (x * 10 + 1) % k
    ans += 1
    return ans if x == 0
  end
  -1
end
''')

add("3791_number_of_balanced_integers_in_a_range", r'''
# LeetCode 3791 - Number of Balanced Integers in a Range
# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_balanced(low, high)
  base = 90
  num = ""
  f = []
  dfs = nil
  dfs = lambda do |pos, diff, lim|
    return (diff == 0 ? 1 : 0) if pos >= num.length
    return f[pos][diff + base] if !lim && f[pos][diff + base] != -1
    up = lim ? (num[pos].ord - 48) : 9
    res = 0
    (0..up).each do |i|
      if pos.even?
        res += dfs.call(pos + 1, diff + i, lim && i == up)
      else
        res += dfs.call(pos + 1, diff - i, lim && i == up)
      end
    end
    f[pos][diff + base] = res unless lim
    res
  end
  return 0 if high < 11
  low = 11 if low < 11
  num = (low - 1).to_s
  f = Array.new(20) { Array.new(181, -1) }
  a = dfs.call(0, 0, true)
  num = high.to_s
  f = Array.new(20) { Array.new(181, -1) }
  b = dfs.call(0, 0, true)
  b - a
end
''')

add("3792_sum_of_increasing_product_blocks", r'''
# LeetCode 3792 - Sum of Increasing Product Blocks
# https://leetcode.com/problems/sum-of-increasing-product-blocks/

# @param {Integer} n
# @return {Integer}
def sum_of_blocks(n)
  mod = 1_000_000_007
  ans = 0
  k = 1
  (1..n).each do |i|
    x = 1
    (k...(k + i)).each { |j| x = x * j % mod }
    ans = (ans + x) % mod
    k += i
  end
  ans
end
''')

add("3794_reverse_string_prefix", r'''
# LeetCode 3794 - Reverse String Prefix
# https://leetcode.com/problems/reverse-string-prefix/

# @param {String} s
# @param {Integer} k
# @return {String}
def reverse_prefix(s, k)
  arr = s.chars
  i = 0
  j = k - 1
  while i < j
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
  end
  arr.join
end
''')


def main() -> None:
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        print(f"wrote {name}")
    print(f"total {len(S)}")


if __name__ == "__main__":
    main()
