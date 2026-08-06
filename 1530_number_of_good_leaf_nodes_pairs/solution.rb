# LeetCode 1530 - Number of Good Leaf Nodes Pairs
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# @param {TreeNode} root
# @param {Integer} distance
# @return {Integer}
def count_pairs(root, distance)
  answer = 0
  dfs = lambda do |node|
    return [] if node.nil?
    return [1] if node.left.nil? && node.right.nil?
    left = dfs.call(node.left)
    right = dfs.call(node.right)
    left.each do |a|
      right.each { |b| answer += 1 if a + b <= distance }
    end
    (left + right).filter_map { |depth| depth + 1 if depth + 1 < distance }
  end
  dfs.call(root)
  answer
end
