# LeetCode 0533 - Lonely Pixel II
# https://leetcode.com/problems/lonely-pixel-ii/

class Solution
  def find_black_pixel(picture, target)
    rows = picture.length
    cols = picture[0].length
    row_strings = picture.map(&:join)
    row_counts = picture.map { |row| row.count("B") }
    col_counts = (0...cols).map do |c|
      (0...rows).count { |r| picture[r][c] == "B" }
    end

    lonely = 0
    (0...rows).each do |r|
      next unless row_counts[r] == target

      (0...cols).each do |c|
        next if picture[r][c] != "B" || col_counts[c] != target

        if (0...rows).all? { |i| picture[i][c] != "B" || row_strings[r] == row_strings[i] }
          lonely += 1
        end
      end
    end
    lonely
  end

  alias_method :findBlackPixel, :find_black_pixel
end
