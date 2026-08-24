// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

export function partitionString(s: string): number {
    let ans = 1, seen = 0;
    for (const c of s) {
        const bit = 1 << (c.charCodeAt(0) - 97);
        if ((seen & bit) !== 0) {
            ans++;
            seen = 0;
        }
        seen |= bit;
    }
    return ans;
}
