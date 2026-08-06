# LeetCode 1302 - Deepest Leaves Sum
# https://leetcode.com/problems/deepest-leaves-sum/

def deepest_leaves_sum(root)
  level = [root]
  answer = 0
  while !level.empty?
    answer = level.sum(&:val)
    level = level.flat_map { |node| [node.left, node.right].compact }
  end
  answer
end
