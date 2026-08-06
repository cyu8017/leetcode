# LeetCode 1483 - Kth Ancestor Of A Tree Node
# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor
  def initialize(n, parent)
    width = [1, n.bit_length].max
    @up = [parent.dup]
    (1...width).each do
      prev = @up[-1]
      @up << prev.map { |p| p == -1 ? -1 : prev[p] }
    end
  end

  def get_kth_ancestor(node, k)
    bit = 0
    while k > 0 && node != -1
      if k & 1 == 1
        return -1 if bit >= @up.length
        node = @up[bit][node]
      end
      bit += 1
      k >>= 1
    end
    node
  end
end
