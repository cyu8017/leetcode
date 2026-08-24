// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

export function oddEvenJumps(arr: number[]): number {
    const n = arr.length;
    const nextHigher = new Array(n).fill(0);
    const nextLower = new Array(n).fill(0);
    let order = Array.from({ length: n }, (_, i) => i);
    order.sort((i, j) => arr[i] === arr[j] ? i - j : arr[i] - arr[j]);
    let stack = [];
    for (const i of order) {
        while (stack.length && stack[stack.length - 1] < i) {
            nextHigher[stack[stack.length - 1]] = i;
            stack.pop();
        }
        stack.push(i);
    }
    stack = [];
    order.sort((i, j) => arr[i] === arr[j] ? i - j : arr[j] - arr[i]);
    for (const i of order) {
        while (stack.length && stack[stack.length - 1] < i) {
            nextLower[stack[stack.length - 1]] = i;
            stack.pop();
        }
        stack.push(i);
    }
    const odd = new Array(n).fill(false);
    const even = new Array(n).fill(false);
    odd[n - 1] = even[n - 1] = true;
    for (let i = n - 2; i >= 0; i--) {
        if (nextHigher[i] !== 0) odd[i] = even[nextHigher[i]];
        if (nextLower[i] !== 0) even[i] = odd[nextLower[i]];
    }
    let ans = 0;
    for (const x of odd) if (x) ans++;
    return ans;
}
