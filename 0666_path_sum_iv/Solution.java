// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private final Map<Long, Integer> tree = new HashMap<>();
    private int total;

    public int pathSum(int[] nums) {
        tree.clear();
        total = 0;
        for (int num : nums) {
            tree.put(key(num / 100, (num / 10) % 10), num % 10);
        }
        dfs(1, 1, 0);
        return total;
    }

    private void dfs(int depth, int pos, int path) {
        Long k = key(depth, pos);
        if (!tree.containsKey(k)) {
            return;
        }
        path += tree.get(k);
        Long left = key(depth + 1, pos * 2 - 1);
        Long right = key(depth + 1, pos * 2);
        if (!tree.containsKey(left) && !tree.containsKey(right)) {
            total += path;
            return;
        }
        dfs(depth + 1, pos * 2 - 1, path);
        dfs(depth + 1, pos * 2, path);
    }

    private long key(int depth, int pos) {
        return (((long) depth) << 32) | (pos & 0xffffffffL);
    }
}
