# LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

# @param {Integer[]} nums
# @return {Integer}
def number_of_subarrays(nums)
  stk = []
  ans = 0
  nums.each do |x|
    stk.pop while !stk.empty? && stk[-1][0] < x
    if stk.empty? || stk[-1][0] > x
      stk << [x, 1]
    else
      stk[-1][1] += 1
    end
    ans += stk[-1][1]
  end
  ans
end
