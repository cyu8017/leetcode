// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

export function* inorderTraversal(arr: any[]): Generator<any> {
    for (const x of arr) {
        if (Array.isArray(x)) yield* inorderTraversal(x);
        else yield x;
    }
}
