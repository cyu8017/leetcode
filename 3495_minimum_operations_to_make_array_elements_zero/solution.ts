// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

export function minOperations(queries: any): any {
    const opsToZero = (x) => {
        let ops = 0;
        while (x > 0) { x = Math.floor(x / 4); ops++; }
        return ops;
    };
    let ans = 0;
    for (const q of queries) {
        const l = q[0], r = q[1];
        let sum = 0;
        for (let x = l; x <= r; x++) sum += opsToZero(x);
        ans += Math.floor((sum + 1) / 2);
    }
    return ans;
}
