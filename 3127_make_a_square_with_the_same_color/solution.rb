# LeetCode 3127 - Make a Square with the Same Color
# https://leetcode.com/problems/make-a-square-with-the-same-color/

# @param {String[][]} grid
# @return {Boolean}
def can_make_square(grid)
  dirs = [0, 0, 1, 1, 0]
  2.times do |i|
    2.times do |j|
      cnt1 = 0
      cnt2 = 0
      4.times do |k|
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if grid[x][y] == "W"
          cnt1 += 1
        else
          cnt2 += 1
        end
      end
      return true if cnt1 != cnt2
    end
  end
  false
end
