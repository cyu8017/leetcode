#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2754_bind_function_to_context"] = r'''# LeetCode 2754 - Bind Function to Context
# https://leetcode.com/problems/bind-function-to-context/

# @param {Proc} fn
# @param {Object} obj
# @return {Proc}
def bind_polyfill(fn, obj)
  lambda do |*args|
    if fn.respond_to?(:call)
      fn.call(*args)
    else
      fn
    end
  end
end
'''

FILES["2755_deep_merge_of_two_objects"] = r'''# LeetCode 2755 - Deep Merge of Two Objects
# https://leetcode.com/problems/deep-merge-of-two-objects/

# @param {Object} obj1
# @param {Object} obj2
# @return {Object}
def deep_merge(obj1, obj2)
  merge = lambda do |a, b|
    if a.is_a?(Hash) && b.is_a?(Hash)
      res = a.dup
      b.each do |k, v|
        res[k] = res.key?(k) ? merge.call(res[k], v) : v
      end
      res
    elsif a.is_a?(Array) && b.is_a?(Array)
      n = [a.length, b.length].max
      (0...n).map do |i|
        if i >= a.length
          b[i]
        elsif i >= b.length
          a[i]
        else
          merge.call(a[i], b[i])
        end
      end
    else
      b
    end
  end
  merge.call(obj1, obj2)
end
'''

FILES["2756_query_batching"] = r'''# LeetCode 2756 - Query Batching
# https://leetcode.com/problems/query-batching/

class QueryBatcher
  def initialize(query_multiple, t)
    @query_multiple = query_multiple
    @t = t
    @pending = []
    @busy_until = 0
  end

  def get_value(key)
    @pending << key
    keys = @pending
    @pending = []
    @busy_until += @t
    result = @query_multiple.call(keys)
    result.is_a?(Array) ? result[0] : result
  end

  def getValue(key)
    get_value(key)
  end
end
'''

FILES["2757_generate_circular_array_values"] = r'''# LeetCode 2757 - Generate Circular Array Values
# https://leetcode.com/problems/generate-circular-array-values/

# @param {Object[]} arr
# @param {Integer} start_index
# @return {Enumerator}
def cycle_generator(arr, start_index)
  Enumerator.new do |y|
    i = start_index
    jump = y.yield(arr[i])
    loop do
      n = arr.length
      jump = 0 if jump.nil?
      i = ((i + jump) % n + n) % n
      jump = y.yield(arr[i])
    end
  end
end
'''

FILES["2758_next_day"] = r'''# LeetCode 2758 - Next Day
# https://leetcode.com/problems/next-day/

require "date"

# @param {Object} date_value
# @return {String}
def next_day(date_value)
  d = if date_value.is_a?(Date) || date_value.is_a?(Time)
        date_value.to_date
      else
        Date.iso8601(date_value.to_s[0, 10])
      end
  nxt = d + 1
  format("%04d-%02d-%02d", nxt.year, nxt.month, nxt.day)
end
'''

FILES["2759_convert_json_string_to_object"] = r'''# LeetCode 2759 - Convert JSON String to Object
# https://leetcode.com/problems/convert-json-string-to-object/

# @param {String} s
# @return {Object}
def json_parse(s)
  i = 0
  parse = lambda do
    if s[i] == '"'
      i += 1
      out = +""
      while s[i] != '"'
        out << s[i]
        i += 1
      end
      i += 1
      return out
    end
    if s[i] == "t"
      i += 4
      return true
    end
    if s[i] == "f"
      i += 5
      return false
    end
    if s[i] == "n"
      i += 4
      return nil
    end
    if s[i] == "["
      i += 1
      arr = []
      if s[i] == "]"
        i += 1
        return arr
      end
      loop do
        arr << parse.call
        if s[i] == ","
          i += 1
          next
        end
        i += 1
        return arr
      end
    end
    if s[i] == "{"
      i += 1
      obj = {}
      if s[i] == "}"
        i += 1
        return obj
      end
      loop do
        key = parse.call
        i += 1
        obj[key] = parse.call
        if s[i] == ","
          i += 1
          next
        end
        i += 1
        return obj
      end
    end
    start = i
    i += 1 if s[i] == "-"
    i += 1 while i < s.length && (s[i] =~ /\d/ || s[i] == ".")
    num = s[start...i]
    num.include?(".") ? num.to_f : num.to_i
  end
  parse.call
end
'''

FILES["2760_longest_even_odd_subarray_with_threshold"] = r'''# LeetCode 2760 - Longest Even Odd Subarray With Threshold
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def longest_alternating_subarray(nums, threshold)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    next if nums[i].odd? || nums[i] > threshold
    j = i
    j += 1 while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2
    ans = [ans, j - i + 1].max
  end
  ans
end
'''

FILES["2761_prime_pairs_with_target_sum"] = r'''# LeetCode 2761 - Prime Pairs With Target Sum
# https://leetcode.com/problems/prime-pairs-with-target-sum/

