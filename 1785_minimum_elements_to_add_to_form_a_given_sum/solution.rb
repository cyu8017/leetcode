# LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

# @param {Integer[]} nums
# @param {Integer} limit
# @param {Integer} goal
# @return {Integer}
def min_elements(nums, limit, goal)
  diff = (nums.sum - goal).abs
  (diff + limit - 1) / limit
end
