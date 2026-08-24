// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

export function dfs(node: any): any {
        if (node == null) return -2147483648;
        let l = dfs(node.left);
        let r = dfs(node.right);
        let mx = Math.max(Math.max(l, r), node.val);
        if (mx == node.val) ans++;
        return mx;
    
}export function countDominantNodes(root: any): any {
        ans = 0;
        dfs(root);
        return ans;
    
}
