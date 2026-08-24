// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

export function findMatrix(nums: number[]): number[][] {
    const freq = new Map();
    const ans = [];
    for (const x of nums) {
        const f = freq.get(x) || 0;
        if (f === ans.length) ans.push([]);
        ans[f].push(x);
        freq.set(x, f + 1);
    }
    return ans;
}
