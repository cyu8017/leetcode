# LeetCode 3828 - Final Element After Subarray Deletions
# https://leetcode.com/problems/final-element-after-subarray-deletions/

# @param {Integer[]} nums
# @return {Integer}
def final_element(nums)
  [nums[0], nums[-1]].max
end
