# LeetCode 3392 - Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

# @param {Integer[]} nums
# @return {Integer}
def count_subarrays(nums)
  ans = 0
  (0...(nums.length - 2)).each do |i|
    ans += 1 if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]
  end
  ans
end
