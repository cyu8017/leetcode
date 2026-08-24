# LeetCode 3645 - Maximum Total from Optimal Activation Order
# https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

# @param {Integer[]} value
# @param {Integer[]} limit
# @return {Integer}
def max_total(value, limit)
  g = {}
  limit.each_with_index do |lim, i|
    (g[lim] ||= []) << value[i]
  end
  ans = 0
  g.each do |lim, vs|
    vs.sort!.reverse!
    ans += vs[0, lim].sum
  end
  ans
end
