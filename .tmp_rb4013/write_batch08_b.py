#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2441_largest_positive_integer_that_exists_with_its_negative", r'''
# LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

# @param {Integer[]} nums
# @return {Integer}
def find_max_k(nums)
  seen = {}
  ans = -1
  nums.each do |x|
    seen[x] = true
    if x > 0 && seen[-x] && x > ans
      ans = x
    elsif x < 0 && seen[-x] && -x > ans
      ans = -x
    end
  end
  ans
end
''')

add("2442_count_number_of_distinct_integers_after_reverse_operations", r'''
# LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

# @param {Integer[]} nums
# @return {Integer}
def count_distinct_integers(nums)
  rev = lambda do |x|
    r = 0
    while x > 0
      r = r * 10 + x % 10
      x /= 10
    end
    r
  end

  seen = {}
  nums.each do |x|
    seen[x] = true
    seen[rev.call(x)] = true
  end
  seen.length
end
''')

add("2443_sum_of_number_and_its_reverse", r'''
# LeetCode 2443 - Sum of Number and Its Reverse
# https://leetcode.com/problems/sum-of-number-and-its-reverse/

# @param {Integer} num
# @return {Boolean}
def sum_of_number_and_reverse(num)
  rev = lambda do |x|
    r = 0
    while x > 0
      r = r * 10 + x % 10
      x /= 10
    end
    r
  end

  (0..num).each { |i| return true if i + rev.call(i) == num }
  false
end
''')

add("2444_count_subarrays_with_fixed_bounds", r'''
# LeetCode 2444 - Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

# @param {Integer[]} nums
# @param {Integer} min_k
# @param {Integer} max_k
# @return {Integer}
def count_subarrays(nums, min_k, max_k)
  ans = 0
  imin = imax = ibad = -1
  nums.each_with_index do |x, i|
    ibad = i if x < min_k || x > max_k
    imin = i if x == min_k
    imax = i if x == max_k
    bound = imin < imax ? imin : imax
    ans += bound - ibad if bound > ibad
  end
  ans
end
''')

add("2445_number_of_nodes_with_value_one", r'''
# LeetCode 2445 - Number of Nodes With Value One
# https://leetcode.com/problems/number-of-nodes-with-value-one/

# @param {Integer} n
# @param {Integer[]} queries
# @return {Integer}
def number_of_nodes(n, queries)
  flip = Array.new(n + 1, 0)
  val = Array.new(n + 1, 0)
  queries.each { |q| flip[q] ^= 1 }
  ans = 0
  (1..n).each do |i|
    val[i] = flip[i]
    val[i] ^= val[i / 2] if i > 1
    ans += val[i]
  end
  ans
end
''')

add("2446_determine_if_two_events_have_conflict", r'''
# LeetCode 2446 - Determine if Two Events Have Conflict
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

# @param {String[]} event1
# @param {String[]} event2
# @return {Boolean}
def have_conflict(event1, event2)
  event1[0] <= event2[1] && event2[0] <= event1[1]
end
''')

add("2447_number_of_subarrays_with_gcd_equal_to_k", r'''
# LeetCode 2447 - Number of Subarrays With GCD Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_gcd(nums, k)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 0
  n = nums.length
  (0...n).each do |i|
    g = 0
    (i...n).each do |j|
      g = gcd.call(g, nums[j])
      break if g < k

      ans += 1 if g == k
    end
  end
  ans
end
''')

add("2448_minimum_cost_to_make_array_equal", r'''
# LeetCode 2448 - Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

# @param {Integer[]} nums
# @param {Integer[]} cost
# @return {Integer}
def min_cost(nums, cost)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  total_cost = cost.sum
  pref = 0
  median = 0
  idx.each do |i|
    pref += cost[i]
    if pref * 2 >= total_cost
      median = nums[i]
      break
    end
  end
  ans = 0
  (0...n).each do |i|
    diff = nums[i] - median
    diff = -diff if diff < 0
    ans += diff * cost[i]
  end
  ans
