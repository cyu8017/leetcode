# LeetCode 2337 - Move Pieces to Obtain a String
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

# @param {String} start
# @param {String} target
# @return {Boolean}
def can_change(start, target)
  n = start.length
  i = 0
  j = 0
  while i < n || j < n
    i += 1 while i < n && start[i] == "_"
    j += 1 while j < n && target[j] == "_"
    return i == n && j == n if i == n || j == n
    return false if start[i] != target[j]
    return false if start[i] == "L" && i < j
    return false if start[i] == "R" && i > j
    i += 1
    j += 1
  end
  true
end
