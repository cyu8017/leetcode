#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}


def add(folder, body):
    FILES[folder] = body if body.endswith("\n") else body + "\n"


add("2620_counter", r'''# LeetCode 2620 - Counter
# https://leetcode.com/problems/counter/

# @param {Integer} n
# @return {Proc}
def create_counter(n)
  lambda do
    v = n
    n += 1
    v
  end
end
''')

add("2621_sleep", r'''# LeetCode 2621 - Sleep
# https://leetcode.com/problems/sleep/

# @param {Integer} millis
# @return {NilClass}
def sleep(millis)
  Kernel.sleep(millis / 1000.0)
  nil
end
''')

add("2622_cache_with_time_limit", r'''# LeetCode 2622 - Cache With Time Limit
# https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache
  def initialize
    @data = {}
  end

  def set(key, value, duration)
    now = (Time.now.to_f * 1000).to_i
    e = @data[key]
    alive = !e.nil? && e[:expire] > now
    @data[key] = { value: value, expire: now + duration }
    alive
  end

  def get(key)
    now = (Time.now.to_f * 1000).to_i
    e = @data[key]
    return -1 if e.nil? || e[:expire] <= now

    e[:value]
  end

  def count
    now = (Time.now.to_f * 1000).to_i
    cnt = 0
    dead = []
    @data.each do |k, e|
      if e[:expire] > now
        cnt += 1
      else
        dead << k
      end
    end
    dead.each { |k| @data.delete(k) }
    cnt
  end
end

# @param {Object} actions
# @return {TimeLimitedCache}
def time_limited_cache(_actions = nil)
  TimeLimitedCache.new
end
''')

add("2623_memoize", r'''# LeetCode 2623 - Memoize
# https://leetcode.com/problems/memoize/

# @param {Proc} fn
# @return {Proc}
def memoize(fn)
  cache = {}
  lambda do |x|
    return cache[x] if cache.key?(x)

    r = fn.call(x)
    cache[x] = r
    r
  end
end
''')

add("2624_snail_traversal", r'''# LeetCode 2624 - Snail Traversal
# https://leetcode.com/problems/snail-traversal/

# @param {Integer[]} nums
# @param {Integer} rows_count
# @param {Integer} cols_count
# @return {Integer[][]}
def snail(nums, rows_count, cols_count)
  return [] if rows_count * cols_count != nums.length

  ans = Array.new(rows_count) { Array.new(cols_count, 0) }
  idx = 0
  (0...cols_count).each do |c|
    if c.even?
      (0...rows_count).each do |r|
        ans[r][c] = nums[idx]
        idx += 1
      end
    else
      (rows_count - 1).downto(0) do |r|
        ans[r][c] = nums[idx]
        idx += 1
      end
    end
  end
  ans
end
''')

add("2625_flatten_deeply_nested_array", r'''# LeetCode 2625 - Flatten Deeply Nested Array
# https://leetcode.com/problems/flatten-deeply-nested-array/

# @param {Object[]} arr
# @param {Integer} n
# @return {Object[]}
def flat(arr, n)
  res = []
  dfs = lambda do |a, depth|
    a.each do |x|
      if x.is_a?(Array) && depth < n
        dfs.call(x, depth + 1)
      else
        res << x
      end
    end
  end
  dfs.call(arr, 0)
  res
end
''')

add("2626_array_reduce_transformation", r'''# LeetCode 2626 - Array Reduce Transformation
# https://leetcode.com/problems/array-reduce-transformation/

# @param {Integer[]} nums
# @param {Proc} fn
# @param {Object} init
# @return {Object}
def reduce(nums, fn, init)
  acc = init
  nums.each { |x| acc = fn.call(acc, x) }
  acc
end
''')

add("2627_debounce", r'''# LeetCode 2627 - Debounce
# https://leetcode.com/problems/debounce/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def debounce(fn, t)
  timer = { id: nil }
  lambda do |*args|
    timer[:id] = { args: args, t: t }
    fn.call(*args)
  end
end
''')

