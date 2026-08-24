#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}


def add(folder, body):
    FILES[folder] = body if body.endswith("\n") else body + "\n"


add("2674_split_a_circular_linked_list", r'''# LeetCode 2674 - Split a Circular Linked List
# https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} list
# @return {ListNode[]}
def split_circular_linked_list(list)
  return [nil, nil] if list.nil?

  slow = list
  fast = list
  while fast.next != list && fast.next.next != list
    slow = slow.next
    fast = fast.next.next
  end
  fast = fast.next if fast.next.next == list
  head2 = slow.next
  slow.next = list
  fast.next = head2
  [list, head2]
end
''')

add("2675_array_of_objects_to_matrix", r'''# LeetCode 2675 - Array of Objects to Matrix
# https://leetcode.com/problems/array-of-objects-to-matrix/

# @param {Object[]} arr
# @return {Object[][]}
def json_to_matrix(arr)
  flatten = nil
  flatten = lambda do |obj, prefix, out|
    unless obj.is_a?(Hash) || obj.is_a?(Array)
      out[prefix] = obj
      return
    end
    if obj.is_a?(Array)
      return if obj.empty?

      obj.each_with_index do |item, i|
        flatten.call(item, prefix.empty? ? i.to_s : prefix + "." + i.to_s, out)
      end
      return
    end
    return if obj.empty?

    obj.each_key do |k|
      flatten.call(obj[k], prefix.empty? ? k.to_s : prefix + "." + k.to_s, out)
    end
  end
  maps = arr.map do |o|
    m = {}
    flatten.call(o, "", m)
    m
  end
  key_set = {}
  maps.each { |m| m.each_key { |k| key_set[k] = true } }
  keys = key_set.keys.sort
  mat = [keys]
  maps.each { |m| mat << keys.map { |k| m.key?(k) ? m[k] : "" } }
  mat
end
''')

add("2676_throttle", r'''# LeetCode 2676 - Throttle
# https://leetcode.com/problems/throttle/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def throttle(fn, t)
  last = -Float::INFINITY
  pending = nil
  timer = nil
  run = lambda do |*args|
    last = Time.now.to_f * 1000
    fn.call(*args)
  end
  lambda do |*args|
    now = Time.now.to_f * 1000
    remaining = t - (now - last)
    if remaining <= 0
      timer = nil
      run.call(*args)
    else
      pending = args
      if timer.nil?
        timer = Thread.new do
          sleep(remaining / 1000.0)
          timer = nil
          unless pending.nil?
            a = pending
            pending = nil
            run.call(*a)
          end
        end
      end
    end
  end
end
''')

add("2677_chunk_array", r'''# LeetCode 2677 - Chunk Array
# https://leetcode.com/problems/chunk-array/

# @param {Object[]} arr
# @param {Integer} size
# @return {Object[][]}
def chunk(arr, size)
  ans = []
  i = 0
  while i < arr.length
    ans << arr[i, size]
    i += size
  end
  ans
end
''')

add("2678_number_of_senior_citizens", r'''# LeetCode 2678 - Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

# @param {String[]} details
# @return {Integer}
def count_seniors(details)
  ans = 0
  details.each do |d|
    age = (d[11].ord - 48) * 10 + (d[12].ord - 48)
    ans += 1 if age > 60
  end
  ans
end
''')

add("2679_sum_in_a_matrix", r'''# LeetCode 2679 - Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/

# @param {Integer[][]} nums
# @return {Integer}
def matrix_sum(nums)
  nums.each(&:sort!)
  ans = 0
  n = nums[0].length
  n.times do |j|
    mx = 0
    nums.each { |row| mx = [mx, row[j]].max }
    ans += mx
  end
  ans
end
''')

add("2680_maximum_or", r'''# LeetCode 2680 - Maximum OR
# https://leetcode.com/problems/maximum-or/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_or(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  suf = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] | nums[i] }
  (n - 1).downto(0) { |i| suf[i] = suf[i + 1] | nums[i] }
  ans = 0
  n.times do |i|
    cur = pref[i] | (nums[i] * (2**k)) | suf[i + 1]
    ans = cur if cur > ans
  end
  ans
end
''')

