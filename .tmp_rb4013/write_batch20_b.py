#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3744_find_kth_character_in_expanded_string", r'''
# LeetCode 3744 - Find Kth Character in Expanded String
# https://leetcode.com/problems/find-kth-character-in-expanded-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def kth_character(s, k)
  words = s.strip.split
  words.each do |w|
    m = (1 + w.length) * w.length / 2
    if k == m
      return " "
    elsif k > m
      k -= m + 1
    else
      cur = 0
      i = 0
      loop do
        cur += i + 1
        return w[i] if k < cur
        i += 1
      end
    end
  end
  " "
end
''')

add("3745_maximize_expression_of_three_elements", r'''
# LeetCode 3745 - Maximize Expression of Three Elements
# https://leetcode.com/problems/maximize-expression-of-three-elements/

# @param {Integer[]} nums
# @return {Integer}
def maximize_expression_of_three(nums)
  inf = 1 << 30
  a = -inf
  b = -inf
  c = inf
  nums.each do |x|
    c = x if x < c
    if x >= a
      b = a
      a = x
    elsif x > b
      b = x
    end
  end
  a + b - c
end
''')

add("3746_minimum_string_length_after_balanced_removals", r'''
# LeetCode 3746 - Minimum String Length After Balanced Removals
# https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

# @param {String} s
# @return {Integer}
def min_length_after_removals(s)
  a = s.each_char.count { |ch| ch == "a" }
  b = s.length - a
  (a - b).abs
end
''')

add("3747_count_distinct_integers_after_removing_zeros", r'''
# LeetCode 3747 - Count Distinct Integers After Removing Zeros
# https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

# @param {Integer} n
# @return {Integer}
def count_distinct(n)
  s = n.to_s
  m = s.length
  f = Array.new(20) { Array.new(2) { Array.new(2) { Array.new(2, -1) } } }
  dfs = nil
  dfs = lambda do |i, zero, lead, limit|
    if i == m
      return (zero == 0 && lead == 0) ? 1 : 0
    end
    return f[i][zero][lead][limit] if limit == 0 && f[i][zero][lead][limit] != -1
    up = limit == 1 ? (s[i].ord - 48) : 9
    ans = 0
    (0..up).each do |d|
      nxt_zero = zero
      nxt_zero = 1 if d == 0 && lead == 0
      nxt_lead = (lead == 1 && d == 0) ? 1 : 0
      nxt_limit = (limit == 1 && d == up) ? 1 : 0
      ans += dfs.call(i + 1, nxt_zero, nxt_lead, nxt_limit)
    end
    f[i][zero][lead][limit] = ans if limit == 0
    ans
  end
  dfs.call(0, 0, 1, 1)
end
''')

add("3748_count_stable_subarrays", r'''
# LeetCode 3748 - Count Stable Subarrays
# https://leetcode.com/problems/count-stable-subarrays/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def count_stable_subarrays(nums, queries)
  n = nums.length
  seg = []
  s = [0]
  l = 0
  (0...n).each do |r|
    if r == n - 1 || nums[r] > nums[r + 1]
      seg << l
      k = r - l + 1
      s << s[-1] + k * (k + 1) / 2
      l = r + 1
    end
  end
  lower_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(left, right), idx|
    i = lower_bound.call(seg, left + 1)
    j = lower_bound.call(seg, right + 1) - 1
    if i > j
      k = right - left + 1
      ans[idx] = k * (k + 1) / 2
    else
      a = seg[i] - left
      b = right - seg[j] + 1
      ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2
    end
  end
  ans
end
''')

add("3749_evaluate_valid_expressions", r'''
# LeetCode 3749 - Evaluate Valid Expressions
# https://leetcode.com/problems/evaluate-valid-expressions/

