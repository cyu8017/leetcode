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
