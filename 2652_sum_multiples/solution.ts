// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

export function sumOfMultiples(n: any): any {
    let ans = 0;
    for (let i = 1; i <= n; i++)
        if (i % 3 === 0 || i % 5 === 0 || i % 7 === 0) ans += i;
    return ans;
}
