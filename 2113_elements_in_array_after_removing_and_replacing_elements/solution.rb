# LeetCode 2113 - Elements in Array After Removing and Replacing Elements
# https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def element_in_nums(nums, queries)
  n = nums.length
  queries.map do |t, idx|
    cycle = t % (2 * n)
    if cycle < n
      size = n - cycle
      offset = cycle
    else
      size = cycle - n
      offset = 0
    end
    idx >= size ? -1 : nums[offset + idx]
  end
end
