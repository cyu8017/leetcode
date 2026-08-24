# LeetCode 0598 - Range Addition II
# https://leetcode.com/problems/range-addition-ii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} ops
# @return {Integer}
def max_count(m, n, ops)
  ops.each do |a, b|
    m = [m, a].min
    n = [n, b].min
  end
  m * n
end
