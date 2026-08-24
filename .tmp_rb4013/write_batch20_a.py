#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3719_longest_balanced_subarray_i", r'''
# LeetCode 3719 - Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/

# @param {Integer[]} nums
# @return {Integer}
def longest_balanced(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    vis = {}
    cnt = [0, 0]
    (i...n).each do |j|
      unless vis[nums[j]]
        vis[nums[j]] = true
        cnt[nums[j] & 1] += 1
      end
      ans = [ans, j - i + 1].max if cnt[0] == cnt[1]
    end
  end
  ans
end
''')

add("3720_lexicographically_smallest_permutation_greater_than_target", r'''
# LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

# @param {String} s
# @param {String} target
# @return {String}
def lex_greater_permutation(s, target)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  n = s.length
  ans = Array.new(n, "")
  dfs = nil
  dfs = lambda do |pos, greater|
    return greater if pos == n
    start = greater ? 0 : (target[pos].ord - 97)
    (start...26).each do |c|
      next if cnt[c] == 0
      cnt[c] -= 1
      ans[pos] = (97 + c).chr
      ng = greater || c > (target[pos].ord - 97)
      return true if dfs.call(pos + 1, ng)
      cnt[c] += 1
    end
    false
  end
  return ans.join if dfs.call(0, false)
  ""
end
''')

add("3721_longest_balanced_subarray_ii", r'''
# LeetCode 3721 - Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/

class LbNode
  attr_accessor :l, :r, :mn, :mx, :lazy

  def initialize
    @l = 0
    @r = 0
    @mn = 0
    @mx = 0
    @lazy = 0
  end
end

class LbSegmentTree
  def initialize(n)
    @tr = Array.new(n << 2) { LbNode.new }
    build(1, 0, n)
  end

  def build(u, l, r)
    tr = @tr
    tr[u].l = l
    tr[u].r = r
    tr[u].mn = 0
    tr[u].mx = 0
    tr[u].lazy = 0
    return if l == r
    mid = (l + r) >> 1
    build(u << 1, l, mid)
    build((u << 1) | 1, mid + 1, r)
  end

  def apply(u, v)
    @tr[u].mn += v
    @tr[u].mx += v
    @tr[u].lazy += v
  end

  def pushup(u)
    tr = @tr
    tr[u].mn = [tr[u << 1].mn, tr[(u << 1) | 1].mn].min
    tr[u].mx = [tr[u << 1].mx, tr[(u << 1) | 1].mx].max
  end

  def pushdown(u)
    if @tr[u].lazy != 0
      v = @tr[u].lazy
      apply(u << 1, v)
      apply((u << 1) | 1, v)
      @tr[u].lazy = 0
    end
  end

  def modify(u, l, r, v)
    tr = @tr
    if tr[u].l >= l && tr[u].r <= r
      apply(u, v)
      return
    end
    pushdown(u)
    mid = (tr[u].l + tr[u].r) >> 1
    modify(u << 1, l, r, v) if l <= mid
    modify((u << 1) | 1, l, r, v) if r > mid
    pushup(u)
  end

  def query(u, target)
    tr = @tr
    return tr[u].l if tr[u].l == tr[u].r
    pushdown(u)
    left = u << 1
    right = (u << 1) | 1
    return query(left, target) if tr[left].mn <= target && target <= tr[left].mx
    query(right, target)
  end
end

# @param {Integer[]} nums
# @return {Integer}
def longest_balanced(nums)
  n = nums.length
  st = LbSegmentTree.new(n)
  last = {}
  now = 0
  ans = 0
  (1..n).each do |i|
    x = nums[i - 1]
    det = (x & 1) != 0 ? 1 : -1
    if last.key?(x)
      st.modify(1, last[x], n, -det)
      now -= det
    end
    last[x] = i
    st.modify(1, i, n, det)
    now += det
    pos = st.query(1, now)
    ans = [ans, i - pos].max
  end
  ans
end
''')

add("3722_lexicographically_smallest_string_after_reverse", r'''
# LeetCode 3722 - Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

# @param {String} s
# @return {String}
def lex_smallest(s)
  ans = s
  n = s.length
  reverse = lambda do |a, l, r|
    i = l
    j = r - 1
    while i < j
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
    end
  end
  (1..n).each do |k|
    a1 = s.chars
    reverse.call(a1, 0, k)
    t1 = a1.join
    a2 = s.chars
    reverse.call(a2, n - k, n)
    t2 = a2.join
    ans = t1 if t1 < ans
    ans = t2 if t2 < ans
  end
  ans
end
''')

add("3723_maximize_sum_of_squares_of_digits", r'''
# LeetCode 3723 - Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

# @param {Integer} num
# @param {Integer} sum
# @return {String}
def max_sum_of_squares(num, sum)
  return "" if num * 9 < sum
  k, rem = sum.divmod(9)
  ans = "9" * k
  ans += (48 + rem).chr if rem > 0
  ans += "0" while ans.length < num
  ans
end
''')

add("3724_minimum_operations_to_transform_array", r'''
# LeetCode 3724 - Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
  ans = 1
  n = nums1.length
  ok = false
  d = 1 << 30
  (0...n).each do |i|
    x = [nums1[i], nums2[i]].max
    y = [nums1[i], nums2[i]].min
    ans += x - y
    d = [d, [(x - nums2[n]).abs, (y - nums2[n]).abs].min].min
    ok = true if nums2[n] >= y && nums2[n] <= x
  end
  ans += d unless ok
  ans
end
''')

add("3725_count_ways_to_choose_coprime_integers_from_rows", r'''
# LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

# @param {Integer[][]} mat
# @return {Integer}
def count_coprime(mat)
  mod = 1_000_000_007
  m = mat.length
  dp = Hash.new(0)
  mat[0].each { |v| dp[v] += 1 }
  (1...m).each do |i|
    ndp = Hash.new(0)
    mat[i].each do |v|
      dp.each do |key, val|
        ng = key.gcd(v)
        ndp[ng] = (ndp[ng] + val) % mod
      end
    end
    dp = ndp
  end
  dp[1]
end
''')

add("3726_remove_zeros_in_decimal_representation", r'''
# LeetCode 3726 - Remove Zeros in Decimal Representation
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/

# @param {Integer} n
# @return {Integer}
def remove_zeros(n)
  ans = 0
  k = 1
  while n > 0
    x = n % 10
    if x > 0
      ans = k * x + ans
      k *= 10
    end
    n /= 10
  end
  ans
end
''')

add("3727_maximum_alternating_sum_of_squares", r'''
# LeetCode 3727 - Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

# @param {Integer[]} nums
# @return {Integer}
def max_alternating_sum(nums)
  a = nums.map { |x| x * x }.sort
  m = a.length / 2
  ans = 0
  (0...m).each { |i| ans -= a[i] }
  (m...a.length).each { |i| ans += a[i] }
  ans
end
''')

add("3728_stable_subarrays_with_equal_boundary_and_interior_sum", r'''
# LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
# https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

# @param {Integer[]} capacity
# @return {Integer}
def count_stable_subarrays(capacity)
  n = capacity.length
  s = Array.new(n + 1, 0)
  (1..n).each { |i| s[i] = s[i - 1] + capacity[i - 1] }
  cnt = Hash.new(0)
  ans = 0
  (2...n).each do |r|
    l = r - 2
    key_l = [capacity[l], capacity[l] + s[l + 1]]
    cnt[key_l] += 1
    key_r = [capacity[r], s[r]]
    ans += cnt[key_r]
  end
  ans
end
''')

add("3729_count_distinct_subarrays_divisible_by_k_in_sorted_array", r'''
# LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def num_good_subarrays(nums, k)
  ans = 0
  s = 0
  cnt = Hash.new(0)
  cnt[0] = 1
  nums.each do |x|
    s = (s + x) % k
    ans += cnt[s]
    cnt[s] += 1
  end
  n = nums.length
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && nums[j] == nums[i]
    m = j - i
    (1..m).each do |h|
      ans -= m - h if (nums[i] * h) % k == 0
    end
    i = j
  end
  ans
end
''')

add("3730_maximum_calories_burnt_from_jumps", r'''
# LeetCode 3730 - Maximum Calories Burnt from Jumps
# https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

# @param {Integer[]} heights
# @return {Integer}
def max_calories_burnt(heights)
  heights = heights.sort
  ans = 0
  pre = 0
  l = 0
  r = heights.length - 1
  while l < r
    d1 = heights[r] - pre
    ans += d1 * d1
    d2 = heights[l] - heights[r]
    ans += d2 * d2
    pre = heights[l]
    l += 1
    r -= 1
  end
  d = heights[r] - pre
  ans += d * d
  ans
end
''')

add("3731_find_missing_elements", r'''
# LeetCode 3731 - Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def find_missing_elements(nums)
  mn = 100
  mx = 0
  s = {}
  nums.each do |x|
    mn = [mn, x].min
    mx = [mx, x].max
    s[x] = true
  end
  ans = []
  ((mn + 1)...mx).each { |x| ans << x unless s[x] }
  ans
end
''')

add("3732_maximum_product_of_three_elements_after_one_replacement", r'''
# LeetCode 3732 - Maximum Product of Three Elements After One Replacement
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  a = nums.sort
  n = a.length
  aa, bb, cc, dd = a[0], a[1], a[n - 2], a[n - 1]
  x = 100000
  [aa * bb * x, cc * dd * x, -aa * dd * x].max
end
''')

add("3733_minimum_time_to_complete_all_deliveries", r'''
# LeetCode 3733 - Minimum Time to Complete All Deliveries
# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

# @param {Integer[]} d
# @param {Integer[]} r
# @return {Integer}
def minimum_time(d, r)
  ok = lambda do |t|
    w0 = t - t / r[0]
    w1 = t - t / r[1]
    w0 + w1 >= d[0] + d[1]
  end
  lo = 1
  hi = 10**18
  while lo < hi
    mid = lo + (hi - lo) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
''')

add("3734_lexicographically_smallest_palindromic_permutation_greater_than_target", r'''
# LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

# @param {String} s
# @param {String} target
# @return {String}
def lex_palindromic_permutation(s, target)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  odd = 0
  mid = -1
  (0...26).each do |i|
    if cnt[i].odd?
      odd += 1
      mid = i
    end
  end
  return "" if odd > 1
  half = (0...26).map { |i| cnt[i] / 2 }
  n = s.length
  half_len = n / 2
  left = Array.new(half_len, "")
  dfs = nil
  dfs = lambda do |pos, greater|
    if pos == half_len
      return greater if mid < 0
      return true if greater
      return (97 + mid).chr > target[half_len]
    end
    start = greater ? 0 : (target[pos].ord - 97)
    (start...26).each do |c|
      next if half[c] == 0
      half[c] -= 1
      left[pos] = (97 + c).chr
      return true if dfs.call(pos + 1, greater || c > (target[pos].ord - 97))
      half[c] += 1
    end
    false
  end
  return "" unless dfs.call(0, false)
  res = left.join
  res += (97 + mid).chr if mid >= 0
  (half_len - 1).downto(0) { |i| res += left[i] }
  return "" if res <= target
  res
end
''')

add("3735_lexicographically_smallest_string_after_reverse_ii", r'''
# LeetCode 3735 - Lexicographically Smallest String After Reverse II
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

# @param {String} s
# @return {String}
def lex_smallest(s)
  n = s.length
  best = s
  reverse = lambda do |a, l, r|
    i = l
    j = r - 1
    while i < j
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
    end
  end
  (1..n).each do |i|
    t = s.chars
    reverse.call(t, 0, i)
    ts = t.join
    best = ts if ts < best
  end
  (0...n).each do |i|
    t = s.chars
    reverse.call(t, i, n)
    ts = t.join
    best = ts if ts < best
  end
  best
end
''')

add("3736_minimum_moves_to_equal_array_elements_iii", r'''
# LeetCode 3736 - Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

# @param {Integer[]} nums
# @return {Integer}
def min_moves(nums)
  mx = 0
  s = 0
  nums.each do |x|
    mx = [mx, x].max
    s += x
  end
  mx * nums.length - s
end
''')

add("3737_count_subarrays_with_majority_element_i", r'''
# LeetCode 3737 - Count Subarrays With Majority Element I
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    cnt = 0
    (i...n).each do |j|
      cnt += 1 if nums[j] == target
      ans += 1 if cnt * 2 > j - i + 1
    end
  end
  ans
end
''')

add("3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element", r'''
# LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
# https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  n = nums.length
  left = Array.new(n, 1)
  right = Array.new(n, 1)
  (1...n).each { |i| left[i] = left[i - 1] + 1 if nums[i] >= nums[i - 1] }
  (n - 2).downto(0) { |i| right[i] = right[i + 1] + 1 if nums[i] <= nums[i + 1] }
  ans = left.max
  (0...n).each do |i|
    a = i > 0 ? left[i - 1] : 0
    b = i + 1 < n ? right[i + 1] : 0
    if i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]
      ans = [ans, a + 1, b + 1].max
    else
      ans = [ans, a + b + 1].max
    end
  end
  ans
