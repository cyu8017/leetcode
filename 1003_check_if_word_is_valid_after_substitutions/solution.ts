// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

function isValid(s: string): boolean {
    const stack = [];
    for (const ch of s) {
        stack.push(ch);
        const n = stack.length;
        if (n >= 3 && stack[n - 3] === 'a' && stack[n - 2] === 'b' && stack[n - 1] === 'c') {
            stack.length = n - 3;
        }
    }
    return stack.length === 0;
}
