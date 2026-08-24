#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2727_is_object_empty"] = r'''# LeetCode 2727 - Is Object Empty
# https://leetcode.com/problems/is-object-empty/

# @param {Object} obj
# @return {Boolean}
def is_empty(obj)
  obj.respond_to?(:empty?) ? obj.empty? : obj.nil?
end
'''

FILES["2728_count_houses_in_a_circular_street"] = r'''# LeetCode 2728 - Count Houses in a Circular Street
# https://leetcode.com/problems/count-houses-in-a-circular-street/

class Street
  def initialize(doors)
    @doors = doors
    @i = 0
  end

  def closeDoor
    @doors[@i] = 0
  end

  def openDoor
    @doors[@i] = 1
  end

  def isDoorOpen
    @doors[@i] == 1
  end

  def moveRight
    @i = (@i + 1) % @doors.length
  end
end

# @param {Object} street
# @param {Integer} k
# @return {Integer}
def house_count(street, k)
  street = Street.new(street) if street.is_a?(Array)
  k.times do
    street.closeDoor
    street.moveRight
  end
  ans = 0
  loop do
    ans += 1
    street.openDoor
    street.moveRight
    break if street.isDoorOpen
  end
  ans
end
'''

FILES["2729_check_if_the_number_is_fascinating"] = r'''# LeetCode 2729 - Check if The Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/

# @param {Integer} n
# @return {Boolean}
def is_fascinating(n)
  s = n.to_s + (2 * n).to_s + (3 * n).to_s
  return false if s.length != 9
  cnt = Array.new(10, 0)
  s.each_char { |c| cnt[c.ord - 48] += 1 }
  return false if cnt[0] != 0
  (1...10).each { |i| return false if cnt[i] != 1 }
  true
end
'''

FILES["2730_find_the_longest_semi_repetitive_substring"] = r'''# LeetCode 2730 - Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

# @param {String} s
# @return {Integer}
def longest_semi_repetitive_substring(s)
  ans = 0
  left = 0
  last_pair = -1
  (0...s.length).each do |right|
    if right > 0 && s[right] == s[right - 1]
      left = last_pair + 1 if last_pair >= left
      last_pair = right - 1
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
'''

FILES["2731_movement_of_robots"] = r'''# LeetCode 2731 - Movement of Robots
# https://leetcode.com/problems/movement-of-robots/

# @param {Integer[]} nums
# @param {String} s
# @param {Integer} d
# @return {Integer}
def sum_distance(nums, s, d)
  mod = 1_000_000_007
  n = nums.length
  pos = (0...n).map { |i| nums[i] + (s[i] == "R" ? d : -d) }
  pos.sort!
  ans = 0
  pref = 0
  (0...n).each do |i|
    ans = (ans + ((pos[i] * i - pref) % mod + mod) % mod) % mod
    pref += pos[i]
  end
  (ans % mod + mod) % mod
end
'''

FILES["2732_find_a_good_subset_of_the_matrix"] = r'''# LeetCode 2732 - Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

# @param {Integer[][]} grid
# @return {Integer[]}
def good_subsetof_binary_matrix(grid)
  n = grid[0].length
  first = {}
  grid.each_with_index do |row, i|
    mask = 0
    (0...n).each { |j| mask |= 1 << j if row[j] == 1 }
    return [i] if mask == 0
    first.each do |pm, idx|
      if (pm & mask) == 0
        return idx < i ? [idx, i] : [i, idx]
      end
    end
    first[mask] = i unless first.key?(mask)
  end
  []
end
'''

FILES["2733_neither_minimum_nor_maximum"] = r'''# LeetCode 2733 - Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/

# @param {Integer[]} nums
# @return {Integer}
def find_non_min_or_max(nums)
  return -1 if nums.length < 3
  a, b, c = nums[0], nums[1], nums[2]
  a + b + c - [a, b, c].max - [a, b, c].min
end
'''

FILES["2734_lexicographically_smallest_string_after_substring_operation"] = r'''# LeetCode 2734 - Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

