#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3144_minimum_substring_partition_of_equal_character_frequency", r'''
# LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

# @param {String} s
# @return {Integer}
def minimum_substrings_in_partition(s)
  n = s.length
  memo = Array.new(n, -1)

  dfs = lambda do |i|
    return 0 if i >= n
    return memo[i] if memo[i] != -1
    cnt = Array.new(26, 0)
    freq = {}
    memo[i] = n - i
    (i...n).each do |j|
      k = s[j].ord - 97
      if cnt[k] > 0
        c = cnt[k]
        nv = freq[c] - 1
        if nv == 0
          freq.delete(c)
        else
          freq[c] = nv
        end
      end
      cnt[k] += 1
      freq[cnt[k]] = freq.fetch(cnt[k], 0) + 1
      memo[i] = [memo[i], 1 + dfs.call(j + 1)].min if freq.length == 1
    end
    memo[i]
  end

  dfs.call(0)
end
''')

add("3145_find_products_of_elements_of_big_array", r'''
# LeetCode 3145 - Find Products of Elements of Big Array
# https://leetcode.com/problems/find-products-of-elements-of-big-array/

# @param {Integer[][]} queries
# @return {Integer[]}
def find_products_of_elements(queries)
  m = 50
  cnt = Array.new(m + 1, 0)
  s = Array.new(m + 1, 0)
  p = 1
  (1..m).each do |i|
    cnt[i] = cnt[i - 1] * 2 + p
    s[i] = s[i - 1] * 2 + p * (i - 1)
    p *= 2
  end

  num_idx_and_sum = lambda do |x|
    idx = 0
    total_sum = 0
    while x > 0
      i = 0
      t = x
      while t > 1
        t >>= 1
        i += 1
      end
      idx += cnt[i]
      total_sum += s[i]
      x -= 1 << i
      total_sum += (x + 1) * i
      idx += x + 1
    end
    [idx, total_sum]
  end

  f = lambda do |i|
    l = 0
    r = 1 << m
    while l < r
      mid = (l + r + 1) >> 1
      p0 = num_idx_and_sum.call(mid)
      if p0[0] < i
        l = mid
      else
        r = mid - 1
      end
    end
    p0 = num_idx_and_sum.call(l)
    total_sum = p0[1]
    i -= p0[0]
    x = l + 1
    i.times do
      y = x & -x
      tz = 0
      yy = y
      while (yy & 1) == 0
        tz += 1
        yy >>= 1
      end
      total_sum += tz
      x -= y
    end
    total_sum
  end

  qpow = lambda do |a, n, mod|
    ans = 1 % mod
    a %= mod
    while n > 0
      ans = ans * a % mod if (n & 1) != 0
      a = a * a % mod
      n >>= 1
    end
    ans
  end

  queries.map do |q|
    left, right, mod = q[0], q[1], q[2]
    power = f.call(right + 1) - f.call(left)
    qpow.call(2, power, mod)
  end
end
''')

add("3146_permutation_difference_between_two_strings", r'''
# LeetCode 3146 - Permutation Difference between Two Strings
# https://leetcode.com/problems/permutation-difference-between-two-strings/

# @param {String} s
# @param {String} t
# @return {Integer}
def find_permutation_difference(s, t)
  d = Array.new(26, 0)
  s.each_char.with_index { |ch, i| d[ch.ord - 97] = i }
  ans = 0
  t.each_char.with_index { |ch, i| ans += (d[ch.ord - 97] - i).abs }
  ans
end
''')

add("3147_taking_maximum_energy_from_the_mystic_dungeon", r'''
# LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

# @param {Integer[]} energy
# @param {Integer} k
# @return {Integer}
def maximum_energy(energy, k)
  ans = -(1 << 30)
  n = energy.length
  (n - k...n).each do |i|
    s = 0
    j = i
    while j >= 0
      s += energy[j]
      ans = [ans, s].max
      j -= k
    end
  end
  ans
end
''')

add("3148_maximum_difference_score_in_a_grid", r'''
# LeetCode 3148 - Maximum Difference Score in a Grid
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_score(grid)
  m = grid.length
  n = grid[0].length
  inf = 1 << 30
  f = Array.new(m) { Array.new(n, 0) }
  ans = -inf
  m.times do |i|
    n.times do |j|
      x = grid[i][j]
      mi = inf
      mi = [mi, f[i - 1][j]].min if i > 0
      mi = [mi, f[i][j - 1]].min if j > 0
      ans = [ans, x - mi].max
      f[i][j] = [x, mi].min
    end
  end
  ans