# @param {String} expression
# @return {Integer}
def evaluate_expression(expression)
  parse = nil
  parse = lambda do |i|
    ch = expression[i]
    if (ch >= "0" && ch <= "9") || ch == "-"
      j = i
      j += 1 if expression[j] == "-"
      j += 1 while j < expression.length && expression[j] >= "0" && expression[j] <= "9"
      return [expression[i...j].to_i, j]
    end
    j = i
    j += 1 while expression[j] != "("
    op = expression[i...j]
    j += 1
    p1 = parse.call(j)
    j = p1[1] + 1
    p2 = parse.call(j)
    j = p2[1] + 1
    res = 0
    case op
    when "add"
      res = p1[0] + p2[0]
    when "sub"
      res = p1[0] - p2[0]
    when "mul"
      res = p1[0] * p2[0]
    when "div"
      res = (p1[0].to_f / p2[0]).to_i
    end
    [res, j]
  end
  parse.call(0)[0]
end
''')

add("3750_minimum_number_of_flips_to_reverse_binary_string", r'''
# LeetCode 3750 - Minimum Number of Flips to Reverse Binary String
# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

# @param {Integer} n
# @return {Integer}
def minimum_flips(n)
  x = n
  if x == 0
    s = "0"
  else
    bits = []
    while x > 0
      bits << (48 + (x & 1)).chr
      x >>= 1
    end
    s = bits.reverse.join
  end
  m = s.length
  cnt = 0
  (0...(m / 2)).each { |i| cnt += 1 if s[i] != s[m - i - 1] }
  cnt * 2
end
''')

add("3751_total_waviness_of_numbers_in_range_i", r'''
# LeetCode 3751 - Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def total_waviness(num1, num2)
  f = lambda do |x|
    nums = []
    while x > 0
      nums << x % 10
      x /= 10
    end
    m = nums.length
    return 0 if m < 3
    s = 0
    (1...(m - 1)).each do |i|
      if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
         (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])
        s += 1
      end
    end
    s
  end
  ans = 0
  (num1..num2).each { |x| ans += f.call(x) }
  ans
end
''')

add("3752_lexicographically_smallest_negated_permutation_that_sums_to_target", r'''
# LeetCode 3752 - Lexicographically Smallest Negated Permutation That Sums to Target
# https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

# @param {Integer} n
# @param {Integer} target
# @return {Integer[]}
def lexicographically_smallest(n, target)
  total = n * (n + 1) / 2
  return [] if target < -total || target > total || (total - target).odd?
  remaining = (total - target) / 2
  negative = Array.new(n + 1, false)
  n.downto(1) do |value|
    if value <= remaining
      negative[value] = true
      remaining -= value
    end
  end
  answer = []
  n.downto(1) { |value| answer << -value if negative[value] }
  (1..n).each { |value| answer << value unless negative[value] }
  answer
end
''')

add("3753_total_waviness_of_numbers_in_range_ii", r'''
# LeetCode 3753 - Total Waviness of Numbers in Range II
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def total_waviness(a, b)
  waviness_up_to = lambda do |limit|
    return 0 if limit < 0
    digits = []
    if limit == 0
      digits << 0
    else
      value = limit
      while value > 0
        digits << value % 10
        value /= 10
      end
      digits.reverse!
    end
    memo = {}
    dfs = nil
    dfs = lambda do |position, second_last, last, started, tight|
      return [1, 0] if position == digits.length
      key = "#{position},#{second_last},#{last},#{started}"
      return memo[key] if !tight && memo.key?(key)
      upper = tight ? digits[position] : 9
      count = 0
      total = 0
      (0..upper).each do |digit|
        next_tight = tight && digit == upper
        next_second_last = second_last
        next_last = last
        next_started = started || digit != 0
        add = 0
        if !next_started
          next_second_last = next_last = 10
        elsif !started
          next_second_last = 10
          next_last = digit
        else
          if second_last != 10 &&
             ((last > second_last && last > digit) || (last < second_last && last < digit))
            add = 1
          end
          next_second_last = last
          next_last = digit
        end
        child_count, child_sum = dfs.call(position + 1, next_second_last, next_last, next_started, next_tight)
        count += child_count
        total += child_sum + add * child_count
      end
      memo[key] = [count, total] unless tight
      [count, total]
    end
    dfs.call(0, 10, 10, false, true)[1]
  end
  waviness_up_to.call(b) - waviness_up_to.call(a - 1)
