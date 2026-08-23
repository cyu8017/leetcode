// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

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

class Codec {
    public String serialize(TreeNode root) {
        List<String> parts = new ArrayList<>();
        preorder(root, parts);
        return String.join(",", parts);
    }

    private void preorder(TreeNode node, List<String> parts) {
        if (node == null) {
            parts.add("#");
            return;
        }
        parts.add(String.valueOf(node.val));
        preorder(node.left, parts);
        preorder(node.right, parts);
    }

    public TreeNode deserialize(String data) {
        if (data == null || data.isEmpty()) {
            return null;
        }
        String[] values = data.split(",");
        int[] index = {0};
        return build(values, index);
    }

    private TreeNode build(String[] values, int[] index) {
        String token = values[index[0]++];
        if ("#".equals(token)) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(token));
        node.left = build(values, index);
        node.right = build(values, index);
        return node;
    }
}
