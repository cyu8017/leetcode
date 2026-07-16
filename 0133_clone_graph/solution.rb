class Node
  attr_accessor :val, :neighbors

  def initialize(val = 0, neighbors = [])
    @val = val
    @neighbors = neighbors
  end
end

class Solution
  def clone_graph(node)
    return nil if node.nil?

    clones = {}
    dfs = lambda do |current|
      return clones[current] if clones.key?(current)

      clone = Node.new(current.val)
      clones[current] = clone
      clone.neighbors = current.neighbors.map { |neighbor| dfs.call(neighbor) }
      clone
    end

    dfs.call(node)
  end
end