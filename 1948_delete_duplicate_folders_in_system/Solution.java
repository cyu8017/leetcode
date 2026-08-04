// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

import java.util.*;

class Solution {
    static class Node {
        Map<String, Node> children = new TreeMap<>();
        String serial = "";
        boolean del;
    }

    Map<String, Integer> freq = new HashMap<>();
    List<List<String>> ans = new ArrayList<>();

    public List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
        Node root = new Node();
        for (List<String> path : paths) {
            Node cur = root;
            for (String folder : path) cur = cur.children.computeIfAbsent(folder, k -> new Node());
        }
        serialize(root);
        mark(root);
        collect(root, new ArrayList<>());
        return ans;
    }

    private String serialize(Node node) {
        if (node.children.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Node> e : node.children.entrySet()) {
            sb.append(e.getKey()).append('(').append(serialize(e.getValue())).append(')');
        }
        node.serial = sb.toString();
        freq.merge(node.serial, 1, Integer::sum);
        return node.serial;
    }

    private void mark(Node node) {
        if (!node.serial.isEmpty() && freq.getOrDefault(node.serial, 0) > 1) {
            node.del = true;
            return;
        }
        for (Node child : node.children.values()) mark(child);
    }

    private void collect(Node node, List<String> path) {
        for (Map.Entry<String, Node> e : node.children.entrySet()) {
            if (e.getValue().del) continue;
            path.add(e.getKey());
            ans.add(new ArrayList<>(path));
            collect(e.getValue(), path);
            path.remove(path.size() - 1);
        }
    }
}
