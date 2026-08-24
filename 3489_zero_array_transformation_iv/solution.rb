# LeetCode 3489 - Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def min_zero_array(nums, queries)
  can_subset_sum = lambda do |vals, target|
    return true if target == 0

    dp = Array.new(target + 1, false)
    dp[0] = true
    vals.each do |v|
      target.downto(v) { |s| dp[s] = true if dp[s - v] }
    end
    dp[target]
  end
  ok = lambda do |k|
    (0...nums.length).each do |i|
      next if nums[i] == 0

      vals = []
      (0...k).each do |q|
        l, r, v = queries[q]
        vals << v if l <= i && i <= r
      end
      return false unless can_subset_sum.call(vals, nums[i])
    end
    true
  end
  return 0 if ok.call(0)

  lo = 1
  hi = queries.length + 1
  while lo < hi
    mid = (lo + hi) / 2
    if mid <= queries.length && ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo > queries.length ? -1 : lo
end
