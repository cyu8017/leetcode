# LeetCode 3826 - Minimum Partition Score
# https://leetcode.com/problems/minimum-partition-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_partition_score(nums, k)
  n = nums.length
  inf = 10**18
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }
  previous = Array.new(n + 1, inf)
  previous[0] = 0
  current = []

  value = lambda do |left, right|
    s = prefix[right] - prefix[left]
    s * (s + 1) / 2
  end

  compute = nil
  compute = lambda do |lo, hi, opt_lo, opt_hi|
    return if lo > hi
    mid = (lo + hi) >> 1
    best_index = -1
    last = [opt_hi, mid - 1].min
    (opt_lo..last).each do |split|
      next if previous[split] == inf
      candidate = previous[split] + value.call(split, mid)
      if candidate < current[mid]
        current[mid] = candidate
        best_index = split
      end
    end
    best_index = opt_lo if best_index == -1
    compute.call(lo, mid - 1, opt_lo, best_index)
    compute.call(mid + 1, hi, best_index, opt_hi)
  end

  (1..k).each do |parts|
    current = Array.new(n + 1, inf)
    compute.call(parts, n, parts - 1, n - 1)
    previous = current
  end
  previous[n]
end
