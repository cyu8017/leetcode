#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
S: dict[str, str] = {}


def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"


add("2860_happy_students", r'''
# LeetCode 2860 - Happy Students
# https://leetcode.com/problems/happy-students/

# @param {Integer[]} nums
# @return {Integer}
def count_ways(nums)
  nums = nums.sort
  n = nums.length
  ans = 0
  ans += 1 if nums[0] > 0
  (0...n).each do |i|
    selected = i + 1
    ans += 1 if selected > nums[i] && (i == n - 1 || selected < nums[i + 1])
  end
  ans
end
''')

add("2861_maximum_number_of_alloys", r'''
# LeetCode 2861 - Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} budget
# @param {Integer[][]} composition
# @param {Integer[]} stock
# @param {Integer[]} cost
# @return {Integer}
def max_number_of_alloys(n, k, budget, composition, stock, cost)
  ok = lambda do |machines|
    composition.each do |comp|
      spend = 0
      (0...n).each do |i|
        need = machines * comp[i] - stock[i]
        spend += need * cost[i] if need > 0
      end
      return true if spend <= budget
    end
    false
  end

  lo = 0
  hi = 10**9
  ans = 0
  while lo <= hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
''')

add("2862_maximum_element_sum_of_a_complete_subset_of_indices", r'''
# LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  square_free = lambda do |x|
    res = 1
    p = 2
    while p * p <= x
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
      end
      res *= p if cnt.odd?
      p += 1
    end
    res *= x if x > 1
    res
  end

  n = nums.length
  groups = {}
  ans = 0
  (1..n).each do |i|
    sf = square_free.call(i)
    s = groups.fetch(sf, 0) + nums[i - 1]
    groups[sf] = s
    ans = s if s > ans
  end
  ans
end
''')

add("2863_maximum_length_of_semi_decreasing_subarrays", r'''
# LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def max_subarray_length(nums)
  n = nums.length
  ans = 0
  st = []
  (0...n).each do |i|
    st << i if st.empty? || nums[i] > nums[st[-1]]
  end
  (n - 1).downto(0) do |i|
    while !st.empty? && nums[st[-1]] > nums[i]
      j = st.pop
      ans = i - j + 1 if i - j + 1 > ans
    end
  end
  ans
end
''')

add("2864_maximum_odd_binary_number", r'''
# LeetCode 2864 - Maximum Odd Binary Number
# https://leetcode.com/problems/maximum-odd-binary-number/

# @param {String} s
# @return {String}
def maximum_odd_binary_number(s)
  ones = s.count("1")
  zeros = s.length - ones
  "1" * (ones - 1) + "0" * zeros + "1"
end
''')

add("2865_beautiful_towers_i", r'''
# LeetCode 2865 - Beautiful Towers I
# https://leetcode.com/problems/beautiful-towers-i/

# @param {Integer[]} heights
# @return {Integer}
def maximum_sum_of_heights(heights)
  n = heights.length
  ans = 0
  (0...n).each do |peak|
    s = heights[peak]
    mn = heights[peak]
    (peak - 1).downto(0) do |i|
      mn = heights[i] if heights[i] < mn
      s += mn
    end
    mn = heights[peak]
    (peak + 1...n).each do |i|
      mn = heights[i] if heights[i] < mn
      s += mn
    end
    ans = s if s > ans
  end
  ans
end
''')

add("2866_beautiful_towers_ii", r'''
# LeetCode 2866 - Beautiful Towers II
# https://leetcode.com/problems/beautiful-towers-ii/

# @param {Integer[]} max_heights
# @return {Integer}
def maximum_sum_of_heights(max_heights)
  n = max_heights.length
  left = Array.new(n, 0)
  st = [-1]
  s = 0
  (0...n).each do |i|
    while st.length > 1 && max_heights[st[-1]] >= max_heights[i]
      j = st.pop
      s -= max_heights[j] * (j - st[-1])
    end
    s += max_heights[i] * (i - st[-1])
    left[i] = s
    st << i
  end
  right = Array.new(n, 0)
  st = [n]
  s = 0
  (n - 1).downto(0) do |i|
    while st.length > 1 && max_heights[st[-1]] >= max_heights[i]
      j = st.pop
      s -= max_heights[j] * (st[-1] - j)
    end
    s += max_heights[i] * (st[-1] - i)
    right[i] = s
    st << i
  end
  ans = 0
  (0...n).each do |i|
    cand = left[i] + right[i] - max_heights[i]
    ans = cand if cand > ans
  end
  ans
end
''')

