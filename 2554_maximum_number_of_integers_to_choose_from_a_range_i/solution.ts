// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

export function maxCount(banned: number[], n: number, maxSum: number): number {
    const ban = new Set(banned);
    let ans = 0, sum = 0;
    for (let i = 1; i <= n; i++) {
        if (ban.has(i)) continue;
        if (sum + i > maxSum) break;
        sum += i;
        ans++;
    }
    return ans;
}
