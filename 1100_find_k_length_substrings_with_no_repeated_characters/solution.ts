// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

function numKLenSubstrNoRepeats(s: string, k: number): number {
    if (k > s.length) return 0;
    const window = new Map();
    for (let i = 0; i < k; i++) {
        window.set(s[i], (window.get(s[i]) || 0) + 1);
    }
    let ans = window.size === k ? 1 : 0;
    for (let i = k; i < s.length; i++) {
        window.set(s[i], (window.get(s[i]) || 0) + 1);
        const left = s[i - k];
        window.set(left, window.get(left) - 1);
        if (window.get(left) === 0) window.delete(left);
        if (window.size === k) ans++;
    }
    return ans;
}
