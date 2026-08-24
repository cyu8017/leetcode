// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

export function percentageLetter(s: any, letter: any): any {
    let cnt = 0;
    for (const c of s) if (c === letter) cnt++;
    return Math.floor(cnt * 100 / s.length);
}