# @param {String} s
# @return {String}
def smallest_string(s)
  arr = s.chars
  n = arr.length
  i = 0
  i += 1 while i < n && arr[i] == "a"
  if i == n
    arr[n - 1] = "z"
    return arr.join
  end
  while i < n && arr[i] != "a"
    arr[i] = (arr[i].ord - 1).chr
    i += 1
  end
  arr.join
end
'''

FILES["2735_collecting_chocolates"] = r'''# LeetCode 2735 - Collecting Chocolates
# https://leetcode.com/problems/collecting-chocolates/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_cost(nums, x)
  n = nums.length
  best = nums.dup
  ans = nums.sum
  (1...n).each do |rot|
    cur = rot * x
    (0...n).each do |i|
      best[i] = [best[i], nums[(i + rot) % n]].min
      cur += best[i]
    end
    ans = [ans, cur].min
  end
  ans
end
'''

FILES["2736_maximum_sum_queries"] = r'''# LeetCode 2736 - Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_sum_queries(nums1, nums2, queries)
  n = nums1.length
  pts = (0...n).map { |i| [nums1[i], nums2[i], nums1[i] + nums2[i]] }
  pts.sort_by! { |p| -p[0] }
  qs = queries.each_with_index.map { |q, i| [q[0], q[1], i] }
  qs.sort_by! { |q| -q[0] }
  ys = (nums2 + qs.map { |q| q[1] }).sort
  uniq = []
  ys.each { |y| uniq << y if uniq.empty? || uniq[-1] != y }
  m = uniq.length
  bit = Array.new(m + 2, -1)

  rank = lambda do |y|
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) >> 1
      if uniq[mid] < y
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  update = lambda do |i, v|
    while i <= m
      bit[i] = v if v > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = -1
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  ans = Array.new(queries.length, 0)
  j = 0
  qs.each do |q|
    while j < n && pts[j][0] >= q[0]
      update.call(m - rank.call(pts[j][1]) + 1, pts[j][2])
      j += 1
    end
    ans[q[2]] = query.call(m - rank.call(q[1]) + 1)
  end
  ans
end
'''

FILES["2737_find_the_closest_marked_node"] = r'''# LeetCode 2737 - Find the Closest Marked Node
# https://leetcode.com/problems/find-the-closest-marked-node/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} s
# @param {Integer[]} marked
# @return {Integer}
def minimum_distance(n, edges, s, marked)
  g = Array.new(n) { [] }
  edges.each { |u, v, w| g[u] << [v, w] }
  mark = marked.to_h { |x| [x, true] }
  dist = Array.new(n, 10**18)
  dist[s] = 0
  pq = [[0, s]]
  until pq.empty?
    pq.sort_by! { |d, _| d }
    d, u = pq.shift
    return d if mark[u]
    next if d > dist[u]
    g[u].each do |v, w|
      if d + w < dist[v]
        dist[v] = d + w
        pq << [dist[v], v]
      end
    end
  end
  -1
end
'''

FILES["2739_total_distance_traveled"] = r'''# LeetCode 2739 - Total Distance Traveled
# https://leetcode.com/problems/total-distance-traveled/

# @param {Integer} main_tank
# @param {Integer} additional_tank
# @return {Integer}
def distance_traveled(main_tank, additional_tank)
  ans = 0
  while main_tank > 0
    if main_tank >= 5
      ans += 50
      main_tank -= 5
      if additional_tank > 0
        additional_tank -= 1
        main_tank += 1
      end
    else
      ans += main_tank * 10
      main_tank = 0
    end
  end
  ans
end
'''

FILES["2740_find_the_value_of_the_partition"] = r'''# LeetCode 2740 - Find the Value of the Partition
# https://leetcode.com/problems/find-the-value-of-the-partition/

# @param {Integer[]} nums
# @return {Integer}
def find_value_of_partition(nums)
  nums = nums.sort
  ans = 10**18
  (1...nums.length).each { |i| ans = [ans, nums[i] - nums[i - 1]].min }
  ans
end
'''

FILES["2741_special_permutations"] = r'''# LeetCode 2741 - Special Permutations
# https://leetcode.com/problems/special-permutations/

