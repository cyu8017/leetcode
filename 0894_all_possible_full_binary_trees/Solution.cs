// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public IList<TreeNode> AllPossibleFBT(int n) {
        var memo = new Dictionary<int, IList<TreeNode>>();
        IList<TreeNode> Build(int nodes) {
            if (memo.ContainsKey(nodes)) return memo[nodes];
            var res = new List<TreeNode>();
            if (nodes % 2 == 0) return memo[nodes] = res;
            if (nodes == 1) {
                res.Add(new TreeNode(0));
                return memo[nodes] = res;
            }
            for (int left = 1; left < nodes; left += 2) {
                int right = nodes - 1 - left;
                foreach (var L in Build(left)) {
                    foreach (var R in Build(right)) {
                        res.Add(new TreeNode(0, L, R));
                    }
                }
            }
            return memo[nodes] = res;
        }
        return Build(n);
    }
}
