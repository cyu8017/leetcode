// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

export function lengthAfterTransformations(s: any, t: any): any {
    const mod = 1000000007;
    let cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    for (let step = 0; step < t; step++) {
        const ncnt = new Array(26).fill(0);
        for (let i = 0; i < 25; i++) ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod;
        ncnt[0] = (ncnt[0] + cnt[25]) % mod;
        ncnt[1] = (ncnt[1] + cnt[25]) % mod;
        cnt = ncnt;
    }
    let ans = 0;
    for (const v of cnt) ans = (ans + v) % mod;
    return ans;
}
