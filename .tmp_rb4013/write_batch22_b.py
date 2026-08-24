#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("3946_maximum_number_of_items_from_sale_i", r'''
# LeetCode 3946 - Maximum Number Of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

# @param {Integer[][]} items
# @param {Integer} budget
# @return {Integer}
def maximum_sale_items(items, budget)
  f = Array.new(budget + 1, 0)
  mn = 2_147_483_647
  items.each do |item|
    factor, price = item[0], item[1]
    mn = price if price < mn
    cnt = items.count { |j_item| j_item[0] % factor == 0 }
    budget.downto(price) do |j|
      v = f[j - price] + cnt
      f[j] = v if v > f[j]
    end
  end
  ans = 0
  (0..budget).each do |i|
    extra = (budget - i) / mn
    v = f[i] + extra
    ans = v if v > ans
  end
  ans
end
''')

add("3947_maximum_number_of_items_from_sale_ii", r'''
# LeetCode 3947 - Maximum Number of Items From Sale II
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

# @param {Integer[][]} items
# @param {Integer} budget
# @return {Integer}
def max_items(items, budget)
  n = items.length
  frequency = Array.new(n + 1, 0)
  minimum_price = items[0][1]
  items.each do |item|
    frequency[item[0]] += 1
    minimum_price = item[1] if item[1] < minimum_price
  end
  batches = []
  items.each do |item|
    gain = 0
    multiple = item[0]
    while multiple <= n
      gain += frequency[multiple]
      multiple += item[0]
    end
    gain -= 1
    batches << [item[1], gain] if gain > 0 && item[1] < 2 * minimum_price
  end
  batches.sort_by! { |a| a[0] }
  remaining = budget
  answer = budget / minimum_price
  boosted = 0
  batches.each do |current|
    count = current[1]
    affordable = remaining / current[0]
    count = affordable if affordable < count
    remaining -= count * current[0]
    boosted += count
    total = 2 * boosted + remaining / minimum_price
    answer = total if total > answer
    break if count < current[1]
  end
  answer
end
''')

add("3948_lexicographically_maximum_mex_array", r'''
# LeetCode 3948 - Lexicographically Maximum MEX Array
# https://leetcode.com/problems/lexicographically-maximum-mex-array/

# @param {Integer[]} nums
# @return {Integer[]}
def max_mex_array(nums)
  n = nums.length
  remaining = Array.new(n + 2, 0)
  nums.each { |x| remaining[x] += 1 if x <= n + 1 }
  mex = 0
  mex += 1 while remaining[mex] > 0
  answer = []
  seen = Array.new(n + 2, 0)
  stamp = 0
  index = 0
  while index < n
    if mex == 0
      answer << 0
      x = nums[index]
      remaining[x] -= 1 if x <= n + 1
      index += 1
      next
    end
    stamp += 1
    need = mex
    while need > 0
      x = nums[index]
      if x < mex && seen[x] != stamp
        seen[x] = stamp
        need -= 1
      end
      remaining[x] -= 1 if x <= n + 1
      index += 1
    end
    answer << mex
    mex = 0
    mex += 1 while remaining[mex] > 0
  end
  answer
end
''')

add("3949_subtree_inversion_sum_ii", r'''
# LeetCode 3949 - Subtree Inversion Sum II
# https://leetcode.com/problems/subtree-inversion-sum-ii/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subtree_inversion_sum(edges, nums, k)
  n = nums.length
  graph = Array.new(n) { [] }
  edges.each do |edge|
    graph[edge[0]] << edge[1]
    graph[edge[1]] << edge[0]
  end
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  infinity = 2**60
  maximum = Array.new(n)
  minimum = Array.new(n)
  (n - 1).downto(0) do |oi|
    u = order[oi]
    current_max = Array.new(k + 1, -infinity)
    current_min = Array.new(k + 1, infinity)
    current_max[k] = current_min[k] = nums[u]
    graph[u].each do |v|
      next if parent[v] != u
      next_max = Array.new(k + 1, -infinity)
      next_min = Array.new(k + 1, infinity)
      (0..k).each do |first|
        next if current_max[first] == -infinity
        (0..k).each do |child_distance|
          next if maximum[v][child_distance] == -infinity
          second = child_distance + 1
          second = k if second > k
          next if first < k && second < k && first + second < k
          distance = [first, second].min
          max_value = current_max[first] + maximum[v][child_distance]
          min_value = current_min[first] + minimum[v][child_distance]
          next_max[distance] = max_value if max_value > next_max[distance]
          next_min[distance] = min_value if min_value < next_min[distance]
        end
      end
      current_max = next_max
      current_min = next_min
    end
    current_max[0] = -current_min[k] if -current_min[k] > current_max[0]
    current_min[0] = -current_max[k] if -current_max[k] < current_min[0]
    maximum[u] = current_max
    minimum[u] = current_min
  end
  answer = -(2**60)
  maximum[0].each { |value| answer = value if value > answer }
  answer
