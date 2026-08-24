# LeetCode 0682 - Baseball Game
# https://leetcode.com/problems/baseball-game/

# @param {String[]} ops
# @return {Integer}
def cal_points(ops)
  stack = []
  ops.each do |op|
    case op
    when "C"
      stack.pop
    when "D"
      stack << stack[-1] * 2
    when "+"
      stack << stack[-1] + stack[-2]
    else
      stack << op.to_i
    end
  end
  stack.sum
end
