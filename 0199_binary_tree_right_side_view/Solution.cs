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
    public System.Collections.Generic.IList<int> RightSideView(TreeNode root) {
        var result = new System.Collections.Generic.List<int>();
        if (root == null) return result;
        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            var size = queue.Count;
            for (var i = 0; i < size; i++) {
                var node = queue.Dequeue();
                if (i == size - 1) result.Add(node.val);
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
        }
        return result;
    }
}