# @param {Integer[]} nums
# @return {Integer}
def special_perm(nums)
  mod = 1_000_000_007
  n = nums.length
  memo = Array.new(1 << n) { Array.new(n, -1) }

  dfs = lambda do |mask, last|
    return 1 if mask == (1 << n) - 1
    return memo[mask][last] if memo[mask][last] != -1
    res = 0
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0
        res = (res + dfs.call(mask | (1 << i), i)) % mod
      end
    end
    memo[mask][last] = res
    res
  end

  ans = 0
  (0...n).each { |i| ans = (ans + dfs.call(1 << i, i)) % mod }
  ans
end
'''

FILES["2742_painting_the_walls"] = r'''# LeetCode 2742 - Painting the Walls
# https://leetcode.com/problems/painting-the-walls/

# @param {Integer[]} cost
# @param {Integer[]} time
# @return {Integer}
def paint_walls(cost, time)
  n = cost.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    n.downto(0) do |j|
      nj = [n, j + time[i] + 1].min
      dp[nj] = dp[j] + cost[i] if dp[j] + cost[i] < dp[nj]
    end
  end
  dp[n]
end
'''

FILES["2743_count_substrings_without_repeating_character"] = r'''# LeetCode 2743 - Count Substrings Without Repeating Character
# https://leetcode.com/problems/count-substrings-without-repeating-character/

# @param {String} s
# @return {Integer}
def number_of_special_substrings(s)
  n = s.length
  ans = 0
  left = 0
  cnt = Array.new(26, 0)
  (0...n).each do |i|
    c = s[i].ord - 97
    cnt[c] += 1
    while cnt[c] > 1
      cnt[s[left].ord - 97] -= 1
      left += 1
    end
    ans += i - left + 1
  end
  ans
end
'''

FILES["2744_find_maximum_number_of_string_pairs"] = r'''# LeetCode 2744 - Find Maximum Number of String Pairs
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

# @param {String[]} words
# @return {Integer}
def maximum_number_of_string_pairs(words)
  freq = Hash.new(0)
  ans = 0
  words.each do |w|
    rev = w.reverse
    c = freq[rev]
    if c > 0
      ans += 1
      freq[rev] = c - 1
    else
      freq[w] += 1
    end
  end
  ans
end
'''

FILES["2745_construct_the_longest_new_string"] = r'''# LeetCode 2745 - Construct the Longest New String
# https://leetcode.com/problems/construct-the-longest-new-string/

# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def longest_string(x, y, z)
  if x < y
    (2 * x + 1 + z) * 2
  elsif y < x
    (2 * y + 1 + z) * 2
  else
    (x + y + z) * 2
  end
end
'''

FILES["2746_decremental_string_concatenation"] = r'''# LeetCode 2746 - Decremental String Concatenation
# https://leetcode.com/problems/decremental-string-concatenation/

# @param {String[]} words
# @return {Integer}
def minimize_concatenated_length(words)
  n = words.length
  memo = {}
  w0 = words[0]

  dfs = lambda do |i, first, last|
    return 0 if i == n
    key = [i, first, last]
    return memo[key] if memo.key?(key)
    w = words[i]
    wf, wl = w[0], w[-1]
    add1 = w.length - (last == wf ? 1 : 0)
    add2 = w.length - (wl == first ? 1 : 0)
    res = [add1 + dfs.call(i + 1, first, wl), add2 + dfs.call(i + 1, wf, last)].min
    memo[key] = res
    res
  end

  w0.length + dfs.call(1, w0[0], w0[-1])
end
'''

FILES["2747_count_zero_request_servers"] = r'''# LeetCode 2747 - Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/

# @param {Integer} n
# @param {Integer[][]} logs
# @param {Integer} x
# @param {Integer[]} queries
# @return {Integer[]}
def count_servers(n, logs, x, queries)
  logs = logs.sort_by { |e| e[1] }
  qs = queries.each_with_index.map { |t, i| [t, i] }.sort_by { |t, _| t }
  freq = Hash.new(0)
  active = 0
  ans = Array.new(queries.length, 0)
  l = 0
  r = 0
  m = logs.length
  qs.each do |t, qi|
    while r < m && logs[r][1] <= t
      sid = logs[r][0]
      freq[sid] += 1
      active += 1 if freq[sid] == 1
      r += 1
    end
    while l < r && logs[l][1] < t - x
      sid = logs[l][0]
      freq[sid] -= 1
      active -= 1 if freq[sid] == 0
      l += 1
    end
    ans[qi] = n - active
  end
  ans
