# LeetCode 2249 - Count Lattice Points Inside a Circle
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

# @param {Integer[][]} circles
# @return {Integer}
def count_lattice_points(circles)
  seen = {}
  circles.each do |x, y, r|
    ((x - r)..(x + r)).each do |i|
      ((y - r)..(y + r)).each do |j|
        seen["#{i},#{j}"] = true if (i - x) * (i - x) + (j - y) * (j - y) <= r * r
      end
    end
  end
  seen.length
end
