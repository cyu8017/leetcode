// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

export function longestPalindrome(words: string[]): number {
    const freq = new Map();
    for (const w of words) freq.set(w, (freq.get(w) || 0) + 1);
    let ans = 0;
    let center = false;
    for (const [w, c] of freq) {
        const rev = w[1] + w[0];
        if (w[0] === w[1]) {
            ans += Math.floor(c / 2) * 4;
            if (c % 2 !== 0) center = true;
        } else if (w < rev) {
            ans += Math.min(c, freq.get(rev) || 0) * 4;
        }
    }
    if (center) ans += 2;
    return ans;
}
