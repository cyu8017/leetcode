# LeetCode 0859 - Buddy Strings
# https://leetcode.com/problems/buddy-strings/

# @param {String} s
# @param {String} goal
# @return {Boolean}
def buddy_strings(s, goal)
  return false if s.length != goal.length
  return s.chars.uniq.length < s.length if s == goal

  diffs = s.chars.zip(goal.chars).select { |a, b| a != b }
  diffs.length == 2 && diffs[0] == diffs[1].reverse
end
