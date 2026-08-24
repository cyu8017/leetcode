// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

export function scoreOfString(s: string): number {
    let ans = 0;
    for (let i = 1; i < s.length; i++)
        ans += Math.abs(s.charCodeAt(i - 1) - s.charCodeAt(i));
    return ans;
}
