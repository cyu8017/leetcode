# LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def tiling_rectangle(n, m)
  n, m = m, n if n > m
  heights = Array.new(m, 0)
  best = n * m
  search = nil
  search = lambda do |used|
    return if used >= best
    low = heights.min
    if low == n
      best = used
      return
    end
    left = heights.index(low)
    right = left
    right += 1 while right < m && heights[right] == low
    max_size = [n - low, right - left].min
    max_size.downto(1) do |size|
      (left...left + size).each { |i| heights[i] = low + size }
      search.call(used + 1)
      (left...left + size).each { |i| heights[i] = low }
    end
  end
  search.call(0)
  best
end
