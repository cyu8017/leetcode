# LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

# @param {String} n
# @return {Integer}
def min_partitions(n)
  n.chars.map(&:to_i).max
end