end
''')

add("3149_find_the_minimum_cost_array_permutation", r'''
# LeetCode 3149 - Find the Minimum Cost Array Permutation
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

# @param {Integer[]} nums
# @return {Integer[]}
def find_permutation(nums)
  n = nums.length
  memo = Array.new(1 << n) { Array.new(n, -1) }

  absv = ->(x) { x < 0 ? -x : x }

  dfs = nil
  dfs = lambda do |mask, pre|
    return absv.call(pre - nums[0]) if mask == (1 << n) - 1
    return memo[mask][pre] if memo[mask][pre] != -1
    res = 10**18
    (1...n).each do |cur|
      if ((mask >> cur) & 1) == 0
        res = [res, absv.call(pre - nums[cur]) + dfs.call(mask | (1 << cur), cur)].min
      end
    end
    memo[mask][pre] = res
    res
  end

  ans = []
  g = nil
  g = lambda do |mask, pre|
    ans << pre
    return if mask == (1 << n) - 1
    res = dfs.call(mask, pre)
    (1...n).each do |cur|
      if ((mask >> cur) & 1) == 0
        if absv.call(pre - nums[cur]) + dfs.call(mask | (1 << cur), cur) == res
          g.call(mask | (1 << cur), cur)
          break
        end
      end
    end
  end

  g.call(1, 0)
  ans
end
''')

add("3151_special_array_i", r'''
# LeetCode 3151 - Special Array I
# https://leetcode.com/problems/special-array-i/

# @param {Integer[]} nums
# @return {Boolean}
def is_array_special(nums)
  (1...nums.length).each do |i|
    return false if nums[i] % 2 == nums[i - 1] % 2
  end
  true
end
''')

add("3152_special_array_ii", r'''
# LeetCode 3152 - Special Array II
# https://leetcode.com/problems/special-array-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean[]}
def is_array_special(nums, queries)
  n = nums.length
  d = (0...n).to_a
  (1...n).each { |i| d[i] = d[i - 1] if nums[i] % 2 != nums[i - 1] % 2 }
  queries.map { |q| d[q[1]] <= q[0] }
end
''')

add("3153_sum_of_digit_differences_of_all_pairs", r'''
# LeetCode 3153 - Sum of Digit Differences of All Pairs
# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

# @param {Integer[]} nums
# @return {Integer}
def sum_digit_differences(nums)
  n = nums.length
  m = 0
  x = nums[0]
  while x > 0
    m += 1
    x /= 10
  end
  m = 1 if m == 0
  ans = 0
  vals = nums.dup
  m.times do
    cnt = Array.new(10, 0)
    n.times do |i|
      cnt[vals[i] % 10] += 1
      vals[i] /= 10
    end
    cnt.each { |v| ans += v * (n - v) }
  end
  ans / 2
end
''')

add("3154_find_number_of_ways_to_reach_the_k_th_stair", r'''
# LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

# @param {Integer} k
# @return {Integer}
def ways_to_reach_stair(k)
  f = {}

  dfs = lambda do |i, j, jump|
    return 0 if i > k + 1
    key = [i, j, jump]
    return f[key] if f.key?(key)
    ans = 0
    ans += 1 if i == k
    ans += dfs.call(i - 1, 1, jump) if i > 0 && j == 0
    ans += dfs.call(i + (1 << jump), 0, jump + 1)
    f[key] = ans
    ans
  end

  dfs.call(1, 0, 0)
end
''')

add("3155_maximum_number_of_upgradable_servers", r'''
# LeetCode 3155 - Maximum Number of Upgradable Servers
# https://leetcode.com/problems/maximum-number-of-upgradable-servers/

# @param {Integer[]} count
# @param {Integer[]} upgrade
# @param {Integer[]} sell
# @param {Integer[]} money
# @return {Integer[]}
def max_upgrades(count, upgrade, sell, money)
  count.each_index.map do |i|
    cnt = count[i]
    [cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i])].min
  end
end
''')

add("3157_find_the_level_of_tree_with_minimum_sum", r'''
# LeetCode 3157 - Find the Level of Tree with Minimum Sum
# https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def minimum_level(root)
  q = [root]
  s = 10**18
  ans = 0
  level = 1
  until q.empty?
    t = 0
    m = q.length
    while m > 0
      node = q.shift
      t += node.val
      q << node.left if node.left
      q << node.right if node.right
      m -= 1
    end
    if s > t
      s = t
      ans = level
    end
    level += 1
  end
  ans
end
''')

add("3158_find_the_xor_of_numbers_which_appear_twice", r'''
# LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

