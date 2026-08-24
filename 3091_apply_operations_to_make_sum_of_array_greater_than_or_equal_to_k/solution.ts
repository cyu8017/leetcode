// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

export function minOperations(k: number): number {
    let ans = k;
    for (let a = 0; a < k; a++) {
        const x = a + 1;
        const b = Math.floor((k + x - 1) / x) - 1;
        ans = Math.min(ans, a + b);
    }
    return ans;
}
