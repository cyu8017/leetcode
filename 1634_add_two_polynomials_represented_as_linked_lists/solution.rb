# LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
# https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

class PolyNode
  attr_accessor :coefficient, :power, :next

  def initialize(x = 0, y = 0, nxt = nil)
    @coefficient = x
    @power = y
    @next = nxt
  end
end

def _build_poly_1634(items)
  dummy = cur = PolyNode.new
  items.each do |c, p|
    cur.next = PolyNode.new(c, p)
    cur = cur.next
  end
  dummy.next
end

# @param {PolyNode|Integer[][]} poly1
# @param {PolyNode|Integer[][]} poly2
# @return {PolyNode|Integer[][]}
def add_poly(poly1, poly2)
  list_mode = poly1.is_a?(Array) || poly2.is_a?(Array)
  poly1 = _build_poly_1634(poly1) if poly1.is_a?(Array)
  poly2 = _build_poly_1634(poly2) if poly2.is_a?(Array)
  dummy = cur = PolyNode.new
  while poly1 || poly2
    if poly2.nil? || (poly1 && poly1.power > poly2.power)
      c = poly1.coefficient
      p = poly1.power
      poly1 = poly1.next
    elsif poly1.nil? || poly2.power > poly1.power
      c = poly2.coefficient
      p = poly2.power
      poly2 = poly2.next
    else
      c = poly1.coefficient + poly2.coefficient
      p = poly1.power
      poly1 = poly1.next
      poly2 = poly2.next
    end
    if c != 0
      cur.next = PolyNode.new(c, p)
      cur = cur.next
    end
  end
  return dummy.next unless list_mode

  out = []
  cur = dummy.next
  while cur
    out << [cur.coefficient, cur.power]
    cur = cur.next
  end
  out
end
