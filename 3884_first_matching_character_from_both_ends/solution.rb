# LeetCode 3884 - First Matching Character From Both Ends
# https://leetcode.com/problems/first-matching-character-from-both-ends/

# @param {String} s
# @return {Integer}
def first_matching_index(s)
  n = s.length
  (0..(n / 2)).each { |i| return i if s[i] == s[n - i - 1] }
  -1
end
