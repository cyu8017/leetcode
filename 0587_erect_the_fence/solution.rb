# LeetCode 0587 - Erect the Fence
# https://leetcode.com/problems/erect-the-fence/

# @param {Integer[][]} trees
# @return {Integer[][]}
def outer_trees(trees)
  points = trees.map { |x, y| [x, y] }.sort
  return points.map(&:dup) if points.length <= 1

  cross = lambda do |o, a, b|
    (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
  end

  build = lambda do |ordered|
    hull = []
    ordered.each do |point|
      hull.pop while hull.length >= 2 && cross.call(hull[-2], hull[-1], point) < 0
      hull << point
    end
    hull
  end

  lower = build.call(points)
  upper = build.call(points.reverse)
  hull = (lower[0...-1] + upper[0...-1]).uniq
  hull.reverse! if hull.length > 1 && hull.all? { |point| point[1] == hull[0][1] }
  hull.map(&:dup)
end
