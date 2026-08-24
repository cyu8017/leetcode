# LeetCode 3929 - Minimum Partition Score II
# https://leetcode.com/problems/minimum-partition-score-ii/

class Line
  attr_accessor :slope, :intercept, :count, :valid

  def initialize(slope = 0, intercept = 0, count = 0, valid = false)
    @slope = slope
    @intercept = intercept
    @count = count
    @valid = valid
  end
end

class State
  attr_accessor :value, :count, :valid

  def initialize(value = 0, count = 0, valid = false)
    @value = value
    @count = count
    @valid = valid
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_partition_score(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }

  better = lambda do |a, b|
    return b unless a.valid
    return a unless b.valid
    return a.value < b.value ? a : b if a.value != b.value
    a.count >= b.count ? a : b
  end

  evaluate = lambda do |line, x|
    return State.new unless line.valid
    State.new(line.slope * x + line.intercept, line.count, true)
  end

  insert = nil
  insert = lambda do |tree, node, left, right, line|
    unless tree[node].valid
      tree[node] = line
      return
    end
    mid = (left + right) / 2
    x_left = prefix[left]
    x_mid = prefix[mid]
    left_better = better.call(evaluate.call(line, x_left), evaluate.call(tree[node], x_left))
    mid_better = better.call(evaluate.call(line, x_mid), evaluate.call(tree[node], x_mid))
    line_wins_left = left_better.value == evaluate.call(line, x_left).value && left_better.count == line.count
    line_wins_mid = mid_better.value == evaluate.call(line, x_mid).value && mid_better.count == line.count
    if line_wins_mid
      tmp = tree[node]
      tree[node] = line
      line = tmp
    end
    return if left == right
    if line_wins_left != line_wins_mid
      insert.call(tree, node * 2, left, mid, line)
    else
      insert.call(tree, node * 2 + 1, mid + 1, right, line)
    end
  end

  query = nil
  query = lambda do |tree, node, left, right, index|
    result = evaluate.call(tree[node], prefix[index])
    return result if left == right
    mid = (left + right) / 2
    if index <= mid
      better.call(result, query.call(tree, node * 2, left, mid, index))
    else
      better.call(result, query.call(tree, node * 2 + 1, mid + 1, right, index))
    end
  end

  run = lambda do |penalty|
    tree = Array.new(4 * (n + 1)) { Line.new }
    insert.call(tree, 1, 0, n, Line.new(0, 0, 0, true))
    current = State.new
    (1..n).each do |i|
      best = query.call(tree, 1, 0, n, i)
      x = prefix[i]
      current = State.new(best.value + x * x + x + penalty, best.count + 1, true)
      insert.call(tree, 1, 0, n, Line.new(-2 * x, current.value + x * x - x, current.count, true))
    end
    current
  end

  bound = prefix[n] * prefix[n] + prefix[n] + 1
  low = 0
  high = bound
  while low < high
    mid = low + (high - low + 1) / 2
    if run.call(mid).count >= k
      low = mid
    else
      high = mid - 1
    end
  end
  state = run.call(low)
  (state.value - low * k) / 2
end
