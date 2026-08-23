// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

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

public class Codec {
    public string Serialize(TreeNode root) {
        List<string> parts = new List<string>();
        void Preorder(TreeNode node) {
            if (node == null) {
                parts.Add("#");
                return;
            }
            parts.Add(node.val.ToString());
            Preorder(node.left);
            Preorder(node.right);
        }
        Preorder(root);
        return string.Join(",", parts);
    }

    public TreeNode Deserialize(string data) {
        if (string.IsNullOrEmpty(data)) {
            return null;
        }
        Queue<string> values = new Queue<string>(data.Split(','));
        TreeNode Build() {
            string token = values.Dequeue();
            if (token == "#") {
                return null;
            }
            TreeNode node = new TreeNode(int.Parse(token));
            node.left = Build();
            node.right = Build();
            return node;
        }
        return Build();
    }
}