end
''')

add("2449_minimum_number_of_operations_to_make_arrays_similar", r'''
# LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def make_similar(nums, target)
  nums = nums.sort
  target = target.sort
  odd_n = []
  even_n = []
  odd_t = []
  even_t = []
  nums.each { |x| (x.even? ? even_n : odd_n) << x }
  target.each { |x| (x.even? ? even_t : odd_t) << x }
  ans = 0
  odd_n.each_index do |i|
    diff = odd_n[i] - odd_t[i]
    ans += diff / 2 if diff > 0
  end
  even_n.each_index do |i|
    diff = even_n[i] - even_t[i]
    ans += diff / 2 if diff > 0
  end
  ans
end
''')

add("2450_number_of_distinct_binary_strings_after_applying_operations", r'''
# LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
# https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_distinct_strings(s, k)
  mod = 1_000_000_007
  n = s.length
  ans = 1
  (n - k + 1).times { ans = (ans * 2) % mod }
  ans
end
''')

add("2451_odd_string_difference", r'''
# LeetCode 2451 - Odd String Difference
# https://leetcode.com/problems/odd-string-difference/

# @param {String[]} words
# @return {String}
def odd_string(words)
  diff = lambda do |w|
    b = ""
    (1...w.length).each do |i|
      d = w[i].ord - w[i - 1].ord
      b << (d + 128).chr << ","
    end
    b
  end

  d0 = diff.call(words[0])
  d1 = diff.call(words[1])
  if d0 == d1
    (2...words.length).each { |i| return words[i] if diff.call(words[i]) != d0 }
  end
  return words[1] if diff.call(words[2]) == d0

  words[0]
end
''')

add("2452_words_within_two_edits_of_dictionary", r'''
# LeetCode 2452 - Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

# @param {String[]} queries
# @param {String[]} dictionary
# @return {String[]}
def two_edit_words(queries, dictionary)
  ans = []
  queries.each do |q|
    ok = false
    dictionary.each do |d|
      df = 0
      (0...q.length).each do |i|
        if q[i] != d[i]
          df += 1
          break if df > 2
        end
      end
      if df <= 2
        ok = true
        break
      end
    end
    ans << q if ok
  end
  ans
end
''')

add("2453_destroy_sequential_targets", r'''
# LeetCode 2453 - Destroy Sequential Targets
# https://leetcode.com/problems/destroy-sequential-targets/

# @param {Integer[]} nums
# @param {Integer} space
# @return {Integer}
def destroy_targets(nums, space)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x % space] += 1 }
  best_cnt = cnt.values.max || 0
  ans = 1_000_000_000
  cnt.each do |key, value|
    next unless value == best_cnt

    nums.each { |x| ans = x if x % space == key && x < ans }
  end
  ans
end
''')

add("2454_next_greater_element_iv", r'''
# LeetCode 2454 - Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/

# @param {Integer[]} nums
# @return {Integer[]}
def second_greater_element(nums)
  n = nums.length
  ans = Array.new(n, -1)
  stack1 = []
  stack2 = []
  (0...n).each do |i|
    x = nums[i]
    ans[stack2.pop] = x while !stack2.empty? && nums[stack2[-1]] < x
    tmp = []
    tmp << stack1.pop while !stack1.empty? && nums[stack1[-1]] < x
    (tmp.length - 1).downto(0) { |j| stack2 << tmp[j] }
    stack1 << i
  end
  ans
end
''')

add("2455_average_value_of_even_numbers_that_are_divisible_by_three", r'''
# LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def average_value(nums)
  total = 0
  cnt = 0
  nums.each do |x|
    if x % 6 == 0
      total += x
      cnt += 1
    end
  end
  cnt == 0 ? 0 : total / cnt
end
''')

add("2456_most_popular_video_creator", r'''
# LeetCode 2456 - Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/

