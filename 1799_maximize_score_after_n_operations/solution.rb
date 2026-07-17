# LeetCode 1799 - Maximize Score After N Operations
# https://leetcode.com/problems/maximize-score-after-n-operations/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  n = nums.length
  full = (1 << n) - 1
  memo = {}

  dp = lambda do |mask|
    return 0 if mask == full
    return memo[mask] if memo.key?(mask)
    step = mask.to_s(2).count('1') / 2 + 1
    best = 0
    (0...n).each do |i|
      next if mask >> i & 1 == 1
      ((i + 1)...n).each do |j|
        next if mask >> j & 1 == 1
        score = step * nums[i].gcd(nums[j]) + dp.call(mask | (1 << i) | (1 << j))
        best = score if score > best
      end
    end
    memo[mask] = best
    best
  end

  dp.call(0)
end
