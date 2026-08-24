# LeetCode 3534 - Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

# @param {Integer} n
# @param {Integer[]} nums
# @param {Integer} max_diff
# @param {Integer[][]} queries
# @return {Integer[]}
def path_existence_queries(n, nums, max_diff, queries)
  pairs = (0...n).map { |i| [nums[i], i] }
  pairs.sort_by! { |x| x[0] }
  m = 20
  f = Array.new(n) { Array.new(m, 0) }
  r = n - 1
  (n - 1).downto(0) do |l|
    r -= 1 while pairs[r][0] - pairs[l][0] > max_diff
    i = pairs[l][1]
    j = pairs[r][1]
    f[i][0] = j
    (1...m).each { |k| f[i][k] = f[f[i][k - 1]][k - 1] }
  end
  ans = []
  queries.each do |q|
    i = q[0]
    j = q[1]
    i, j = j, i if nums[i] > nums[j]
    if i == j
      ans << 0
      next
    end
    if nums[i] == nums[j]
      ans << 1
      next
    end
    d = 0
    (m - 1).downto(0) do |k|
      if nums[f[i][k]] < nums[j]
        d |= 1 << k
        i = f[i][k]
      end
    end
    ans << (nums[f[i][0]] < nums[j] ? -1 : d + 1)
  end
  ans
end
