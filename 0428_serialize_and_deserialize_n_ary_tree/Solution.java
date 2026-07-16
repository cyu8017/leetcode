// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int val) {
        this.val = val;
        this.children = new ArrayList<>();
    }

    public Node(int val, List<Node> children) {
        this.val = val;
        this.children = children;
    }
}

class Codec {
    public String encode(Node root) {
        if (root == null) {
            return "";
        }

        List<String> parts = new ArrayList<>();
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            parts.add(String.valueOf(node.val));
            parts.add(String.valueOf(node.children.size()));
            for (Node child : node.children) {
                parts.add(String.valueOf(child.val));
                queue.offer(child);
            }
        }

        return String.join(",", parts);
    }

    public Node decode(String data) {
        if (data == null || data.isEmpty()) {
            return null;
        }

        String[] values = data.split(",");
        int index = 0;

        int rootValue = Integer.parseInt(values[index++]);
        int rootChildCount = Integer.parseInt(values[index++]);
        Node root = new Node(rootValue, new ArrayList<>());
        for (int i = 0; i < rootChildCount; i++) {
            root.children.add(new Node(Integer.parseInt(values[index++]), new ArrayList<>()));
        }

        Queue<Node> queue = new ArrayDeque<>(root.children);
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int value = Integer.parseInt(values[index++]);
            int childCount = Integer.parseInt(values[index++]);
            if (value != node.val) {
                throw new IllegalStateException(
                        "expected node value " + node.val + ", found " + value);
            }
            for (int i = 0; i < childCount; i++) {
                Node child = new Node(Integer.parseInt(values[index++]), new ArrayList<>());
                node.children.add(child);
                queue.offer(child);
            }
        }

        return root;
    }

    public String serialize(Node root) {
        return encode(root);
    }

    public Node deserialize(String data) {
        return decode(data);
    }
}
