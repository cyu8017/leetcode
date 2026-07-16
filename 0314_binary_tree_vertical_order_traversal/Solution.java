// LeetCode 0314 - Binary Tree Vertical Order Traversal

// https://leetcode.com/problems/binary-tree-vertical-order-traversal/



import java.util.ArrayDeque;

import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;

import java.util.Queue;



class TreeNode {

    int val;

    TreeNode left;

    TreeNode right;

    TreeNode() {}

    TreeNode(int val) { this.val = val; }

    TreeNode(int val, TreeNode left, TreeNode right) {

        this.val = val;

        this.left = left;

        this.right = right;

    }

}



class Solution {

    public List<List<Integer>> verticalOrder(TreeNode root) {

        if (root == null) {

            return new ArrayList<>();

        }



        Map<Integer, List<Integer>> columns = new HashMap<>();

        Queue<TreeNode> nodes = new ArrayDeque<>();

        Queue<Integer> columnIndexes = new ArrayDeque<>();

        nodes.add(root);

        columnIndexes.add(0);

        int minCol = 0;

        int maxCol = 0;



        while (!nodes.isEmpty()) {

            TreeNode node = nodes.poll();

            int column = columnIndexes.poll();

            minCol = Math.min(minCol, column);

            maxCol = Math.max(maxCol, column);

            columns.computeIfAbsent(column, key -> new ArrayList<>()).add(node.val);

            if (node.left != null) {

                nodes.add(node.left);

                columnIndexes.add(column - 1);

            }

            if (node.right != null) {

                nodes.add(node.right);

                columnIndexes.add(column + 1);

            }

        }



        List<List<Integer>> result = new ArrayList<>();

        for (int column = minCol; column <= maxCol; column++) {

            result.add(columns.get(column));

        }

        return result;

    }

}

