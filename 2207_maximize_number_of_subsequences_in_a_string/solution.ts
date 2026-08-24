// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

export function maximumSubsequenceCount(text: string, pattern: string): number {
    const a = pattern[0], b = pattern[1];
    function count(s: any): any {
        let ca = 0, ans = 0;
        for (const ch of s) {
            if (ch === b) ans += ca;
            if (ch === a) ca++;
        }
        return ans;
    }    return Math.max(count(a + text), count(text + b));
}
