#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2146_k_highest_ranked_items_within_a_price_range", r'''
# LeetCode 2146 - K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

# @param {Integer[][]} grid
# @param {Integer[]} pricing
# @param {Integer[]} start
# @param {Integer} k
# @return {Integer[][]}
def highest_ranked_k_items(grid, pricing, start, k)
  m = grid.length
  n = grid[0].length
  low, high = pricing
  vis = Array.new(m) { Array.new(n, false) }
  q = [[start[0], start[1], 0]]
  vis[start[0]][start[1]] = true
  cands = []
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until q.empty?
    r, c, d = q.shift
    cands << [d, grid[r][c], r, c] if grid[r][c] >= low && grid[r][c] <= high
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0
        vis[nr][nc] = true
        q << [nr, nc, d + 1]
      end
    end
  end
  cands.sort!
  k = cands.length if k > cands.length
  (0...k).map { |i| [cands[i][2], cands[i][3]] }
end
''')

add("2147_number_of_ways_to_divide_a_long_corridor", r'''
# LeetCode 2147 - Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# @param {String} corridor
# @return {Integer}
def number_of_ways(corridor)
  mod = 1_000_000_007
  seats = []
  corridor.chars.each_with_index { |ch, i| seats << i if ch == "S" }
  return 0 if seats.empty? || seats.length.odd?

  ans = 1
  2.step(seats.length - 1, 2) { |i| ans = ans * (seats[i] - seats[i - 1]) % mod }
  ans
end
''')

add("2148_count_elements_with_strictly_smaller_and_greater_elements", r'''
# LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

# @param {Integer[]} nums
# @return {Integer}
def count_elements(nums)
  mn = nums.min
  mx = nums.max
  nums.count { |x| x > mn && x < mx }
end
''')

add("2149_rearrange_array_elements_by_sign", r'''
# LeetCode 2149 - Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
  ans = Array.new(nums.length)
  pos = 0
  neg = 1
  nums.each do |x|
    if x > 0
      ans[pos] = x
      pos += 2
    else
      ans[neg] = x
      neg += 2
    end
  end
  ans