end
''')

add("3754_concatenate_non_zero_digits_and_multiply_by_sum_i", r'''
# LeetCode 3754 - Concatenate Non Zero Digits and Multiply by Sum I
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

# @param {Integer} n
# @return {Integer}
def sum_and_multiply(n)
  p = 1
  x = 0
  s = 0
  while n > 0
    v = n % 10
    if v != 0
      s += v
      x += p * v
      p *= 10
    end
    n /= 10
  end
  x * s
end
''')

add("3755_find_maximum_balanced_xor_subarray_length", r'''
# LeetCode 3755 - Find Maximum Balanced XOR Subarray Length
# https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

# @param {Integer[]} nums
# @return {Integer}
def max_balanced_subarray(nums)
  d = {}
  a = 0
  b = nums.length
  ans = 0
  d[b] = -1
  nums.each_with_index do |x, i|
    a ^= x
    b += x.even? ? 1 : -1
    key = (a << 32) | (b & 0xFFFFFFFF)
    if d.key?(key)
      ans = [ans, i - d[key]].max
    else
      d[key] = i
    end
  end
  ans
end
''')

add("3756_concatenate_non_zero_digits_and_multiply_by_sum_ii", r'''
# LeetCode 3756 - Concatenate Non Zero Digits and Multiply by Sum II
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_and_multiply(s, queries)
  mx = 100001
  mod = 1_000_000_007
  pw = Array.new(mx, 0)
  pw[0] = 1
  (1...mx).each { |i| pw[i] = pw[i - 1] * 10 % mod }
  n = s.length
  sum_d = Array.new(n + 1, 0)
  cnt_n0 = Array.new(n + 1, 0)
  p = Array.new(n + 1, 0)
  (1..n).each do |i|
    d = s[i - 1].ord - 48
    sum_d[i] = sum_d[i - 1] + d
    cnt_n0[i] = cnt_n0[i - 1]
    if d > 0
      cnt_n0[i] += 1
      p[i] = (p[i - 1] * 10 + d) % mod
    else
      p[i] = p[i - 1]
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r), i|
    n0 = cnt_n0[r + 1] - cnt_n0[l]
    sd = sum_d[r + 1] - sum_d[l]
    x = (p[r + 1] - p[l] * pw[n0] % mod + mod) % mod
    ans[i] = x * sd % mod
  end
  ans
end
''')

add("3757_number_of_effective_subsequences", r'''
# LeetCode 3757 - Number of Effective Subsequences
# https://leetcode.com/problems/number-of-effective-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def count_effective_subsequences(nums)
  pop_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  mod = 1_000_000_007
  allv = 0
  nums.each { |x| allv |= x }
  bits = []
  (0...20).each { |b| bits << b if ((allv >> b) & 1) != 0 }
  m = bits.length
  freq = Array.new(1 << m, 0)
  nums.each do |x|
    mask = 0
    (0...m).each { |i| mask |= 1 << i if ((x >> bits[i]) & 1) != 0 }
    freq[mask] += 1
  end
  disjoint = freq.dup
  (0...m).each do |b|
    (0...(1 << m)).each do |mask|
      disjoint[mask] += disjoint[mask ^ (1 << b)] if ((mask >> b) & 1) != 0
    end
  end
  pow2 = Array.new(nums.length + 1, 0)
  pow2[0] = 1
  (1..nums.length).each { |i| pow2[i] = pow2[i - 1] * 2 % mod }
  ans = 0
  full = (1 << m) - 1
  (1..full).each do |s|
    ways = pow2[disjoint[full ^ s]]
    bc = pop_count.call(s)
    if bc.odd?
      ans += ways
      ans -= mod if ans >= mod
    else
      ans -= ways
      ans += mod if ans < 0
    end
  end
  ans
