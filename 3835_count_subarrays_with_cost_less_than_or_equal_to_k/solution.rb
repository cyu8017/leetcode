# LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
# https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  ans = 0
  q1 = []
  q2 = []
  l = 0
  nums.each_with_index do |x, r|
    q1.pop while !q1.empty? && nums[q1[-1]] <= x
    q2.pop while !q2.empty? && nums[q2[-1]] >= x
    q1 << r
    q2 << r
    while l < r && (nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k
      l += 1
      q1.shift if q1[0] < l
      q2.shift if q2[0] < l
    end
    ans += r - l + 1
  end
  ans
end
