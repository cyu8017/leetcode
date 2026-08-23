// LeetCode 0366 - Find Leaves of Binary Tree

// https://leetcode.com/problems/find-leaves-of-binary-tree/



using System.Collections.Generic;



public class TreeNode {

    public int val;

    public TreeNode? left;

    public TreeNode? right;



    public TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null) {

        this.val = val;

        this.left = left;

        this.right = right;

    }

}



public class Solution {

    public IList<IList<int>> FindLeaves(TreeNode? root) {

        List<IList<int>> layers = new();

        Dfs(root, layers);

        return layers;

    }



    private int Dfs(TreeNode? node, List<IList<int>> layers) {

        if (node == null) {

            return -1;

        }



        int height = Math.Max(Dfs(node.left, layers), Dfs(node.right, layers)) + 1;

        while (layers.Count <= height) {

            layers.Add(new List<int>());

        }

        layers[height].Add(node.val);

        return height;

    }

}
