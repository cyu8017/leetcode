// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

var replaceValueInTree = function(root) {
    if (!root) return null;
    root.val = 0;
    const q = [root];
    while (q.length) {
        const sz = q.length;
        let levelSum = 0;
        const level = [];
        for (let i = 0; i < sz; i++) {
            const node = q.shift();
            level.push(node);
            if (node.left) levelSum += node.left.val;
            if (node.right) levelSum += node.right.val;
        }
        for (const node of level) {
            let cousin = levelSum;
            if (node.left) cousin -= node.left.val;
            if (node.right) cousin -= node.right.val;
            if (node.left) { node.left.val = cousin; q.push(node.left); }
            if (node.right) { node.right.val = cousin; q.push(node.right); }
        }
    }
    return root;
};
