// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool LeafSimilar(TreeNode root1, TreeNode root2) {
        List<int> Leaves(TreeNode node) {
            var result = new List<int>();
            void Dfs(TreeNode cur) {
                if (cur == null) return;
                if (cur.left == null && cur.right == null) { result.Add(cur.val); return; }
                Dfs(cur.left);
                Dfs(cur.right);
            }
            Dfs(node);
            return result;
        }
        return Leaves(root1).SequenceEqual(Leaves(root2));
    }
}
