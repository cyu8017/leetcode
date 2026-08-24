# LeetCode 2206 - Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/

# @param {Integer[]} nums
# @return {Boolean}
def divide_array(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  freq.each_value { |c| return false if c.odd? }
  true
end