end
''')

add("3950_exactly_one_consecutive_set_bits_pair", r'''
# LeetCode 3950 - Exactly One Consecutive Set Bits Pair
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

# @param {Integer} n
# @return {Boolean}
def consecutive_set_bits(n)
  vis = false
  pre = 0
  while n > 0
    cur = n & 1
    if pre == cur && cur == 1
      return false if vis
      vis = true
    end
    pre = cur
    n >>= 1
  end
  vis
end
''')

add("3951_minimum_energy_to_maintain_brightness", r'''
# LeetCode 3951 - Minimum Energy To Maintain Brightness
# https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

# @param {Integer} n
# @param {Integer} brightness
# @param {Integer[][]} intervals
# @return {Integer}
def min_energy(n, brightness, intervals)
  intervals.sort_by! { |a| a[0] }
  merged = [[intervals[0][0], intervals[0][1]]]
  (1...intervals.length).each do |i|
    x = intervals[i]
    last = merged[-1]
    if last[1] < x[0]
      merged << [x[0], x[1]]
    elsif x[1] > last[1]
      last[1] = x[1]
    end
  end
  ans = 0
  merged.each do |interval|
    m = interval[1] - interval[0] + 1
    ans += ((brightness + 2) / 3) * m
  end
  ans
end
''')

add("3952_maximum_total_value_of_covered_indices", r'''
# LeetCode 3952 - Maximum Total Value of Covered Indices
# https://leetcode.com/problems/maximum-total-value-of-covered-indices/

# @param {Integer[]} nums
# @param {String} s
# @return {Integer}
def max_total_value(nums, s)
  answer = 0
  i = 0
  while i < s.length
    if s[i] == "0"
      i += 1
      next
    end
    start = i
    i += 1 while i < s.length && s[i] == "1"
    finish = i - 1
    if start == 0
      (start..finish).each { |index| answer += nums[index] }
      next
    end
    minimum = nums[start - 1]
    total = 0
    ((start - 1)..finish).each do |index|
      total += nums[index]
      minimum = nums[index] if nums[index] < minimum
    end
    answer += total - minimum
  end
  answer
end
''')

add("3953_maximum_score_with_co_prime_element", r'''
# LeetCode 3953 - Maximum Score with Co-Prime Element
# https://leetcode.com/problems/maximum-score-with-co-prime-element/

# @param {Integer[]} nums
# @param {Integer} max_val
# @return {Integer}
def max_score(nums, max_val)
  bad_count = lambda do |x, divisible|
    primes = []
    y = x
    p = 2
    while p * p <= y
      if y % p == 0
        primes << p
        y /= p while y % p == 0
      end
      p += 1
    end
    primes << y if y > 1
    bad = 0
    psz = primes.length
    (1...(1 << psz)).each do |mask|
      product = 1
      bits = 0
      psz.times do |i|
        if ((mask >> i) & 1) != 0
          product *= primes[i]
          bits += 1
        end
      end
      if bits.odd?
        bad += divisible[product]
      else
        bad -= divisible[product]
      end
    end
    bad
  end
  evaluate = lambda do |x, exists, checked, divisible|
    return -2_147_483_648 / 4 if checked[x]
    checked[x] = true
    bad = bad_count.call(x, divisible)
    cost = if exists
             x > 1 ? bad - 1 : 0
           else
             bad > 0 ? bad : 1
           end
    x - cost
  end
  limit = max_val
  frequency = Array.new(100001, 0)
  nums.each do |x|
    frequency[x] += 1
    limit = x if x > limit
  end
  divisible = Array.new(limit + 1, 0)
  (1..limit).each do |d|
    multiple = d
    while multiple <= limit
      divisible[d] += frequency[multiple] if multiple < frequency.length
      multiple += d
    end
  end
  best = -nums.length
  checked = Array.new(limit + 1, false)
  (1..max_val).each do |x|
    v = evaluate.call(x, x < frequency.length && frequency[x] > 0, checked, divisible)
    best = v if v > best
  end
  nums.each do |x|
    v = evaluate.call(x, true, checked, divisible)
    best = v if v > best
  end
  best