add("2681_power_of_heroes", r'''# LeetCode 2681 - Power of Heroes
# https://leetcode.com/problems/power-of-heroes/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_power(nums)
  mod = 1_000_000_007
  nums = nums.sort
  ans = 0
  s = 0
  nums.each do |x|
    ans = (ans + ((s + x) % mod) * x % mod * x) % mod
    s = (s * 2 + x) % mod
  end
  ans
end
''')

add("2682_find_the_losers_of_the_circular_game", r'''# LeetCode 2682 - Find the Losers of the Circular Game
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def circular_game_losers(n, k)
  seen = Array.new(n + 1, false)
  cur = 1
  step = 1
  until seen[cur]
    seen[cur] = true
    cur = (cur - 1 + step * k) % n + 1
    step += 1
  end
  (1..n).select { |i| !seen[i] }
end
''')

add("2683_neighboring_bitwise_xor", r'''# LeetCode 2683 - Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/

# @param {Integer[]} derived
# @return {Boolean}
def does_valid_array_exist(derived)
  x = 0
  derived.each { |v| x ^= v }
  x == 0
end
''')

add("2684_maximum_number_of_moves_in_a_grid", r'''# LeetCode 2684 - Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_moves(grid)
  m = grid.length
  n = grid[0].length
  dp = Array.new(m, 0)
  (n - 2).downto(0) do |c|
    ndp = Array.new(m, 0)
    m.times do |r|
      best = 0
      [-1, 0, 1].each do |dr|
        nr = r + dr
        best = [best, 1 + dp[nr]].max if nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c]
      end
      ndp[r] = best
    end
    dp = ndp
  end
  dp.max
end
''')

add("2685_count_the_number_of_complete_components", r'''# LeetCode 2685 - Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_complete_components(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  vis = Array.new(n, false)
  ans = 0
  dfs = nil
  dfs = lambda do |u, nodes|
    vis[u] = true
    nodes << u
    g[u].each { |v| dfs.call(v, nodes) unless vis[v] }
  end
  n.times do |i|
    next if vis[i]

    nodes = []
    dfs.call(i, nodes)
    ecount = 0
    nodes.each { |u| ecount += g[u].length }
    ecount /= 2
    sz = nodes.length
    ans += 1 if ecount == sz * (sz - 1) / 2
  end
  ans
end
''')

add("2689_extract_kth_character_from_the_rope_tree", r'''# LeetCode 2689 - Extract Kth Character From The Rope Tree
# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode
  attr_accessor :len, :val, :left, :right

  def initialize(len = 0, val = "", left = nil, right = nil)
    @len = len
    @val = val
    @left = left
    @right = right
  end
end

# @param {RopeTreeNode} root
# @param {Integer} k
# @return {String}
def get_kth_character(root, k)
  dfs = nil
  dfs = lambda do |node, kk|
    return node.val if node.left.nil? && node.right.nil?

    left_len = 0
    if node.left
      left_len = node.left.len > 0 ? node.left.len : 1
    end
    return dfs.call(node.left, kk) if kk <= left_len

    dfs.call(node.right, kk - left_len)
  end
  dfs.call(root, k)
end
''')

add("2690_infinite_method_object", r'''# LeetCode 2690 - Infinite Method Object
# https://leetcode.com/problems/infinite-method-object/

class InfiniteObject
  def method_missing(*_args, **_kwargs)
    "Hello World"
  end

  def respond_to_missing?(_name, _include_private = false)
    true
  end
end

# @return {InfiniteObject}
def create_infinite_object
  InfiniteObject.new
end
''')

