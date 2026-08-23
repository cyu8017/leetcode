// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var allPossibleFBT = function(n) {
    const memo = new Map();
    const build = (nodes) => {
        if (memo.has(nodes)) return memo.get(nodes);
        const res = [];
        if (nodes % 2 === 0) {
            memo.set(nodes, res);
            return res;
        }
        if (nodes === 1) {
            res.push(new TreeNode(0));
            memo.set(nodes, res);
            return res;
        }
        for (let left = 1; left < nodes; left += 2) {
            const right = nodes - 1 - left;
            for (const L of build(left)) {
                for (const R of build(right)) {
                    res.push(new TreeNode(0, L, R));
                }
            }
        }
        memo.set(nodes, res);
        return res;
    };
    return build(n);
};
