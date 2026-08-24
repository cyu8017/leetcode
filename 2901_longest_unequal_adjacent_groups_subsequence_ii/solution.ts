// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

export function getWordsInLongestSubsequence(words: string[], groups: number[]): string[] {
    const n = words.length;
    const dp = Array(n).fill(1);
    const prev = Array(n).fill(-1);
    const hamming = (a, b) => {
        if (a.length !== b.length) return 100;
        let d = 0;
        for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) d++;
        return d;
    };
    let best = 1, bestI = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (groups[i] !== groups[j] && hamming(words[i], words[j]) === 1 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > best) { best = dp[i]; bestI = i; }
    }
    const path = [];
    for (let i = bestI; i !== -1; i = prev[i]) path.push(words[i]);
    path.reverse();
    return path;
}
