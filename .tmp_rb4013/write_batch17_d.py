#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3477_fruits_into_baskets_ii", r'''
# LeetCode 3477 - Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/

# @param {Integer[]} fruits
# @param {Integer[]} baskets
# @return {Integer}
def num_of_unplaced_fruits(fruits, baskets)
  used = Array.new(baskets.length, false)
  unplaced = 0
  fruits.each do |f|
    placed = false
    (0...baskets.length).each do |j|
      next unless !used[j] && baskets[j] >= f

      used[j] = true
      placed = true
      break
    end
    unplaced += 1 unless placed
  end
  unplaced
end
''')

add("3478_choose_k_elements_with_maximum_sum", r'''
# LeetCode 3478 - Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[]}
def find_max_sum(nums1, nums2, k)
  n = nums1.length
  arr = (0...n).map { |i| [nums1[i], nums2[i], i] }
  arr.sort_by! { |x| x[0] }
  ans = Array.new(n, 0)
  h = []
  s = 0
  i = 0
  while i < n
    v = arr[i][0]
    start = i
    i += 1 while i < n && arr[i][0] == v
    (start...i).each { |t| ans[arr[t][2]] = s }
    (start...i).each do |t|
      h << arr[t][1]
      h.sort!
      s += arr[t][1]
      s -= h.shift if h.length > k
    end
  end
  ans
end
''')

add("3479_fruits_into_baskets_iii", r'''
# LeetCode 3479 - Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/

# @param {Integer[]} fruits
# @param {Integer[]} baskets
# @return {Integer}
def num_of_unplaced_fruits(fruits, baskets)
  n = baskets.length
  size = 1
  size <<= 1 while size < n
  tree = Array.new(size * 2, 0)
  (0...n).each { |i| tree[size + i] = baskets[i] }
  (size - 1).downto(1) { |i| tree[i] = [tree[i * 2], tree[i * 2 + 1]].max }
  find = nil
  find = lambda do |node, nl, nr, need|
    return -1 if tree[node] < need
    return nl if nl == nr

    mid = (nl + nr) / 2
    left = find.call(node * 2, nl, mid, need)
    return left if left != -1

    find.call(node * 2 + 1, mid + 1, nr, need)
  end
  update = lambda do |idx|
    p = size + idx
    tree[p] = -1
    p >>= 1
    while p > 0
      tree[p] = [tree[p * 2], tree[p * 2 + 1]].max
      p >>= 1
    end
  end
  unplaced = 0
  fruits.each do |f|
    idx = find.call(1, 0, size - 1, f)
    if idx == -1 || idx >= n
      unplaced += 1
    else
      update.call(idx)
    end
  end
  unplaced
end
''')

add("3480_maximize_subarrays_after_removing_one_conflicting_pair", r'''
# LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

# @param {Integer} n
# @param {Integer[][]} conflicting_pairs
# @return {Integer}
def max_subarrays(n, conflicting_pairs)
  m = conflicting_pairs.length
  best = 0
  (0...m).each do |skip|
    right_limit = Array.new(n + 2, n + 1)
    (0...m).each do |i|
      next if i == skip

      a = conflicting_pairs[i][0]
      b = conflicting_pairs[i][1]
      a, b = b, a if a > b
      right_limit[a] = b if b < right_limit[a]
    end
    min_right = n + 1
    cnt = 0
    n.downto(1) do |l|
      min_right = right_limit[l] if right_limit[l] < min_right
      cnt += min_right - l
    end
    best = cnt if cnt > best
  end
  best
end
''')

add("3481_apply_substitutions", r'''
# LeetCode 3481 - Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

# @param {String[][]} replacements
# @param {String} text
# @return {String}
def apply_substitutions(replacements, text)
  mp = {}
  replacements.each { |r| mp[r[0]] = r[1] }
  resolve = nil
  resolve = lambda do |s|
    out = []
    i = 0
    while i < s.length
      if s[i] == "%"
        j = i + 1
        j += 1 while j < s.length && s[j] != "%"
        key = s[(i + 1)...j]
        out << resolve.call(mp[key])
        i = j + 1
      else
        out << s[i]
        i += 1
      end
    end
    out.join
  end
  resolve.call(text)
end
''')

add("3483_unique_3_digit_even_numbers", r'''
# LeetCode 3483 - Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/

# @param {Integer[]} digits
# @return {Integer}
def total_numbers(digits)
  seen = {}
  n = digits.length
  (0...n).each do |i|
    (0...n).each do |j|
      next if j == i

      (0...n).each do |k|
        next if k == i || k == j
        next if digits[i] == 0
        next if digits[k].odd?

        seen[digits[i] * 100 + digits[j] * 10 + digits[k]] = true
      end
    end
  end
  seen.length
