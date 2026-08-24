// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

export function similarPairs(words: string[]): number {
    const freq = new Map();
    let ans = 0;
    for (const w of words) {
        let mask = 0;
        for (let i = 0; i < w.length; i++) mask |= 1 << (w.charCodeAt(i) - 97);
        ans += freq.get(mask) || 0;
        freq.set(mask, (freq.get(mask) || 0) + 1);
    }
    return ans;
}
