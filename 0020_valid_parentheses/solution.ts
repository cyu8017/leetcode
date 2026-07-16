// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

export function isValid(s: string): boolean {
    const stack: string[] = [];
    const pairs: Record<string, string> = {
        ")": "(",
        "]": "[",
        "}": "{",
    };

    for (const ch of s) {
        if (ch === "(" || ch === "[" || ch === "{") {
            stack.push(ch);
        } else if (stack.length === 0 || stack.pop() !== pairs[ch]) {
            return false;
        }
    }

    return stack.length === 0;
}
