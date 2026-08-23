// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class FileSystem {
    private class Node {
        public bool IsFile;
        public string Content = "";
        public SortedDictionary<string, Node> Children = new();
    }

    private readonly Node root = new();

    public FileSystem() {}

    private List<string> Split(string path) {
        return path.Split('/', System.StringSplitOptions.RemoveEmptyEntries).ToList();
    }

    public IList<string> Ls(string path) {
        if (path == "/") {
            return root.Children.Keys.ToList();
        }
        var parts = Split(path);
        Node node = root;
        foreach (string part in parts) node = node.Children[part];
        if (node.IsFile) return new List<string> { parts[^1] };
        return node.Children.Keys.ToList();
    }

    public void Mkdir(string path) {
        Node node = root;
        foreach (string part in Split(path)) {
            if (!node.Children.ContainsKey(part)) node.Children[part] = new Node();
            node = node.Children[part];
        }
    }

    public void AddContentToFile(string filePath, string content) {
        var parts = Split(filePath);
        Node node = root;
        for (int i = 0; i + 1 < parts.Count; ++i) {
            if (!node.Children.ContainsKey(parts[i])) node.Children[parts[i]] = new Node();
            node = node.Children[parts[i]];
        }
        string name = parts[^1];
        if (!node.Children.ContainsKey(name)) {
            node.Children[name] = new Node { IsFile = true };
        }
        node.Children[name].Content += content;
    }

    public string ReadContentFromFile(string filePath) {
        Node node = root;
        foreach (string part in Split(filePath)) node = node.Children[part];
        return node.Content;
    }
}
