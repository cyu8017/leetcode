// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

function maxProduct(s: string): number {
    const n = s.length;
    const radius = new Array(n).fill(0);
    let center = 0, right = 0;
    for (let i = 0; i < n; i++) {
        if (i < right) radius[i] = Math.min(right - i, radius[2 * center - i]);
        while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n && s[i - radius[i] - 1] === s[i + radius[i] + 1]) {
            radius[i]++;
        }
        if (i + radius[i] > right) {
            center = i;
            right = i + radius[i];
        }
    }
    const end = new Array(n).fill(1);
    const start = new Array(n).fill(1);
    for (let i = 0; i < n; i++) {
        const r = radius[i];
        end[i + r] = Math.max(end[i + r], 2 * r + 1);
        start[i - r] = Math.max(start[i - r], 2 * r + 1);
    }
    for (let i = n - 2; i >= 0; i--) end[i] = Math.max(end[i], end[i + 1] - 2);
    for (let i = 1; i < n; i++) start[i] = Math.max(start[i], start[i - 1] - 2);
    const pre = new Array(n).fill(0);
    pre[0] = end[0];
    for (let i = 1; i < n; i++) pre[i] = Math.max(pre[i - 1], end[i]);
    const suf = new Array(n).fill(0);
    suf[n - 1] = start[n - 1];
    for (let i = n - 2; i >= 0; i--) suf[i] = Math.max(suf[i + 1], start[i]);
    let ans = 0;
    for (let i = 0; i < n - 1; i++) ans = Math.max(ans, pre[i] * suf[i + 1]);
    return ans;
}
