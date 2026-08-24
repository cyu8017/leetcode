// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

export function longestPalindrome(s: any, t: any): any {
    const expand = (str, g, l, r) => {
        while (l >= 0 && r < str.length && str[l] === str[r]) {
            g[l] = Math.max(g[l], r - l + 1);
            l--; r++;
        }
    };
    const calc = (str) => {
        const n = str.length;
        const g = new Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            expand(str, g, i, i);
            expand(str, g, i, i + 1);
        }
        return g;
    };
    const m = s.length, n = t.length;
    t = t.split("").reverse().join("");
    const g1 = calc(s), g2 = calc(t);
    let ans = 0;
    for (const v of g1) ans = Math.max(ans, v);
    for (const v of g2) ans = Math.max(ans, v);
    const f = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s[i - 1] === t[j - 1]) {
                f[i][j] = f[i - 1][j - 1] + 1;
                const a = i < m ? g1[i] : 0;
                const b = j < n ? g2[j] : 0;
                ans = Math.max(ans, f[i][j] * 2 + a);
                ans = Math.max(ans, f[i][j] * 2 + b);
            }
        }
    }
    return ans;
}