end
''')

add("2150_find_all_lonely_numbers_in_the_array", r'''
# LeetCode 2150 - Find All Lonely Numbers in the Array
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_lonely(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  freq.filter_map { |k, v| k if v == 1 && !freq.key?(k - 1) && !freq.key?(k + 1) }
end
''')

add("2151_maximum_good_people_based_on_statements", r'''
# LeetCode 2151 - Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/

# @param {Integer[][]} statements
# @return {Integer}
def maximum_good(statements)
  n = statements.length
  ok = lambda do |mask|
    n.times do |i|
      next if (mask & (1 << i)).zero?

      n.times do |j|
        s = statements[i][j]
        next if s == 2

        good_j = (mask & (1 << j)) != 0
        return false if (s == 1 && !good_j) || (s == 0 && good_j)
      end
    end
    true
  end

  ans = 0
  (1 << n).times do |mask|
    next unless ok.call(mask)

    bc = 0
    x = mask
    while x > 0
      bc += x & 1
      x >>= 1
    end
    ans = [ans, bc].max
  end
  ans
end
''')

add("2152_minimum_number_of_lines_to_cover_points", r'''
# LeetCode 2152 - Minimum Number of Lines to Cover Points
# https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

# @param {Integer[][]} points
# @return {Integer}
def minimum_lines(points)
  n = points.length
  return 1 if n <= 2

  colinear = lambda do |a, b, c|
    (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
  end
  inf = n
  dp = Array.new(1 << n, inf)
  dp[0] = 0
  (1 << n).times do |mask|
    next if dp[mask] == inf

    i = 0
    i += 1 while i < n && (mask & (1 << i)) != 0
    next if i == n

    nm = mask | (1 << i)
    dp[nm] = [dp[nm], dp[mask] + 1].min
    ((i + 1)...n).each do |j|
      next if (mask & (1 << j)) != 0

      nm = mask | (1 << i) | (1 << j)
      n.times do |k|
        nm |= 1 << k if (nm & (1 << k)).zero? && colinear.call(points[i], points[j], points[k])
      end
      dp[nm] = [dp[nm], dp[mask] + 1].min
    end
  end
  dp[(1 << n) - 1]
end
''')

add("2154_keep_multiplying_found_values_by_two", r'''
# LeetCode 2154 - Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
  have = {}
  nums.each { |x| have[x] = true }
  original *= 2 while have[original]
  original
end
''')

add("2155_all_divisions_with_the_highest_score_of_a_binary_array", r'''
# LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

# @param {Integer[]} nums
# @return {Integer[]}
def max_score_indices(nums)
  n = nums.length
  total1 = nums.sum
  best = total1
  left0 = 0
  right1 = total1
  ans = [0]
  n.times do |i|
    if nums[i] == 0
      left0 += 1
    else
      right1 -= 1
    end
    score = left0 + right1
    if score > best
      best = score
      ans = [i + 1]
    elsif score == best
      ans << i + 1
    end
  end
  ans
end
''')

add("2156_find_substring_with_given_hash_value", r'''
# LeetCode 2156 - Find Substring With Given Hash Value
# https://leetcode.com/problems/find-substring-with-given-hash-value/

# @param {String} s
# @param {Integer} power
# @param {Integer} modulo
# @param {Integer} k
# @param {Integer} hash_value
# @return {String}
def sub_str_hash(s, power, modulo, k, hash_value)
  n = s.length
  pk = 1
  (k - 1).times { pk = pk * power % modulo }
  h = 0
  ans = 0
  (n - 1).downto(n - k) do |i|
    h = (h * power + (s[i].ord - 96)) % modulo
  end
  ans = n - k if h == hash_value
  (n - k - 1).downto(0) do |i|
    h = (h - (s[i + k].ord - 96) * pk % modulo + modulo) % modulo
    h = (h * power + (s[i].ord - 96)) % modulo
    ans = i if h == hash_value
  end
  s[ans, k]
end
''')

add("2157_groups_of_strings", r'''
# LeetCode 2157 - Groups of Strings
# https://leetcode.com/problems/groups-of-strings/

# @param {String[]} words
# @return {Integer[]}
def group_strings(words)
  parent = {}
  size = {}
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb

    ra, rb = rb, ra if size[ra] < size[rb]
    parent[rb] = ra
    size[ra] += size[rb]
  end
  mask_of = lambda do |w|
    m = 0
    w.each_byte { |b| m |= 1 << (b - 97) }
    m
  end

  freq = Hash.new(0)
  words.each { |w| freq[mask_of.call(w)] += 1 }
  freq.each do |k, v|
    parent[k] = k
    size[k] = v
  end
  freq.each_key do |m|
    26.times do |b|
      if (m & (1 << b)) != 0
        nm = m ^ (1 << b)
        unite.call(m, nm) if freq.key?(nm)
        26.times do |a|
          if (nm & (1 << a)).zero?
            rm = nm | (1 << a)
            unite.call(m, rm) if freq.key?(rm)
          end
        end
      else
        nm = m | (1 << b)
        unite.call(m, nm) if freq.key?(nm)
      end
    end
  end
  groups = 0
  max_size = 0
  seen = {}
  freq.each_key do |m|
    r = find.call(m)
    next if seen[r]

    seen[r] = true
    groups += 1
    max_size = [max_size, size[r]].max
  end
  [groups, max_size]
end
''')

add("2158_amount_of_new_area_painted_each_day", r'''
# LeetCode 2158 - Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/

# @param {Integer[][]} paint
# @return {Integer[]}
def amount_painted(paint)
  ans = Array.new(paint.length, 0)
  line = Array.new(50_001, 0)
  paint.each_with_index do |(start, finish), i|
    j = start
    while j < finish
      if line[j] == 0
        ans[i] += 1
        line[j] = finish
        j += 1
      else
        nxt = line[j]
        line[j] = [finish, nxt].max
        j = nxt
      end
    end
  end
  ans
end
''')

add("2160_minimum_sum_of_four_digit_number_after_splitting_digits", r'''
# LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

# @param {Integer} num
# @return {Integer}
def minimum_sum(num)
  d = [num / 1000, num / 100 % 10, num / 10 % 10, num % 10].sort
  10 * d[0] + d[2] + 10 * d[1] + d[3]
end
''')

add("2161_partition_array_according_to_given_pivot", r'''
# LeetCode 2161 - Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

# @param {Integer[]} nums
# @param {Integer} pivot
# @return {Integer[]}
def pivot_array(nums, pivot)
  ans = Array.new(nums.length)
  i = 0
  nums.each do |x|
    if x < pivot
      ans[i] = x
      i += 1
    end
  end
  nums.each do |x|
    if x == pivot
      ans[i] = x
      i += 1
    end
  end
  nums.each do |x|
    if x > pivot
      ans[i] = x
      i += 1
    end
  end
  ans
end
''')

add("2162_minimum_cost_to_set_cooking_time", r'''
# LeetCode 2162 - Minimum Cost to Set Cooking Time
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

# @param {Integer} start_at
# @param {Integer} move_cost
# @param {Integer} push_cost
# @param {Integer} target_seconds
# @return {Integer}
def min_cost_set_time(start_at, move_cost, push_cost, target_seconds)
  cost = lambda do |mins, secs|
    return (2**53 - 1) / 2 if mins < 0 || mins > 99 || secs < 0 || secs > 99

    s = if mins > 0
          mins.to_s + (secs / 10).to_s + (secs % 10).to_s
        else
          secs.to_s
        end
    cur = start_at.to_s
    ans = 0
    s.each_char do |c|
      if c != cur
        ans += move_cost
        cur = c
      end
      ans += push_cost
    end
    ans
  end

  mins = target_seconds / 60
  secs = target_seconds % 60
  ans = cost.call(mins, secs)
  ans = [ans, cost.call(mins - 1, secs + 60)].min if mins > 0
  ans
end
''')

add("2163_minimum_difference_in_sums_after_removal_of_elements", r'''
# LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
  n = nums.length / 3
  left = Array.new(nums.length, 0)
  right = Array.new(nums.length, 0)
  hmax = []
  push_max = lambda do |x|
    hmax << x
    i = hmax.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if hmax[p] >= hmax[i]

      hmax[p], hmax[i] = hmax[i], hmax[p]
      i = p
    end
  end
  pop_max = lambda do
    top = hmax[0]
    last = hmax.pop
    if hmax.empty?
      return top
    end

    hmax[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      s = i
      s = l if l < hmax.length && hmax[l] > hmax[s]
      s = r if r < hmax.length && hmax[r] > hmax[s]
      break if s == i

      hmax[s], hmax[i] = hmax[i], hmax[s]
      i = s
    end
    top
  end

  sum = 0
  n.times do |i|
    push_max.call(nums[i])
    sum += nums[i]
  end
  left[n - 1] = sum
  (n...(2 * n)).each do |i|
    push_max.call(nums[i])
    sum += nums[i]
    sum -= pop_max.call
    left[i] = sum
  end

  hmin = []
  push_min = lambda do |x|
    hmin << x
    i = hmin.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if hmin[p] <= hmin[i]

      hmin[p], hmin[i] = hmin[i], hmin[p]
      i = p
    end
  end
  pop_min = lambda do
    top = hmin[0]
    last = hmin.pop
    if hmin.empty?
      return top
    end

    hmin[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      s = i
      s = l if l < hmin.length && hmin[l] < hmin[s]
      s = r if r < hmin.length && hmin[r] < hmin[s]
      break if s == i

      hmin[s], hmin[i] = hmin[i], hmin[s]
      i = s
    end
    top
  end

  sum = 0
  (nums.length - 1).downto(2 * n) do |i|
    push_min.call(nums[i])
    sum += nums[i]
  end
  right[2 * n] = sum
  (2 * n - 1).downto(n) do |i|
    push_min.call(nums[i])
    sum += nums[i]
    sum -= pop_min.call
    right[i] = sum
  end
  ans = left[n - 1] - right[n]
  (n...(2 * n)).each { |i| ans = [ans, left[i] - right[i + 1]].min }
  ans
end
''')

add("2164_sort_even_and_odd_indices_independently", r'''
# LeetCode 2164 - Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_even_odd(nums)
  even = []
  odd = []
  nums.each_with_index do |x, i|
    if i.even?
      even << x
    else
      odd << x
    end
  end
  even.sort!
  odd.sort!.reverse!
  ei = 0
  oi = 0
  nums.each_index do |i|
    if i.even?
      nums[i] = even[ei]
      ei += 1
    else
      nums[i] = odd[oi]
      oi += 1
    end
  end
  nums
end
''')

add("2165_smallest_value_of_the_rearranged_number", r'''
# LeetCode 2165 - Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

# @param {Integer} num
# @return {Integer}
def smallest_number(num)
  neg = num < 0
  num = -num if neg
  return 0 if num == 0

  digits = []
  while num > 0
    digits << num % 10
    num /= 10
  end
  if neg
    digits.sort!.reverse!
    ans = 0
    digits.each { |d| ans = ans * 10 + d }
    return -ans
  end
  digits.sort!
  if digits[0] == 0
    (1...digits.length).each do |i|
      next if digits[i] == 0

      digits[0], digits[i] = digits[i], digits[0]
      break
    end
  end
  res = 0
  digits.each { |d| res = res * 10 + d }
  res
end
''')

written = 0
for folder, body in S.items():
    (ROOT / folder / "solution.rb").write_text(body, encoding="utf-8")
    written += 1
    print(f"wrote {folder}")
print(f"written={written}")
