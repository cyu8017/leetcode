// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/
// @ts-nocheck

function restoreString(s: string, indices: number[]): string {
    const answer = Array(s.length);
    for (let i = 0; i < s.length; i++) answer[indices[i]] = s[i];
    return answer.join("");
}
