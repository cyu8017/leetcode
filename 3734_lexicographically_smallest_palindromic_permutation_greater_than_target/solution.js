// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_palindromic_permutation_greater_than_target/

var lexPalindromicPermutation = function(s, target) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let odd = 0, mid = -1;
    for (let i = 0; i < 26; i++) {
        if (cnt[i] % 2 === 1) { odd++; mid = i; }
    }
    if (odd > 1) return "";
    const half = new Array(26).fill(0);
    for (let i = 0; i < 26; i++) half[i] = Math.floor(cnt[i] / 2);
    const n = s.length;
    const halfLen = Math.floor(n / 2);
    const left = new Array(halfLen);
    const dfs = (pos, greater) => {
        if (pos === halfLen) {
            if (mid >= 0) {
                if (greater) return true;
                return String.fromCharCode(97 + mid) > target[halfLen];
            }
            return greater;
        }
        const start = greater ? 0 : (target.charCodeAt(pos) - 97);
        for (let c = start; c < 26; c++) {
            if (half[c] === 0) continue;
            half[c]--;
            left[pos] = String.fromCharCode(97 + c);
            if (dfs(pos + 1, greater || c > (target.charCodeAt(pos) - 97))) return true;
            half[c]++;
        }
        return false;
    };
    if (!dfs(0, false)) return "";
    let res = left.join('');
    if (mid >= 0) res += String.fromCharCode(97 + mid);
    for (let i = halfLen - 1; i >= 0; i--) res += left[i];
    if (res <= target) return "";
    return res;
};