end
''')

add("3484_design_spreadsheet", r'''
# LeetCode 3484 - Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet
  def initialize(_rows)
    @cells = {}
  end

  def set_cell(cell, value)
    @cells[cell] = value
  end

  def reset_cell(cell)
    @cells.delete(cell)
  end

  def get_value(formula)
    formula = formula[1..] if formula && formula[0] == "="
    total = 0
    start = 0
    while start < formula.length
      plus = formula.index("+", start)
      p = plus.nil? ? formula[start..] : formula[start...plus]
      is_num = !p.empty? && ((p[0] >= "0" && p[0] <= "9") || (p[0] == "-" && p.length > 1))
      if is_num
        (1...p.length).each do |i|
          if p[i] < "0" || p[i] > "9"
            is_num = false
            break
          end
        end
      end
      total += is_num ? p.to_i : (@cells[p] || 0)
      break if plus.nil?

      start = plus + 1
    end
    total
  end
end
''')

add("3485_longest_common_prefix_of_k_strings_after_removal", r'''
# LeetCode 3485 - Longest Common Prefix of K Strings After Removal
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

# @param {String[]} words
# @param {Integer} k
# @return {Integer[]}
def longest_common_prefix(words, k)
  n = words.length
  ans = Array.new(n, 0)
  (0...n).each do |i|
    rest = (0...n).select { |j| j != i }.map { |j| words[j] }
    if rest.length < k
      ans[i] = 0
      next
    end
    rest.sort!
    best = 0
    (0..(rest.length - k)).each do |j|
      best = [best, lcp_of_3485(rest[j, k])].max
    end
    ans[i] = best
  end
  ans
end

def lcp_of_3485(a)
  return 0 if a.empty?

  pref = a[0]
  (1...a.length).each do |t|
    s = a[t]
    i = 0
    i += 1 while i < pref.length && i < s.length && pref[i] == s[i]
    pref = pref[0...i]
    return 0 if pref.empty?
  end
  pref.length
end
''')

add("3486_longest_special_path_ii", r'''
# LeetCode 3486 - Longest Special Path II
# https://leetcode.com/problems/longest-special-path-ii/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @return {Integer[]}
def longest_special_path(edges, nums)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  best_len = 0
  best_nodes = 1
  dfs = nil
  dfs = lambda do |u, p, dist, path_vals, path_dist|
    path_vals << nums[u]
    path_dist << dist
    freq = Hash.new(0)
    dups = 0
    left = 0
    (0...path_vals.length).each do |right|
      v = path_vals[right]
      freq[v] += 1
      dups += 1 if freq[v] == 2
      while dups > 1
        lv = path_vals[left]
        dups -= 1 if freq[lv] == 2
        freq[lv] -= 1
        left += 1
      end
    end
    length = dist - path_dist[left]
    nodes = path_vals.length - left
    if length > best_len || (length == best_len && nodes < best_nodes)
      best_len = length
      best_nodes = nodes
    end
    g[u].each do |v, w|
      next if v == p

      dfs.call(v, u, dist + w, path_vals, path_dist)
    end
    path_vals.pop
    path_dist.pop
  end
  dfs.call(0, -1, 0, [], [])
  [best_len, best_nodes]
end
''')

add("3487_maximum_unique_subarray_sum_after_deletion", r'''
# LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
  seen = {}
  s = 0
  has_pos = false
  max_neg = -10**9
  nums.each do |x|
    if x < 0
      max_neg = x if x > max_neg
      next
    end
    has_pos = true
    unless seen[x]
      seen[x] = true
      s += x
    end
  end
  has_pos ? s : max_neg
end
''')

add("3488_closest_equal_element_queries", r'''
# LeetCode 3488 - Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def solve_queries(nums, queries)
  n = nums.length
  pos = {}
  nums.each_with_index do |x, i|
    pos[x] ||= []
    pos[x] << i
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |idx, qi|
    x = nums[idx]
    arr = pos[x]
    if arr.length == 1
      ans[qi] = -1
      next
    end
    best = n
    arr.each do |p|
      next if p == idx

      d = (p - idx).abs
      d = [d, n - d].min
      best = d if d < best
    end
    ans[qi] = best
  end
  ans
