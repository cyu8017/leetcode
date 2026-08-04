// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class BSTIterator {
    private final List<Integer> values = new ArrayList<>();
    private int index;

    public BSTIterator(TreeNode root) {
        index = -1;
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            values.add(root.val);
            root = root.right;
        }
    }

    public boolean hasNext() {
        return index + 1 < values.size();
    }

    public int next() {
        return values.get(++index);
    }

    public boolean hasPrev() {
        return index > 0;
    }

    public int prev() {
        return values.get(--index);
    }
}