add("2691_immutability_helper", r'''# LeetCode 2691 - Immutability Helper
# https://leetcode.com/problems/immutability-helper/

class ImmutableHelper
  def initialize(obj)
    @obj = obj
  end

  def produce(mutator)
    clones = {}
    is_obj = lambda { |v| v.is_a?(Hash) || v.is_a?(Array) }
    get_clone = lambda do |original|
      oid = original.object_id
      return clones[oid] if clones.key?(oid)

      copy = original.is_a?(Array) ? original.dup : original.dup
      clones[oid] = copy
      copy
    end
    root_result = [@obj]
    proxy = nil
    proxy = lambda do |node, on_replace|
      obj = Object.new
      obj.define_singleton_method(:[]) do |prop|
        val = node[prop]
        if is_obj.call(val)
          child_replace = lambda do |child_clone|
            clone = get_clone.call(node)
            clone[prop] = child_clone
            on_replace.call(clone)
          end
          return proxy.call(val, child_replace)
        end
        val
      end
      obj.define_singleton_method(:[]=) do |prop, value|
        clone = get_clone.call(node)
        clone[prop] = value
        on_replace.call(clone)
      end
      obj.define_singleton_method(:delete) do |prop|
        clone = get_clone.call(node)
        clone.delete(prop)
        on_replace.call(clone)
      end
      obj
    end
    on_root = lambda { |clone| root_result[0] = clone }
    mutator.call(proxy.call(@obj, on_root))
    root_result[0]
  end
end

# @param {Object} obj
# @param {Object} mutators
# @return {ImmutableHelper}
def immutable_helper(obj, _mutators = nil)
  ImmutableHelper.new(obj)
end
''')

add("2692_make_object_immutable", r'''# LeetCode 2692 - Make Object Immutable
# https://leetcode.com/problems/make-object-immutable/

class ImmutableList < Array
  MUTATORS = %w[pop append push concat insert delete clear sort! reverse!].freeze

  def []=(index, _value)
    raise "Error Modifying Index: #{index}"
  end

  def delete_at(index)
    raise "Error Modifying Index: #{index}"
  end

  def method_missing(name, *args, &blk)
    raise "Error Calling Method: #{name}" if MUTATORS.include?(name.to_s)

    super
  end
end

class ImmutableDict < Hash
  def []=(key, _value)
    raise "Error Modifying: #{key}"
  end

  def delete(key)
    raise "Error Modifying: #{key}"
  end
end

# @param {Object} obj
# @return {Object}
def make_immutable(obj)
  wrap = nil
  wrap = lambda do |val|
    return val if val.nil? || !(val.is_a?(Hash) || val.is_a?(Array))
    return ImmutableList.new(val.map { |x| wrap.call(x) }) if val.is_a?(Array)

    ImmutableDict[val.map { |k, v| [k, wrap.call(v)] }]
  end
  wrap.call(obj)
end
''')

add("2693_call_function_with_custom_context", r'''# LeetCode 2693 - Call Function with Custom Context
# https://leetcode.com/problems/call-function-with-custom-context/

# @param {Proc} fn
# @param {Object} obj
# @return {Object}
def call_polyfill(fn, obj, *args)
  if obj.is_a?(Hash)
    key = Object.new
    obj[key] = fn
    res = obj[key].call(*args)
    obj.delete(key)
    return res
  end
  obj.define_singleton_method(:_call_polyfill_fn) { |*a| fn.call(*a) }
  res = obj._call_polyfill_fn(*args)
  res
end
''')

add("2694_event_emitter", r'''# LeetCode 2694 - Event Emitter
# https://leetcode.com/problems/event-emitter/

class EventEmitter
  def initialize
    @handlers = {}
  end

  def subscribe(event_name, callback)
    @handlers[event_name] ||= []
    lst = @handlers[event_name]
    lst << callback
    {
      "unsubscribe" => lambda {
        lst.delete(callback)
        nil
      }
    }
  end

  def emit(event_name, args = [])
    args = [] if args.nil?
    lst = @handlers[event_name] || []
    lst.map { |cb| cb.call(*args) }
  end
end

# @param {Object} actions
# @param {Object} values
# @return {EventEmitter}
def event_emitter(_actions = nil, _values = nil)
  EventEmitter.new
end
''')

add("2695_array_wrapper", r'''# LeetCode 2695 - Array Wrapper
# https://leetcode.com/problems/array-wrapper/

class ArrayWrapper
  def initialize(nums)
    @nums = nums
  end

  def value_of
    s = 0
    @nums.each { |x| s += x }
    s
  end

  def +(other)
    value_of + other.value_of
  end

  def to_i
    value_of
  end

  def to_s
    "[" + @nums.map(&:to_s).join(",") + "]"
  end
end

# @param {Integer[]} nums
# @return {ArrayWrapper}
def array_wrapper(nums)
  ArrayWrapper.new(nums)
end
''')

