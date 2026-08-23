// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

/**
 * @param {Node} root
 * @param {Node} p
 * @param {Node} q
 * @return {Node}
 */
var moveSubTree = function(root, p, q) {
    const parent = new Map();
    const build = (node) => {
        for (const child of node.children || []) {
            parent.set(child, node);
            build(child);
        }
    };
    build(root);
    if (parent.get(p) === q) return root;
    const isAncestor = (a, b) => {
        let cur = b;
        while (parent.has(cur)) {
            cur = parent.get(cur);
            if (cur === a) return true;
        }
        return false;
    };
    const pParent = parent.get(p);
    const qParent = parent.get(q);
    if (isAncestor(p, q)) {
        qParent.children.splice(qParent.children.indexOf(q), 1);
        if (!pParent) root = q;
        else pParent.children[pParent.children.indexOf(p)] = q;
        q.children.push(p);
    } else {
        if (!pParent) root = q;
        else pParent.children.splice(pParent.children.indexOf(p), 1);
        q.children.push(p);
    }
    return root;
};
