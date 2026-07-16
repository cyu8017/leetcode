# LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

# @param {Integer[]} preorder
# @return {Boolean}
def verify_preorder(preorder)
  low = -Float::INFINITY
  stack = []

  preorder.each do |value|
    return false if value < low

    while !stack.empty? && stack.last < value
      low = stack.pop
    end
    stack << value
  end

  true
end