add("2867_count_valid_paths_in_a_tree", r'''
# LeetCode 2867 - Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_paths(n, edges)
  is_prime = Array.new(n + 1, true)
  is_prime[0] = is_prime[1] = false
  i = 2
  while i * i <= n
    if is_prime[i]
      (i * i).step(n, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  g = Array.new(n + 1) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  dfs = lambda do |u, p|
    return 0 if is_prime[u]

    sz = 1
    g[u].each { |v| sz += dfs.call(v, u) if v != p }
    sz
  end

  ans = 0
  (1..n).each do |u|
    next unless is_prime[u]

    total = 0
    g[u].each do |v|
      c = dfs.call(v, u)
      ans += c
      ans += total * c
      total += c
    end
  end
  ans
end
''')

add("2868_the_wording_game", r'''
# LeetCode 2868 - The Wording Game
# https://leetcode.com/problems/the-wording-game/

# @param {String[]} a
# @param {String[]} b
# @return {Boolean}
def can_alice_win(a, b)
  closely_greater = lambda do |w, z|
    w > z && (w[0] == z[0] || w[0].ord == z[0].ord + 1)
  end

  i = 1
  j = 0
  last = a[0]
  alice = false
  loop do
    if alice
      i += 1 while i < a.length && !closely_greater.call(a[i], last)
      return false if i == a.length

      last = a[i]
      i += 1
    else
      j += 1 while j < b.length && !closely_greater.call(b[j], last)
      return true if j == b.length

      last = b[j]
      j += 1
    end
    alice = !alice
  end
end
''')

add("2869_minimum_operations_to_collect_elements", r'''
# LeetCode 2869 - Minimum Operations to Collect Elements
# https://leetcode.com/problems/minimum-operations-to-collect-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  need = {}
  (1..k).each { |x| need[x] = true }
  (nums.length - 1).downto(0) do |i|
    need.delete(nums[i])
    return nums.length - i if need.empty?
  end
  nums.length
end
''')

add("2870_minimum_number_of_operations_to_make_array_empty", r'''
# LeetCode 2870 - Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  freq = {}
  nums.each { |v| freq[v] = freq.fetch(v, 0) + 1 }
  ans = 0
  freq.each_value do |c|
    return -1 if c == 1

    ans += (c + 2) / 3
  end
  ans
end
''')

add("2871_split_array_into_maximum_number_of_subarrays", r'''
# LeetCode 2871 - Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def max_subarrays(nums)
  ans = 0
  cur = -1
  nums.each do |v|
    if cur == -1
      cur = v
    else
      cur &= v
    end
    if cur == 0
      ans += 1
      cur = -1
    end
  end
  ans == 0 ? 1 : ans
end
''')

add("2872_maximum_number_of_k_divisible_components", r'''
# LeetCode 2872 - Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} values
# @param {Integer} k
# @return {Integer}
def max_k_divisible_components(n, edges, values, k)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = 0

  dfs = lambda do |u, p|
    s = values[u] % k
    g[u].each do |v|
      next if v == p

      s = (s + dfs.call(v, u)) % k
    end
    ans += 1 if s == 0
    s
  end

  dfs.call(0, -1)
  ans
end
''')

add("2873_maximum_value_of_an_ordered_triplet_i", r'''
# LeetCode 2873 - Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    (i + 1...n).each do |j|
      (j + 1...n).each do |k|
        cand = (nums[i] - nums[j]) * nums[k]
        ans = cand if cand > ans
      end
    end
  end
  ans
end
''')

add("2874_maximum_value_of_an_ordered_triplet_ii", r'''
# LeetCode 2874 - Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  ans = 0
  max_i = 0
  max_diff = 0
  nums.each do |v|
    ans = max_diff * v if max_diff * v > ans
    max_diff = max_i - v if max_i - v > max_diff
    max_i = v if v > max_i
  end
  ans
end
''')

add("2875_minimum_size_subarray_in_infinite_array", r'''
# LeetCode 2875 - Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_size_subarray(nums, target)
  n = nums.length
  total = nums.sum
  ans = 1 << 30
  if total > 0
    loops = target / total
    remain = target % total
    return loops * n if remain == 0

    arr = nums + nums
    left = 0
    s = 0
    best = 1 << 30
    (0...arr.length).each do |right|
      s += arr[right]
      while s > remain && left <= right
        s -= arr[left]
        left += 1
      end
      best = right - left + 1 if s == remain && right - left + 1 < best
    end
    ans = loops * n + best if best < (1 << 30)
  end
  ans == (1 << 30) ? -1 : ans
end
''')

