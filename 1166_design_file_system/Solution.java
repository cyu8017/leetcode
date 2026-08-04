// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

import java.util.*;

class FileSystem {
    private final Map<String, Integer> paths = new HashMap<>();

    public FileSystem() {
        paths.put("", -1);
    }

    public boolean createPath(String path, int value) {
        if (paths.containsKey(path)) return false;
        int idx = path.lastIndexOf('/');
        String parent = path.substring(0, idx);
        if (!paths.containsKey(parent)) return false;
        paths.put(path, value);
        return true;
    }

    public int get(String path) {
        return paths.getOrDefault(path, -1);
    }
}