# @param {Integer} n
# @return {Integer[][]}
def find_prime_pairs(n)
  is_prime = Array.new(n + 1, true)
  is_prime[0] = is_prime[1] = false
  i = 2
  while i * i <= n
    if is_prime[i]
      (i * i).step(n, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  ans = []
  (2..(n / 2)).each do |x|
    y = n - x
    ans << [x, y] if is_prime[x] && is_prime[y]
  end
  ans
end
'''

FILES["2762_continuous_subarrays"] = r'''# LeetCode 2762 - Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def continuous_subarrays(nums)
  ans = 0
  left = 0
  min_q = []
  max_q = []
  nums.each_with_index do |val, right|
    min_q.pop while !min_q.empty? && nums[min_q[-1]] > val
    max_q.pop while !max_q.empty? && nums[max_q[-1]] < val
    min_q << right
    max_q << right
    while nums[max_q[0]] - nums[min_q[0]] > 2
      left += 1
      min_q.shift if min_q[0] < left
      max_q.shift if max_q[0] < left
    end
    ans += right - left + 1
  end
  ans
end
'''

FILES["2763_sum_of_imbalance_numbers_of_all_subarrays"] = r'''# LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def sum_imbalance_numbers(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    seen = {}
    sorted_vals = []
    imbalance = 0
    (i...n).each do |j|
      x = nums[j]
      unless seen[x]
        seen[x] = true
        lo = 0
        hi = sorted_vals.length
        while lo < hi
          mid = (lo + hi) >> 1
          if sorted_vals[mid] < x
            lo = mid + 1
          else
            hi = mid
          end
        end
        nxt = lo < sorted_vals.length ? sorted_vals[lo] : nil
        prev = lo > 0 ? sorted_vals[lo - 1] : nil
        imbalance += 1 if !prev.nil? && x - prev != 1
        imbalance += 1 if !nxt.nil? && nxt - x != 1
        imbalance -= 1 if !prev.nil? && !nxt.nil? && nxt - prev > 1
        sorted_vals.insert(lo, x)
      end
      ans += imbalance
    end
  end
  ans
end
'''

FILES["2764_is_array_a_preorder_of_some_binary_tree"] = r'''# LeetCode 2764 - Is Array a Preorder of Some Binary Tree
# https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

# @param {Integer[][]} nodes
# @return {Boolean}
def is_preorder(nodes)
  return true if nodes.nil? || nodes.empty?
  stack = [nodes[0][0]]
  (1...nodes.length).each do |i|
    node_id, parent = nodes[i][0], nodes[i][1]
    stack.pop while !stack.empty? && stack[-1] != parent
    return false if stack.empty?
    stack << node_id
  end
  true
end
'''

FILES["2765_longest_alternating_subarray"] = r'''# LeetCode 2765 - Longest Alternating Subarray
# https://leetcode.com/problems/longest-alternating-subarray/

# @param {Integer[]} nums
# @return {Integer}
def alternating_subarray(nums)
  ans = -1
  n = nums.length
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      expect = (j - i).even? ? -1 : 1
      break if nums[j] - nums[j - 1] != expect
      break if nums[i + 1] - nums[i] != 1
      ans = [ans, j - i + 1].max
    end
  end
  ans
end
'''

FILES["2766_relocate_marbles"] = r'''# LeetCode 2766 - Relocate Marbles
# https://leetcode.com/problems/relocate-marbles/

# @param {Integer[]} nums
# @param {Integer[]} move_from
# @param {Integer[]} move_to
# @return {Integer[]}
def relocate_marbles(nums, move_from, move_to)
  pos = {}
  nums.each { |v| pos[v] = true }
  move_from.each_with_index do |src, i|
    pos.delete(src)
    pos[move_to[i]] = true
  end
  pos.keys.sort
end
'''

FILES["2767_partition_string_into_minimum_beautiful_substrings"] = r'''# LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

# @param {String} s
# @return {Integer}
def minimum_beautiful_substrings(s)
  n = s.length
  pow5 = {}
  x = 1
  loop do
    b = x.to_s(2)
    break if b.length > n
    pow5[b] = true
    x *= 5
  end
  inf = 10**9
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] == inf || s[i] == "0"
    ((i + 1)..n).each do |j|
      dp[j] = [dp[j], dp[i] + 1].min if pow5[s[i...j]]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
'''

FILES["2768_number_of_black_blocks"] = r'''# LeetCode 2768 - Number of Black Blocks
# https://leetcode.com/problems/number-of-black-blocks/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} coordinates
# @return {Integer[]}
def count_black_blocks(m, n, coordinates)
  cnt = Hash.new(0)
  coordinates.each do |x, y|
    ((x - 1)..x).each do |i|
      ((y - 1)..y).each do |j|
        cnt[[i, j]] += 1 if i >= 0 && i < m - 1 && j >= 0 && j < n - 1
      end
    end
  end
  out = Array.new(5, 0)
  out[0] = (m - 1) * (n - 1)
  cnt.each_value do |v|
    out[v] += 1
    out[0] -= 1
  end
  out
end
'''

FILES["2769_find_the_maximum_achievable_number"] = r'''# LeetCode 2769 - Find the Maximum Achievable Number
# https://leetcode.com/problems/find-the-maximum-achievable-number/

