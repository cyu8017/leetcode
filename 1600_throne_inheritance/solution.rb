# LeetCode 1600 - Throne Inheritance
# https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance
  def initialize(king_name)
    @king = king_name
    @children = Hash.new { |h, k| h[k] = [] }
    @dead = {}
  end

  def birth(parent_name, child_name)
    @children[parent_name] << child_name
    nil
  end

  def death(name)
    @dead[name] = true
    nil
  end

  def get_inheritance_order
    order = []
    visit = lambda do |name|
      order << name unless @dead[name]
      @children[name].each { |child| visit.call(child) }
    end
    visit.call(@king)
    order
  end
end
