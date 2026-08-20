// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function btreeGameWinningMove(root: TreeNode | null, n: number, x: number): boolean {
    let left = 0, right = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const l = dfs(node.left), r = dfs(node.right);
        if (node.val === x) {
            left = l;
            right = r;
        }
        return l + r + 1;
    };
    dfs(root);
    return Math.max(left, right, n - left - right - 1) > Math.floor(n / 2);
}
