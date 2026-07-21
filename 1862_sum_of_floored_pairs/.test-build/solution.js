"use strict";
// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/
function sumOfFlooredPairs(nums) {
    const mod = 1e9 + 7;
    const maxVal = Math.max(...nums);
    const count = new Array(maxVal + 1).fill(0);
    for (const num of nums)
        count[num]++;
    const prefix = new Array(maxVal + 1).fill(0);
    prefix[0] = count[0];
    for (let v = 1; v <= maxVal; v++)
        prefix[v] = prefix[v - 1] + count[v];
    let answer = 0;
    for (let divisor = 1; divisor <= maxVal; divisor++) {
        if (!count[divisor])
            continue;
        let quotient = 1;
        while (quotient * divisor <= maxVal) {
            const low = quotient * divisor;
            const high = Math.min((quotient + 1) * divisor - 1, maxVal);
            const matches = prefix[high] - (low ? prefix[low - 1] : 0);
            answer = (answer + count[divisor] * matches * quotient) % mod;
            quotient++;
        }
    }
    return answer;
}
