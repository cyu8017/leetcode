// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

export function prefixCount(words: string[], pref: string): number {
    let ans = 0;
    for (const w of words)
        if (w.length >= pref.length && w.startsWith(pref)) ans++;
    return ans;
}
