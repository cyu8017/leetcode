// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

export function replaceNonCoprimes(nums: number[]): number[] {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const stack = [];
    for (let x0 of nums) {
        let x = x0;
        while (stack.length) {
            const g = gcd(stack[stack.length - 1], x);
            if (g === 1) break;
            x = Math.floor(stack[stack.length - 1] / g) * x;
            stack.pop();
        }
        stack.push(x);
    }
    return stack;
}
