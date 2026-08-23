// LeetCode 1305 - All Elements In Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

import java.util.*;

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
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> a = new ArrayList<>(), b = new ArrayList<>();
        inorder(root1, a);
        inorder(root2, b);
        List<Integer> answer = new ArrayList<>();
        int i = 0, j = 0;
        while (i < a.size() || j < b.size()) {
            if (j == b.size() || (i < a.size() && a.get(i) <= b.get(j))) {
                answer.add(a.get(i++));
            } else {
                answer.add(b.get(j++));
            }
        }
        return answer;
    }

    private void inorder(TreeNode root, List<Integer> out) {
        if (root == null) return;
        inorder(root.left, out);
        out.add(root.val);
        inorder(root.right, out);
    }
}
