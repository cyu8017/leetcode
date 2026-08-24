# LeetCode 3159 - Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @param {Integer} x
# @return {Integer[]}
def occurrences_of_element(nums, queries, x)
  ids = []
  nums.each_with_index { |v, i| ids << i if v == x }
  queries.map { |i| i - 1 < ids.length ? ids[i - 1] : -1 }
end