# @param {Integer} num
# @param {Integer} t
# @return {Integer}
def the_maximum_achievable_x(num, t)
  num + 2 * t
end
'''

FILES["2770_maximum_number_of_jumps_to_reach_the_last_index"] = r'''# LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def maximum_jumps(nums, target)
  n = nums.length
  dp = Array.new(n, -1)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] < 0
    ((i + 1)...n).each do |j|
      dp[j] = [dp[j], dp[i] + 1].max if (nums[j] - nums[i]).abs <= target
    end
  end
  dp[n - 1]
end
'''

FILES["2771_longest_non_decreasing_subarray_from_two_arrays"] = r'''# LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_non_decreasing_length(nums1, nums2)
  n = nums1.length
  dp1 = 1
  dp2 = 1
  ans = 1
  (1...n).each do |i|
    nd1 = 1
    nd2 = 1
    nd1 = [nd1, dp1 + 1].max if nums1[i] >= nums1[i - 1]
    nd1 = [nd1, dp2 + 1].max if nums1[i] >= nums2[i - 1]
    nd2 = [nd2, dp1 + 1].max if nums2[i] >= nums1[i - 1]
    nd2 = [nd2, dp2 + 1].max if nums2[i] >= nums2[i - 1]
    dp1 = nd1
    dp2 = nd2
    ans = [ans, dp1, dp2].max
  end
  ans
end
'''

FILES["2772_apply_operations_to_make_all_array_elements_equal_to_zero"] = r'''# LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_array(nums, k)
  n = nums.length
  diff = Array.new(n + 1, 0)
  cur = 0
  (0...n).each do |i|
    cur += diff[i]
    need = nums[i] - cur
    return false if need < 0
    if need > 0
      return false if i + k > n
      cur += need
      diff[i + k] -= need
    end
  end
  true
end
'''

FILES["2773_height_of_special_binary_tree"] = r'''# LeetCode 2773 - Height of Special Binary Tree
# https://leetcode.com/problems/height-of-special-binary-tree/

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
def height_of_tree(root)
  return -1 if root.nil?

  dfs = lambda do |node|
    return -1 if node.nil?
    return dfs.call(node.right) + 1 if node.left && node.left.right.equal?(node)
    return dfs.call(node.left) + 1 if node.right && node.right.left.equal?(node)
    [dfs.call(node.left), dfs.call(node.right)].max + 1
  end
  dfs.call(root)
end
'''

FILES["2774_array_upper_bound"] = r'''# LeetCode 2774 - Array Upper Bound
# https://leetcode.com/problems/array-upper-bound/

# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def upper_bound(arr, target)
  lo = 0
  hi = arr.length
  while lo < hi
    mid = (lo + hi) >> 1
    if arr[mid] <= target
      lo = mid + 1
    else
      hi = mid
    end
  end
  return -1 if lo == 0 || arr[lo - 1] != target
  lo - 1
end
'''

FILES["2775_undefined_to_null"] = r'''# LeetCode 2775 - Undefined to Null
# https://leetcode.com/problems/undefined-to-null/

# @param {Object} obj
# @return {Object}
def undefined_to_null(obj)
  if obj.is_a?(String) && obj.lstrip.start_with?("{", "[")
    require "json"
    obj = JSON.parse(obj.gsub(/\bundefined\b/, "null"))
  end
  return nil if obj.nil?
  return obj unless obj.is_a?(Hash) || obj.is_a?(Array)
  if obj.is_a?(Array)
    obj.each_index { |i| obj[i] = undefined_to_null(obj[i]) }
    return obj
  end
  obj.keys.each { |k| obj[k] = undefined_to_null(obj[k]) }
  obj
end
'''

FILES["2776_convert_callback_based_function_to_promise_based_function"] = r'''# LeetCode 2776 - Convert Callback Based Function to Promise Based Function
# https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

# @param {Proc} fn
# @return {Proc}
def promisify(fn)
  lambda do |*args|
    err = nil
    result = nil
    callback = lambda do |e, r = nil|
      err = e
      result = r
    end
    fn.call(callback, *args)
    raise err if err
    result
  end
end
'''

FILES["2777_date_range_generator"] = r'''# LeetCode 2777 - Date Range Generator
# https://leetcode.com/problems/date-range-generator/

require "date"

# @param {String} start
# @param {String} last
# @param {Integer} step
# @return {String[]}
def date_range_generator(start, last, step)
  cur = Date.iso8601(start)
  stop = Date.iso8601(last)
  ans = []
  while cur <= stop
    ans << format("%04d-%02d-%02d", cur.year, cur.month, cur.day)
    cur += step
  end
  ans
end
'''

FILES["2778_sum_of_squares_of_special_elements"] = r'''# LeetCode 2778 - Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_squares(nums)
  n = nums.length
  ans = 0
  (0...n).each { |i| ans += nums[i] * nums[i] if n % (i + 1) == 0 }
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
print(f"batch_b wrote {written} files, failed {failed}")
