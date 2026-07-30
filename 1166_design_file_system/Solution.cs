// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

using System.Collections.Generic;

public class FileSystem {
    private readonly Dictionary<string, int> paths = new Dictionary<string, int> { [""] = -1 };

    public bool CreatePath(string path, int value) {
        if (paths.ContainsKey(path)) return false;
        int pos = path.LastIndexOf('/');
        string parent = path.Substring(0, pos);
        if (!paths.ContainsKey(parent)) return false;
        paths[path] = value;
        return true;
    }

    public int Get(string path) {
        return paths.TryGetValue(path, out int v) ? v : -1;
    }
}