add("2628_json_deep_equal", r'''# LeetCode 2628 - JSON Deep Equal
# https://leetcode.com/problems/json-deep-equal/

# @param {Object} o1
# @param {Object} o2
# @return {Boolean}
def are_deeply_equal(o1, o2)
  return true if o1.equal?(o2)
  return false if o1.class != o2.class
  return false if o1.nil? || o2.nil?
  return o1 == o2 unless o1.is_a?(Array) || o1.is_a?(Hash)
  return false if o1.is_a?(Array) != o2.is_a?(Array)

  if o1.is_a?(Array)
    return false if o1.length != o2.length

    o1.each_index { |i| return false unless are_deeply_equal(o1[i], o2[i]) }
    return true
  end
  return false if o1.length != o2.length

  o1.each_key { |k| return false if !o2.key?(k) || !are_deeply_equal(o1[k], o2[k]) }
  true
end
''')

add("2629_function_composition", r'''# LeetCode 2629 - Function Composition
# https://leetcode.com/problems/function-composition/

# @param {Proc[]} functions
# @return {Proc}
def compose(functions)
  lambda do |x|
    (functions.length - 1).downto(0) { |i| x = functions[i].call(x) }
    x
  end
end
''')

add("2630_memoize_ii", r'''# LeetCode 2630 - Memoize II
# https://leetcode.com/problems/memoize-ii/

# @param {Proc} fn
# @return {Proc}
def memoize(fn)
  root = {}
  res_key = Object.new
  lambda do |*args|
    node = root
    args.each do |a|
      node[a] = {} unless node.key?(a)
      node = node[a]
    end
    return node[res_key] if node.key?(res_key)

    v = fn.call(*args)
    node[res_key] = v
    v
  end
end
''')

add("2631_group_by", r'''# LeetCode 2631 - Group By
# https://leetcode.com/problems/group-by/

# @param {Object[]} array
# @param {Proc} fn
# @return {Hash}
def group_by(array, fn)
  out = {}
  array.each do |x|
    k = fn.call(x)
    out[k] ||= []
    out[k] << x
  end
  out
end
''')

add("2632_curry", r'''# LeetCode 2632 - Curry
# https://leetcode.com/problems/curry/

# @param {Proc} fn
# @return {Proc}
def curry(fn)
  arity = fn.arity
  arity = arity.abs - 1 if arity.negative?
  curried = nil
  curried = lambda do |*args|
    return fn.call(*args) if args.length >= arity

    lambda { |*next_args| curried.call(*args, *next_args) }
  end
  curried
end
''')

add("2633_convert_object_to_json_string", r'''# LeetCode 2633 - Convert Object to JSON String
# https://leetcode.com/problems/convert-object-to-json-string/

# @param {Object} object
# @return {String}
def json_stringify(object)
  return "null" if object.nil?
  return '"' + object + '"' if object.is_a?(String)
  return object ? "true" : "false" if object == true || object == false
  return object.to_s if object.is_a?(Integer) || object.is_a?(Float)
  return "[" + object.map { |x| json_stringify(x) }.join(",") + "]" if object.is_a?(Array)

  "{" + object.keys.map { |k| '"' + k.to_s + '":' + json_stringify(object[k]) }.join(",") + "}"
end
''')

add("2634_filter_elements_from_array", r'''# LeetCode 2634 - Filter Elements from Array
# https://leetcode.com/problems/filter-elements-from-array/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def filter(arr, fn)
  out = []
  arr.each_with_index { |x, i| out << x if fn.call(x, i) }
  out
end
''')

add("2635_apply_transform_over_each_element_in_array", r'''# LeetCode 2635 - Apply Transform Over Each Element in Array
# https://leetcode.com/problems/apply-transform-over-each-element-in-array/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def map(arr, fn)
  out = Array.new(arr.length)
  arr.each_index { |i| out[i] = fn.call(arr[i], i) }
  out
end
''')

add("2636_promise_pool", r'''# LeetCode 2636 - Promise Pool
# https://leetcode.com/problems/promise-pool/

# @param {Proc[]} functions
# @param {Integer} n
# @return {NilClass}
def promise_pool(functions, n = 1)
  i = 0
  worker = lambda do
    while i < functions.length
      cur = i
      i += 1
      functions[cur].call
    end
  end
  [n, functions.length].min.times { worker.call }
  nil
end
''')

add("2637_promise_time_limit", r'''# LeetCode 2637 - Promise Time Limit
# https://leetcode.com/problems/promise-time-limit/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def time_limit(fn, t)
  lambda do |*args|
    start = Time.now
    res = fn.call(*args)
    raise "Time Limit Exceeded" if (Time.now - start) * 1000 > t

    res
  end
end
''')

