// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

export function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack = [];
    let j = 0;
    for (const x of pushed) {
        stack.push(x);
        while (stack.length && stack[stack.length - 1] === popped[j]) {
            stack.pop();
            j++;
        }
    }
    return stack.length === 0;
}
