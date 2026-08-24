// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

export function secondsToRemoveOccurrences(s: string): number {
    let ans = 0, zeros = 0;
    for (const c of s) {
        if (c === '0') zeros++;
        else if (zeros > 0) ans = Math.max(ans + 1, zeros);
    }
    return ans;
}
