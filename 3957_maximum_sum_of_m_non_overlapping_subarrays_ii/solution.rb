# LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

class State
  attr_accessor :value, :count

  def initialize(value = 0, count = 0)
    @value = value
    @count = count
  end
end

# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def max_sum(nums, m, l, r)
  better = lambda { |a, b| a.value > b.value || (a.value == b.value && a.count > b.count) }
  candidate_better = lambda do |dp, prefix, a, b|
    left = State.new(dp[a].value - prefix[a], dp[a].count)
    right = State.new(dp[b].value - prefix[b], dp[b].count)
    better.call(left, right)
  end
  run = lambda do |prefix, n, l, r, penalty|
    dp = Array.new(n + 1) { State.new }
    deque = []
    (1..n).each do |ending|
      add_index = ending - l
      if add_index >= 0
        deque.pop while !deque.empty? && candidate_better.call(dp, prefix, add_index, deque[-1])
        deque << add_index
      end
      min_index = ending - r
      deque.shift while !deque.empty? && deque[0] < min_index
      dp[ending] = State.new(dp[ending - 1].value, dp[ending - 1].count)
      unless deque.empty?
        start = deque[0]
        take = State.new(dp[start].value + prefix[ending] - prefix[start] - penalty, dp[start].count + 1)
        dp[ending] = take if better.call(take, dp[ending])
      end
    end
    dp[n]
  end
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  unconstrained = run.call(prefix, n, l, r, 0)
  return unconstrained.value if unconstrained.count > 0 && unconstrained.count <= m
  if unconstrained.count > m
    bound = nums.sum { |value| value >= 0 ? value : -value }
    low = 0
    high = bound + 1
    while low < high
      mid = low + (high - low + 1) / 2
      if run.call(prefix, n, l, r, mid).count >= m
        low = mid
      else
        high = mid - 1
      end
    end
    state = run.call(prefix, n, l, r, low)
    return state.value + low * m
  end
  infinity = 2**60
  best_single = -infinity
  deque = []
  (1..n).each do |ending|
    add_index = ending - l
    if add_index >= 0
      deque.pop while !deque.empty? && prefix[deque[-1]] >= prefix[add_index]
      deque << add_index
    end
    min_index = ending - r
    deque.shift while !deque.empty? && deque[0] < min_index
    unless deque.empty?
      s = prefix[ending] - prefix[deque[0]]
      best_single = s if s > best_single
    end
  end
  best_single
end
