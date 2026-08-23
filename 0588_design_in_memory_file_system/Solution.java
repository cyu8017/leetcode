// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class FileSystem {
    private static class Node {
        boolean isFile = false;
        String content = "";
        TreeMap<String, Node> children = new TreeMap<>();
    }

    private final Node root;

    public FileSystem() {
        root = new Node();
    }

    public List<String> ls(String path) {
        if (path.equals("/")) {
            return new ArrayList<>(root.children.keySet());
        }

        List<String> parts = split(path);
        Node node = root;
        for (String part : parts) {
            node = node.children.get(part);
        }

        if (node.isFile) {
            List<String> only = new ArrayList<>();
            only.add(parts.get(parts.size() - 1));
            return only;
        }
        return new ArrayList<>(node.children.keySet());
    }

    public void mkdir(String path) {
        Node node = root;
        for (String part : split(path)) {
            node.children.putIfAbsent(part, new Node());
            node = node.children.get(part);
        }
    }

    public void addContentToFile(String filePath, String content) {
        List<String> parts = split(filePath);
        Node node = root;
        for (int i = 0; i + 1 < parts.size(); ++i) {
            node.children.putIfAbsent(parts.get(i), new Node());
            node = node.children.get(parts.get(i));
        }
        String name = parts.get(parts.size() - 1);
        node.children.putIfAbsent(name, new Node());
        Node file = node.children.get(name);
        file.isFile = true;
        file.content += content;
    }

    public String readContentFromFile(String filePath) {
        Node node = root;
        for (String part : split(filePath)) {
            node = node.children.get(part);
        }
        return node.content;
    }

    private List<String> split(String path) {
        List<String> parts = new ArrayList<>();
        for (String part : path.split("/")) {
            if (!part.isEmpty()) {
                parts.add(part);
            }
        }
        return parts;
    }
}
