// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

export function getResults(nums: any, queries: any): any {
    const a = nums.slice();
    const ans = [];
    for (const q of queries) {
        const typ = q[0];
        if (typ === 1) {
            let l = q[1], r = q[2];
            while (l < r) { const tmp = a[l]; a[l] = a[r]; a[r] = tmp; l++; r--; }
        } else if (typ === 2) {
            let x = 0;
            for (let i = q[1]; i <= q[2]; i++) x ^= a[i];
            ans.push(x);
        } else {
            a[q[1]] = q[2];
        }
    }
    return ans;
}
