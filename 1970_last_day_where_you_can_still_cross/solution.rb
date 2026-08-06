# LeetCode 1970 - Last Day Where You Can Still Cross
# https://leetcode.com/problems/last-day-where-you-can-still-cross/

# @param {Integer} row
# @param {Integer} col
# @param {Integer[][]} cells
# @return {Integer}
def latest_day_to_cross(row, col, cells)
  can = lambda do |day|
    blocked = {}
    day.times { |i| blocked[[cells[i][0] - 1, cells[i][1] - 1]] = true }
    stack = []
    seen = {}
    col.times do |c|
      next if blocked[[0, c]]
      stack << [0, c]
      seen[[0, c]] = true
    end
    until stack.empty?
      r, c = stack.pop
      return true if r == row - 1
      [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].each do |nr, nc|
        key = [nr, nc]
        next unless nr >= 0 && nr < row && nc >= 0 && nc < col && !blocked[key] && !seen[key]
        seen[key] = true
        stack << [nr, nc]
      end
    end
    false
  end

  lo = 1
  hi = cells.length
  ans = 0
  while lo <= hi
    mid = (lo + hi) / 2
    if can.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
