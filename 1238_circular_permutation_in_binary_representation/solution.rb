# LeetCode 1238 - Circular Permutation in Binary Representation
# https://leetcode.com/problems/circular-permutation-in-binary-representation/

# @param {Integer} n
# @param {Integer} start
# @return {Integer[]}
def circular_permutation(n, start)
  (0...(1 << n)).map { |i| start ^ i ^ (i >> 1) }
end
