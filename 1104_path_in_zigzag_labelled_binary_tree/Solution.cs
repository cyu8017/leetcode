// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

using System.Collections.Generic;

public class Solution {
    public IList<int> PathInZigZagTree(int label) {
        var path = new List<int>();
        path.Add(label);
        while (label > 1) {
            int level = 0;
            for (int x = label; x > 0; x >>= 1) level++;
            level--;
            label >>= 1;
            label = (1 << level) - 1 - label + (1 << (level - 1));
            path.Add(label);
        }
        path.Reverse();
        return path;
    }
}
