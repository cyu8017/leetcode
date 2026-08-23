// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

var inorderTraversal = function*(arr) {
    for (const x of arr) {
        if (Array.isArray(x)) yield* inorderTraversal(x);
        else yield x;
    }
};
