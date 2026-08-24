# LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sum_of_three_subarrays(nums, k)
  n = nums.length
  windows = n - k + 1
  sums = Array.new(windows, 0)
  total = nums[0, k].sum
  sums[0] = total
  (1...windows).each do |i|
    total += nums[i + k - 1] - nums[i - 1]
    sums[i] = total
  end

  left = Array.new(windows, 0)
  best = 0
  windows.times do |i|
    best = i if sums[i] > sums[best]
    left[i] = best
  end

  right = Array.new(windows, 0)
  best = windows - 1
  (windows - 1).downto(0) do |i|
    best = i if sums[i] >= sums[best]
    right[i] = best
  end

  answer = [0, 0, 0]
  best_total = -1
  (k...(windows - k)).each do |mid|
    l = left[mid - k]
    r = right[mid + k]
    total = sums[l] + sums[mid] + sums[r]
    if total > best_total
      best_total = total
      answer = [l, mid, r]
    end
  end
  answer
end
