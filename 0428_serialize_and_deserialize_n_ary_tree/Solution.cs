// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

using System.Collections.Generic;
using System.Linq;

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

public class Codec {
    public string Encode(Node root) {
        if (root == null) {
            return "";
        }

        List<string> parts = new();
        Queue<Node> queue = new();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            Node node = queue.Dequeue();
            parts.Add(node.val.ToString());
            parts.Add(node.children.Count.ToString());
            foreach (Node child in node.children) {
                parts.Add(child.val.ToString());
                queue.Enqueue(child);
            }
        }
        return string.Join(",", parts);
    }

    public Node Decode(string data) {
        if (string.IsNullOrEmpty(data)) {
            return null;
        }

        string[] values = data.Split(',');
        int index = 0;

        Node ReadRoot() {
            int value = int.Parse(values[index]);
            int childCount = int.Parse(values[index + 1]);
            index += 2;
            Node node = new Node(value, new List<Node>());
            for (int i = 0; i < childCount; i++) {
                node.children.Add(new Node(int.Parse(values[index]), new List<Node>()));
                index++;
            }
            return node;
        }

        Node root = ReadRoot();
        Queue<Node> queue = new(root.children);
        while (queue.Count > 0) {
            Node node = queue.Dequeue();
            int value = int.Parse(values[index]);
            int childCount = int.Parse(values[index + 1]);
            index += 2;
            if (value != node.val) {
                throw new System.InvalidOperationException($"expected node value {node.val}, found {value}");
            }
            for (int i = 0; i < childCount; i++) {
                Node child = new Node(int.Parse(values[index]), new List<Node>());
                node.children.Add(child);
                queue.Enqueue(child);
                index++;
            }
        }
        return root;
    }
}
