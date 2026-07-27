"use strict";
// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
function findNearestRightNode(root, u) {
    const asNode = typeof u === "object" && u !== null && "val" in u;
    const target = asNode ? u.val : u;
    let q = root ? [root] : [];
    while (q.length) {
        const nxt = [];
        for (let i = 0; i < q.length; i++) {
            const node = q[i];
            if (node.val === target) {
                const ans = i + 1 < q.length ? q[i + 1] : null;
                return asNode ? ans : (ans ? ans.val : null);
            }
            if (node.left)
                nxt.push(node.left);
            if (node.right)
                nxt.push(node.right);
        }
        q = nxt;
    }
    return null;
}
