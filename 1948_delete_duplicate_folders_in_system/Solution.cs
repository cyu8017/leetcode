// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    class Node {
        public Dictionary<string, Node> Children = new();
    }

    Dictionary<string, bool> dup = new();
    Dictionary<Node, string> serialOf = new();

    public IList<IList<string>> DeleteDuplicateFolder(IList<IList<string>> paths) {
        var root = new Node();
        foreach (var path in paths) {
            var node = root;
            foreach (var folder in path) {
                if (!node.Children.ContainsKey(folder))
                    node.Children[folder] = new Node();
                node = node.Children[folder];
            }
        }
        Serialize(root);
        var ans = new List<IList<string>>();
        Collect(root, new List<string>(), ans);
        return ans;
    }

    string Serialize(Node node) {
        if (node.Children.Count == 0) return "";
        var parts = new List<string>();
        foreach (var name in node.Children.Keys.OrderBy(x => x))
            parts.Add(name + "(" + Serialize(node.Children[name]) + ")");
        string serial = string.Concat(parts);
        if (serial.Length > 0) {
            if (dup.ContainsKey(serial)) dup[serial] = true;
            else dup[serial] = false;
            serialOf[node] = serial;
        }
        return serial;
    }

    void Collect(Node node, List<string> path, List<IList<string>> ans) {
        foreach (var (name, child) in node.Children) {
            serialOf.TryGetValue(child, out string serial);
            if (!string.IsNullOrEmpty(serial) && dup.GetValueOrDefault(serial)) continue;
            path.Add(name);
            ans.Add(path.ToList());
            Collect(child, path, ans);
            path.RemoveAt(path.Count - 1);
        }
    }
}