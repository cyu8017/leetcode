// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

export function flat(arr: any, n: any): any {
    const res = [];
    const dfs = (a, depth) => {
        for (const x of a) {
            if (Array.isArray(x) && depth < n) dfs(x, depth + 1);
            else res.push(x);
        }
    };
    dfs(arr, 0);
    return res;
}