end
''')

add("3758_convert_number_words_to_digits", r'''
# LeetCode 3758 - Convert Number Words to Digits
# https://leetcode.com/problems/convert-number-words-to-digits/

# @param {String} s
# @return {String}
def convert_number(s)
  d = %w[zero one two three four five six seven eight nine]
  n = s.length
  ans = []
  i = 0
  while i < n
    (0...10).each do |j|
      m = d[j].length
      if i + m <= n && s[i, m] == d[j]
        ans << (48 + j).chr
        i += m - 1
        break
      end
    end
    i += 1
  end
  ans.join
end
''')

add("3759_count_elements_with_at_least_k_greater_values", r'''
# LeetCode 3759 - Count Elements with at Least K Greater Values
# https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_elements(nums, k)
  n = nums.length
  return n if k == 0
  a = nums.sort
  ans = 0
  (0...(n - k)).each { |i| ans += 1 if a[n - k] > a[i] }
  ans
end
''')

add("3760_maximum_substrings_with_distinct_start", r'''
# LeetCode 3760 - Maximum Substrings with Distinct Start
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/

# @param {String} s
# @return {Integer}
def max_distinct(s)
  cnt = Array.new(26, 0)
  ans = 0
  s.each_char do |c|
    i = c.ord - 97
    cnt[i] += 1
    ans += 1 if cnt[i] == 1
  end
  ans
end
''')

add("3761_minimum_absolute_distance_between_mirror_pairs", r'''
# LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

# @param {Integer[]} nums
# @return {Integer}
def min_mirror_pair_distance(nums)
  reverse = lambda do |x|
    y = 0
    while x > 0
      y = y * 10 + x % 10
      x /= 10
    end
    y
  end
  n = nums.length
  pos = {}
  ans = n + 1
  nums.each_with_index do |val, i|
    ans = [ans, i - pos[val]].min if pos.key?(val)
    pos[reverse.call(val)] = i
  end
  ans > n ? -1 : ans
end
''')

add("3762_minimum_operations_to_equalize_subarrays", r'''
# LeetCode 3762 - Minimum Operations to Equalize Subarrays
# https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

