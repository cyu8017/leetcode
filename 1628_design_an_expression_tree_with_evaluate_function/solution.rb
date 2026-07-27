# LeetCode 1628 - Design an Expression Tree With Evaluate Function
# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

class Node
  attr_accessor :val, :left, :right

  def initialize(val, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end

  def evaluate
    return @val.to_i unless "+-*/".include?(@val)

    a = @left.evaluate
    b = @right.evaluate
    case @val
    when "+" then a + b
    when "-" then a - b
    when "*" then a * b
    when "/" then a / b
    end
  end

  def ==(other)
    evaluate == other
  end
end

class TreeBuilder
  def expTree(postfix)
    stack = []
    postfix.each do |token|
      node = Node.new(token)
      if "+-*/".include?(token)
        node.right = stack.pop
        node.left = stack.pop
      end
      stack << node
    end
    stack[-1]
  end

  alias exp_tree expTree
end
