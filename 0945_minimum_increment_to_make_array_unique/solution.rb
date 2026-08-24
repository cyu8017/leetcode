# LeetCode 0945 - Minimum Increment to Make Array Unique
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# @param {Integer[]} nums
# @return {Integer}
def min_increment_for_unique(nums)
  nums.sort!
  ans = 0
  (1...nums.length).each do |i|
    if nums[i] <= nums[i - 1]
      need = nums[i - 1] + 1
      ans += need - nums[i]
      nums[i] = need
    end
  end
  ans
end
