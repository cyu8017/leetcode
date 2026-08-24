// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

export function valueAfterKSeconds(n: any, k: any): any {
    const mod = 1000000007;
    const a = new Array(n).fill(1);
    while (k-- > 0) {
        for (let i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
    }
    return a[n - 1];
}
