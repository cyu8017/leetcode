# LeetCode 0330 - Patching Array
# https://leetcode.com/problems/patching-array/

class Solution
  def minPatches(nums, n)
    patches = 0
    miss = 1
    index = 0
    while miss <= n
      if index < nums.length && nums[index] <= miss
        miss += nums[index]
        index += 1
      else
        miss += miss
        patches += 1
      end
    end
    patches
  end
end
