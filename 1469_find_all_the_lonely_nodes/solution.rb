# LeetCode 1469 - Find All The Lonely Nodes
# https://leetcode.com/problems/find-all-the-lonely-nodes/

def get_lonely_nodes(root)
  ans = []
  dfs = lambda do |node|
    return if node.nil?
    if node.left.nil? ^ node.right.nil?
      ans << (node.left || node.right).val
    end
    dfs.call(node.left)
    dfs.call(node.right)
  end
  dfs.call(root)
  ans
end
