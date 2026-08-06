# LeetCode 1597 - Build Binary Expression Tree From Infix Expression
# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = ' ', left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {String} s
# @return {TreeNode}
def exp_tree(s)
  nodes = []
  ops = []
  priority = { '+' => 1, '-' => 1, '*' => 2, '/' => 2 }
  apply = lambda do
    op = ops.pop
    right = nodes.pop
    left = nodes.pop
    nodes << TreeNode.new(op, left, right)
  end
  s.each_char do |ch|
    if ch.match?(/\d/)
      nodes << TreeNode.new(ch)
    elsif ch == '('
      ops << ch
    elsif ch == ')'
      apply.call while ops[-1] != '('
      ops.pop
    else
      apply.call while !ops.empty? && ops[-1] != '(' && priority[ops[-1]] >= priority[ch]
      ops << ch
    end
  end
  apply.call until ops.empty?
  nodes[0]
end
