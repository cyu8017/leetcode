# LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

# @param {String[]} words
# @return {Integer}
def max_distance(words)
  n = words.length
  ans = 0
  (0...n).each do |i|
    ans = i + 1 if words[i] != words[0] && i + 1 > ans
    ans = n - i if words[i] != words[n - 1] && n - i > ans
  end
  ans
end
