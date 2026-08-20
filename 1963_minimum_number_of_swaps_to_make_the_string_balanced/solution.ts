// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

function minSwaps(s: string): number {
    let bal = 0, mx = 0;
    for (const ch of s) {
        if (ch === "[") bal++;
        else bal--;
        mx = Math.min(mx, bal);
    }
    return Math.floor((-mx + 1) / 2);
}
