# LeetCode 2943 - Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} h_bars
# @param {Integer[]} v_bars
# @return {Integer}
def maximize_square_hole_area(n, m, h_bars, v_bars)
  side = max_gap(h_bars.dup)
  vs = max_gap(v_bars.dup)
  side = vs if vs < side
  side * side
end

def max_gap(bars)
  return 1 if bars.empty?

  bars.sort!
  best = 1
  cur = 1
  (1...bars.length).each do |i|
    if bars[i] == bars[i - 1] + 1
      cur += 1
    else
      cur = 1
    end
    best = cur if cur > best
  end
  best + 1
end
