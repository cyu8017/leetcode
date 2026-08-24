# LeetCode 3143 - Maximum Points Inside the Square
# https://leetcode.com/problems/maximum-points-inside-the-square/

# @param {Integer[][]} points
# @param {String} s
# @return {Integer}
def max_points_inside_square(points, s)
  g = {}
  keys = []
  points.each_with_index do |p, i|
    key = [[p[0], -p[0]].max, [p[1], -p[1]].max].max
    unless g.key?(key)
      g[key] = []
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) / 2
        if keys[mid] < key
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, key)
    end
    g[key] << i
  end
  vis = Array.new(26, false)
  ans = 0
  keys.each do |key|
    lst = g[key]
    lst.each do |i|
      j = s[i].ord - 97
      return ans if vis[j]
      vis[j] = true
    end
    ans += lst.length
  end
  ans
end
