# LeetCode 2361 - Minimum Costs Using the Train Line
# https://leetcode.com/problems/minimum-costs-using-the-train-line/

# @param {Integer[]} regular
# @param {Integer[]} express
# @param {Integer} express_cost
# @return {Integer[]}
def minimum_costs(regular, express, express_cost)
  n = regular.length
  ans = Array.new(n, 0)
  reg = 0
  exp = express_cost
  (0...n).each do |i|
    next_reg = [reg + regular[i], exp + express[i]].min
    next_exp = [reg + regular[i] + express_cost, exp + express[i]].min
    reg = next_reg
    exp = next_exp
    ans[i] = [reg, exp].min
  end
  ans
end

alias solve minimum_costs