end
'''

FILES["2748_number_of_beautiful_pairs"] = r'''# LeetCode 2748 - Number of Beautiful Pairs
# https://leetcode.com/problems/number-of-beautiful-pairs/

# @param {Integer[]} nums
# @return {Integer}
def count_beautiful_pairs(nums)
  def gcd(a, b)
    while b != 0
      a, b = b, a % b
    end
    a
  end

  firsts = nums.map { |x| x.to_s[0].ord - 48 }
  lasts = nums.map { |x| x % 10 }
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each do |j|
      ans += 1 if gcd(firsts[i], lasts[j]) == 1
    end
  end
  ans
end
'''

FILES["2749_minimum_operations_to_make_the_integer_zero"] = r'''# LeetCode 2749 - Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def make_the_integer_zero(num1, num2)
  (1..60).each do |k|
    target = num1 - k * num2
    next if target < k
    bits = target.to_s(2).count("1")
    return k if bits <= k
  end
  -1
end
'''

FILES["2750_ways_to_split_array_into_good_subarrays"] = r'''# LeetCode 2750 - Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_subarray_splits(nums)
  mod = 1_000_000_007
  ones = []
  nums.each_with_index { |v, i| ones << i if v == 1 }
  return 0 if ones.empty?
  ans = 1
  (1...ones.length).each do |i|
    ans = (ans * (ones[i] - ones[i - 1])) % mod
  end
  ans
end
'''

FILES["2751_robot_collisions"] = r'''# LeetCode 2751 - Robot Collisions
# https://leetcode.com/problems/robot-collisions/

# @param {Integer[]} positions
# @param {Integer[]} healths
# @param {String} directions
# @return {Integer[]}
def survived_robots_healths(positions, healths, directions)
  n = positions.length
  idx = (0...n).to_a.sort_by { |i| positions[i] }
  stack = []
  idx.each do |i|
    if directions[i] == "R"
      stack << i
    else
      while !stack.empty? && directions[stack[-1]] == "R" && healths[i] > 0
        j = stack[-1]
        if healths[j] < healths[i]
          healths[j] = 0
          healths[i] -= 1
          stack.pop
        elsif healths[j] > healths[i]
          healths[j] -= 1
          healths[i] = 0
        else
          healths[j] = 0
          healths[i] = 0
          stack.pop
        end
      end
      stack << i if healths[i] > 0
    end
  end
  (0...n).filter_map { |i| healths[i] if healths[i] > 0 }
end
'''

FILES["2753_count_houses_in_a_circular_street_ii"] = r'''# LeetCode 2753 - Count Houses in a Circular Street II
# https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Street
  def initialize(doors)
    @doors = doors
    @i = 0
  end

  def closeDoor
    @doors[@i] = 0
  end

  def isDoorOpen
    @doors[@i] == 1
  end

  def moveRight
    @i = (@i + 1) % @doors.length
  end

  def moveLeft
    @i = (@i - 1) % @doors.length
  end
end

# @param {Object} street
# @param {Integer} k
# @return {Integer}
def house_count(street, k)
  street = Street.new(street) if street.is_a?(Array)
  street.moveRight until street.isDoorOpen
  street.closeDoor
  street.moveRight
  ans = 1
  (1...k).each do
    if street.isDoorOpen
      street.closeDoor
      ans = 0
    end
    ans += 1
    street.moveRight
  end
  ans
end
'''

written = 0
failed = []
for folder, content in FILES.items():
    path = ROOT / folder / "solution.rb"
    if path.parent.exists():
        path.write_text(content, encoding="utf-8")
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            path.write_bytes(data[3:])
        written += 1
    else:
        failed.append(folder)
print(f"batch_a wrote {written} files, failed {failed}")
