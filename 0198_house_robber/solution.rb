# LeetCode 0198 - House Robber
class Solution
  def rob(nums)
    prev2 = 0
    prev1 = 0
    nums.each do |num|
      prev2, prev1 = prev1, [prev1, prev2 + num].max
    end
    prev1
  end
end