class EqNode
  attr_accessor :left, :right, :count, :sum

  def initialize(o = nil)
    if o
      @left = o.left
      @right = o.right
      @count = o.count
      @sum = o.sum
    else
      @left = 0
      @right = 0
      @count = 0
      @sum = 0
    end
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def min_operations(nums, k, queries)
  n = nums.length
  quotient = Array.new(n, 0)
  remainder = Array.new(n, 0)
  values = Array.new(n, 0)
  (0...n).each do |i|
    quotient[i] = nums[i] / k
    remainder[i] = nums[i] % k
    values[i] = quotient[i]
  end
  values.sort!
  vu = 1
  (1...n).each do |i|
    if values[i] != values[vu - 1]
      values[vu] = values[i]
      vu += 1
    end
  end
  values = values[0, vu]
  nodes = [EqNode.new]
  roots = Array.new(n + 1, 0)
  umax = values.length - 1
  lower_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  update = nil
  update = lambda do |previous, lo, hi, position, value|
    current = nodes.length
    nodes << EqNode.new(nodes[previous])
    nodes[current].count += 1
    nodes[current].sum += value
    if lo < hi
      mid = (lo + hi) >> 1
      if position <= mid
        nodes[current].left = update.call(nodes[previous].left, lo, mid, position, value)
      else
        nodes[current].right = update.call(nodes[previous].right, mid + 1, hi, position, value)
      end
    end
    current
  end
  kth = nil
  kth = lambda do |right_root, left_root, lo, hi, rank|
    return lo if lo == hi
    left_count = nodes[nodes[right_root].left].count - nodes[nodes[left_root].left].count
    mid = (lo + hi) >> 1
    return kth.call(nodes[right_root].left, nodes[left_root].left, lo, mid, rank) if rank <= left_count
    kth.call(nodes[right_root].right, nodes[left_root].right, mid + 1, hi, rank - left_count)
  end
  prefix_stats = nil
  prefix_stats = lambda do |right_root, left_root, lo, hi, ending|
    return [0, 0] if ending < lo
    if hi <= ending
      return [nodes[right_root].count - nodes[left_root].count, nodes[right_root].sum - nodes[left_root].sum]
    end
    mid = (lo + hi) >> 1
    count, total = prefix_stats.call(nodes[right_root].left, nodes[left_root].left, lo, mid, ending)
    if ending > mid
      rc, rs = prefix_stats.call(nodes[right_root].right, nodes[left_root].right, mid + 1, hi, ending)
      count += rc
      total += rs
    end
    [count, total]
  end
  (0...n).each do |i|
    position = lower_bound.call(values, quotient[i])
    roots[i + 1] = update.call(roots[i], 0, umax, position, quotient[i])
  end
  logv = Array.new(n + 1, 0)
  (2..n).each { |i| logv[i] = logv[i >> 1] + 1 }
  levels = logv[n] + 1
  min_table = Array.new(levels)
  max_table = Array.new(levels)
  min_table[0] = remainder.dup
  max_table[0] = remainder.dup
  (1...levels).each do |level|
    length = n - (1 << level) + 1
    min_table[level] = Array.new(length, 0)
    max_table[level] = Array.new(length, 0)
    half = 1 << (level - 1)
    (0...length).each do |i|
      min_table[level][i] = [min_table[level - 1][i], min_table[level - 1][i + half]].min
      max_table[level][i] = [max_table[level - 1][i], max_table[level - 1][i + half]].max
    end
  end
  answer = Array.new(queries.length, 0)
  queries.each_with_index do |(left, right), qi|
    length = right - left + 1
    level = logv[length]
    offset = right - (1 << level) + 1
    min_r = [min_table[level][left], min_table[level][offset]].min
    max_r = [max_table[level][left], max_table[level][offset]].max
    if min_r != max_r
      answer[qi] = -1
      next
    end
    median_index = kth.call(roots[right + 1], roots[left], 0, umax, (length + 1) / 2)
    median = values[median_index]
    left_count, left_sum = prefix_stats.call(roots[right + 1], roots[left], 0, umax, median_index)
    total_sum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum
    answer[qi] = median * left_count - left_sum + (total_sum - left_sum) - median * (length - left_count)
  end
  answer
end
''')

add("3763_maximum_total_sum_with_threshold_constraints", r'''
# LeetCode 3763 - Maximum Total Sum with Threshold Constraints
# https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

