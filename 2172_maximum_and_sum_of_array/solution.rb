# LeetCode 2172 - Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array/

# @param {Integer[]} nums
# @param {Integer} num_slots
# @return {Integer}
def maximum_and_sum(nums, num_slots)
  n = nums.length
  slots = num_slots
  max_mask = 3**slots
  dp = Array.new(max_mask, 0)
  max_mask.times do |mask|
    cnt = 0
    x = mask
    while x > 0
      cnt += x % 3
      x /= 3
    end
    next if cnt >= n

    v = nums[cnt]
    bas = 1
    (1..slots).each do |s|
      occ = mask / bas % 3
      if occ < 2
        nm = mask + bas
        dp[nm] = [dp[nm], dp[mask] + (v & s)].max
      end
      bas *= 3
    end
  end
  dp.max
end
