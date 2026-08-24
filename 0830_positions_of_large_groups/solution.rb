# LeetCode 0830 - Positions of Large Groups
# https://leetcode.com/problems/positions-of-large-groups/

# @param {String} s
# @return {Integer[][]}
def large_group_positions(s)
  ans = []
  i = 0
  n = s.length
  while i < n
    j = i
    j += 1 while j < n && s[j] == s[i]
    ans << [i, j - 1] if j - i >= 3
    i = j
  end
  ans
end
