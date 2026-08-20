"use strict";
// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/
function validateBinaryTreeNodes(n, leftChild, rightChild) {
    const indeg = Array(n).fill(0);
    for (const x of leftChild.concat(rightChild)) {
        if (x !== -1) {
            indeg[x]++;
            if (indeg[x] > 1)
                return false;
        }
    }
    const roots = [];
    for (let i = 0; i < n; i++)
        if (indeg[i] === 0)
            roots.push(i);
    if (roots.length !== 1)
        return false;
    const seen = new Set();
    const st = [...roots];
    while (st.length) {
        const u = st.pop();
        if (seen.has(u))
            return false;
        seen.add(u);
        for (const v of [leftChild[u], rightChild[u]])
            if (v !== -1)
                st.push(v);
    }
    return seen.size === n;
}
