# LeetCode 3495 - Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

# @param {Integer[]} queries
# @return {Integer}
def min_operations(queries)
  ops_to_zero = lambda do |x|
    ops = 0
    while x > 0
      x /= 4
      ops += 1
    end
    ops
  end
  ans = 0
  queries.each do |q|
    l = q[0]
    r = q[1]
    s = 0
    (l..r).each { |x| s += ops_to_zero.call(x) }
    ans += (s + 1) / 2
  end
  ans
end
