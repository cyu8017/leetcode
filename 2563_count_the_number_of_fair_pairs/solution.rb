# LeetCode 2563 - Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def count_fair_pairs(nums, lower, upper)
  nums = nums.sort

  count = lambda do |x|
    ans = 0
    l = 0
    r = nums.length - 1
    while l < r
      if nums[l] + nums[r] <= x
        ans += r - l
        l += 1
      else
        r -= 1
      end
    end
    ans
  end

  count.call(upper) - count.call(lower - 1)
end
