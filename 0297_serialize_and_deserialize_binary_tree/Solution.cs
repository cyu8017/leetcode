// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

using System.Collections.Generic;
using System.Text;

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
        if (root == null) {
            return "";
        }
        var values = new List<string>();
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            TreeNode node = queue.Dequeue();
            if (node == null) {
                values.Add("");
            } else {
                values.Add(node.val.ToString());
                queue.Enqueue(node.left);
                queue.Enqueue(node.right);
            }
        }
        while (values.Count > 0 && values[values.Count - 1] == "") {
            values.RemoveAt(values.Count - 1);
        }
        return string.Join(",", values);
    }

    public TreeNode Deserialize(string data) {
        if (string.IsNullOrEmpty(data)) {
            return null;
        }
        string[] values = data.Split(',');
        TreeNode root = new TreeNode(int.Parse(values[0]));
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int index = 1;
        while (queue.Count > 0 && index < values.Length) {
            TreeNode node = queue.Dequeue();
            if (index < values.Length && values[index] != "") {
                node.left = new TreeNode(int.Parse(values[index]));
                queue.Enqueue(node.left);
            }
            index++;
            if (index < values.Length && values[index] != "") {
                node.right = new TreeNode(int.Parse(values[index]));
                queue.Enqueue(node.right);
            }
            index++;
        }
        return root;
    }
}
