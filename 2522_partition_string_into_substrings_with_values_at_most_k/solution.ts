// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

export function minimumPartition(s: string, k: number): number {
    let ans = 1, cur = 0;
    for (const ch of s) {
        const d = ch.charCodeAt(0) - 48;
        if (d > k) return -1;
        const nxt = cur * 10 + d;
        if (nxt > k) {
            ans++;
            cur = d;
        } else {
            cur = nxt;
        }
    }
    return ans;
}
