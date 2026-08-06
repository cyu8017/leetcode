# LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

# @param {Integer[][]} arrays
# @return {Integer[]}
def longest_common_subsequence(arrays)
  cnt = Hash.new(0)
  arrays.each { |arr| arr.each { |x| cnt[x] += 1 } }
  m = arrays.length
  arrays[0].select { |x| cnt[x] == m }
end