# @param {Integer[]} nums
# @return {Integer}
def duplicate_numbers_xor(nums)
  cnt = Array.new(51, 0)
  ans = 0
  nums.each do |x|
    cnt[x] += 1
    ans ^= x if cnt[x] == 2
  end
  ans
end
''')

add("3159_find_occurrences_of_an_element_in_an_array", r'''
# LeetCode 3159 - Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @param {Integer} x
# @return {Integer[]}
def occurrences_of_element(nums, queries, x)
  ids = []
  nums.each_with_index { |v, i| ids << i if v == x }
  queries.map { |i| i - 1 < ids.length ? ids[i - 1] : -1 }
end
''')

add("3160_find_the_number_of_distinct_colors_among_the_balls", r'''
# LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

# @param {Integer} limit
# @param {Integer[][]} queries
# @return {Integer[]}
def query_results(limit, queries)
  g = {}
  cnt = {}
  queries.map do |q|
    x = q[0]
    y = q[1]
    cnt[y] = cnt.fetch(y, 0) + 1
    old = g[x]
    unless old.nil?
      nv = cnt[old] - 1
      if nv == 0
        cnt.delete(old)
      else
        cnt[old] = nv
      end
    end
    g[x] = y
    cnt.length
  end
end
''')

add("3161_block_placement_queries", r'''
# LeetCode 3161 - Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/

class FenwickMax
  def initialize(n)
    @vals = Array.new(n + 1, 0)
  end

  def maximize(i, val)
    while i < @vals.length
      @vals[i] = [@vals[i], val].max
      i += i & -i
    end
  end

  def get(i)
    res = 0
    while i > 0
      res = [res, @vals[i]].max
      i -= i & -i
    end
    res
  end
end

# @param {Integer[][]} queries
# @return {Boolean[]}
def get_results(queries)
  n = queries.length * 3
  n = 50_000 if n > 50_000
  tree = FenwickMax.new(n + 1)
  obs = [0, n]
  queries.each do |q|
    next unless q[0] == 1
    x = q[1]
    idx = bisect_left(obs, x)
    obs.insert(idx, x) if idx == obs.length || obs[idx] != x
  end
  (0...obs.length - 1).each { |i| tree.maximize(obs[i + 1], obs[i + 1] - obs[i]) }
  ans = []
  (queries.length - 1).downto(0) do |i|
    typ = queries[i][0]
    x = queries[i][1]
    if typ == 1
      j = bisect_left(obs, x)
      prev = obs[j - 1]
      nxt = obs[j + 1]
      obs.delete_at(j)
      tree.maximize(nxt, nxt - prev)
    else
      sz = queries[i][2]
      j = bisect_left(obs, x + 1) - 1
      prev = obs[j]
      ans << (tree.get(prev) >= sz || x - prev >= sz)
    end
  end
  ans.reverse
end

