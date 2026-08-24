// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

export function checkValidString(s: string): boolean {
    let lo = 0, hi = 0;
    for (const ch of s) {
        if (ch === "(") {
            ++lo;
            ++hi;
        } else if (ch === ")") {
            lo = Math.max(lo - 1, 0);
            --hi;
            if (hi < 0) return false;
        } else {
            lo = Math.max(lo - 1, 0);
            ++hi;
        }
    }
    return lo === 0;
}
