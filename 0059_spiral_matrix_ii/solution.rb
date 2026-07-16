# LeetCode 0059 - Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/

# @param {Integer} n
# @return {Integer[][]}
def generate_matrix(n)
  matrix = Array.new(n) { Array.new(n, 0) }
  top = 0
  bottom = n - 1
  left = 0
  right = n - 1
  num = 1

  while top <= bottom && left <= right
    (left..right).each do |col|
      matrix[top][col] = num
      num += 1
    end
    top += 1

    (top..bottom).each do |row|
      matrix[row][right] = num
      num += 1
    end
    right -= 1

    if top <= bottom
      right.downto(left) do |col|
        matrix[bottom][col] = num
        num += 1
      end
      bottom -= 1
    end

    if left <= right
      bottom.downto(top) do |row|
        matrix[row][left] = num
        num += 1
      end
      left += 1
    end
  end

  matrix
end