end
''')

add("3954_sum_of_compatible_numbers_in_range_i", r'''
# LeetCode 3954 - Sum Of Compatible Numbers In Range I
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def sum_of_good_integers(n, k)
  start = [1, n - k].max
  finish = n + k
  ans = 0
  (start..finish).each { |x| ans += x if (n & x) == 0 }
  ans
end
''')

add("3955_valid_binary_strings_with_cost_limit", r'''
# LeetCode 3955 - Valid Binary Strings With Cost Limit
# https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

# @param {Integer} n
# @param {Integer} k
# @return {String[]}
def generate_valid_strings(n, k)
  ans = []
  path = []
  dfs = nil
  dfs = lambda do |i, tot|
    if i >= n
      ans << path.join
      return
    end
    path << "0"
    dfs.call(i + 1, tot)
    path.pop
    if (path.empty? || path[-1] == "0") && tot + i <= k
      path << "1"
      dfs.call(i + 1, tot + i)
      path.pop
    end
  end
  dfs.call(0, 0)
  ans
end
''')

add("3956_maximum_sum_of_m_non_overlapping_subarrays_i", r'''
# LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def max_sum(nums, m, l, r)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  dp = Array.new(n + 1, 0)
  best_selected = -(2**62)
  (1..m).each do |_count|
    nxt = dp.dup
    deque = []
    (1..n).each do |ending|
      add_index = ending - l
      if add_index >= 0
        value = dp[add_index] - prefix[add_index]
        while !deque.empty?
          last = deque[-1]
          break if dp[last] - prefix[last] > value
          deque.pop
        end
        deque << add_index
      end
      min_index = ending - r
      deque.shift while !deque.empty? && deque[0] < min_index
      unless deque.empty?
        candidate = prefix[ending] + dp[deque[0]] - prefix[deque[0]]
        nxt[ending] = candidate if candidate > nxt[ending]
        best_selected = candidate if candidate > best_selected
      end
      nxt[ending] = nxt[ending - 1] if nxt[ending - 1] > nxt[ending]
    end
    dp = nxt
  end
  best_selected
end
''')

add("3957_maximum_sum_of_m_non_overlapping_subarrays_ii", r'''
# LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

class State
  attr_accessor :value, :count

  def initialize(value = 0, count = 0)
    @value = value
    @count = count
  end
end

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def max_sum(nums, m, l, r)
  better = lambda { |a, b| a.value > b.value || (a.value == b.value && a.count > b.count) }
  candidate_better = lambda do |dp, prefix, a, b|
    left = State.new(dp[a].value - prefix[a], dp[a].count)
    right = State.new(dp[b].value - prefix[b], dp[b].count)
    better.call(left, right)
  end
  run = lambda do |prefix, n, l, r, penalty|
    dp = Array.new(n + 1) { State.new }
    deque = []
    (1..n).each do |ending|
      add_index = ending - l
      if add_index >= 0
        deque.pop while !deque.empty? && candidate_better.call(dp, prefix, add_index, deque[-1])
        deque << add_index
      end
      min_index = ending - r
      deque.shift while !deque.empty? && deque[0] < min_index
      dp[ending] = State.new(dp[ending - 1].value, dp[ending - 1].count)
      unless deque.empty?
        start = deque[0]
        take = State.new(dp[start].value + prefix[ending] - prefix[start] - penalty, dp[start].count + 1)
        dp[ending] = take if better.call(take, dp[ending])
      end
    end
    dp[n]
  end
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  unconstrained = run.call(prefix, n, l, r, 0)
  return unconstrained.value if unconstrained.count > 0 && unconstrained.count <= m
  if unconstrained.count > m
    bound = nums.sum { |value| value >= 0 ? value : -value }
    low = 0
    high = bound + 1
    while low < high
      mid = low + (high - low + 1) / 2
      if run.call(prefix, n, l, r, mid).count >= m
        low = mid
      else
        high = mid - 1
      end
    end
    state = run.call(prefix, n, l, r, low)
    return state.value + low * m
  end
  infinity = 2**60
  best_single = -infinity
  deque = []
  (1..n).each do |ending|
    add_index = ending - l
    if add_index >= 0
      deque.pop while !deque.empty? && prefix[deque[-1]] >= prefix[add_index]
      deque << add_index
    end
    min_index = ending - r
    deque.shift while !deque.empty? && deque[0] < min_index
    unless deque.empty?
      s = prefix[ending] - prefix[deque[0]]
      best_single = s if s > best_single
    end
  end
  best_single
