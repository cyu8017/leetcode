// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

export function zigzagLevelSum(root: any): any {
    const ans = [];
    let q = [root];
    let left = true;
    while (q.length) {
        const nq = [];
        for (const node of q) {
            if (node.left) nq.push(node.left);
            if (node.right) nq.push(node.right);
        }
        const m = q.length;
        let s = 0;
        for (let i = 0; i < m; i++) {
            const node = left ? q[i] : q[m - i - 1];
            const child = left ? node.left : node.right;
            if (!child) break;
            s += node.val;
        }
        ans.push(s);
        left = !left;
        q = nq;
    }
    return ans;
}
