// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

export function findTheLongestBalancedSubstring(s: string): number {
    let ans = 0, zeros = 0, ones = 0;
    for (const c of s) {
        if (c === '0') {
            if (ones > 0) zeros = ones = 0;
            zeros++;
        } else {
            ones++;
            const cur = Math.min(ones, zeros);
            if (2 * cur > ans) ans = 2 * cur;
        }
    }
    return ans;
}
