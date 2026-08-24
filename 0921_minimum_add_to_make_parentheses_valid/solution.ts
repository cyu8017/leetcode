// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

export function minAddToMakeValid(s: string): number {
    let openNeed = 0, closeNeed = 0;
    for (const ch of s) {
        if (ch === "(") closeNeed++;
        else if (closeNeed > 0) closeNeed--;
        else openNeed++;
    }
    return openNeed + closeNeed;
}
