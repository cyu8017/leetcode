# LeetCode 0657 - Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/

# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
  moves.count("U") == moves.count("D") && moves.count("L") == moves.count("R")
end
