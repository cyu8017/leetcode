# LeetCode 1529 - Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/

# @param {String} target
# @return {Integer}
def min_flips(target)
  ("0" + target).chars.zip(target.chars).count { |a, b| a != b }
end
