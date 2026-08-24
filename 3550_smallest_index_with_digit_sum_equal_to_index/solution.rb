# LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

# @param {Integer[]} nums
# @return {Integer}
def smallest_index(nums)
  nums.each_with_index do |num, i|
    x = num
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    return i if s == i
  end
  -1
end
