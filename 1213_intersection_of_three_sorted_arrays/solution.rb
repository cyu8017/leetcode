# LeetCode 1213 - Intersection of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

require "set"

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @param {Integer[]} arr3
# @return {Integer[]}
def arrays_intersection(arr1, arr2, arr3)
  (Set.new(arr1) & Set.new(arr2) & Set.new(arr3)).to_a.sort
end
