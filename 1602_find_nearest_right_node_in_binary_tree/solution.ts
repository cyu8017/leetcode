// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function findNearestRightNode(root: TreeNode | null, u: TreeNode | number): TreeNode | number | null {
    const asNode = typeof u === "object" && u !== null && "val" in u;
    const target = asNode ? (u as TreeNode).val : (u as number);
    let q: TreeNode[] = root ? [root] : [];
    while (q.length) {
        const nxt: TreeNode[] = [];
        for (let i = 0; i < q.length; i++) {
            const node = q[i];
            if (node.val === target) {
                const ans = i + 1 < q.length ? q[i + 1] : null;
                return asNode ? ans : (ans ? ans.val : null);
            }
            if (node.left) nxt.push(node.left);
            if (node.right) nxt.push(node.right);
        }
        q = nxt;
    }
    return null;
}
