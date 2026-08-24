# LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

# @param {Integer[]} x
# @param {Integer[]} y
# @return {Integer}
def max_sum_distinct_triplet(x, y)
  n = x.length
  arr = (0...n).map { |i| [x[i], y[i]] }
  arr.sort_by! { |p| -p[1] }
  ans = 0
  vis = {}
  arr.each do |a, b|
    next if vis[a]
    vis[a] = true
    ans += b
    return ans if vis.length == 3
  end
  -1
end