add("2876_count_visited_nodes_in_a_directed_graph", r'''
# LeetCode 2876 - Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

# @param {Integer[]} edges
# @return {Integer[]}
def count_visited_nodes(edges)
  n = edges.length
  ans = Array.new(n, 0)
  state = Array.new(n, 0)
  stack = []

  dfs = lambda do |u|
    state[u] = 1
    stack << u
    v = edges[u]
    if state[v] == 0
      dfs.call(v)
    elsif state[v] == 1
      idx = stack.length - 1
      idx -= 1 while stack[idx] != v
      cyc = stack.length - idx
      (idx...stack.length).each { |i| ans[stack[i]] = cyc }
    end
    ans[u] = ans[edges[u]] + 1 if ans[u] == 0
    state[u] = 2
    stack.pop
  end

  (0...n).each { |i| dfs.call(i) if state[i] == 0 }
  ans
end
''')

add("2877_create_a_dataframe_from_list", r'''
# LeetCode 2877 - Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/

# @param {Integer[][]} student_data
# @return {Object[]}
def create_dataframe(student_data)
  student_data.map { |student_id, age| { "student_id" => student_id, "age" => age } }
end
''')

add("2878_get_the_size_of_a_dataframe", r'''
# LeetCode 2878 - Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe/

# @param {Object} players
# @return {Integer[]}
def get_dataframe_size(players)
  return [0, 0] if !players || (players.respond_to?(:empty?) && players.empty?)

  rows = players.length
  first = players[0]
  cols = first.is_a?(Array) ? first.length : first.keys.length
  [rows, cols]
end
''')

add("2879_display_the_first_three_rows", r'''
# LeetCode 2879 - Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/

# @param {Object[]} employees
# @return {Object[]}
def select_first_rows(employees)
  employees[0, 3] || []
end
''')

add("2880_select_data", r'''
# LeetCode 2880 - Select Data
# https://leetcode.com/problems/select-data/

# @param {Object[]} students
# @return {Object[]}
def select_data(students)
  out = []
  students.each do |r|
    sid = r.is_a?(Array) ? r[0] : r["student_id"]
    next unless sid == 101

    if r.is_a?(Array)
      out << { "name" => r[1], "age" => r[2] }
    else
      out << { "name" => r["name"], "age" => r["age"] }
    end
  end
  out
end
''')

add("2881_create_a_new_column", r'''
# LeetCode 2881 - Create a New Column
# https://leetcode.com/problems/create-a-new-column/

# @param {Object[]} employees
# @return {Object[]}
def create_bonus_column(employees)
  employees.map do |r|
    if r.is_a?(Array)
      { "name" => r[0], "salary" => r[1], "bonus" => r[1] * 2 }
    else
      row = r.dup
      row["bonus"] = r["salary"] * 2
      row
    end
  end
end
''')

add("2882_drop_duplicate_rows", r'''
# LeetCode 2882 - Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows/

# @param {Object[]} customers
# @return {Object[]}
def drop_duplicate_emails(customers)
  seen = {}
  out = []
  customers.each do |r|
    email = r.is_a?(Array) ? r[2] : r["email"]
    next if seen[email]

    seen[email] = true
    out << r
  end
  out
end
''')

add("2883_drop_missing_data", r'''
# LeetCode 2883 - Drop Missing Data
# https://leetcode.com/problems/drop-missing-data/

# @param {Object[]} students
# @return {Object[]}
def drop_missing_data(students)
  out = []
  students.each do |r|
    name = r.is_a?(Array) ? r[1] : r["name"]
    out << r if !name.nil? && name != ""
  end
  out
end
''')

add("2884_modify_columns", r'''
# LeetCode 2884 - Modify Columns
# https://leetcode.com/problems/modify-columns/

# @param {Object[]} employees
# @return {Object[]}
def modify_salary_column(employees)
  employees.map do |r|
    if r.is_a?(Array)
      [r[0], r[1] * 2]
    else
      row = r.dup
      row["salary"] = r["salary"] * 2
      row
    end
  end
end
''')


def main() -> None:
    written = 0
    missing = []
    for name, body in S.items():
        path = ROOT / name / "solution.rb"
        if not path.parent.exists():
            missing.append(name)
            continue
        path.write_text(body, encoding="utf-8", newline="\n")
        written += 1
    print(f"wrote={written} missing={missing}")


if __name__ == "__main__":
    main()