end
''')

add("3958_minimum_cost_to_split_into_ones_ii", r'''
# LeetCode 3958 - Minimum Cost To Split Into Ones II
# https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

# @param {Integer} n
# @return {Integer}
def min_cost(n)
  n * (n - 1) / 2
end
''')

add("3959_check_good_integer", r'''
# LeetCode 3959 - Check Good Integer
# https://leetcode.com/problems/check-good-integer/

# @param {Integer} n
# @return {Boolean}
def check_good_integer(n)
  s = 0
  while n > 0
    x = n % 10
    s += x * (x - 1)
    n /= 10
  end
  s >= 50
end
''')

add("3960_frequency_balance_subarray", r'''
# LeetCode 3960 - Frequency Balance Subarray
# https://leetcode.com/problems/frequency-balance-subarray/

# @param {Integer[]} nums
# @return {Integer}
def get_length(nums)
  n = nums.length
  ans = 1
  n.times do |l|
    cnt = {}
    freq = {}
    (l...n).each do |r|
      x = nums[r]
      c = cnt.fetch(x, 0)
      if freq.fetch(c, 0) > 0
        fc = freq[c] - 1
        if fc == 0
          freq.delete(c)
        else
          freq[c] = fc
        end
      end
      cnt[x] = c + 1
      freq[cnt[x]] = freq.fetch(cnt[x], 0) + 1
      cx = cnt[x]
      if cnt.length == 1 || (freq.length == 2 && (freq.fetch(cx * 2, 0) > 0 || (cx.even? && freq.fetch(cx / 2, 0) > 0)))
        ans = r - l + 1 if r - l + 1 > ans
      end
    end
  end
  ans
end
''')

add("3961_maximize_sum_of_device_ratings", r'''
# LeetCode 3961 - Maximize Sum Of Device Ratings
# https://leetcode.com/problems/maximize-sum-of-device-ratings/

# @param {Integer[][]} units
# @return {Integer}
def max_ratings(units)
  n = units[0].length
  if n == 1
    ans = 0
    units.each { |x| ans += x[0] }
    return ans
  end
  answer = 0
  mn = 2_147_483_647
  mn2 = 2_147_483_647
  units.each do |x|
    x = x.sort
    answer += x[1]
    mn2 = x[1] if x[1] < mn2
    mn = x[0] if x[0] < mn
  end
  answer - (mn2 - mn)