add("2696_minimum_string_length_after_removing_substrings", r'''# LeetCode 2696 - Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# @param {String} s
# @return {Integer}
def min_length(s)
  st = []
  s.each_char do |c|
    last = st.empty? ? nil : st[-1]
    if !st.empty? && ((last == "A" && c == "B") || (last == "C" && c == "D"))
      st.pop
    else
      st << c
    end
  end
  st.length
end
''')

add("2697_lexicographically_smallest_palindrome", r'''# LeetCode 2697 - Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/

# @param {String} s
# @return {String}
def make_smallest_palindrome(s)
  arr = s.chars
  n = arr.length
  (n / 2).times do |i|
    c = arr[i] < arr[n - 1 - i] ? arr[i] : arr[n - 1 - i]
    arr[i] = arr[n - 1 - i] = c
  end
  arr.join
end
''')

add("2698_find_the_punishment_number_of_an_integer", r'''# LeetCode 2698 - Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

# @param {Integer} n
# @return {Integer}
def punishment_number(n)
  dfs = nil
  dfs = lambda do |s, i, sm, target|
    return sm == target if i == s.length

    cur = 0
    (i...s.length).each do |j|
      cur = cur * 10 + (s[j].ord - 48)
      break if sm + cur > target
      return true if dfs.call(s, j + 1, sm + cur, target)
    end
    false
  end
  ans = 0
  (1..n).each do |i|
    sq = i * i
    ans += sq if dfs.call(sq.to_s, 0, 0, i)
  end
  ans
end
''')

add("2699_modify_graph_edge_weights", r'''# LeetCode 2699 - Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @param {Integer} target
# @return {Integer[][]}
def modified_graph_edges(n, edges, source, destination, target)
  inf = 2_000_000_000
  dijkstra = lambda do |ignore_neg|
    dist = Array.new(n, inf)
    dist[source] = 0
    pq = [[0, source]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      next if d != dist[u]

      edges.each do |e|
        a, b, w = e[0], e[1], e[2]
        next if a != u && b != u

        to = a == u ? b : a
        if w == -1
          next if ignore_neg

          w = 1
        end
        if d + w < dist[to]
          dist[to] = d + w
          pq << [dist[to], to]
        end
      end
    end
    dist
  end
  d = dijkstra.call(true)
  return [] if d[destination] < target

  matched = d[destination] == target
  edges.each_index do |i|
    next if edges[i][2] != -1

    if matched
      edges[i][2] = inf
      next
    end
    edges[i][2] = 1
    d = dijkstra.call(false)
    if d[destination] <= target
      edges[i][2] += target - d[destination]
      matched = true
    end
  end
  d = dijkstra.call(false)
  return [] if d[destination] != target

  edges
end
''')

add("2700_differences_between_two_objects", r'''# LeetCode 2700 - Differences Between Two Objects
# https://leetcode.com/problems/differences-between-two-objects/

# @param {Object} obj1
# @param {Object} obj2
# @return {Object}
def obj_diff(obj1, obj2)
  diff = {}
  keys = if obj1.is_a?(Hash)
           obj1.keys
         else
           obj1.is_a?(Array) ? (0...obj1.length).to_a : []
         end
  keys.each do |k|
    if obj1.is_a?(Hash)
      next unless obj2.is_a?(Hash) && obj2.key?(k)

      v1 = obj1[k]
      v2 = obj2[k]
    else
      next unless obj2.is_a?(Array) && k < obj2.length

      v1 = obj1[k]
      v2 = obj2[k]
    end
    if v1.is_a?(Hash) && v2.is_a?(Hash)
      child = obj_diff(v1, v2)
      diff[k] = child unless child.empty?
    elsif v1.is_a?(Array) && v2.is_a?(Array)
      child = obj_diff(v1, v2)
      diff[k] = child unless child.empty?
    elsif v1 != v2
      diff[k] = [v1, v2]
    end
  end
  diff
end
''')

for folder, body in FILES.items():
    path = ROOT / folder / "solution.rb"
    path.write_text(body, encoding="utf-8")
    print("wrote", folder)

print("batch C", len(FILES))
