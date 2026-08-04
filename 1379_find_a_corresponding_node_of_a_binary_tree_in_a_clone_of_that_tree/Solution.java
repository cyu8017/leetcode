// LeetCode 1379 - Find A Corresponding Node Of A Binary Tree In A Clone Of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

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
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        Deque<TreeNode[]> stack = new ArrayDeque<>();
        stack.push(new TreeNode[]{original, cloned});
        while (!stack.isEmpty()) {
            TreeNode[] cur = stack.pop();
            if (cur[0] == target || cur[0].val == target.val) return cur[1];
            if (cur[0].left != null) stack.push(new TreeNode[]{cur[0].left, cur[1].left});
            if (cur[0].right != null) stack.push(new TreeNode[]{cur[0].right, cur[1].right});
        }
        return null;
    }
}
