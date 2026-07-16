# LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

class Solution
  def minArea(image, x, y)
    rows = image.length
    cols = image[0].length

    column_has_black = lambda do |col|
      rows.times.any? { |row| image[row][col] == "1" }
    end

    row_has_black = lambda do |row|
      cols.times.any? { |col| image[row][col] == "1" }
    end

    left = 0
    right = y
    while left < right
      mid = (left + right) / 2
      if column_has_black.call(mid)
        right = mid
      else
        left = mid + 1
      end
    end
    left_bound = left

    left = y
    right = cols - 1
    while left < right
      mid = (left + right + 1) / 2
      if column_has_black.call(mid)
        left = mid
      else
        right = mid - 1
      end
    end
    right_bound = left

    top = 0
    bottom = x
    while top < bottom
      mid = (top + bottom) / 2
      if row_has_black.call(mid)
        bottom = mid
      else
        top = mid + 1
      end
    end
    top_bound = top

    top = x
    bottom = rows - 1
    while top < bottom
      mid = (top + bottom + 1) / 2
      if row_has_black.call(mid)
        top = mid
      else
        bottom = mid - 1
      end
    end
    bottom_bound = top

    (right_bound - left_bound + 1) * (bottom_bound - top_bound + 1)
  end
end
