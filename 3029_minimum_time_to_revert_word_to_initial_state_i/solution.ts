// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

export function minimumTimeToInitialState(word: any, k: any): any {
    const n = word.length;
    for (let i = k; i < n; i += k)
        if (word.substring(i) === word.substring(0, n - i)) return (i / k) | 0;
    return ((n + k - 1) / k) | 0;
}
