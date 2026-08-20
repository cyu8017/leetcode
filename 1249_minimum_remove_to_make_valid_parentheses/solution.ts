// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

function minRemoveToMakeValid(s: string): string {
    const chars = s.split("");
    const opens = [];
    for (let i = 0; i < chars.length; i++) {
        if (chars[i] === "(") opens.push(i);
        else if (chars[i] === ")") {
            if (opens.length) opens.pop();
            else chars[i] = "";
        }
    }
    for (const i of opens) chars[i] = "";
    return chars.join("");
}
