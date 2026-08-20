// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

function sortString(s: string): string {
    const c = Array(26).fill(0);
    for (const ch of s) c[ch.charCodeAt(0) - 97]++;
    const out: any[] = [];
    while (out.length < s.length) {
        for (let i = 0; i < 26; i++) if (c[i]) { out.push(String.fromCharCode(97 + i)); c[i]--; }
        for (let i = 25; i >= 0; i--) if (c[i]) { out.push(String.fromCharCode(97 + i)); c[i]--; }
    }
    return out.join("");
}
