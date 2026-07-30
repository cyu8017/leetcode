// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxDepthBST(int[] order) {
        var nodes = new List<(int value, int depth)>();
        int ans = 0;
        foreach (int value in order) {
            int i = nodes.BinarySearch((value, 0), Comparer<(int, int)>.Create((a, b) => a.Item1.CompareTo(b.Item1)));
            if (i < 0) i = ~i;
            int depth = 1;
            if (i > 0) depth = Math.Max(depth, nodes[i - 1].depth + 1);
            if (i < nodes.Count) depth = Math.Max(depth, nodes[i].depth + 1);
            nodes.Insert(i, (value, depth));
            ans = Math.Max(ans, depth);
        }
        return ans;
    }
}