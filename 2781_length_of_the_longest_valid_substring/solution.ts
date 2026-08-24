// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

export function longestValidSubstring(word: string, forbidden: string[]): number {
    const forbid = new Set(forbidden);
    let maxLen = 0;
    for (const f of forbidden) maxLen = Math.max(maxLen, f.length);
    let ans = 0, right = word.length - 1;
    for (let left = word.length - 1; left >= 0; left--) {
        for (let k = left; k <= right && k - left + 1 <= maxLen; k++) {
            if (forbid.has(word.slice(left, k + 1))) {
                right = k - 1;
                break;
            }
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
