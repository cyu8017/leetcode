// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

export function findTheString(lcp: number[][]): string {
    const n = lcp.length;
    const s = new Array(n).fill(0);
    let c = 97;
    for (let i = 0; i < n; ++i) {
        if (s[i] !== 0) continue;
        if (c > 122) return "";
        s[i] = c;
        for (let j = i + 1; j < n; ++j) {
            if (lcp[i][j] > 0) s[j] = c;
        }
        c++;
    }
    for (let i = n - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            let v = 0;
            if (s[i] === s[j]) {
                v = 1;
                if (i + 1 < n && j + 1 < n) v += lcp[i + 1][j + 1];
            }
            if (lcp[i][j] !== v) return "";
        }
    }
    return String.fromCharCode(...s);
}
