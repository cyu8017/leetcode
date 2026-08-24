// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

export function countBinarySubstrings(s: string): number {
    let prev = 0, cur = 1, ans = 0;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) cur++;
        else {
            ans += Math.min(prev, cur);
            prev = cur;
            cur = 1;
        }
    }
    return ans + Math.min(prev, cur);
}
