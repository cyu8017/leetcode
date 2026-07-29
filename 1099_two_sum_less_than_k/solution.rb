# LeetCode 1099 - Two Sum Less Than K
# https://leetcode.com/problems/two-sum-less-than-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def two_sum_less_than_k(nums, k)
  nums = nums.sort
  lo = 0
  hi = nums.length - 1
  ans = -1
  while lo < hi
    total = nums[lo] + nums[hi]
    if total < k
      ans = [ans, total].max
      lo += 1
    else
      hi -= 1
    end
  end
  ans
end