end
''')

add("3962_maximum_subarray_sum_after_at_most_k_swaps", r'''
# LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
# https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  unique = nums.sort
  u = 0
  unique.each_with_index do |v, i|
    if u == 0 || v != unique[u - 1]
      unique[u] = v
      u += 1
    end
  end
  unique = unique[0...u]
  n = nums.length
  lower_bound = lambda do |a, x|
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
  add = lambda do |count, s, index, delta|
    value = unique[index - 1]
    while index < count.length
      count[index] += delta
      s[index] += delta * value
      index += index & -index
    end
  end
  query_count = lambda do |bit, index|
    result = 0
    while index > 0
      result += bit[index]
      index -= index & -index
    end
    result
  end
  query_sum = lambda do |bit, index|
    result = 0
    while index > 0
      result += bit[index]
      index -= index & -index
    end
    result
  end
  kth = lambda do |bit, order|
    index = 0
    step = 1
    step <<= 1 while (step << 1) < bit.length
    while step > 0
      nxt = index + step
      if nxt < bit.length && bit[nxt] < order
        index = nxt
        order -= bit[nxt]
      end
      step >>= 1
    end
    index + 1
  end
  sum_smallest = lambda do |count, s, amount|
    return 0 if amount <= 0
    index = kth.call(count, amount)
    count_before = query_count.call(count, index - 1)
    sum_before = query_sum.call(s, index - 1)
    sum_before + (amount - count_before) * unique[index - 1]
  end
  rank = Array.new(n, 0)
  global_count = Array.new(unique.length + 1, 0)
  global_sum = Array.new(unique.length + 1, 0)
  n.times do |i|
    rank[i] = lower_bound.call(unique, nums[i]) + 1
    add.call(global_count, global_sum, rank[i], 1)
  end
  answer = -(1 << 60)
  n.times do |left|
    inside_count = Array.new(unique.length + 1, 0)
    inside_sum = Array.new(unique.length + 1, 0)
    outside_count = global_count.dup
    outside_sum = global_sum.dup
    subarray_sum = 0
    (left...n).each do |right|
      add.call(outside_count, outside_sum, rank[right], -1)
      add.call(inside_count, inside_sum, rank[right], 1)
      subarray_sum += nums[right]
      inside_size = right - left + 1
      outside_size = n - inside_size
      limit = [k, [inside_size, outside_size].min].min
      low = 0
      high = limit
      while low < high
        mid = (low + high + 1) / 2
        inside_value = unique[kth.call(inside_count, mid) - 1]
        outside_order = outside_size - mid + 1
        outside_value = unique[kth.call(outside_count, outside_order) - 1]
        if outside_value > inside_value
          low = mid
        else
          high = mid - 1
        end
      end
      swaps = low
      gain = 0
      if swaps > 0
        small_inside = sum_smallest.call(inside_count, inside_sum, swaps)
        total_outside = query_sum.call(outside_sum, unique.length)
        large_outside = total_outside - sum_smallest.call(outside_count, outside_sum, outside_size - swaps)
        gain = large_outside - small_inside
      end
      v = subarray_sum + gain
      answer = v if v > answer
    end
  end
  answer
end
''')

add("3963_create_grid_with_exactly_one_path", r'''
# LeetCode 3963 - Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

# @param {Integer} m
# @param {Integer} n
# @return {String[]}
def create_grid(m, n)
  g = []
  m.times do |i|
    row = Array.new(n, "#")
    n.times { |j| row[j] = "." } if i == 0
    row[n - 1] = "."
    g << row.join
  end
  g
end
''')

add("3964_minimum_lights_to_illuminate_a_road", r'''
# LeetCode 3964 - Minimum Lights To Illuminate A Road
# https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

# @param {Integer[]} lights
# @return {Integer}
def min_lights(lights)
  n = lights.length
  d = Array.new(n, 0)
  n.times do |i|
    v = lights[i]
    next unless v > 0
    l = [0, i - v].max
    r = [n - 1, i + v].min
    d[l] += 1
    d[r + 1] -= 1 if r + 1 < n
  end
  s = 0
  cnt = 0
  ans = 0
  d.each do |x|
    s += x
    if s == 0
      cnt += 1
    else
      ans += (cnt + 2) / 3
      cnt = 0
    end
  end
  ans += (cnt + 2) / 3
  ans
end
''')

add("3965_finish_time_of_tasks_i", r'''
# LeetCode 3965 - Finish Time Of Tasks I
# https://leetcode.com/problems/finish-time-of-tasks-i/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} base_time
# @return {Integer}
def finish_time(n, edges, base_time)
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << e[1] }
  dfs = nil
  dfs = lambda do |i|
    return base_time[i] if g[i].empty?
    inf = 1 << 62
    earliest = inf
    latest = -inf
    g[i].each do |j|
      a = dfs.call(j)
      earliest = a if a < earliest
      latest = a if a > latest
    end
    own_duration = (latest - earliest) + base_time[i]
    latest + own_duration
  end
  dfs.call(0)
