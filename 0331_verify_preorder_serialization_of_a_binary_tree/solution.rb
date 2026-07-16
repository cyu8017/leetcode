# LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution
  def is_valid_serialization(preorder)
    slots = 1
    preorder.split(",").each do |node|
      slots -= 1
      return false if slots.negative?

      slots += 2 if node != "#"
    end
    slots.zero?
  end

  alias_method :isValidSerialization, :is_valid_serialization
end
