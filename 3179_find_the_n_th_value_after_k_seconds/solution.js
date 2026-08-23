// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

var valueAfterKSeconds = function(n, k) {
    const mod = 1000000007;
    const a = new Array(n).fill(1);
    while (k-- > 0) {
        for (let i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
    }
    return a[n - 1];
};
