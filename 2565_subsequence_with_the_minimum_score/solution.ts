// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

export function minimumScore(s: string, t: string): number {
    const n = s.length, m = t.length;
    const left = new Array(m).fill(-1), right = new Array(m).fill(-1);
    let j = 0;
    for (let i = 0; i < n && j < m; ++i) {
        if (s[i] === t[j]) {
            left[j] = i;
            j++;
        }
    }
    j = m - 1;
    for (let i = n - 1; i >= 0 && j >= 0; --i) {
        if (s[i] === t[j]) {
            right[j] = i;
            j--;
        }
    }
    if (left[m - 1] !== -1) return 0;
    let ans = m;
    for (let i = 0; i < m; ++i) {
        if (right[i] !== -1) {
            if (i < ans) ans = i;
            break;
        }
    }
    for (let i = m - 1; i >= 0; --i) {
        if (left[i] !== -1) {
            if (m - 1 - i < ans) ans = m - 1 - i;
            break;
        }
    }
    j = 0;
    for (let i = 0; i < m; ++i) {
        if (left[i] === -1) break;
        while (j < m && (right[j] === -1 || right[j] <= left[i])) j++;
        if (j < m) {
            const rem = j - i - 1;
            if (rem < ans) ans = rem;
        }
    }
    return ans;
}