# @param {String[]} creators
# @param {String[]} ids
# @param {Integer[]} views
# @return {String[][]}
def most_popular_creator(creators, ids, views)
  mp = {}
  max_total = 0
  creators.each_index do |i|
    info = mp[creators[i]]
    if info.nil?
      info = { "total" => views[i], "bestID" => ids[i], "bestViews" => views[i] }
      mp[creators[i]] = info
    else
      info["total"] += views[i]
      if views[i] > info["bestViews"] || (views[i] == info["bestViews"] && ids[i] < info["bestID"])
        info["bestViews"] = views[i]
        info["bestID"] = ids[i]
      end
    end
    max_total = mp[creators[i]]["total"] if mp[creators[i]]["total"] > max_total
  end
  ans = []
  mp.each { |creator, info| ans << [creator, info["bestID"]] if info["total"] == max_total }
  ans
end
''')

add("2457_minimum_addition_to_make_integer_beautiful", r'''
# LeetCode 2457 - Minimum Addition to Make Integer Beautiful
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def make_integer_beautiful(n, target)
  digit_sum = lambda do |x|
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    s
  end

  orig = n
  pow10 = 1
  while digit_sum.call(n) > target
    n = n / 10 + 1
    pow10 *= 10
  end
  n * pow10 - orig
end
''')

add("2458_height_of_binary_tree_after_subtree_removal_queries", r'''
# LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer[]} queries
# @return {Integer[]}
def tree_queries(root, queries)
  height = {}
  level = {}
  level_max = {}

  dfs = lambda do |node, d|
    return -1 if node.nil?

    level[node.val] = d
    h = 1 + [dfs.call(node.left, d + 1), dfs.call(node.right, d + 1)].max
    height[node.val] = h
    arr = level_max[d]
    if arr.nil?
      arr = []
      level_max[d] = arr
    end
    if arr.empty?
      arr << h
    elsif h >= arr[0]
      if arr.length == 1
        arr << arr[0]
      else
        arr[1] = arr[0]
      end
      arr[0] = h
    elsif arr.length == 1 || h > arr[1]
      if arr.length == 1
        arr << h
      else
        arr[1] = h
      end
    end
    h
  end

  dfs.call(root, 0)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    d = level[q]
    h = height[q]
    top = level_max[d]
    ans[i] = if top[0] == h
               top.length > 1 ? d + top[1] : d - 1
             else
               d + top[0]
             end
  end
  ans
end
''')

add("2459_sort_array_by_moving_items_to_empty_space", r'''
# LeetCode 2459 - Sort Array By Moving Items to Empty Space
# https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

# @param {Integer[]} nums
# @return {Integer}
def sort_array(nums)
  solve_one = lambda do |start_zero|
    n = nums.length
    arr = nums.dup
    pos = {}
    arr.each_with_index { |v, i| pos[v] = i }
    ops = 0
    loop do
      empty = pos[0]
      should = start_zero ? empty : (empty == n - 1 ? 0 : empty + 1)
      if arr[empty] == should
        found = -1
        (0...n).each do |i|
          want = start_zero ? i : (i == n - 1 ? 0 : i + 1)
          if arr[i] != want
            found = i
            break
          end
        end
        return ops if found == -1

        v = arr[found]
        arr[empty] = arr[found]
        arr[found] = 0
        pos[0] = found
        pos[v] = empty
        ops += 1
        next
      end
      j = pos[should]
      vv = arr[j]
      arr[empty] = arr[j]
      arr[j] = 0
      pos[0] = j
      pos[vv] = empty
      ops += 1
    end
  end

  [solve_one.call(true), solve_one.call(false)].min
end
''')

add("2460_apply_operations_to_an_array", r'''
# LeetCode 2460 - Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def apply_operations(nums)
  n = nums.length
  a = nums.dup
  (0...(n - 1)).each do |i|
    if a[i] == a[i + 1]
      a[i] *= 2
      a[i + 1] = 0
    end
  end
  ans = Array.new(n, 0)
  j = 0
  a.each do |x|
    if x != 0
      ans[j] = x
      j += 1
    end
  end
  ans
