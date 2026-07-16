# LeetCode 0531 - Lonely Pixel I
# https://leetcode.com/problems/lonely-pixel-i/

class Solution
  def find_lonely_pixel(picture)
    rows = picture.length
    cols = picture[0].length
    row_counts = picture.map { |row| row.count("B") }
    col_counts = (0...cols).map do |c|
      (0...rows).count { |r| picture[r][c] == "B" }
    end

    lonely = 0
    (0...rows).each do |r|
      (0...cols).each do |c|
        if picture[r][c] == "B" && row_counts[r] == 1 && col_counts[c] == 1
          lonely += 1
        end
      end
    end
    lonely
  end

  alias_method :findLonelyPixel, :find_lonely_pixel
end