# @param {Integer[]} nums
# @param {Integer[]} threshold
# @return {Integer}
def max_sum(nums, threshold)
  n = nums.length
  idx = (0...n).to_a.sort_by { |i| threshold[i] }
  tree = []
  push = lambda do |x|
    tree << x
    i = tree.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if tree[i] <= tree[p]
      tree[i], tree[p] = tree[p], tree[i]
      i = p
    end
  end
  pop = lambda do
    top = tree[0]
    last = tree.pop
    if !tree.empty?
      tree[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = l + 1
        s = l if l < tree.length && tree[l] > tree[s]
        s = r if r < tree.length && tree[r] > tree[s]
        break if s == i
        tree[i], tree[s] = tree[s], tree[i]
        i = s
      end
    end
    top
  end
  ans = 0
  i = 0
  step = 1
  loop do
    while i < n && threshold[idx[i]] <= step
      push.call(nums[idx[i]])
      i += 1
    end
    break if tree.empty?
    ans += pop.call
    step += 1
  end
  ans
end
''')

add("3765_complete_prime_number", r'''
# LeetCode 3765 - Complete Prime Number
# https://leetcode.com/problems/complete-prime-number/

# @param {Integer} num
# @return {Boolean}
def complete_prime(num)
  is_prime = lambda do |x|
    return false if x < 2
    i = 2
    while i * i <= x
      return false if x % i == 0
      i += 1
    end
    true
  end
  s = num.to_s
  x = 0
  s.each_char do |c|
    x = x * 10 + (c.ord - 48)
    return false unless is_prime.call(x)
  end
  x = 0
  p = 1
  (s.length - 1).downto(0) do |i|
    x = p * (s[i].ord - 48) + x
    p *= 10
    return false unless is_prime.call(x)
  end
  true
end
''')

add("3766_minimum_operations_to_make_binary_palindrome", r'''
# LeetCode 3766 - Minimum Operations to Make Binary Palindrome
# https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

# @param {Integer[]} nums
# @return {Integer[]}
def min_operations(nums)
  pals = []
  nmax = 1 << 14
  is_palindrome = lambda do |s|
    m = s.length
    (0...(m / 2)).each { |i| return false if s[i] != s[m - 1 - i] }
    true
  end
  (0...nmax).each do |i|
    x = i
    if x == 0
      sb = "0"
    else
      bits = []
      while x > 0
        bits << (48 + (x & 1)).chr
        x >>= 1
      end
      sb = bits.reverse.join
    end
    pals << i if is_palindrome.call(sb)
  end
  lower_bound = lambda do |x|
    lo = 0
    hi = pals.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pals[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  ans = Array.new(nums.length, 0)
  nums.each_with_index do |x, k|
    it = lower_bound.call(x)
    t = 10**18
    t = pals[it] - x if it < pals.length
    t = [t, x - pals[it - 1]].min if it > 0
    ans[k] = t
  end
  ans
end
''')

add("3767_maximize_points_after_choosing_k_tasks", r'''
# LeetCode 3767 - Maximize Points After Choosing K Tasks
# https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

# @param {Integer[]} technique1
# @param {Integer[]} technique2
# @param {Integer} k
# @return {Integer}
def max_points(technique1, technique2, k)
  n = technique1.length
  idx = (0...n).to_a.sort_by { |i| -(technique1[i] - technique2[i]) }
  ans = technique2.sum
  (0...k).each do |i|
    index = idx[i]
    ans -= technique2[index]
    ans += technique1[index]
  end
  (k...n).each do |i|
    index = idx[i]
    if technique1[index] >= technique2[index]
      ans -= technique2[index]
      ans += technique1[index]
    end
  end
  ans
end
''')

add("3768_minimum_inversion_count_in_subarrays_of_fixed_length", r'''
# LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
# https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_inversion_count(nums, k)
  vals = nums.sort
  n = 0
  (0...vals.length).each do |i|
    if n == 0 || vals[i] != vals[n - 1]
      vals[n] = vals[i]
      n += 1
    end
  end
  vals = vals[0, n]
  bit = Array.new(vals.length + 1, 0)
  add = lambda do |i, delta|
    while i < bit.length
      bit[i] += delta
      i += i & -i
    end
  end
  sum_fn = lambda do |i|
    res = 0
    while i > 0
      res += bit[i]
      i -= i & -i
    end
    res
  end
  lower_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  rank = Array.new(nums.length, 0)
  inv = 0
  (0...nums.length).each do |i|
    rank[i] = lower_bound.call(vals, nums[i]) + 1
    if i < k
      inv += i - sum_fn.call(rank[i])
      add.call(rank[i], 1)
    end
  end
  best = inv
  (k...nums.length).each do |r|
    left = rank[r - k]
    inv -= sum_fn.call(left - 1)
    add.call(left, -1)
    inv += k - 1 - sum_fn.call(rank[r])
    add.call(rank[r], 1)
    best = inv if inv < best
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
