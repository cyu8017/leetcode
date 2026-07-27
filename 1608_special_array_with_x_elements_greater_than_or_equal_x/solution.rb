# LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

# @param {Integer[]} nums
# @return {Integer}
def special_array(nums)
  (0..nums.length).each do |x|
    return x if nums.count { |v| v >= x } == x
  end
  -1
end
