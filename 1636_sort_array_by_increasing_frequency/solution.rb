# LeetCode 1636 - Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

# @param {Integer[]} nums
# @return {Integer[]}
def frequency_sort(nums)
  count = Hash.new(0)
  nums.each { |x| count[x] += 1 }
  nums.sort_by { |x| [count[x], -x] }
end
