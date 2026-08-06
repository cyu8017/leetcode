# LeetCode 1973 - Count Nodes Equal to Sum of Descendants
# https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

# @param {TreeNode} root
# @return {Integer}
def equal_to_descendants(root)
  ans = [0]
  dfs = lambda do |node|
    return 0 unless node
    total = dfs.call(node.left) + dfs.call(node.right)
    ans[0] += 1 if total == node.val
    total + node.val
  end
  dfs.call(root)
  ans[0]
end
