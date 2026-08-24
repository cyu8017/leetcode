# LeetCode 0777 - Swap Adjacent in LR String
# https://leetcode.com/problems/swap-adjacent-in-lr-string/

# @param {String} start
# @param {String} result
# @return {Boolean}
def can_transform(start, result)
  return false if start.delete("X") != result.delete("X")

  i = 0
  j = 0
  n = start.length
  while i < n && j < n
    i += 1 while i < n && start[i] == "X"
    j += 1 while j < n && result[j] == "X"
    break if i == n || j == n
    return false if start[i] != result[j]
    return false if start[i] == "L" && i < j
    return false if start[i] == "R" && i > j

    i += 1
    j += 1
  end
  true
end
