// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

export function makeSubKSumEqual(arr: number[], k: number): number {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const n = arr.length;
    const g = gcd(n, k);
    let ans = 0;
    for (let r = 0; r < g; ++r) {
        const group = [];
        for (let i = r; i < n; i += g) group.push(arr[i]);
        group.sort((a, b) => a - b);
        const med = group[Math.floor(group.length / 2)];
        for (const x of group) ans += Math.abs(x - med);
    }
    return ans;
}
