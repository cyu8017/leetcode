// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

export function kthLargestPerfectSubtree(root: any, k: any): any {
    const sizes = [];
    const dfs = (node) => {
        if (!node) return [0, 0, 1];
        const L = dfs(node.left);
        const R = dfs(node.right);
        const sz = L[1] + R[1] + 1;
        const perf = L[2] === 1 && R[2] === 1 && L[0] === R[0];
        if (perf) sizes.push(sz);
        return [Math.max(L[0], R[0]) + 1, sz, perf ? 1 : 0];
    };
    dfs(root);
    sizes.sort((a, b) => b - a);
    if (k > sizes.length) return -1;
    return sizes[k - 1];
}
