// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

function reverseParentheses(s: string): string {
    const stack = [];
    for (const ch of s) {
        if (ch === ')') {
            const chunk = [];
            while (stack.length && stack[stack.length - 1] !== '(') chunk.push(stack.pop());
            stack.pop();
            stack.push(...chunk);
        } else {
            stack.push(ch);
        }
    }
    return stack.join('');
}
