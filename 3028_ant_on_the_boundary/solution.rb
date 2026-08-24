# LeetCode 3028 - Ant on the Boundary
# https://leetcode.com/problems/ant-on-the-boundary/

# @param {Integer[]} nums
# @return {Integer}
def return_to_boundary_count(nums)
  s = 0
  ans = 0
  nums.each do |x|
    s += x
    ans += 1 if s == 0
  end
  ans
end
