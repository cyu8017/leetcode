# LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  stk = []
  ans = 0
  nums.each do |x|
    while !stk.empty? && stk[-1] > x
      ans += 1
      stk.pop
    end
    stk << x if x != 0 && (stk.empty? || stk[-1] != x)
  end
  ans + stk.length
end
