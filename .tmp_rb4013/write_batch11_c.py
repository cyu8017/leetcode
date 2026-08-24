#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2779_maximum_beauty_of_an_array_after_applying_operation"] = r'''# LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_beauty(nums, k)
  nums = nums.sort
  ans = 0
  left = 0
  (0...nums.length).each do |right|
    left += 1 while nums[right] - nums[left] > 2 * k
    ans = [ans, right - left + 1].max
  end
  ans
end
'''

FILES["2780_minimum_index_of_a_valid_split"] = r'''# LeetCode 2780 - Minimum Index of a Valid Split
# https://leetcode.com/problems/minimum-index-of-a-valid-split/

# @param {Integer[]} nums
# @return {Integer}
def minimum_index(nums)
  freq = Hash.new(0)
  dom = 0
  best = 0
  nums.each do |v|
    freq[v] += 1
    if freq[v] > best
      best = freq[v]
      dom = v
    end
  end
  left = 0
  n = nums.length
  (0...(n - 1)).each do |i|
    left += 1 if nums[i] == dom
    right = best - left
    return i if left * 2 > i + 1 && right * 2 > n - i - 1
  end
  -1
end
'''

FILES["2781_length_of_the_longest_valid_substring"] = r'''# LeetCode 2781 - Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/

# @param {String} word
# @param {String[]} forbidden
# @return {Integer}
def longest_valid_substring(word, forbidden)
  forbid = {}
  max_len = 0
  forbidden.each do |f|
    forbid[f] = true
    max_len = [max_len, f.length].max
  end
  ans = 0
  right = word.length - 1
  (word.length - 1).downto(0) do |left|
    (left..right).each do |k|
      break if k - left + 1 > max_len
      if forbid[word[left..k]]
        right = k - 1
        break
      end
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
'''

FILES["2782_number_of_unique_categories"] = r'''# LeetCode 2782 - Number of Unique Categories
# https://leetcode.com/problems/number-of-unique-categories/

class CategoryHandler
  def initialize(cats)
    @cats = cats
  end

  def haveSameCategory(a, b)
    @cats[a] == @cats[b]
  end
end

