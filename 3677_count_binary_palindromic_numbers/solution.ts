// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

export function countBinaryPalindromes(n: any): any {
    if (n === 0) return 1;
    let ans = 1;
    let s = '';
    for (let x = n; x > 0; x = Math.floor(x / 2)) s += String(x & 1);
    s = s.split('').reverse().join('');
    const L = s.length;
    for (let len = 1; len < L; len++) {
        const half = Math.floor((len + 1) / 2);
        ans += 1 << (half - 1);
    }
    const half = Math.floor((L + 1) / 2);
    const prefix = s.substring(0, half);
    const start = 1 << (half - 1);
    let prefVal = 0;
    for (const c of prefix) prefVal = (prefVal << 1) | (c.charCodeAt(0) - 48);
    ans += prefVal - start;
    let pal = prefix;
    for (let i = half - 1 - (L % 2); i >= 0; i--) pal += prefix[i];
    let pval = 0;
    for (const c of pal) pval = (pval << 1) | (c.charCodeAt(0) - 48);
    if (pval <= n) ans++;
    return ans;
}
