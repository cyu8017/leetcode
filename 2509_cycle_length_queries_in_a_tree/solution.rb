# LeetCode 2509 - Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def cycle_length_queries(n, queries)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    a = q[0]
    b = q[1]
    steps = 0
    while a != b
      if a > b
        a /= 2
      else
        b /= 2
      end
      steps += 1
    end
    ans[i] = steps + 1
  end
  ans
end