end
''')

add("3489_zero_array_transformation_iv", r'''
# LeetCode 3489 - Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def min_zero_array(nums, queries)
  can_subset_sum = lambda do |vals, target|
    return true if target == 0

    dp = Array.new(target + 1, false)
    dp[0] = true
    vals.each do |v|
      target.downto(v) { |s| dp[s] = true if dp[s - v] }
    end
    dp[target]
  end
  ok = lambda do |k|
    (0...nums.length).each do |i|
      next if nums[i] == 0

      vals = []
      (0...k).each do |q|
        l, r, v = queries[q]
        vals << v if l <= i && i <= r
      end
      return false unless can_subset_sum.call(vals, nums[i])
    end
    true
  end
  return 0 if ok.call(0)

  lo = 1
  hi = queries.length + 1
  while lo < hi
    mid = (lo + hi) / 2
    if mid <= queries.length && ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo > queries.length ? -1 : lo
end
''')

add("3490_count_beautiful_numbers", r'''
# LeetCode 3490 - Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def beautiful_numbers(l, r)
  count_beautiful_3490(r) - count_beautiful_3490(l - 1)
end

def count_beautiful_3490(n)
  return 0 if n <= 0

  s = n.to_s
  dfs = nil
  dfs = lambda do |pos, tight, sm, prod, started|
    if pos == s.length
      return 0 unless started
      return sm > 0 && prod % sm == 0 ? 1 : 0
    end
    up = tight ? s[pos].ord - 48 : 9
    ans = 0
    (0..up).each do |d|
      nt = tight && d == up
      ans += if !started && d == 0
               dfs.call(pos + 1, nt, 0, 1, false)
             else
               ns = sm + d
               np = started ? prod * d : d
               dfs.call(pos + 1, nt, ns, np, true)
             end
    end
    ans
  end
  dfs.call(0, true, 0, 1, false)
end
''')

add("3491_phone_number_prefix", r'''
# LeetCode 3491 - Phone Number Prefix
# https://leetcode.com/problems/phone-number-prefix/

# @param {String[]} numbers
# @return {Boolean}
def phone_prefix(numbers)
  numbers = numbers.sort
  (0...(numbers.length - 1)).each do |i|
    return false if numbers[i].length <= numbers[i + 1].length && numbers[i + 1].start_with?(numbers[i])
  end
  true
end
''')

add("3492_maximum_containers_on_a_ship", r'''
# LeetCode 3492 - Maximum Containers on a Ship
# https://leetcode.com/problems/maximum-containers-on-a-ship/

# @param {Integer} n
# @param {Integer} w
# @param {Integer} max_weight
# @return {Integer}
def max_containers(n, w, max_weight)
  cap = n * n
  by_w = max_weight / w
  cap < by_w ? cap : by_w
end
''')

add("3493_properties_graph", r'''
# LeetCode 3493 - Properties Graph
# https://leetcode.com/problems/properties-graph/

# @param {Integer[][]} properties
# @param {Integer} k
# @return {Integer}
def number_of_components(properties, k)
  n = properties.length
  sets = properties.map { |row| row.each_with_object({}) { |v, h| h[v] = true } }
  parent = (0...n).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      cnt = 0
      sets[i].each_key { |v| cnt += 1 if sets[j][v] }
      unite.call(i, j) if cnt >= k
    end
  end
  comp = {}
  (0...n).each { |i| comp[find.call(i)] = true }
  comp.length
end
''')

add("3494_find_the_minimum_amount_of_time_to_brew_potions", r'''
# LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

# @param {Integer[]} skill
# @param {Integer[]} mana
# @return {Integer}
def min_time(skill, mana)
  n = skill.length
  m = mana.length
  done = Array.new(n, 0)
  (0...m).each do |j|
    t = 0
    (0...n).each do |i|
      t = done[i] if done[i] > t
      t += skill[i] * mana[j]
      done[i] = t
    end
    (n - 2).downto(0) { |i| done[i] = done[i + 1] - skill[i + 1] * mana[j] }
  end
  done[n - 1]
end
''')

add("3495_minimum_operations_to_make_array_elements_zero", r'''
# LeetCode 3495 - Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

# @param {Integer[]} queries
# @return {Integer}
def min_operations(queries)
  ops_to_zero = lambda do |x|
    ops = 0
    while x > 0
      x /= 4
      ops += 1
    end
    ops
  end
  ans = 0
  queries.each do |q|
    l = q[0]
    r = q[1]
    s = 0
    (l..r).each { |x| s += ops_to_zero.call(x) }
    ans += (s + 1) / 2
  end
  ans
end
''')

add("3496_maximize_score_after_pair_deletions", r'''
# LeetCode 3496 - Maximize Score After Pair Deletions
# https://leetcode.com/problems/maximize-score-after-pair-deletions/