# @param {Integer} n
# @param {Object} category_handler
# @return {Integer}
def number_of_categories(n, category_handler)
  category_handler = CategoryHandler.new(category_handler) if category_handler.is_a?(Array)
  parent = (0...n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      if category_handler.haveSameCategory(i, j)
        a = find.call(i)
        b = find.call(j)
        parent[a] = b if a != b
      end
    end
  end
  (0...n).count { |i| find.call(i) == i }
end
'''

FILES["2784_check_if_array_is_good"] = r'''# LeetCode 2784 - Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/

# @param {Integer[]} nums
# @return {Boolean}
def is_good(nums)
  n = nums.length - 1
  return false if n < 1
  freq = Array.new(n + 1, 0)
  nums.each do |v|
    return false if v < 1 || v > n
    freq[v] += 1
  end
  (1...n).each { |i| return false if freq[i] != 1 }
  freq[n] == 2
end
'''

FILES["2785_sort_vowels_in_a_string"] = r'''# LeetCode 2785 - Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/

# @param {String} s
# @return {String}
def sort_vowels(s)
  vowels_set = "aeiouAEIOU"
  vowels = s.chars.select { |c| vowels_set.include?(c) }.sort
  arr = s.chars
  vi = 0
  arr.each_with_index do |c, i|
    if vowels_set.include?(c)
      arr[i] = vowels[vi]
      vi += 1
    end
  end
  arr.join
end
'''

FILES["2786_visit_array_positions_to_maximize_score"] = r'''# LeetCode 2786 - Visit Array Positions to Maximize Score
# https://leetcode.com/problems/visit-array-positions-to-maximize-score/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def max_score(nums, x)
  neg = -10**18
  even = odd = nums[0]
  if nums[0].even?
    odd = neg
  else
    even = neg
  end
  (1...nums.length).each do |i|
    v = nums[i]
    if v.even?
      even = [even + v, odd + v - x].max
    else
      odd = [odd + v, even + v - x].max
    end
  end
  [even, odd].max
end
'''

FILES["2787_ways_to_express_an_integer_as_sum_of_powers"] = r'''# LeetCode 2787 - Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def number_of_ways(n, x)
  mod = 1_000_000_007
  powers = []
  i = 1
  loop do
    p = 1
    x.times do
      p *= i
      break if p > n
    end
    break if p > n
    powers << p
    i += 1
  end
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  powers.each do |pw|
    n.downto(pw) { |s| dp[s] = (dp[s] + dp[s - pw]) % mod }
  end
  dp[n]
end
'''

FILES["2788_split_strings_by_separator"] = r'''# LeetCode 2788 - Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/

# @param {String[]} words
# @param {String} separator
# @return {String[]}
def split_words_by_separator(words, separator)
  ans = []
  words.each do |w|
    start = 0
    (0..w.length).each do |i|
      if i == w.length || w[i] == separator
        ans << w[start...i] if i > start
        start = i + 1
      end
    end
  end
  ans
end
'''

FILES["2789_largest_element_in_an_array_after_merge_operations"] = r'''# LeetCode 2789 - Largest Element in an Array after Merge Operations
# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

# @param {Integer[]} nums
# @return {Integer}
def max_array_value(nums)
  n = nums.length
  cur = nums[n - 1]
  ans = cur
  (n - 2).downto(0) do |i|
    cur = nums[i] <= cur ? cur + nums[i] : nums[i]
    ans = [ans, cur].max
  end
  ans
end
'''

FILES["2790_maximum_number_of_groups_with_increasing_length"] = r'''# LeetCode 2790 - Maximum Number of Groups With Increasing Length
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

# @param {Integer[]} usage_limits
# @return {Integer}
def max_increasing_groups(usage_limits)
  arr = usage_limits.sort
  ans = 0
  total = 0
  arr.each do |v|
    total += v
    need = (ans + 1) * (ans + 2) / 2.0
    ans += 1 if total >= need
  end
  ans
end
'''

FILES["2791_count_paths_that_can_form_a_palindrome_in_a_tree"] = r'''# LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

# @param {Integer[]} parent
# @param {String} s
# @return {Integer}
def count_palindrome_paths(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  freq = Hash.new(0)
  freq[0] = 1
  ans = [0]
  dfs = lambda do |u, mask|
    g[u].each do |v|
      nm = mask ^ (1 << (s[v].ord - 97))
      ans[0] += freq[nm]
      (0...26).each { |b| ans[0] += freq[nm ^ (1 << b)] }
      freq[nm] += 1
      dfs.call(v, nm)
    end
  end
  dfs.call(0, 0)
  ans[0]
end
'''

FILES["2792_count_nodes_that_are_great_enough"] = r'''# LeetCode 2792 - Count Nodes That Are Great Enough
# https://leetcode.com/problems/count-nodes-that-are-great-enough/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def count_great_enough_nodes(root, k)
  ans = [0]
  dfs = lambda do |node|
    return [] if node.nil?
    vals = [node.val] + dfs.call(node.left) + dfs.call(node.right)
    smaller = vals.count { |v| v < node.val }
    ans[0] += 1 if smaller >= k
    vals
  end
  dfs.call(root)
  ans[0]
end
'''

FILES["2794_create_object_from_two_arrays"] = r'''# LeetCode 2794 - Create Object from Two Arrays
# https://leetcode.com/problems/create-object-from-two-arrays/

# @param {Object[]} keys_arr
# @param {Object[]} values_arr
# @return {Hash}
def create_object(keys_arr, values_arr)
  output = {}
  n = [keys_arr.length, values_arr.length].min
  (0...n).each do |i|
    key = keys_arr[i]
    key = if key == true
            "true"
          elsif key == false
            "false"
          else
            key.to_s
          end
    output[key] = values_arr[i] unless output.key?(key)
  end
  output
end
'''

FILES["2795_parallel_execution_of_promises_for_individual_results_retrieval"] = r'''# LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
# https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

# @param {Proc[]} functions
# @return {Hash[]}
def promise_all_settled(functions)
  functions.map do |fn|
    begin
      value = fn.respond_to?(:call) ? fn.call : fn
      { "status" => "fulfilled", "value" => value }
    rescue StandardError => reason
      { "status" => "rejected", "reason" => reason }
    end
  end
end
'''

FILES["2796_repeat_string"] = r'''# LeetCode 2796 - Repeat String
# https://leetcode.com/problems/repeat-string/

# @param {String} s
# @param {Integer} times
# @return {String}
def replicate(s, times)
  res = +""
  times.times { res << s }
  res
end
'''

FILES["2797_partial_function_with_placeholders"] = r'''# LeetCode 2797 - Partial Function with Placeholders
# https://leetcode.com/problems/partial-function-with-placeholders/

# @param {Proc} fn
# @param {Object[]} args
# @return {Proc}
def partial(fn, args)
  lambda do |*rest_args|
    full = []
    ri = 0
    args.each do |a|
      if a == "_"
        if ri < rest_args.length
          full << rest_args[ri]
          ri += 1
        end
      else
        full << a
      end
    end
    while ri < rest_args.length
      full << rest_args[ri]
      ri += 1
    end
    fn.call(*full)
  end
end
'''

FILES["2798_number_of_employees_who_met_the_target"] = r'''# LeetCode 2798 - Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/

# @param {Integer[]} hours
# @param {Integer} target
# @return {Integer}
def number_of_employees_who_met_target(hours, target)
  hours.count { |h| h >= target }
end
'''

FILES["2799_count_complete_subarrays_in_an_array"] = r'''# LeetCode 2799 - Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def count_complete_subarrays(nums)
  need = nums.uniq.length
  ans = 0
  n = nums.length
  (0...n).each do |i|
    seen = {}
    (i...n).each do |j|
      seen[nums[j]] = true
      if seen.length == need
        ans += n - j
        break
      end
    end
  end
  ans
end
'''

FILES["2800_shortest_string_that_contains_three_strings"] = r'''# LeetCode 2800 - Shortest String That Contains Three Strings
# https://leetcode.com/problems/shortest-string-that-contains-three-strings/

# @param {String} a
# @param {String} b
# @param {String} c
# @return {String}
def minimum_string(a, b, c)
  merge = lambda do |x, y|
    return x if x.include?(y)
    best = x + y
    n = [x.length, y.length].min
    n.downto(1) do |i|
      if x[-i..] == y[0, i]
        cand = x + y[i..]
        best = cand if cand.length < best.length || (cand.length == best.length && cand < best)
        break
      end
    end
    best
  end
  perms = [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]
  ans = ""
  perms.each do |p|
    cur = merge.call(merge.call(p[0], p[1]), p[2])
    ans = cur if ans.empty? || cur.length < ans.length || (cur.length == ans.length && cur < ans)
  end
  ans
end
'''

FILES["2801_count_stepping_numbers_in_range"] = r'''# LeetCode 2801 - Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/

# @param {String} low
# @param {String} high
# @return {Integer}
def count_stepping_numbers(low, high)
  mod = 1_000_000_007

  dec = lambda do |s|
    arr = s.chars
    i = arr.length - 1
    while i >= 0 && arr[i] == "0"
      arr[i] = "9"
      i -= 1
    end
    arr[i] = (arr[i].ord - 1).chr if i >= 0
    j = 0
    j += 1 while j < arr.length - 1 && arr[j] == "0"
    arr[j..].join
  end

  count_to = lambda do |s|
    memo = Array.new(105) { Array.new(2) { Array.new(11) { Array.new(2, -1) } } }
    dfs = lambda do |pos, tight, last, started|
      return started if pos == s.length
      return memo[pos][tight][last + 1][started] if memo[pos][tight][last + 1][started] != -1
      up = tight == 1 ? s[pos].ord - 48 : 9
      ans = 0
      (0..up).each do |d|
        nt = tight == 1 && d == up ? 1 : 0
        if started == 0
          ans += d == 0 ? dfs.call(pos + 1, nt, -1, 0) : dfs.call(pos + 1, nt, d, 1)
        elsif (d - last).abs == 1
          ans += dfs.call(pos + 1, nt, d, 1)
        end
      end
      memo[pos][tight][last + 1][started] = ans % mod
      memo[pos][tight][last + 1][started]
    end
    dfs.call(0, 1, -1, 0)
  end

  ans = (count_to.call(high) - count_to.call(dec.call(low))) % mod
  ans += mod if ans < 0
  ans
end
'''

FILES["2802_find_the_k_th_lucky_number"] = r'''# LeetCode 2802 - Find The K-th Lucky Number
# https://leetcode.com/problems/find-the-k-th-lucky-number/

# @param {Integer} k
# @return {String}
def kth_lucky_number(k)
  k += 1
  bits = +""
  while k > 1
    bits = (k.even? ? "4" : "7") + bits
    k /= 2
  end
  bits
end
'''

FILES["2803_factorial_generator"] = r'''# LeetCode 2803 - Factorial Generator
# https://leetcode.com/problems/factorial-generator/

# @param {Integer} n
# @return {Integer[]}
def factorial_generator(n)
  cur = 1
  return [1] if n == 0
  (1..n).map do |i|
    cur *= i
    cur
  end
end
'''

FILES["2804_array_prototype_foreach"] = r'''# LeetCode 2804 - Array Prototype ForEach
# https://leetcode.com/problems/array-prototype-foreach/

# @param {Object[]} arr
# @param {Proc} callback
# @param {Object} context
# @return {NilClass}
def for_each(arr, callback, context = nil)
  arr.each_with_index { |val, i| callback.call(val, i, arr) }
  nil
end
'''

FILES["2805_custom_interval"] = r'''# LeetCode 2805 - Custom Interval
# https://leetcode.com/problems/custom-interval/

class Solution
  @@next_id = 1
  @@cancelled = {}

  def custom_interval(fn, delay, period)
    @@next_id += 1
    interval_id = @@next_id
    @@cancelled[interval_id] = false
    interval_id
  end

  def customInterval(fn, delay, period)
    custom_interval(fn, delay, period)
  end

  def custom_clear_interval(interval_id)
    @@cancelled[interval_id] = true
  end

  def customClearInterval(interval_id)
    custom_clear_interval(interval_id)
  end
end

# @param {Proc} fn
# @param {Integer} delay
# @param {Integer} period
# @return {Integer}
def custom_interval(fn, delay, period)
  Solution.new.custom_interval(fn, delay, period)
end

# @param {Integer} interval_id
# @return {NilClass}
def custom_clear_interval(interval_id)
  Solution.new.custom_clear_interval(interval_id)
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
print(f"batch_c wrote {written} files, failed {failed}")