end
''')

add("3739_count_subarrays_with_majority_element_ii", r'''
# LeetCode 3739 - Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class MajorityBit
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

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  n = nums.length
  tree = MajorityBit.new(2 * n + 1)
  s = n + 1
  tree.update(s, 1)
  ans = 0
  nums.each do |x|
    s += x == target ? 1 : -1
    ans += tree.query(s - 1)
    tree.update(s, 1)
  end
  ans
end
''')

add("3740_minimum_distance_between_three_equal_elements_i", r'''
# LeetCode 3740 - Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_distance(nums)
  g = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index { |x, i| g[x] << i }
  inf = 1 << 30
  ans = inf
  g.each_value do |ls|
    m = ls.length
    (0...(m - 2)).each { |h| ans = [ans, (ls[h + 2] - ls[h]) * 2].min }
  end
  ans == inf ? -1 : ans
end
''')

add("3741_minimum_distance_between_three_equal_elements_ii", r'''
# LeetCode 3741 - Minimum Distance Between Three Equal Elements II
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

# @param {Integer[]} nums
# @return {Integer}
def minimum_distance(nums)
  g = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index { |x, i| g[x] << i }
  inf = 1 << 30
  ans = inf
  g.each_value do |ls|
    m = ls.length
    (0...(m - 2)).each { |h| ans = [ans, (ls[h + 2] - ls[h]) * 2].min }
  end
  ans == inf ? -1 : ans
