# LeetCode 3996 - Even Number of Knight Moves
# https://leetcode.com/problems/even-number-of-knight-moves/

# @param {Integer[]} start
# @param {Integer[]} target
# @return {Boolean}
def can_reach(start, target)
  ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2)
end
