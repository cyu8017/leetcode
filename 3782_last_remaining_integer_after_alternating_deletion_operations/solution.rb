# LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
# https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

# @param {Integer} n
# @return {Integer}
def last_remaining(n)
  first = 1
  step = 2
  left = true
  while n > 1
    first += step if !left && n.even?
    n = (n + 1) / 2
    step *= 2
    left = !left
  end
  first
end
