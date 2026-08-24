# LeetCode 2239 - Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def find_closest_number(nums)
  ans = nums[0]
  nums.each do |x|
    ans = x if x.abs < ans.abs || (x.abs == ans.abs && x > ans)
  end
  ans
end
