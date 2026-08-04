// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

/**
 * @param {number[]} order
 * @return {number}
 */
var maxDepthBST = function(order) {
    const nodes = [];
    let ans = 0;
    for (const value of order) {
        let lo = 0, hi = nodes.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (nodes[mid][0] < value) lo = mid + 1;
            else hi = mid;
        }
        const i = lo;
        let depth = 1;
        if (i) depth = Math.max(depth, nodes[i - 1][1] + 1);
        if (i < nodes.length) depth = Math.max(depth, nodes[i][1] + 1);
        nodes.splice(i, 0, [value, depth]);
        ans = Math.max(ans, depth);
    }
    return ans;
};
