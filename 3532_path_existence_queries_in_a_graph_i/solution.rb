# LeetCode 3532 - Path Existence Queries in a Graph I
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

# @param {Integer} n
# @param {Integer[]} nums
# @param {Integer} max_diff
# @param {Integer[][]} queries
# @return {Boolean[]}
def path_existence_queries(n, nums, max_diff, queries)
  g = Array.new(n, 0)
  cnt = 0
  (1...n).each do |i|
    cnt += 1 if nums[i] - nums[i - 1] > max_diff
    g[i] = cnt
  end
  queries.map { |q| g[q[0]] == g[q[1]] }
end
