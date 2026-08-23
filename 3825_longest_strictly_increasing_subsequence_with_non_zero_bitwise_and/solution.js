// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest_strictly_increasing_subsequence_with_non_zero_bitwise_and/

function bitLen(x) {
    if (x === 0) return 0;
    let n = 0;
    while (x > 0) { n++; x >>= 1; }
    return n;
}
function lis(arr) {
    const g = [];
    for (const x of arr) {
        let lo = 0, hi = g.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (g[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        if (lo === g.length) g.push(x);
        else g[lo] = x;
    }
    return g.length;
}
var longestSubsequence = function(nums) {
    let ans = 0, mx = 0;
    for (const x of nums) mx = Math.max(mx, x);
    const m = bitLen(mx);
    for (let i = 0; i < m; i++) {
        const arr = [];
        for (const x of nums) {
            if (((x >> i) & 1) !== 0) arr.push(x);
        }
        ans = Math.max(ans, lis(arr));
    }
    return ans;
};
