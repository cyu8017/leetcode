# LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

# @param {Integer[]} target
# @return {Integer}
def min_number_operations(target)
  target[0] + (1...target.length).sum { |i| [0, target[i] - target[i - 1]].max }
end