end
''')

add("2461_maximum_sum_of_distinct_subarrays_with_length_k", r'''
# LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_subarray_sum(nums, k)
  cnt = Hash.new(0)
  total = 0
  ans = 0
  nums.each_with_index do |x, i|
    total += x
    cnt[x] += 1
    if i >= k
      y = nums[i - k]
      total -= y
      c = cnt[y] - 1
      if c == 0
        cnt.delete(y)
      else
        cnt[y] = c
      end
    end
    ans = total if i >= k - 1 && cnt.length == k && total > ans
  end
  ans
end
''')

add("2462_total_cost_to_hire_k_workers", r'''
# LeetCode 2462 - Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

# @param {Integer[]} costs
# @param {Integer} k
# @param {Integer} candidates
# @return {Integer}
def total_cost(costs, k, candidates)
  n = costs.length
  left_h = []
  right_h = []
  l = 0
  r = n - 1

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    return top if heap.empty?

    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left] < heap[smallest]
      smallest = right if right < heap.length && heap[right] < heap[smallest]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  while l <= r && left_h.length < candidates
    heap_push.call(left_h, [costs[l], l])
    l += 1
  end
  while r >= l && right_h.length < candidates
    heap_push.call(right_h, [costs[r], r])
    r -= 1
  end
  ans = 0
  k.times do
    use_left = false
    if !left_h.empty? && !right_h.empty?
      lt = left_h[0]
      rt = right_h[0]
      use_left = true if lt[0] < rt[0] || (lt[0] == rt[0] && lt[1] <= rt[1])
    elsif !left_h.empty?
      use_left = true
    end
    if use_left
      ans += heap_pop.call(left_h)[0]
      if l <= r
        heap_push.call(left_h, [costs[l], l])
        l += 1
      end
    else
      ans += heap_pop.call(right_h)[0]
      if l <= r
        heap_push.call(right_h, [costs[r], r])
        r -= 1
      end
    end
  end
  ans
end
''')

add("2463_minimum_total_distance_traveled", r'''
# LeetCode 2463 - Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/

# @param {Integer[]} robot
# @param {Integer[][]} factory
# @return {Integer}
def minimum_total_distance(robot, factory)
  robots = robot.sort
  factory = factory.sort_by { |x| x[0] }
  m = robots.length
  pos = []
  factory.each { |f| f[1].times { pos << f[0] } }
  n = pos.length
  inf = 10**18
  dp = Array.new(m + 1) { Array.new(n + 1, inf) }
  (0..n).each { |j| dp[0][j] = 0 }
  (1..m).each do |i|
    (i..n).each do |j|
      dp[i][j] = dp[i][j - 1]
      diff = robots[i - 1] - pos[j - 1]
      diff = -diff if diff < 0
      dp[i][j] = dp[i - 1][j - 1] + diff if dp[i - 1][j - 1] + diff < dp[i][j]
    end
  end
  dp[m][n]
end
''')

add("2464_minimum_subarrays_in_a_valid_split", r'''
# LeetCode 2464 - Minimum Subarrays in a Valid Split
# https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

# @param {Integer[]} nums
# @return {Integer}
def valid_subarray_split(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  n = nums.length
  inf = 1 << 30
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] >= inf

    (i...n).each do |j|
      dp[j + 1] = dp[i] + 1 if gcd.call(nums[i], nums[j]) > 1 && dp[i] + 1 < dp[j + 1]
    end
  end
  dp[n] >= inf ? -1 : dp[n]
end
''')

add("2465_number_of_distinct_averages", r'''
# LeetCode 2465 - Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/

# @param {Integer[]} nums
# @return {Integer}
def distinct_averages(nums)
  nums = nums.sort
  seen = {}
  l = 0
  r = nums.length - 1
  while l < r
    seen[nums[l] + nums[r]] = true
    l += 1
    r -= 1
  end
  seen.length
end
''')


def write_all() -> None:
    written = 0
    for folder, content in S.items():
        path = ROOT / folder / "solution.rb"
        path.write_bytes(content.encode("utf-8"))
        written += 1
        print(folder)
    print(f"wrote {written}")


if __name__ == "__main__":
    write_all()
