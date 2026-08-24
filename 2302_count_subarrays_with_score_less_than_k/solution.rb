# LeetCode 2302 - Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  ans = s = left = 0
  nums.each_with_index do |x, right|
    s += x
    while s * (right - left + 1) >= k
      s -= nums[left]
      left += 1
    end
    ans += right - left + 1
  end
  ans
end
