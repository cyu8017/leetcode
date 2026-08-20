// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/
// @ts-nocheck

function numSub(s: string): number {
    let ans = 0, run = 0;
    for (const ch of s) {
        run = ch === "1" ? run + 1 : 0;
        ans += run;
    }
    return ans % 1000000007;
}
