// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

interface Node1666 {
    val: number;
    left: Node1666 | null;
    right: Node1666 | null;
    parent: Node1666 | null;
}

function flipBinaryTree(root: Node1666, leaf: Node1666): Node1666 {
    let node: Node1666 = leaf;
    while (node !== root) {
        const parent = node.parent!;
        if (parent.left === node) parent.left = null;
        else parent.right = null;
        const originalLeft = node.left;
        node.left = parent;
        if (originalLeft !== null) node.right = originalLeft;
        node = parent;
    }
    const fixParent = (cur: Node1666 | null, parent: Node1666 | null): void => {
        if (!cur) return;
        cur.parent = parent;
        fixParent(cur.left, cur);
        fixParent(cur.right, cur);
    };
    fixParent(leaf, null);
    return leaf;
}
