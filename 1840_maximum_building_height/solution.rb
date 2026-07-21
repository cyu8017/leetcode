
# @param {Integer} n
# @param {Integer[][]} restrictions
# @return {Integer}
def max_building(n, restrictions)
  points = [[1, 0]] + restrictions.sort_by { |id, _| id }
  points << [n, n - 1] if points[-1][0] != n

  (1...points.length).each do |i|
    prev_id, prev_height = points[i - 1]
    curr_id, curr_height = points[i]
    points[i][1] = [curr_height, prev_height + curr_id - prev_id].min
  end

  (points.length - 2).downto(0) do |i|
    next_id, next_height = points[i + 1]
    curr_id, curr_height = points[i]
    points[i][1] = [curr_height, next_height + next_id - curr_id].min
  end

  best = points.map { |_, h| h }.max
  (0...points.length - 1).each do |i|
    id1, h1 = points[i]
    id2, h2 = points[i + 1]
    best = [best, (h1 + h2 + id2 - id1) / 2].max
  end
  best
end
