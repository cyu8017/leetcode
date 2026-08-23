// LeetCode 0314 - Binary Tree Vertical Order Traversal

// https://leetcode.com/problems/binary-tree-vertical-order-traversal/



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

    public IList<IList<int>> VerticalOrder(TreeNode root) {

        if (root == null) {

            return new List<IList<int>>();

        }



        Dictionary<int, List<int>> columns = new();

        Queue<TreeNode> nodes = new();

        Queue<int> columnIndexes = new();

        nodes.Enqueue(root);

        columnIndexes.Enqueue(0);

        int minCol = 0;

        int maxCol = 0;



        while (nodes.Count > 0) {

            TreeNode node = nodes.Dequeue();

            int column = columnIndexes.Dequeue();

            minCol = System.Math.Min(minCol, column);

            maxCol = System.Math.Max(maxCol, column);

            if (!columns.ContainsKey(column)) {

                columns[column] = new List<int>();

            }

            columns[column].Add(node.val);

            if (node.left != null) {

                nodes.Enqueue(node.left);

                columnIndexes.Enqueue(column - 1);

            }

            if (node.right != null) {

                nodes.Enqueue(node.right);

                columnIndexes.Enqueue(column + 1);

            }

        }



        List<IList<int>> result = new();

        for (int column = minCol; column <= maxCol; column++) {

            result.Add(columns[column]);

        }

        return result;

    }

}

