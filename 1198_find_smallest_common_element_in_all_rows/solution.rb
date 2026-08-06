# LeetCode 1198 - Find Smallest Common Element in All Rows
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

require "set"

# @param {Integer[][]} mat
# @return {Integer}
def smallest_common_element(mat)
  common = Set.new(mat[0])
  mat[1..].each do |row|
    common &= Set.new(row)
    return -1 if common.empty?
  end
  common.min
end
