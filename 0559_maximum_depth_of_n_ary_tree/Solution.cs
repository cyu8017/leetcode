// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;
}
*/

public class Solution {
    public int MaxDepth(Node root) {
        if (root == null) return 0;
        if (root.children == null || root.children.Count == 0) return 1;
        int best = 0;
        foreach (Node child in root.children) {
            int d = MaxDepth(child);
            if (d > best) best = d;
        }
        return best + 1;
    }
}
