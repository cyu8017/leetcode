# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
  return points.length if points.length <= 2

  best = 1
  points.each_with_index do |point, i|
    slopes = Hash.new(0)
    local_best = 1
    ((i + 1)...points.length).each do |j|
      dx = points[j][0] - point[0]
      dy = points[j][1] - point[1]
      divisor = dx.gcd(dy)
      dx /= divisor
      dy /= divisor
      dx, dy = -dx, -dy if dx.negative? || (dx.zero? && dy.negative?)

      slopes[[dx, dy]] += 1
      local_best = [local_best, slopes[[dx, dy]] + 1].max
    end
    best = [best, local_best].max
  end
  best
end