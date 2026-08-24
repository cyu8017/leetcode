# LeetCode 0593 - Valid Square
# https://leetcode.com/problems/valid-square/

# @param {Integer[]} p1
# @param {Integer[]} p2
# @param {Integer[]} p3
# @param {Integer[]} p4
# @return {Boolean}
def valid_square(p1, p2, p3, p4)
  dist = lambda { |a, b| (a[0] - b[0])**2 + (a[1] - b[1])**2 }

  points = [p1, p2, p3, p4]
  distances = []
  4.times do |i|
    ((i + 1)...4).each do |j|
      distances << dist.call(points[i], points[j])
    end
  end
  distances.sort!

  distances[0] > 0 &&
    distances[0] == distances[1] && distances[1] == distances[2] && distances[2] == distances[3] &&
    distances[4] == distances[5] &&
    distances[4] == 2 * distances[0]
end
