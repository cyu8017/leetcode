// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

export function minimumSum(n: number, k: number): number {
    const used = new Set();
    let sum = 0, x = 1;
    while (used.size < n) {
        if (!used.has(k - x)) {
            used.add(x);
            sum += x;
        }
        x++;
    }
    return sum;
}
