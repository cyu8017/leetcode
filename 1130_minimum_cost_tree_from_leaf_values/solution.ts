// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

function mctFromLeafValues(arr: number[]): number {
    const stack = [Infinity];
    let ans = 0;
    for (const x of arr) {
        while (stack[stack.length - 1] <= x) {
            const mid = stack.pop();
            ans += mid * Math.min(stack[stack.length - 1], x);
        }
        stack.push(x);
    }
    while (stack.length > 2) {
        ans += stack.pop() * stack[stack.length - 1];
    }
    return ans;
}
