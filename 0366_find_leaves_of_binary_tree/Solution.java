// LeetCode 0366 - Find Leaves of Binary Tree

// https://leetcode.com/problems/find-leaves-of-binary-tree/



import java.util.ArrayList;

import java.util.List;



class TreeNode {

    int val;

    TreeNode left;

    TreeNode right;



    TreeNode() {}



    TreeNode(int val) {

        this.val = val;

    }



    TreeNode(int val, TreeNode left, TreeNode right) {

        this.val = val;

        this.left = left;

        this.right = right;

    }

}



class Solution {

    public List<List<Integer>> findLeaves(TreeNode root) {

        List<List<Integer>> layers = new ArrayList<>();

        dfs(root, layers);

        return layers;

    }



    private int dfs(TreeNode node, List<List<Integer>> layers) {

        if (node == null) {

            return -1;

        }



        int height = Math.max(dfs(node.left, layers), dfs(node.right, layers)) + 1;

        while (layers.size() <= height) {

            layers.add(new ArrayList<>());

        }

        layers.get(height).add(node.val);

        return height;

    }

}
