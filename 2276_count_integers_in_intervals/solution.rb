# LeetCode 2276 - Count Integers in Intervals
# https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals
  class Node
    attr_accessor :left, :right, :covered

    def initialize
      @left = nil
      @right = nil
      @covered = false
    end
  end

  def initialize
    @root = nil
    @cnt = 0
  end

  def add(left, right)
    extra, @root = add_range(1, 1_000_000_000, left, right, @root)
    @cnt += extra
    nil
  end

  def count
    @cnt
  end

  private

  def covered_len(node, range_l, range_r)
    return 0 if node.nil?
    return range_r - range_l + 1 if node.covered

    mid = (range_l + range_r) / 2
    covered_len(node.left, range_l, mid) + covered_len(node.right, mid + 1, range_r)
  end

  def add_range(range_l, range_r, l, r, node)
    node ||= Node.new
    return [0, node] if node.covered

    if l <= range_l && range_r <= r
      already = covered_len(node, range_l, range_r)
      node.covered = true
      node.left = node.right = nil
      return [range_r - range_l + 1 - already, node]
    end
    mid = (range_l + range_r) / 2
    added = 0
    if l <= mid
      extra, node.left = add_range(range_l, mid, l, r, node.left)
      added += extra
    end
    if r > mid
      extra, node.right = add_range(mid + 1, range_r, l, r, node.right)
      added += extra
    end
    if node.left && node.right && node.left.covered && node.right.covered
      node.covered = true
      node.left = node.right = nil
    end
    [added, node]
  end
end
