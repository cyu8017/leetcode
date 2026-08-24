# LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
# https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D
  def initialize(n)
    @n = n
    @m = Array.new(n) { Array.new(n) { Array.new(n, 0) } }
    @ones = Array.new(n, 0)
  end

  def set_cell(x, y, z)
    if @m[x][y][z] == 0
      @m[x][y][z] = 1
      @ones[x] += 1
    end
    nil
  end

  def unset_cell(x, y, z)
    if @m[x][y][z] == 1
      @m[x][y][z] = 0
      @ones[x] -= 1
    end
    nil
  end

  def largest_matrix
    best = -1
    idx = 0
    @n.times do |i|
      if @ones[i] >= best
        best = @ones[i]
        idx = i
      end
    end
    idx
  end
end
