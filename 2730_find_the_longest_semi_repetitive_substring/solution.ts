// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

export function longestSemiRepetitiveSubstring(s: string): number {
    let ans = 0, left = 0, lastPair = -1;
    for (let right = 0; right < s.length; right++) {
        if (right > 0 && s[right] === s[right - 1]) {
            if (lastPair >= left) left = lastPair + 1;
            lastPair = right - 1;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
