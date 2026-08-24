// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

export function scoreOfParentheses(s: string): number {
    const stack = [0];
    for (const ch of s) {
        if (ch === '(') stack.push(0);
        else {
            const val = stack.pop();
            stack.push(stack.pop() + Math.max(2 * val, 1));
        }
    }
    return stack[stack.length - 1];
}
