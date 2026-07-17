# LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_moves(nums, k)
  adjusted = []
  nums.each_with_index do |v, i|
    adjusted << i - adjusted.length if v == 1
  end
  prefix = [0]
  adjusted.each { |value| prefix << prefix[-1] + value }
  best = Float::INFINITY
  (0..adjusted.length - k).each do |left|
    right = left + k
    mid = left + k / 2
    median = adjusted[mid]
    cost = median * (mid - left) - (prefix[mid] - prefix[left])
    cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1)
    best = cost if cost < best
  end
  best
end
