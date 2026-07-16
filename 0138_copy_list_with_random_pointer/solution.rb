class Node
  attr_accessor :val, :next, :random

  def initialize(x)
    @val = x
    @next = nil
    @random = nil
  end
end

class Solution
  def copy_random_list(head)
    clones = {}
    clone = lambda do |node|
      return nil if node.nil?
      return clones[node] if clones.key?(node)

      copy = Node.new(node.val)
      clones[node] = copy
      copy.next = clone.call(node.next)
      copy.random = clone.call(node.random)
      copy
    end

    clone.call(head)
  end
end