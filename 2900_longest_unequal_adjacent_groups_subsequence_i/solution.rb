# LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_longest_subsequence(words, groups)
  ans = [words[0]]
  last = groups[0]
  (1...words.length).each do |i|
    if groups[i] != last
      ans << words[i]
      last = groups[i]
    end
  end
  ans
end
