"use strict";
// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
// @ts-nocheck
function countPairs(root, distance) {
    let answer = 0;
    const dfs = (node) => {
        if (!node)
            return [];
        if (!node.left && !node.right)
            return [1];
        const left = dfs(node.left);
        const right = dfs(node.right);
        for (const a of left) {
            for (const b of right) {
                if (a + b <= distance)
                    answer++;
            }
        }
        const out = [];
        for (const depth of left.concat(right)) {
            if (depth + 1 < distance)
                out.push(depth + 1);
        }
        return out;
    };
    dfs(root);
    return answer;
}
