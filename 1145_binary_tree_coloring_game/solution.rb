# LeetCode 1145 - Binary Tree Coloring Game
# https://leetcode.com/problems/binary-tree-coloring-game/

# @param {TreeNode} root
# @param {Integer} n
# @param {Integer} x
# @return {Boolean}
def btree_game_winning_move(root, n, x)
  left = 0
  right = 0
  dfs = nil
  dfs = lambda do |node|
    return 0 if node.nil?
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    if node.val == x
      left = l
      right = r
    end
    l + r + 1
  end
  dfs.call(root)
  [left, right, n - left - right - 1].max > n / 2
end