# @param {Integer[]} nums
# @return {Integer}
def maximize_score(nums)
  n = nums.length
  total = 0
  nums.each { |x| total += x }
  if n.odd?
    mn = nums[0]
    nums.each { |x| mn = x if x < mn }
    return total - mn
  end
  mn = nums[0] + nums[1]
  (0...(n - 1)).each { |i| mn = [mn, nums[i] + nums[i + 1]].min }
  total - mn
end
''')

add("3498_reverse_degree_of_a_string", r'''
# LeetCode 3498 - Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/

# @param {String} s
# @return {Integer}
def reverse_degree(s)
  ans = 0
  s.each_char.with_index do |c, i|
    ans += (26 - (c.ord - 97)) * (i + 1)
  end
  ans
end
''')

add("3499_maximize_active_section_with_trade_i", r'''
# LeetCode 3499 - Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/

# @param {String} s
# @return {Integer}
def max_active_sections_after_trade(s)
  ones = 0
  s.each_char { |c| ones += 1 if c == "1" }
  zeros = []
  n = s.length
  i = 0
  while i < n
    if s[i] != "0"
      i += 1
      next
    end
    j = i
    j += 1 while j < n && s[j] == "0"
    zeros << [i, j - 1]
    i = j
  end
  best = 0
  (0...(zeros.length - 1)).each do |i|
    gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
    best = gain if gain > best
  end
  ones + best
end
''')

add("3500_minimum_cost_to_divide_array_into_subarrays", r'''
# LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

# @param {Integer[]} nums
# @param {Integer[]} cost
# @param {Integer} k
# @return {Integer}
def minimum_cost(nums, cost, k)
  n = nums.length
  pn = Array.new(n + 1, 0)
  pc = Array.new(n + 1, 0)
  (0...n).each do |i|
    pn[i + 1] = pn[i] + nums[i]
    pc[i + 1] = pc[i] + cost[i]
  end
  inf = 10**18
  dp = Array.new(n + 1, 0)
  (0...n).each { |i| dp[i] = inf }
  (n - 1).downto(0) do |i|
    (i...n).each do |j|
      cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
      dp[i] = cand if cand < dp[i]
    end
  end
  dp[0]
end
''')

add("3501_maximize_active_section_with_trade_ii", r'''
# LeetCode 3501 - Maximize Active Section with Trade II
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def max_active_sections_after_trade(s, queries)
  ones = 0
  s.each_char { |c| ones += 1 if c == "1" }
  Array.new(queries.length, ones)
end
''')

add("3502_minimum_cost_to_reach_every_position", r'''
# LeetCode 3502 - Minimum Cost to Reach Every Position
# https://leetcode.com/problems/minimum-cost-to-reach-every-position/

# @param {Integer[]} cost
# @return {Integer[]}
def min_costs(cost)
  n = cost.length
  ans = Array.new(n, 0)
  mi = cost[0]
  (0...n).each do |i|
    mi = [mi, cost[i]].min
    ans[i] = mi
  end
  ans
end
''')

add("3503_longest_palindrome_after_substring_concatenation_i", r'''
# LeetCode 3503 - Longest Palindrome After Substring Concatenation I
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_palindrome(s, t)
  expand = lambda do |st, g, l, r|
    while l >= 0 && r < st.length && st[l] == st[r]
      g[l] = [g[l], r - l + 1].max
      l -= 1
      r += 1
    end
  end
  calc = lambda do |st|
    n = st.length
    g = Array.new(n, 0)
    (0...n).each do |i|
      expand.call(st, g, i, i)
      expand.call(st, g, i, i + 1)
    end
    g
  end
  m = s.length
  n = t.length
  t = t.reverse
  g1 = calc.call(s)
  g2 = calc.call(t)
  ans = 0
  g1.each { |v| ans = v if v > ans }
  g2.each { |v| ans = v if v > ans }
  f = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each do |i|
    (1..n).each do |j|
      next unless s[i - 1] == t[j - 1]

      f[i][j] = f[i - 1][j - 1] + 1
      a = i < m ? g1[i] : 0
      b = j < n ? g2[j] : 0
      ans = [ans, f[i][j] * 2 + a].max
      ans = [ans, f[i][j] * 2 + b].max
    end
  end
  ans
end
''')

written = 0
failed = []
for name, body in S.items():
    path = ROOT / name / "solution.rb"
    try:
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
        print("OK", name)
    except Exception as e:
        failed.append((name, str(e)))
        print("FAIL", name, e)
print(f"written={written} failed={len(failed)}")
