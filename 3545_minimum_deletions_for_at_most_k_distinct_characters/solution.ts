// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

export function minDeletion(s: any, k: any): any {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    cnt.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i + k < 26; i++) ans += cnt[i];
    return ans;
}
