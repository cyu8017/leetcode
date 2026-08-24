// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

export function minOperations(word1: any, word2: any): any {
    function calc(l: any, r: any, rev: any): any {
        const cnt = Array.from({length: 26}, () => new Array(26).fill(0));
        let res = 0;
        for (let i = l; i <= r; i++) {
            const j = rev ? r - (i - l) : i;
            const a = word1.charCodeAt(j) - 97;
            const b = word2.charCodeAt(i) - 97;
            if (a !== b) {
                if (cnt[b][a] > 0) cnt[b][a]--;
                else {
                    cnt[a][b]++;
                    res++;
                }
            }
        }
        return res;
    }    const n = word1.length;
    const f = new Array(n + 1).fill(Math.floor(2147483647 / 2));
    f[0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            const a = calc(j, i - 1, false);
            const b = 1 + calc(j, i - 1, true);
            f[i] = Math.min(f[i], f[j] + Math.min(a, b));
        }
    }
    return f[n];
}