add("2638_count_the_number_of_k_free_subsets", r'''# LeetCode 2638 - Count the Number of K-Free Subsets
# https://leetcode.com/problems/count-the-number-of-k-free-subsets/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_the_num_of_k_free_subsets(nums, k)
  nums = nums.sort
  groups = {}
  nums.each do |x|
    key = x % k
    groups[key] ||= []
    groups[key] << x
  end
  ans = 1
  groups.each_value do |g|
    prev_val = -1
    prev_take = 0
    prev_skip = 1
    g.each do |v|
      skip = prev_take + prev_skip
      take = prev_val + k == v ? prev_skip : prev_take + prev_skip
      prev_take = take
      prev_skip = skip
      prev_val = v
    end
    ans *= prev_take + prev_skip
  end
  ans
end
''')

add("2639_find_the_width_of_columns_of_a_grid", r'''# LeetCode 2639 - Find the Width of Columns of a Grid
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

# @param {Integer[][]} grid
# @return {Integer[]}
def find_column_width(grid)
  n = grid[0].length
  ans = Array.new(n, 0)
  width = lambda do |x|
    return 1 if x == 0

    w = 0
    if x < 0
      w += 1
      x = -x
    end
    while x > 0
      w += 1
      x /= 10
    end
    w
  end
  grid.each do |row|
    n.times { |j| ans[j] = [ans[j], width.call(row[j])].max }
  end
  ans
end
''')

add("2640_find_the_score_of_all_prefixes_of_an_array", r'''# LeetCode 2640 - Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_prefix_score(nums)
  ans = Array.new(nums.length, 0)
  mx = 0
  s = 0
  nums.each_with_index do |x, i|
    mx = x if x > mx
    s += x + mx
    ans[i] = s
  end
  ans
end
''')

add("2641_cousins_in_binary_tree_ii", r'''# LeetCode 2641 - Cousins in Binary Tree II
# https://leetcode.com/problems/cousins-in-binary-tree-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def replace_value_in_tree(root)
  return nil if root.nil?

  root.val = 0
  q = [root]
  until q.empty?
    sz = q.length
    level_sum = 0
    level = []
    sz.times do
      node = q.shift
      level << node
      level_sum += node.left.val if node.left
      level_sum += node.right.val if node.right
    end
    level.each do |node|
      cousin = level_sum
      cousin -= node.left.val if node.left
      cousin -= node.right.val if node.right
      if node.left
        node.left.val = cousin
        q << node.left
      end
      if node.right
        node.right.val = cousin
        q << node.right
      end
    end
  end
  root
end
''')

add("2642_design_graph_with_shortest_path_calculator", r'''# LeetCode 2642 - Design Graph With Shortest Path Calculator
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph
  def initialize(n, edges)
    @g = Array.new(n) { [] }
    edges.each { |e| @g[e[0]] << [e[1], e[2]] }
  end

  def add_edge(edge)
    @g[edge[0]] << [edge[1], edge[2]]
    nil
  end

  def shortest_path(node1, node2)
    n = @g.length
    dist = Array.new(n, 1 << 30)
    dist[node1] = 0
    pq = [[0, node1]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      return d if u == node2
      next if d > dist[u]

      @g[u].each do |v, w|
        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          pq << [nd, v]
        end
      end
    end
    -1
  end
end
''')

add("2643_row_with_maximum_ones", r'''# LeetCode 2643 - Row With Maximum Ones
# https://leetcode.com/problems/row-with-maximum-ones/

# @param {Integer[][]} mat
# @return {Integer[]}
def row_and_maximum_ones(mat)
  best_row = 0
  best_cnt = -1
  mat.each_with_index do |row, i|
    cnt = row.sum
    if cnt > best_cnt
      best_cnt = cnt
      best_row = i
    end
  end
  [best_row, best_cnt]
end
''')

add("2644_find_the_maximum_divisibility_score", r'''# LeetCode 2644 - Find the Maximum Divisibility Score
# https://leetcode.com/problems/find-the-maximum-divisibility-score/

# @param {Integer[]} nums
# @param {Integer[]} divisors
# @return {Integer}
def max_div_score(nums, divisors)
  best = divisors[0]
  best_score = -1
  divisors.each do |d|
    score = 0
    nums.each { |x| score += 1 if x % d == 0 }
    if score > best_score || (score == best_score && d < best)
      best_score = score
      best = d
    end
  end
  best
end
''')

for folder, body in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print("wrote", folder)

print("batch A", len(FILES))