end
''')

add("3742_maximum_path_score_in_a_grid", r'''
# LeetCode 3742 - Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def max_path_score(grid, k)
  inf = 1 << 30
  m = grid.length
  n = grid[0].length
  f = Array.new(m) { Array.new(n) { Array.new(k + 1, -1) } }
  dfs = nil
  dfs = lambda do |i, j, kk|
    return -inf if i < 0 || j < 0 || kk < 0
    return 0 if i == 0 && j == 0
    return f[i][j][kk] if f[i][j][kk] != -1
    res = grid[i][j]
    nk = kk
    nk -= 1 if grid[i][j] != 0
    a = dfs.call(i - 1, j, nk)
    b = dfs.call(i, j - 1, nk)
    res += [a, b].max
    f[i][j][kk] = res
    res
  end
  ans = dfs.call(m - 1, n - 1, k)
  ans < 0 ? -1 : ans
end
''')

add("3743_maximize_cyclic_partition_score", r'''
# LeetCode 3743 - Maximize Cyclic Partition Score
# https://leetcode.com/problems/maximize-cyclic-partition-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  n = nums.length
  a = nums + nums
  k = n if k > n
  best = 0
  neg = -(10**18)
  (0...n).each do |start|
    seg = a[start, n]
    dp = Array.new(n + 1) { Array.new(k + 1, neg) }
    dp[0][0] = 0
    (1..n).each do |i|
      (1..[k, i].min).each do |j|
        mx = neg
        i.downto(j) do |t|
          mx = seg[t - 1] if seg[t - 1] > mx
          if dp[t - 1][j - 1] > neg
            cand = dp[t - 1][j - 1] + mx
            dp[i][j] = cand if cand > dp[i][j]
          end
        end
      end
    end
    best = dp[n][k] if dp[n][k] > best
  end
  best
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
