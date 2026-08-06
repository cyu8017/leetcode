# LeetCode 1133 - Largest Unique Number
# https://leetcode.com/problems/largest-unique-number/

# @param {Integer[]} nums
# @return {Integer}
def largest_unique_number(nums)
  count = Hash.new(0)
  nums.each { |x| count[x] += 1 }
  ans = -1
  count.each { |v, f| ans = [ans, v].max if f == 1 }
  ans
end
