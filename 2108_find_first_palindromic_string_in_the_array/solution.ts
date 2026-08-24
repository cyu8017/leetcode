// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

export function firstPalindrome(words: string[]): string {
    for (const w of words) {
        let ok = true;
        for (let l = 0, r = w.length - 1; l < r; l++, r--)
            if (w[l] !== w[r]) { ok = false; break; }
        if (ok) return w;
    }
    return "";
}
