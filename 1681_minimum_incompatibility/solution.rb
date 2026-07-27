# LeetCode 1681 - Minimum Incompatibility
# https://leetcode.com/problems/minimum-incompatibility/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_incompatibility(nums, k)
  n = nums.length
  size = n / k
  full = (1 << n) - 1
  groups = {}
  (1 << n).times do |mask|
    next unless mask.to_s(2).count("1") == size

    vals = (0...n).select { |i| (mask >> i) & 1 == 1 }.map { |i| nums[i] }
    groups[mask] = vals.max - vals.min if vals.uniq.length == size
  end
  memo = {}
  dp = lambda do |mask|
    return 0 if mask == full
    return memo[mask] if memo.key?(mask)

    first = (0...n).find { |i| ((mask >> i) & 1).zero? }
    best = 10**9
    groups.each do |g, c|
      next unless ((g >> first) & 1) == 1 && (g & mask).zero?

      best = [best, c + dp.call(mask | g)].min
    end
    memo[mask] = best
  end
  ans = dp.call(0)
  ans >= 10**9 ? -1 : ans
end
