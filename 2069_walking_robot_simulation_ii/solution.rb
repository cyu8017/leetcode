# LeetCode 2069 - Walking Robot Simulation II
# https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot
  def initialize(width, height)
    @w = width
    @h = height
    @peri = 2 * (width + height) - 4
    @pos = 0
    @moved = false
  end

  def step(num)
    @moved = true
    @pos = (@pos + num) % @peri
    nil
  end

  def get_pos
    pd = pos_dir
    [pd[0], pd[1]]
  end

  def get_dir
    %w[East North West South][pos_dir[2]]
  end

  private

  def pos_dir
    p = @pos
    return [0, 0, 0] if p.zero? && !@moved
    return [0, 0, 3] if p.zero?

    return [p, 0, 0] if p <= @w - 1

    p -= @w - 1
    return [@w - 1, p, 1] if p <= @h - 1

    p -= @h - 1
    return [@w - 1 - p, @h - 1, 2] if p <= @w - 1

    p -= @w - 1
    [0, @h - 1 - p, 3]
  end
end
