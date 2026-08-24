// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

const MAX = 1000001;
function nCk(n, kk) {
    if (kk < 0 || kk > n) return 0;
    let res = 1;
    if (kk > n - kk) kk = n - kk;
    for (let i = 1; i <= kk; i++) {
        res = Math.floor(res * (n - i + 1) / i);
        if (res >= MAX) return MAX;
    }
    return res;
}
function countArr(h) {
    let total = 0;
    for (const f of h) total += f;
    let res = 1;
    for (const f of h) {
        res *= nCk(total, f);
        if (res >= MAX) return MAX;
        total -= f;
    }
    return res;
}
var smallestPalindrome = function(s, k) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let odd = 0;
    for (const c of cnt) if (c % 2 !== 0) odd++;
    if (odd > 1) return '';
    const half = new Array(26).fill(0);
    let mid = '';
    for (let i = 0; i < 26; i++) {
        half[i] = Math.floor(cnt[i] / 2);
        if (cnt[i] % 2 !== 0) mid = String.fromCharCode(97 + i);
    }
    if (countArr(half) < k) return '';
    let halfLen = 0;
    for (const f of half) halfLen += f;
    let left = '';
    for (let t = 0; t < halfLen; t++) {
        for (let i = 0; i < 26; i++) {
            if (half[i] === 0) continue;
            half[i]--;
            const arr = countArr(half);
            if (arr >= k) {
                left += String.fromCharCode(97 + i);
                break;
            }
            k -= arr;
            half[i]++;
        }
    }
    let res = left;
    if (mid) res += mid;
    for (let i = left.length - 1; i >= 0; i--) res += left[i];
    return res;
};
