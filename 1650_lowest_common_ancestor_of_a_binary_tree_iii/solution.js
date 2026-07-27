// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

/**
 * @param {object} p
 * @param {object} q
 * @return {object|number}
 */
var lowestCommonAncestor = function(p, q) {
    const compatibility = p && typeof p === "object" && !("val" in p) && "tree" in p;
    if (compatibility) {
        const data = p;
        const vals = data.tree;
        const nodes = vals.map((v) => (v === null || v === undefined ? null : { val: v, left: null, right: null, parent: null }));
        for (let i = 0; i < nodes.length; i++) {
            const node = nodes[i];
            if (!node) continue;
            const leftI = 2 * i + 1;
            const rightI = 2 * i + 2;
            if (leftI < nodes.length && nodes[leftI]) {
                node.left = nodes[leftI];
                nodes[leftI].parent = node;
            }
            if (rightI < nodes.length && nodes[rightI]) {
                node.right = nodes[rightI];
                nodes[rightI].parent = node;
            }
        }
        p = nodes.find((x) => x && x.val === data.p);
        q = nodes.find((x) => x && x.val === data.q);
    }
    let a = p, b = q;
    while (a !== b) {
        a = a ? a.parent : q;
        b = b ? b.parent : p;
    }
    return compatibility ? a.val : a;
};
