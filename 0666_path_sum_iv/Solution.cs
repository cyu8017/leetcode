// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<(int, int), int> tree = new();
    private int total;

    public int PathSum(int[] nums) {
        tree.Clear();
        total = 0;
        foreach (int num in nums) {
            tree[(num / 100, (num / 10) % 10)] = num % 10;
        }
        Dfs(1, 1, 0);
        return total;
    }

    private void Dfs(int depth, int pos, int path) {
        if (!tree.ContainsKey((depth, pos))) return;
        path += tree[(depth, pos)];
        var left = (depth + 1, pos * 2 - 1);
        var right = (depth + 1, pos * 2);
        if (!tree.ContainsKey(left) && !tree.ContainsKey(right)) {
            total += path;
            return;
        }
        Dfs(depth + 1, pos * 2 - 1, path);
        Dfs(depth + 1, pos * 2, path);
    }
}
