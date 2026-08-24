// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

export function applyOperations(nums: number[]): number[] {
    const n = nums.length;
    const a = nums.slice();
    for (let i = 0; i + 1 < n; i++) {
        if (a[i] === a[i + 1]) {
            a[i] *= 2;
            a[i + 1] = 0;
        }
    }
    const ans = Array(n).fill(0);
    let j = 0;
    for (const x of a) if (x !== 0) ans[j++] = x;
    return ans;
}
