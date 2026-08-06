# LeetCode 1956 - Minimum Time For K Virus Variants to Spread
# https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer}
def min_daysk_variants(points, k)
  ans = Float::INFINITY
  (1..100).each do |x|
    (1..100).each do |y|
      dists = points.map { |px, py| (px - x).abs + (py - y).abs }.sort
      ans = [ans, dists[k - 1]].min
    end
  end
  ans
end
