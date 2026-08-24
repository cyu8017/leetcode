# LeetCode 2649 - Nested Array Generator
# https://leetcode.com/problems/nested-array-generator/

# @param {Object[]} arr
# @return {Enumerator}
def inorder_traversal(arr)
  Enumerator.new do |y|
    walk = lambda do |a|
      a.each do |x|
        if x.is_a?(Array)
          walk.call(x)
        else
          y << x
        end
      end
    end
    walk.call(arr)
  end
end

def solve(*args)
  inorder_traversal(*args)
end
