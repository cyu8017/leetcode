
# @param {Integer[][]} points
# @param {Integer[][]} queries
# @return {Integer[]}
def count_points(points, queries)
  queries.map do |xq, yq, r|
    radius_sq = r * r
    points.count { |x, y| (x - xq)**2 + (y - yq)**2 <= radius_sq }
  end
end
