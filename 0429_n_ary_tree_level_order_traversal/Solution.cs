// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

using System.Collections.Generic;

public class Node {
    public int val;
    public IList<Node> children;
    public Node() {
        children = new List<Node>();
    }
    public Node(int val, IList<Node> children = null) {
        this.val = val;
        this.children = children ?? new List<Node>();
    }
}

public class Solution {
    public IList<IList<int>> LevelOrder(Node root) {
        IList<IList<int>> result = new List<IList<int>>();
        if (root == null) {
            return result;
        }

        Queue<Node> queue = new();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            int size = queue.Count;
            IList<int> level = new List<int>();
            for (int i = 0; i < size; i++) {
                Node node = queue.Dequeue();
                level.Add(node.val);
                foreach (Node child in node.children) {
                    queue.Enqueue(child);
                }
            }
            result.Add(level);
        }

        return result;
    }
}
