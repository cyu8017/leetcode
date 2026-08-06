# LeetCode 1425 - Constrained Subsequence Sum
# https://leetcode.com/problems/constrained-subsequence-sum/

def constrained_subset_sum(nums, k)
  queue = []
  best = nums.dup
  nums.each_with_index do |value, i|
    queue.shift while !queue.empty? && queue[0] < i - k
    best[i] = value + [0, queue.empty? ? 0 : best[queue[0]]].max
    queue.pop while !queue.empty? && best[queue[-1]] <= best[i]
    queue << i
  end
  best.max
end
