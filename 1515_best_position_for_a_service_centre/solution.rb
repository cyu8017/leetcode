# LeetCode 1515 - Best Position for a Service Centre
# https://leetcode.com/problems/best-position-for-a-service-centre/

# @param {Integer[][]} positions
# @return {Float}
def get_min_dist_sum(positions)
  x = positions.sum { |p| p[0] }.to_f / positions.length
  y = positions.sum { |p| p[1] }.to_f / positions.length

  distance = lambda do |a, b|
    positions.sum { |px, py| Math.hypot(a - px, b - py) }
  end

  10000.times do
    numerator_x = numerator_y = denominator = 0.0
    coincident = nil
    positions.each do |px, py|
      d = Math.hypot(x - px, y - py)
      if d < 1e-12
        coincident = [px, py]
        break
      end
      numerator_x += px / d
      numerator_y += py / d
      denominator += 1.0 / d
    end
    nx, ny = coincident || [numerator_x / denominator, numerator_y / denominator]
    break if Math.hypot(nx - x, ny - y) < 1e-8
    x, y = nx, ny
  end
  distance.call(x, y)
end
