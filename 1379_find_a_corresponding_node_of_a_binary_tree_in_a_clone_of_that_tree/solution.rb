# LeetCode 1379 - Find A Corresponding Node Of A Binary Tree In A Clone Of That Tree
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

def get_target_copy(original, cloned, target)
  wanted = target.is_a?(Integer) ? target : target.val
  stack = [[original, cloned]]
  until stack.empty?
    a, b = stack.pop
    return (target.is_a?(Integer) ? b.val : b) if a.val == wanted
    stack << [a.left, b.left] if a.left
    stack << [a.right, b.right] if a.right
  end
end
