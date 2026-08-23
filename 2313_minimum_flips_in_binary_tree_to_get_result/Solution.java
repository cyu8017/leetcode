// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class Solution {
    public int minimumFlips(TreeNode root, boolean result) {
        int[] res = dfs(root);
        return result ? res[1] : res[0];
    }

    // returns {flipsToFalse, flipsToTrue}
    private int[] dfs(TreeNode node) {
        if (node.left == null && node.right == null) {
            return node.val == 0 ? new int[] {0, 1} : new int[] {1, 0};
        }
        if (node.val == 5) {
            int[] x = dfs(node.left);
            return new int[] {x[1], x[0]};
        }
        int[] L = dfs(node.left);
        int[] R = dfs(node.right);
        int lf = L[0], lt = L[1], rf = R[0], rt = R[1];
        if (node.val == 2) {
            return new int[] {
                lf + rf,
                Math.min(lt + rt, Math.min(lt + rf, lf + rt))
            };
        }
        if (node.val == 3) {
            return new int[] {
                Math.min(lf + rf, Math.min(lf + rt, lt + rf)),
                lt + rt
            };
        }
        if (node.val == 4) {
            return new int[] {
                Math.min(lf + rf, lt + rt),
                Math.min(lf + rt, lt + rf)
            };
        }
        return new int[] {0, 0};
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
