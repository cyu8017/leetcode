// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

export function longestPalindrome(s: string): string {
    let bestStart = 0;
    let bestLen = 0;

    function expand(left: number, right: number): void {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        const len = right - left - 1;
        if (len > bestLen) {
            bestLen = len;
            bestStart = left + 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        expand(i, i);
        expand(i, i + 1);
    }

    return s.slice(bestStart, bestStart + bestLen);
}
