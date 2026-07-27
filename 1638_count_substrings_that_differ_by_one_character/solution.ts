// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

function countSubstrings(s: string, t: string): number {
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; j < t.length; j++) {
            let diff = 0;
            for (let k = 0; k < Math.min(s.length - i, t.length - j); k++) {
                if (s[i + k] !== t[j + k]) diff++;
                if (diff === 1) ans++;
                else if (diff > 1) break;
            }
        }
    }
    return ans;
}
