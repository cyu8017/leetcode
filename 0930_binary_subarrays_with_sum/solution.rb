# LeetCode 0930 - Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/

# @param {Integer[]} nums
# @param {Integer} goal
# @return {Integer}
def num_subarrays_with_sum(nums, goal)
  prefix = 0
  count = Hash.new(0)
  count[0] = 1
  ans = 0
  nums.each do |x|
    prefix += x
    ans += count[prefix - goal]
    count[prefix] += 1
  end
  ans
end
