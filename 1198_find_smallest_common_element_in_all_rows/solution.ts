// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

function smallestCommonElement(mat: number[][]): number {
    let common = new Set(mat[0]);
    for (let i = 1; i < mat.length; i++) {
        const row = new Set(mat[i]);
        common = new Set([...common].filter((x) => row.has(x)));
        if (!common.size) return -1;
    }
    return Math.min(...common);
}
