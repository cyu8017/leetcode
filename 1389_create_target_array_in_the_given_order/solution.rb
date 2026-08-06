# LeetCode 1389 - Create Target Array In The Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/

def create_target_array(nums, index)
  out = []
  nums.zip(index).each { |x, i| out.insert(i, x) }
  out
end
