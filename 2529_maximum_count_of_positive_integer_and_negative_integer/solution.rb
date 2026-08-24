# LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

# @param {Integer[]} nums
# @return {Integer}
def maximum_count(nums)
  pos = 0
  neg = 0
  nums.each do |x|
    if x > 0
      pos += 1
    elsif x < 0
      neg += 1
    end
  end
  [pos, neg].max
end