end
''')

add("3966_count_good_integers_in_a_range", r'''
# LeetCode 3966 - Count Good Integers in a Range
# https://leetcode.com/problems/count-good-integers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def count_good_integers(l, r, k)
  dfs = nil
  dfs = lambda do |position, previous, started, tight, digits, k, memo|
    return started ? 1 : 0 if position == digits.length
    key = [position, previous, started]
    return memo[key] if !tight && memo.key?(key)
    limit = tight ? digits[position].ord - 48 : 9
    result = 0
    (0..limit).each do |digit|
      next_started = started || digit != 0
      next if started && (previous - digit).abs > k
      next_previous = next_started ? digit : previous
      result += dfs.call(position + 1, next_previous, next_started, tight && digit == limit, digits, k, memo)
    end
    memo[key] = result unless tight
    result
  end
  count = lambda do |bound, k|
    return 0 if bound <= 0
    digits = bound.to_s
    dfs.call(0, 0, false, true, digits, k, {})
  end
  count.call(r, k) - count.call(l - 1, k)
end
''')

add("3967_finish_time_of_tasks_ii", r'''
# LeetCode 3967 - Finish Time of Tasks II
# https://leetcode.com/problems/finish-time-of-tasks-ii/

class Edge
  attr_accessor :to, :reverse

  def initialize(to, reverse)
    @to = to
    @reverse = reverse
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} base_time
# @return {Integer}
def min_finish_time(n, edges, base_time)
  combine = lambda do |minimum, maximum, count, base|
    return base if count == 0
    2 * maximum - minimum + base
  end
  graph = Array.new(n) { [] }
  edges.each do |edge|
    u, v = edge[0], edge[1]
    iu = graph[u].length
    iv = graph[v].length
    graph[u] << Edge.new(v, iv)
    graph[v] << Edge.new(u, iu)
  end
  parent = Array.new(n, -2)
  parent_edge = Array.new(n, 0)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    graph[u].each do |edge|
      if parent[edge.to] == -2
        parent[edge.to] = u
        parent_edge[edge.to] = edge.reverse
        order << edge.to
      end
    end
    i += 1
  end
  incoming = Array.new(n) { |i| Array.new(graph[i].length, 0) }
  (n - 1).downto(1) do |oi|
    u = order[oi]
    minimum = 2**62
    maximum = -1
    count = 0
    incoming[u].each_index do |edge_index|
      next if edge_index == parent_edge[u]
      value = incoming[u][edge_index]
      minimum = value if value < minimum
      maximum = value if value > maximum
      count += 1
    end
    value = combine.call(minimum, maximum, count, base_time[u])
    parent_node = parent[u]
    reverse_index = graph[u][parent_edge[u]].reverse
    incoming[parent_node][reverse_index] = value
  end
  answer = 2**62
  order.each do |u|
    min1 = 2**62
    min2 = 2**62
    min_index = -1
    max1 = -1
    max2 = -1
    max_index = -1
    incoming[u].each_with_index do |value, i|
      if value < min1
        min2 = min1
        min1 = value
        min_index = i
      elsif value < min2
        min2 = value
      end
      if value > max1
        max2 = max1
        max1 = value
        max_index = i
      elsif value > max2
        max2 = value
      end
    end
    root_value = combine.call(min1, max1, graph[u].length, base_time[u])
    answer = root_value if root_value < answer
    graph[u].each_with_index do |edge, i|
      next if edge.to == parent[u]
      if graph[u].length == 1
        incoming[edge.to][edge.reverse] = base_time[u]
        next
      end
      minimum = min1
      maximum = max1
      minimum = min2 if i == min_index
      maximum = max2 if i == max_index
      incoming[edge.to][edge.reverse] = combine.call(minimum, maximum, graph[u].length - 1, base_time[u])
    end
  end
  answer
end
''')

add("3968_maximum_manhattan_distance_after_all_moves", r'''
# LeetCode 3968 - Maximum Manhattan Distance After All Moves
# https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

# @param {String} moves
# @return {Integer}
def max_distance(moves)
  x = 0
  y = 0
  z = 0
  moves.each_char do |c|
    case c
    when "U" then x -= 1
    when "D" then x += 1
    when "L" then y -= 1
    when "R" then y += 1
    else z += 1
    end
  end
  x.abs + y.abs + z
end
''')

for name, body in S.items():
    path = ROOT / name / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {name}")

print(f"TOTAL {len(S)}")
