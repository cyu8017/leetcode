// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

export class Solution {
    checkPerfectNumber(num: number): boolean {
        if (num <= 1) return false;
        let total = 1;
        const limit = Math.floor(Math.sqrt(num));
        for (let divisor = 2; divisor <= limit; divisor += 1) {
            if (num % divisor === 0) {
                total += divisor;
                const pair = Math.floor(num / divisor);
                if (pair !== divisor) total += pair;
            }
        }
        return total === num;
    }
}
