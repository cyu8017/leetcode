// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public IList<int> LargestValues(TreeNode root) {
        IList<int> result = new List<int>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            int levelMax = int.MinValue;
            int levelSize = queue.Count;
            for (int count = 0; count < levelSize; count++) {
                TreeNode node = queue.Dequeue();
                levelMax = System.Math.Max(levelMax, node.val);
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
            result.Add(levelMax);
        }
        return result;
    }
}
