"use strict";
// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
// @ts-nocheck
function numOfWays(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const choose = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
    for (let i = 0; i <= n; i++) {
        choose[i][0] = choose[i][i] = 1;
        for (let j = 1; j < i; j++) {
            choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
        }
    }
    const ways = (values) => {
        if (values.length < 3)
            return 1;
        const left = values.slice(1).filter((x) => x < values[0]);
        const right = values.slice(1).filter((x) => x > values[0]);
        return Number(BigInt(choose[values.length - 1][left.length]) * BigInt(ways(left)) * BigInt(ways(right)) % BigInt(MOD));
    };
    return (ways(nums) - 1 + MOD) % MOD;
}