def bisect_left(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) / 2
    if a[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
''')

add("3162_find_the_number_of_good_pairs_i", r'''
# LeetCode 3162 - Find the Number of Good Pairs I
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def number_of_pairs(nums1, nums2, k)
  ans = 0
  nums1.each do |x|
    nums2.each { |y| ans += 1 if x % (y * k) == 0 }
  end
  ans
end
''')

add("3163_string_compression_iii", r'''
# LeetCode 3163 - String Compression III
# https://leetcode.com/problems/string-compression-iii/

# @param {String} word
# @return {String}
def compressed_string(word)
  ans = []
  n = word.length
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && word[j] == word[i]
    k = j - i
    while k > 0
      x = [9, k].min
      ans << x.to_s
      ans << word[i]
      k -= x
    end
    i = j
  end
  ans.join
end
''')

add("3164_find_the_number_of_good_pairs_ii", r'''
# LeetCode 3164 - Find the Number of Good Pairs II
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def number_of_pairs(nums1, nums2, k)
  cnt1 = {}
  nums1.each do |x|
    if x % k == 0
      cnt1[x / k] = cnt1.fetch(x / k, 0) + 1
    end
  end
  return 0 if cnt1.empty?
  cnt2 = Hash.new(0)
  nums2.each { |x| cnt2[x] += 1 }
  mx = cnt1.keys.max
  ans = 0
  cnt2.each do |x, v|
    s = 0
    y = x
    while y <= mx
      c = cnt1[y]
      s += c unless c.nil?
      y += x
    end
    ans += s * v
  end
  ans
end
''')

add("3165_maximum_sum_of_subsequence_with_non_adjacent_elements", r'''
# LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Node
  attr_accessor :l, :r, :s00, :s01, :s10, :s11
  def initialize
    @l = 0
    @r = 0
    @s00 = 0
    @s01 = 0
    @s10 = 0
    @s11 = 0
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def maximum_sum_subsequence(nums, queries)
  n = nums.length
  tr = Array.new(n * 4) { Node.new }

  build = nil
  build = lambda do |u, l, r|
    tr[u].l = l
    tr[u].r = r
    return if l == r
    mid = (l + r) >> 1
    build.call(u << 1, l, mid)
    build.call(u << 1 | 1, mid + 1, r)
  end

  pushup = lambda do |u|
    left = tr[u << 1]
    right = tr[u << 1 | 1]
    tr[u].s00 = [left.s00 + right.s10, left.s01 + right.s00].max
    tr[u].s01 = [left.s00 + right.s11, left.s01 + right.s01].max
    tr[u].s10 = [left.s10 + right.s10, left.s11 + right.s00].max
    tr[u].s11 = [left.s10 + right.s11, left.s11 + right.s01].max
  end

  modify = nil
  modify = lambda do |u, x, v|
    if tr[u].l == tr[u].r
      tr[u].s11 = [0, v].max
      return
    end
    mid = (tr[u].l + tr[u].r) >> 1
    if x <= mid
      modify.call(u << 1, x, v)
    else
      modify.call(u << 1 | 1, x, v)
    end
    pushup.call(u)
  end

  query = nil
  query = lambda do |u, l, r|
    return tr[u].s11 if tr[u].l >= l && tr[u].r <= r
    mid = (tr[u].l + tr[u].r) >> 1
    ans = 0
    ans = query.call(u << 1, l, r) if r <= mid
    ans = [ans, query.call(u << 1 | 1, l, r)].max if l > mid
    ans
  end

  build.call(1, 1, n)
  n.times { |i| modify.call(1, i + 1, nums[i]) }
  mod = 1_000_000_007
  ans = 0
  queries.each do |q|
    modify.call(1, q[0] + 1, q[1])
    ans = (ans + query.call(1, 1, n)) % mod
  end
  ans
end
''')

add("3167_better_compression_of_string", r'''
# LeetCode 3167 - Better Compression of String
# https://leetcode.com/problems/better-compression-of-string/

# @param {String} compressed
# @return {String}
def better_compression(compressed)
  cnt = Array.new(26, 0)
  n = compressed.length
  i = 0
  while i < n
    c = compressed[i]
    j = i + 1
    x = 0
    while j < n
      d = compressed[j]
      break if d < "0" || d > "9"
      x = x * 10 + (d.ord - 48)
      j += 1
    end
    cnt[c.ord - 97] += x
    i = j
  end
  ans = []
  26.times do |c|
    if cnt[c] > 0
      ans << (97 + c).chr
      ans << cnt[c].to_s
    end
  end
  ans.join
end
''')

add("3168_minimum_number_of_chairs_in_a_waiting_room", r'''
# LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

# @param {String} s
# @return {Integer}
def minimum_chairs(s)
  cnt = 0
  left = 0
  s.each_char do |c|
    if c == "E"
      if left > 0
        left -= 1
      else
        cnt += 1
      end
    else
      left += 1
    end
  end
  cnt
end
''')

add("3169_count_days_without_meetings", r'''
# LeetCode 3169 - Count Days Without Meetings
# https://leetcode.com/problems/count-days-without-meetings/

# @param {Integer} days
# @param {Integer[][]} meetings
# @return {Integer}
def count_days(days, meetings)
  meetings = meetings.sort_by { |e| e[0] }
  last = 0
  ans = 0
  meetings.each do |st, ed|
    ans += st - last - 1 if last < st
    last = [last, ed].max
  end
  ans + days - last
end
''')

add("3170_lexicographically_minimum_string_after_removing_stars", r'''
# LeetCode 3170 - Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

# @param {String} s
# @return {String}
def clear_stars(s)
  g = Array.new(26) { [] }
  n = s.length
  rem = Array.new(n, false)
  s.each_char.with_index do |ch, i|
    if ch == "*"
      rem[i] = true
      26.times do |j|
        if !g[j].empty?
          rem[g[j].pop] = true
          break
        end
      end
    else
      g[ch.ord - 97] << i
    end
  end
  n.times.select { |i| !rem[i] }.map { |i| s[i] }.join
end
''')


def main() -> None:
    written = 0
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        path.write_text(body, encoding="utf-8")
        written += 1
        print(f"wrote {name}")
    print(f"batch_d written={written}")


if __name__ == "__main__":
    main()
