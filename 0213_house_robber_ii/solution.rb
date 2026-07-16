# LeetCode 0213 - House Robber II
# https://leetcode.com/problems/house-robber-ii/

class Solution
  def rob(nums)
    return nums[0] if nums.length == 1

    [rob_linear(nums[0...-2]), rob_linear(nums[1..])].max
  end

  private

  def rob_linear(houses)
    prev2 = 0
    prev1 = 0
    houses.each do |num|
      prev2, prev1 = prev1, [prev1, prev2 + num].max
    end
    prev1
  end
end
